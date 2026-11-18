import json
import uuid
import os
import re
from datetime import datetime
from pathlib import Path
from typing import Dict, Any, List, Optional
from fastapi import FastAPI, Depends, HTTPException, Body
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
from sqlalchemy.orm import Session

from backend.config import (
    APP_TITLE, APP_VERSION, STATIC_DIR, FRONTEND_DIR,
    OPENAI_API_KEY, GEMINI_API_KEY, OPENAI_MODEL
)
from backend.database import init_db, get_db, ExamModel, SubmissionModel
from backend.exam_engine.benchmark_exam import BENCHMARK_EXAM_METADATA, BENCHMARK_QUESTIONS
from backend.exam_engine.spt_sample_data import ALL_SPT_SAMPLE_EXAMS, SPT_SUBJECTS_METADATA
from backend.exam_engine.vact_2026_data import VACT_2026_SAMPLE_EXAM
from backend.exam_engine.grader import grade_submission, calculate_question_weights, propagate_passages
from backend.exam_engine.analytics import generate_radar_chart_base64, calculate_competency_insights
from backend.exam_engine.advisor import generate_personalized_advice
from backend.agent_council.graph import run_agent_council_pipeline

# Khởi tạo cơ sở dữ liệu
init_db()

app = FastAPI(title=APP_TITLE, version=APP_VERSION)

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Đảm bảo nạp đề thi Benchmark và các đề tham khảo chính thức vào SQLite nếu chưa có
def seed_benchmark_exam():
    db = next(get_db())
    try:
        # 1. Đề Benchmark chuẩn gốc
        existing = db.query(ExamModel).filter(ExamModel.id == BENCHMARK_EXAM_METADATA["id"]).first()
        if not existing:
            exam = ExamModel(
                id=BENCHMARK_EXAM_METADATA["id"],
                title=BENCHMARK_EXAM_METADATA["title"],
                description=BENCHMARK_EXAM_METADATA["description"],
                total_questions=BENCHMARK_EXAM_METADATA["total_questions"],
                duration_minutes=BENCHMARK_EXAM_METADATA["duration_minutes"],
                source=BENCHMARK_EXAM_METADATA["source"],
                exam_type="vact",
                max_score=1200.0,
                data_json=json.dumps(propagate_passages(BENCHMARK_QUESTIONS), ensure_ascii=False)
            )
            db.add(exam)
            print("Successfully seeded benchmark exam into database!")

        # 2. Đề Tham Khảo V-ACT 2026 chính thức (120 câu)
        existing_vact = db.query(ExamModel).filter(ExamModel.id == VACT_2026_SAMPLE_EXAM["id"]).first()
        if not existing_vact:
            vact_exam = ExamModel(
                id=VACT_2026_SAMPLE_EXAM["id"],
                title=VACT_2026_SAMPLE_EXAM["title"],
                description=VACT_2026_SAMPLE_EXAM["description"],
                total_questions=VACT_2026_SAMPLE_EXAM["total_questions"],
                duration_minutes=VACT_2026_SAMPLE_EXAM["duration_minutes"],
                source="benchmark",
                exam_type="vact",
                max_score=1200.0,
                data_json=json.dumps(propagate_passages(VACT_2026_SAMPLE_EXAM["questions"]), ensure_ascii=False)
            )
            db.add(vact_exam)
            print("Successfully seeded V-ACT 2026 official sample exam into database!")

        # 3. Nạp 8 Đề Tham Khảo SPT (ĐH Sư phạm Hà Nội - Mã 075)
        for spt in ALL_SPT_SAMPLE_EXAMS:
            existing_spt = db.query(ExamModel).filter(ExamModel.id == spt["id"]).first()
            if not existing_spt:
                spt_db = ExamModel(
                    id=spt["id"],
                    title=spt["title"],
                    description=spt["description"],
                    total_questions=spt["total_questions"],
                    duration_minutes=spt["duration_minutes"],
                    source="benchmark",
                    exam_type="spt",
                    subject=spt.get("subject"),
                    max_score=spt.get("max_score", 10.0),
                    data_json=json.dumps(propagate_passages(spt["questions"]), ensure_ascii=False)
                )
                db.add(spt_db)
                print(f"Successfully seeded SPT exam: {spt['title']}")

        db.commit()
    except Exception as e:
        print(f"Error seeding exams: {e}")
        db.rollback()
    finally:
        db.close()

seed_benchmark_exam()

# --- Pydantic Schemas ---
class SubmitExamRequest(BaseModel):
    candidate_name: Optional[str] = "Thí sinh ĐGNL"
    answers: Dict[str, Any] # { "1": "A", "17": {"a": "Đ", ...}, ... }
    time_spent_seconds: int

class GenerateAgentRequest(BaseModel):
    topic: str
    section_target: str = "language" # "language", "logic_data", "problem_solving"
    difficulty: str = "medium"
    count: int = 2

class GenerateFullExamRequest(BaseModel):
    title: Optional[str] = "Đề Thi ĐGNL 120 Câu AI Tự Động"
    theme: Optional[str] = "Khoa học, Xã hội & Đổi mới"

class SaveSettingsRequest(BaseModel):
    openai_api_key: Optional[str] = None
    gemini_api_key: Optional[str] = None
    gemini_api_keys: Optional[str] = None
    gemini_model: Optional[str] = None
    openai_model: Optional[str] = None

# --- API Endpoints ---

@app.get("/api/health")
def health_check():
    return {
        "status": "online",
        "app": APP_TITLE,
        "version": APP_VERSION,
        "llm_configured": bool(os.getenv("OPENAI_API_KEY") or os.getenv("GEMINI_API_KEY"))
    }

@app.get("/api/exams")
def list_exams(db: Session = Depends(get_db)):
    exams = db.query(ExamModel).all()
    return [
        {
            "id": e.id,
            "title": e.title,
            "description": e.description,
            "total_questions": e.total_questions,
            "duration_minutes": e.duration_minutes,
            "source": e.source,
            "exam_type": e.exam_type or "vact",
            "subject": e.subject,
            "max_score": e.max_score or (10.0 if e.exam_type == "spt" else 1200.0),
            "created_at": e.created_at.isoformat() if e.created_at else None
        }
        for e in exams
    ]

@app.get("/api/spt/subjects")
def get_spt_subjects():
    return SPT_SUBJECTS_METADATA

def resolve_next_exam_title(requested_title: Optional[str], db: Session) -> str:
    """
    Tự động tính toán số thứ tự tăng dần (02 -> 03 -> 04 -> ...)
    để các đề thi AI sinh ra không bị trùng lặp tên gọi.
    """
    exams = db.query(ExamModel).all()
    existing_titles = set(e.title.strip() for e in exams)
    
    max_num = 1
    for e in exams:
        match = re.search(r"(?:Số|Đề)\s*0*(\d+)", e.title, re.IGNORECASE)
        if match:
            try:
                n = int(match.group(1))
                if n > max_num:
                    max_num = n
            except ValueError:
                pass
    next_num = max(max_num + 1, len(exams) + 1)
    next_num_str = f"{next_num:02d}"

    if not requested_title or not requested_title.strip():
        return f"Đề Thi ĐGNL Số {next_num_str} - Luyện Thi Bứt Phá Điểm Số"

    req_clean = requested_title.strip()

    # Nếu trùng lặp tiêu đề với đề đã có sẵn trong CSDL
    if req_clean in existing_titles:
        if re.search(r"(?:Số|Đề)\s*0*(\d+)", req_clean, re.IGNORECASE):
            return re.sub(r"((?:Số|Đề)\s*)0*\d+", rf"\g<1>{next_num_str}", req_clean, count=1, flags=re.IGNORECASE)
        else:
            return f"{req_clean} (Số {next_num_str})"

    return req_clean

@app.get("/api/exams/next-info")
def get_next_exam_info(db: Session = Depends(get_db)):
    """
    Trả về số thứ tự tiếp theo và tiêu đề gợi ý cho đề mới
    """
    suggested = resolve_next_exam_title("", db)
    match = re.search(r"Số\s*0*(\d+)", suggested)
    next_num = int(match.group(1)) if match else 2
    return {
        "next_number": next_num,
        "next_number_formatted": f"{next_num:02d}",
        "suggested_title": suggested
    }

@app.get("/api/exams/{exam_id}")
def get_exam(exam_id: str, mode: str = "test", db: Session = Depends(get_db)):
    """
    Lấy thông tin đề thi.
    Nếu mode == 'test', ẩn đáp án đúng (correct_answer) và lời giải (explanation) để chống gian lận.
    """
    exam = db.query(ExamModel).filter(ExamModel.id == exam_id).first()
    if not exam:
        raise HTTPException(status_code=404, detail="Không tìm thấy đề thi.")

    questions = json.loads(exam.data_json)
    
    exam_max_score = exam.max_score or (10.0 if exam.exam_type == "spt" else 1200.0)
    # Tính trọng số điểm từng câu để hiển thị cho thí sinh biết
    weights = calculate_question_weights(questions, max_total_score=exam_max_score)

    sanitized_questions = []
    for q in questions:
        q_copy = dict(q)
        q_num = q_copy.get("question_number", 1)
        q_copy["points"] = weights.get(q_num, 0.25 if exam.exam_type == "spt" else 10.0)
        
        if mode == "test":
            q_copy.pop("correct_answer", None)
            q_copy.pop("explanation", None)

        sanitized_questions.append(q_copy)

    return {
        "id": exam.id,
        "title": exam.title,
        "description": exam.description,
        "total_questions": exam.total_questions,
        "duration_minutes": exam.duration_minutes,
        "source": exam.source,
        "exam_type": exam.exam_type or "vact",
        "subject": exam.subject,
        "max_score": exam_max_score,
        "questions": sanitized_questions
    }

@app.delete("/api/exams-generated")
def delete_all_generated_exams(db: Session = Depends(get_db)):
    """Xóa tất cả các đề thi do AI tạo"""
    deleted_count = db.query(ExamModel).filter(ExamModel.source == "langgraph_generated").delete()
    db.commit()
    return {"status": "success", "message": f"Đã xóa {deleted_count} đề thi do AI tạo thành công!"}

@app.delete("/api/exams/{exam_id}")
def delete_exam(exam_id: str, db: Session = Depends(get_db)):
    """Xóa một đề thi cụ thể theo ID (bảo vệ đề chuẩn gốc benchmark)"""
    exam = db.query(ExamModel).filter(ExamModel.id == exam_id).first()
    if not exam:
        raise HTTPException(status_code=404, detail="Không tìm thấy đề thi cần xóa.")
    
    if exam.source == "benchmark":
        raise HTTPException(status_code=400, detail="Không thể xóa đề thi chuẩn gốc của hệ thống.")

    db.delete(exam)
    db.commit()
    return {"status": "success", "message": f"Đã xóa đề thi '{exam.title}' thành công!"}

@app.post("/api/exams/{exam_id}/submit")
def submit_exam(exam_id: str, req: SubmitExamRequest, db: Session = Depends(get_db)):
    exam = db.query(ExamModel).filter(ExamModel.id == exam_id).first()
    if not exam:
        raise HTTPException(status_code=404, detail="Không tìm thấy đề thi.")

    questions = json.loads(exam.data_json)
    exam_max_score = exam.max_score or (10.0 if exam.exam_type == "spt" else 1200.0)
    grade_report = grade_submission(
        questions, 
        req.answers, 
        exam_type=exam.exam_type or "vact", 
        max_score=exam_max_score
    )
    
    # Phân tích năng lực chuyên sâu (Pandas & Scipy)
    competency_analysis = calculate_competency_insights(
        grade_report["domain_stats"], 
        grade_report["total_score"]
    )
    
    # Vẽ Biểu đồ Mạng nhện Radar Chart (Matplotlib)
    radar_image_base64 = generate_radar_chart_base64(grade_report["domain_stats"])

    # Sinh lời khuyên ôn tập cá nhân hóa từ Chuyên gia AI
    ai_advice = generate_personalized_advice(
        grade_report["domain_stats"],
        grade_report["total_score"]
    )

    # Lưu kết quả nộp bài vào DB
    sub_id = f"sub_{uuid.uuid4().hex[:12]}"
    submission = SubmissionModel(
        id=sub_id,
        exam_id=exam_id,
        candidate_name=req.candidate_name,
        started_at=datetime.utcnow(),
        submitted_at=datetime.utcnow(),
        time_spent_seconds=req.time_spent_seconds,
        total_score=grade_report["total_score"],
        sec1_score=grade_report["sec1_score"],
        sec2_score=grade_report["sec2_score"],
        sec3_score=grade_report["sec3_score"],
        answers_json=json.dumps(req.answers, ensure_ascii=False),
        results_json=json.dumps(grade_report, ensure_ascii=False),
        radar_data_json=json.dumps({
            "domain_stats": grade_report["domain_stats"],
            "competency": competency_analysis,
            "radar_image": radar_image_base64
        }, ensure_ascii=False),
        ai_advice=ai_advice
    )
    db.add(submission)
    db.commit()

    return {
        "submission_id": sub_id,
        "candidate_name": req.candidate_name,
        "time_spent_seconds": req.time_spent_seconds,
        "grade_report": grade_report,
        "competency_analysis": competency_analysis,
        "radar_image": radar_image_base64,
        "ai_advice": ai_advice
    }

@app.get("/api/submissions/{submission_id}")
def get_submission(submission_id: str, db: Session = Depends(get_db)):
    sub = db.query(SubmissionModel).filter(SubmissionModel.id == submission_id).first()
    if not sub:
        raise HTTPException(status_code=404, detail="Không tìm thấy kết quả làm bài.")
    return sub.to_dict()

@app.post("/api/agents/generate")
def generate_questions_with_council(req: GenerateAgentRequest):
    """
    Kích hoạt Hội đồng Tác tử LangGraph (Language, Logic/Data, Critic, HyDE RAG, Ragas)
    để sinh câu hỏi mới.
    """
    try:
        council_result = run_agent_council_pipeline(
            topic=req.topic,
            section_target=req.section_target,
            count=req.count,
            difficulty=req.difficulty
        )
        return {
            "status": "success",
            "topic": req.topic,
            "section_target": req.section_target,
            "hypothetical_doc": council_result.get("hypothetical_doc"),
            "ragas_faithfulness": council_result.get("ragas_faithfulness"),
            "ragas_relevance": council_result.get("ragas_relevance"),
            "critic_evaluations": council_result.get("critic_evaluations"),
            "final_questions": council_result.get("final_questions"),
            "agent_logs": council_result.get("agent_logs")
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Lỗi hội đồng tác tử: {str(e)}")

@app.post("/api/exams/generate-120")
def generate_full_exam(req: GenerateFullExamRequest, db: Session = Depends(get_db)):
    """
    Kích hoạt Hội đồng Tác tử LangGraph sinh trọn vẹn bộ đề 120 câu chuẩn ĐGNL.
    Tự động chuẩn hóa số thứ tự đề (02 -> 03 -> 04...) nếu bị trùng lặp.
    Chạy trong luồng nền và trả về task_id để frontend theo dõi tiến độ %.
    """
    final_title = resolve_next_exam_title(req.title, db)
    from backend.agent_council.full_exam_generator import full_exam_generator
    task_id = full_exam_generator.generate_full_exam_async(
        exam_title=final_title,
        topic_theme=req.theme or "Khoa học, Xã hội & Đổi mới"
    )
    return {"status": "started", "task_id": task_id, "resolved_title": final_title}

@app.get("/api/exams/generate-120/status/{task_id}")
def get_generation_status(task_id: str):
    """Truy vấn tiến độ sinh đề 120 câu theo thời gian thực (0% -> 100%)"""
    from backend.agent_council.full_exam_generator import GENERATION_TASKS
    task = GENERATION_TASKS.get(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Không tìm thấy tác vụ sinh đề.")
    return task

@app.get("/api/settings")
def get_settings():
    """Lấy trạng thái cấu hình hiện tại và số lượng key đang nạp"""
    from backend.agent_council.gemini_rotator import gemini_rotator
    gemini_rotator.reload_keys()
    return {
        "gemini_keys_count": len(gemini_rotator.keys),
        "gemini_model": os.getenv("GEMINI_MODEL", "gemini-2.5-flash"),
        "openai_configured": bool(os.getenv("OPENAI_API_KEY")),
        "openai_model": os.getenv("OPENAI_MODEL", "gpt-4o-mini")
    }

@app.post("/api/settings")
def update_settings(req: SaveSettingsRequest):
    """Cập nhật API Keys (nhiều key Gemini xoay vòng) và Model trong phiên làm việc"""
    env_path = Path(__file__).resolve().parent.parent / ".env"
    env_lines = []
    if env_path.exists():
        with open(env_path, "r", encoding="utf-8") as f:
            env_lines = f.readlines()

    def set_env_var(key, val):
        if val is None:
            return
        os.environ[key] = val
        found = False
        for i, line in enumerate(env_lines):
            if line.startswith(f"{key}="):
                env_lines[i] = f"{key}={val}\n"
                found = True
                break
        if not found:
            env_lines.append(f"{key}={val}\n")

    set_env_var("OPENAI_API_KEY", req.openai_api_key)
    set_env_var("GEMINI_API_KEY", req.gemini_api_key)
    set_env_var("GEMINI_API_KEYS", req.gemini_api_keys)
    if req.gemini_model:
        set_env_var("GEMINI_MODEL", req.gemini_model)
    if req.openai_model:
        set_env_var("OPENAI_MODEL", req.openai_model)

    with open(env_path, "w", encoding="utf-8") as f:
        f.writelines(env_lines)

    # Nạp lại keys cho rotator
    from backend.agent_council.gemini_rotator import gemini_rotator
    gemini_rotator.reload_keys()

    return {
        "status": "success",
        "message": f"Đã lưu cài đặt! Tổng số Gemini API Keys khả dụng: {len(gemini_rotator.keys)} keys."
    }

# Mount static files
app.mount("/static", StaticFiles(directory=str(STATIC_DIR)), name="static")

# Mount frontend
app.mount("/css", StaticFiles(directory=str(FRONTEND_DIR / "css")), name="css")
app.mount("/js", StaticFiles(directory=str(FRONTEND_DIR / "js")), name="js")

@app.get("/")
def serve_index():
    return FileResponse(FRONTEND_DIR / "index.html")

@app.get("/{full_path:path}")
def serve_spa(full_path: str):
    file_path = FRONTEND_DIR / full_path
    if file_path.is_file():
        return FileResponse(file_path)
    return FileResponse(FRONTEND_DIR / "index.html")
