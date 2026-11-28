import json
import uuid
import os
import re
from datetime import datetime
from pathlib import Path
import hashlib
from typing import Dict, Any, List, Optional
from fastapi import FastAPI, Depends, HTTPException, Body, Header
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
from sqlalchemy.orm import Session

from backend.config import (
    APP_TITLE, APP_VERSION, STATIC_DIR, FRONTEND_DIR,
    OPENAI_API_KEY, GEMINI_API_KEY, OPENAI_MODEL
)
from backend.database import init_db, get_db, ExamModel, SubmissionModel, UserModel
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

        # 3. Nạp 8 Đề Tham Khảo SPT (ĐH Sư phạm Hà Nội)
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
            else:
                existing_spt.data_json = json.dumps(propagate_passages(spt["questions"]), ensure_ascii=False)

        db.commit()

        # Tự động đồng bộ các hình vẽ và biểu đồ khoa học kỹ thuật
        from backend.exam_engine.update_db_diagrams import apply_diagrams_to_db
        apply_diagrams_to_db()
    except Exception as e:
        print(f"Error seeding exams: {e}")
        db.rollback()
    finally:
        db.close()

seed_benchmark_exam()

# --- Pydantic Schemas ---
class RegisterUserRequest(BaseModel):
    username: str
    password: str
    full_name: str
    student_class: Optional[str] = "12A1"
    school: Optional[str] = "THPT Chuyên"

class LoginUserRequest(BaseModel):
    username: str
    password: str

class SubmitExamRequest(BaseModel):
    candidate_name: Optional[str] = "Thí sinh ĐGNL"
    user_id: Optional[str] = None
    answers: Dict[str, Any] # { "1": "A", "17": {"a": "Đ", ...}, ... }
    time_spent_seconds: Optional[int] = 0

class GenerateAgentRequest(BaseModel):
    topic: str
    section_target: str = "language" # "language", "logic_data", "problem_solving"
    difficulty: str = "medium"
    count: int = 2

class GenerateFullExamRequest(BaseModel):
    title: Optional[str] = "Đề Thi ĐGNL 120 Câu AI Tự Động"
    theme: Optional[str] = "Khoa học, Xã hội & Đổi mới"
    mode: Optional[str] = "vact_full"
    user_id: Optional[str] = None
    role: Optional[str] = None

class SaveSettingsRequest(BaseModel):
    openai_api_key: Optional[str] = None
    gemini_api_key: Optional[str] = None
    gemini_api_keys: Optional[str] = None
    gemini_model: Optional[str] = None
    openai_model: Optional[str] = None

class BatchDeleteUsersRequest(BaseModel):
    user_ids: List[str]

class BatchDeleteSubmissionsRequest(BaseModel):
    submission_ids: List[str]

# --- API Endpoints ---

# --- Authentication & Student Profile Endpoints ---
def hash_password(password: str) -> str:
    return hashlib.sha256(password.strip().encode("utf-8")).hexdigest()

@app.post("/api/auth/register")
def register_student(req: RegisterUserRequest, db: Session = Depends(get_db)):
    """Đăng ký tài khoản học sinh mới"""
    uname = req.username.strip().lower()
    if not uname:
        raise HTTPException(status_code=400, detail="Tên đăng nhập không được để trống.")
    if len(req.password.strip()) < 3:
        raise HTTPException(status_code=400, detail="Mật khẩu phải từ 3 ký tự trở lên.")
    
    existing = db.query(UserModel).filter(UserModel.username == uname).first()
    if existing:
        raise HTTPException(status_code=400, detail=f"Tên tài khoản '{uname}' đã tồn tại, vui lòng chọn tên khác.")

    user_id = f"stu_{uuid.uuid4().hex[:10]}"
    user = UserModel(
        id=user_id,
        username=uname,
        password_hash=hash_password(req.password),
        full_name=req.full_name.strip() or "Học sinh",
        student_class=req.student_class.strip() if req.student_class else "12",
        school=req.school.strip() if req.school else "THPT"
    )
    db.add(user)
    db.commit()
    db.refresh(user)

    return {
        "status": "success",
        "message": "Đăng ký tài khoản thành công!",
        "user": user.to_dict()
    }

@app.post("/api/auth/login")
def login_student(req: LoginUserRequest, db: Session = Depends(get_db)):
    """Đăng nhập tài khoản học sinh"""
    uname = req.username.strip().lower()
    user = db.query(UserModel).filter(UserModel.username == uname).first()
    if not user:
        raise HTTPException(status_code=401, detail="Tài khoản không tồn tại trên hệ thống.")
    
    if user.password_hash != hash_password(req.password):
        raise HTTPException(status_code=401, detail="Mật khẩu không chính xác, vui lòng kiểm tra lại.")

    return {
        "status": "success",
        "message": f"Chào mừng {user.full_name} đăng nhập thành công!",
        "user": user.to_dict()
    }

@app.get("/api/auth/students")
def list_demo_students(db: Session = Depends(get_db)):
    """Danh sách học sinh (phục vụ chọn nhanh hồ sơ khi trình diễn KHKT)"""
    # Đảm bảo có tài khoản Admin mặc định
    admin_user = db.query(UserModel).filter(UserModel.username == "admin").first()
    if not admin_user:
        admin_user = UserModel(
            id="user_admin_root",
            username="admin",
            password_hash=hash_password("admin123"),
            full_name="Quản Trị Viên (Admin)",
            role="admin",
            student_class="Ban Giám Khảo / Quản Trị",
            school="Sở GD&ĐT / Hội Đồng KHKT"
        )
        db.add(admin_user)
        db.commit()

    users = db.query(UserModel).filter(UserModel.role != "admin").order_by(UserModel.created_at.desc()).limit(20).all()
    # Nếu chưa có học sinh nào, tự động seed 2 học sinh mẫu tiện cho thi cử & KHKT
    if not users:
        demo1 = UserModel(
            id="stu_ngoc_vy",
            username="ngocvy",
            password_hash=hash_password("123"),
            full_name="Nguyễn Ngọc Yến Vy",
            role="student",
            student_class="12A1",
            school="THPT Chuyên"
        )
        demo2 = UserModel(
            id="stu_minh_khoi",
            username="minhkhoi",
            password_hash=hash_password("123"),
            full_name="Trần Minh Khôi",
            role="student",
            student_class="12A2",
            school="THPT Chuyên"
        )
        db.add(demo1)
        demo_users = [demo1, demo2]
        db.add(demo2)
        db.commit()
        users = [demo1, demo2]

    return {
        "students": [u.to_dict() for u in users],
        "admin_available": True
    }

# --- ADMIN MANAGEMENT ENDPOINTS ---
@app.get("/api/admin/users")
def admin_list_all_users(admin_id: Optional[str] = None, db: Session = Depends(get_db)):
    """Admin xem danh sách toàn bộ tài khoản học sinh kèm thống kê số bài đã thi và điểm trung bình"""
    users = db.query(UserModel).order_by(UserModel.created_at.desc()).all()
    user_stats = []
    for u in users:
        subs = db.query(SubmissionModel).filter(SubmissionModel.user_id == u.id).all()
        exam_count = len(subs)
        avg_pct = round(sum([s.total_score / (10.0 if s.total_score <= 10.0 else 1200.0) * 100 for s in subs]) / exam_count, 1) if exam_count > 0 else 0.0
        user_stats.append({
            **u.to_dict(),
            "exam_count": exam_count,
            "avg_percentage": avg_pct,
            "latest_submission": subs[-1].submitted_at.strftime("%d/%m/%Y %H:%M") if exam_count > 0 and subs[-1].submitted_at else "Chưa thi"
        })
    return {"users": user_stats}

@app.delete("/api/admin/users/{user_id}")
def admin_delete_user(user_id: str, db: Session = Depends(get_db)):
    """Admin xóa tài khoản học sinh và toàn bộ bài thi liên quan"""
    u = db.query(UserModel).filter(UserModel.id == user_id).first()
    if not u:
        raise HTTPException(status_code=404, detail="Không tìm thấy tài khoản học sinh.")
    if u.role == "admin" or u.username == "admin":
        raise HTTPException(status_code=400, detail="Không thể xóa tài khoản Quản trị viên tối cao!")

    # Xóa cả submissions của học sinh này
    db.query(SubmissionModel).filter(SubmissionModel.user_id == user_id).delete()
    db.delete(u)
    db.commit()
    return {"status": "success", "message": f"Đã xóa học sinh '{u.full_name}' và dữ liệu bài thi liên quan!"}

@app.post("/api/admin/users/batch-delete")
def admin_batch_delete_users(req: BatchDeleteUsersRequest, db: Session = Depends(get_db)):
    """Admin xóa nhiều tài khoản học sinh đã chọn cùng lúc"""
    if not req.user_ids:
        return {"status": "success", "message": "Không có tài khoản nào được chọn.", "deleted_count": 0}

    users = db.query(UserModel).filter(UserModel.id.in_(req.user_ids)).all()
    deleted_count = 0
    for u in users:
        if u.role != "admin" and u.username != "admin":
            db.query(SubmissionModel).filter(SubmissionModel.user_id == u.id).delete()
            db.delete(u)
            deleted_count += 1
    db.commit()
    return {"status": "success", "message": f"Đã xóa thành công {deleted_count} tài khoản học sinh đã chọn!", "deleted_count": deleted_count}

@app.post("/api/admin/users/{user_id}/reset-password")
def admin_reset_password(user_id: str, new_pass: str = Body(..., embed=True), db: Session = Depends(get_db)):
    """Admin đặt lại mật khẩu cho học sinh"""
    u = db.query(UserModel).filter(UserModel.id == user_id).first()
    if not u:
        raise HTTPException(status_code=404, detail="Không tìm thấy tài khoản học sinh.")
    u.password_hash = hash_password(new_pass)
    db.commit()
    return {"status": "success", "message": f"Đã đổi mật khẩu cho học sinh '{u.full_name}' thành '{new_pass}'!"}

@app.get("/api/admin/leaderboard")
def admin_leaderboard(exam_id: Optional[str] = None, db: Session = Depends(get_db)):
    """
    Bảng vàng xếp hạng điểm số toàn hệ thống:
    Sắp xếp tất cả các bài thi từ CAO XUỐNG THẤP kèm tên học sinh, lớp, đề thi, thời gian và điểm số.
    """
    query = db.query(SubmissionModel)
    if exam_id and exam_id != "all":
        query = query.filter(SubmissionModel.exam_id == exam_id)

    subs = query.all()

    # Tính phần trăm điểm để sắp xếp công bằng giữa đề SPT (thang 10) và V-ACT (thang 1200)
    records = []
    for s in subs:
        exam = db.query(ExamModel).filter(ExamModel.id == s.exam_id).first()
        exam_title = exam.title if exam else "Bài thi ĐGNL"
        max_score = exam.max_score if (exam and exam.max_score) else (10.0 if (exam and exam.exam_type == "spt") else 1200.0)
        percentage = round((s.total_score / max_score) * 100.0, 1) if max_score > 0 else 0.0

        user = db.query(UserModel).filter(UserModel.id == s.user_id).first() if s.user_id else None
        student_class = user.student_class if user else "12"
        school = user.school if user else "THPT"

        records.append({
            "id": s.id,
            "candidate_name": s.candidate_name,
            "username": user.username if user else "khach",
            "student_class": student_class,
            "school": school,
            "exam_id": s.exam_id,
            "exam_title": exam_title,
            "total_score": s.total_score,
            "max_score": max_score,
            "percentage": percentage,
            "time_spent_seconds": s.time_spent_seconds,
            "submitted_at": s.submitted_at.strftime("%d/%m/%Y %H:%M") if s.submitted_at else ""
        })

    # Sắp xếp từ CAO XUỐNG THẤP theo percentage, sau đó theo total_score
    records.sort(key=lambda r: (r["percentage"], r["total_score"]), reverse=True)

    return {
        "leaderboard": records,
        "total_submissions": len(records)
    }

@app.delete("/api/admin/submissions/{submission_id}")
def admin_delete_single_submission(submission_id: str, db: Session = Depends(get_db)):
    """Admin xóa một bài làm cụ thể của thí sinh"""
    sub = db.query(SubmissionModel).filter(SubmissionModel.id == submission_id).first()
    if not sub:
        raise HTTPException(status_code=404, detail="Không tìm thấy bài làm cần xóa.")
    
    candidate = sub.candidate_name
    db.delete(sub)
    db.commit()
    return {"status": "success", "message": f"Đã xóa bài làm của thí sinh '{candidate}' thành công!"}

@app.post("/api/admin/submissions/batch-delete")
def admin_batch_delete_submissions(req: BatchDeleteSubmissionsRequest, db: Session = Depends(get_db)):
    """Admin xóa nhiều bài làm đã chọn cùng lúc"""
    if not req.submission_ids:
        return {"status": "success", "message": "Không có bài làm nào được chọn.", "deleted_count": 0}

    deleted_count = db.query(SubmissionModel).filter(SubmissionModel.id.in_(req.submission_ids)).delete(synchronize_session=False)
    db.commit()
    return {"status": "success", "message": f"Đã xóa thành công {deleted_count} bài làm đã chọn!", "deleted_count": deleted_count}

@app.delete("/api/admin/submissions")
def admin_delete_all_submissions(db: Session = Depends(get_db)):
    """Admin xóa toàn bộ bài làm của tất cả thí sinh để làm mới kỳ thi"""
    count = db.query(SubmissionModel).count()
    db.query(SubmissionModel).delete()
    db.commit()
    return {"status": "success", "message": f"Đã xóa toàn bộ {count} bài làm của thí sinh thành công!"}

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
    
    # Phân tích năng lực chuyên sâu (Pandas & Scipy & IRT Item Response Theory)
    competency_analysis = calculate_competency_insights(
        grade_report["domain_stats"], 
        grade_report["total_score"],
        max_score=exam_max_score,
        is_spt=grade_report.get("is_spt", False),
        detailed_results=grade_report.get("detailed_results", [])
    )
    
    # Vẽ Biểu đồ Mạng nhện Radar Chart (Matplotlib)
    radar_image_base64 = generate_radar_chart_base64(
        grade_report["domain_stats"], 
        is_spt=grade_report.get("is_spt", False)
    )

    # Sinh lời khuyên ôn tập cá nhân hóa từ Chuyên gia AI
    ai_advice = generate_personalized_advice(
        grade_report["domain_stats"],
        grade_report["total_score"],
        max_score=exam_max_score,
        is_spt=grade_report.get("is_spt", False),
        exam_title=exam.title
    )

    # Lưu kết quả nộp bài vào DB (gắn kết user_id nếu có)
    sub_id = f"sub_{uuid.uuid4().hex[:12]}"
    submission = SubmissionModel(
        id=sub_id,
        user_id=req.user_id,
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

def format_submission_for_analytics(sub: SubmissionModel, db: Session):
    results = json.loads(sub.results_json) if sub.results_json else {}
    radar_data = json.loads(sub.radar_data_json) if sub.radar_data_json else {}
    competency = radar_data.get("competency", {})
    radar_image = radar_data.get("radar_image", "")
    
    # If radar_image is missing or empty, regenerate dynamically
    if not radar_image and "domain_stats" in results:
        try:
            radar_image = generate_radar_chart_base64(
                results["domain_stats"],
                is_spt=results.get("is_spt", False)
            )
        except Exception as e:
            print(f"Error generating radar image on format: {e}")

    # If competency is missing, recalculate it
    if not competency and "domain_stats" in results:
        try:
            exam = db.query(ExamModel).filter(ExamModel.id == sub.exam_id).first()
            exam_max = exam.max_score if exam and exam.max_score else (10.0 if results.get("is_spt") else 1200.0)
            competency = calculate_competency_insights(
                results["domain_stats"],
                sub.total_score,
                max_score=exam_max,
                is_spt=results.get("is_spt", False),
                detailed_results=results.get("detailed_results", [])
            )
        except Exception as e:
            print(f"Error generating competency on format: {e}")

    exam = db.query(ExamModel).filter(ExamModel.id == sub.exam_id).first()
    exam_title = exam.title if exam else "Bài thi ĐGNL"

    return {
        "submission_id": sub.id,
        "exam_id": sub.exam_id,
        "exam_title": exam_title,
        "candidate_name": sub.candidate_name,
        "time_spent_seconds": sub.time_spent_seconds,
        "grade_report": results,
        "competency_analysis": competency,
        "radar_image": radar_image,
        "ai_advice": sub.ai_advice,
        "submitted_at": sub.submitted_at.strftime("%d/%m/%Y %H:%M") if sub.submitted_at else ""
    }

@app.get("/api/submissions/latest")
def get_latest_submission(user_id: Optional[str] = None, candidate_name: Optional[str] = None, db: Session = Depends(get_db)):
    query = db.query(SubmissionModel)
    sub = None
    if user_id:
        sub = query.filter(SubmissionModel.user_id == user_id).order_by(SubmissionModel.submitted_at.desc()).first()
    elif candidate_name:
        sub = query.filter(SubmissionModel.candidate_name == candidate_name).order_by(SubmissionModel.submitted_at.desc()).first()

    # Fallback to latest overall submission in the system if no user-specific submission found
    if not sub:
        sub = db.query(SubmissionModel).order_by(SubmissionModel.submitted_at.desc()).first()

    if not sub:
        return {"has_submission": False, "data": None}

    formatted = format_submission_for_analytics(sub, db)
    return {"has_submission": True, "data": formatted}

@app.get("/api/submissions/{submission_id}/analytics")
def get_submission_analytics(submission_id: str, db: Session = Depends(get_db)):
    sub = db.query(SubmissionModel).filter(SubmissionModel.id == submission_id).first()
    if not sub:
        raise HTTPException(status_code=404, detail="Không tìm thấy kết quả làm bài.")
    return format_submission_for_analytics(sub, db)

@app.get("/api/submissions/{submission_id}")
def get_submission(submission_id: str, user_id: Optional[str] = None, db: Session = Depends(get_db)):
    """
    Xem chi tiết kết quả bài thi.
    BẢO MẬT: Nếu submission đã gắn với một user_id cụ thể, chỉ cho phép đúng user_id đó xem!
    """
    sub = db.query(SubmissionModel).filter(SubmissionModel.id == submission_id).first()
    if not sub:
        raise HTTPException(status_code=404, detail="Không tìm thấy kết quả làm bài.")
    
    # Kiểm tra phân quyền: nếu bài thi có chủ sở hữu và có yêu cầu kiểm tra user_id
    if sub.user_id and user_id and sub.user_id != user_id:
        raise HTTPException(status_code=403, detail="Bạn không có quyền xem bài làm của học sinh khác!")

    return sub.to_dict()

from fastapi.responses import HTMLResponse

@app.get("/api/exams/{exam_id}/print", response_class=HTMLResponse)
def print_exam_paper(exam_id: str, db: Session = Depends(get_db)):
    """
    Xuất đề thi ra định dạng in ấn chuẩn khảo thí (A4 Printable PDF).
    Bao gồm: Quốc hiệu, Tiêu đề kỳ thi, Mã đề, Hướng dẫn làm bài và Bảng đáp án trang cuối.
    """
    exam = db.query(ExamModel).filter(ExamModel.id == exam_id).first()
    if not exam:
        raise HTTPException(status_code=404, detail="Không tìm thấy đề thi.")

    questions = json.loads(exam.data_json) if exam.data_json else []
    is_spt = (exam.exam_type == "spt")
    univ_header = "TRƯỜNG ĐẠI HỌC SƯ PHẠM HÀ NỘI" if is_spt else "ĐẠI HỌC QUỐC GIA TP. HỒ CHÍ MINH"
    exam_badge = f"KỲ THI ĐÁNH GIÁ NĂNG LỰC ({'SPT' if is_spt else 'V-ACT'})"

    # Xây dựng HTML danh sách câu hỏi
    questions_html = []
    answer_keys = []

    for q in questions:
        q_num = q.get("question_number", 1)
        prompt = q.get("prompt", "")
        q_type = q.get("question_type", "multiple_choice")
        ans_raw = q.get("correct_answer", "")

        opt_html = ""
        if q_type == "multiple_choice":
            options = q.get("options", {})
            opt_items = "".join([f'<div class="print-opt"><strong>{k}.</strong> {v}</div>' for k, v in options.items()])
            opt_html = f'<div class="print-opts-grid">{opt_items}</div>'
            answer_keys.append((q_num, str(ans_raw)))
        elif q_type == "true_false":
            tf_map = q.get("tf_statements", {})
            rows = "".join([f'<tr><td style="width: 30px; text-align: center;">{k}</td><td>{v}</td><td style="width: 60px; text-align: center;">[ &nbsp; ]</td></tr>' for k, v in tf_map.items()])
            opt_html = f'<table class="print-tf-table"><thead><tr><th>Ý</th><th>Nội dung nhận định</th><th>Đúng/Sai</th></tr></thead><tbody>{rows}</tbody></table>'
            c_dict = ans_raw if isinstance(ans_raw, dict) else {}
            ans_str = ", ".join([f"{k}:{v}" for k, v in c_dict.items()])
            answer_keys.append((q_num, ans_str))
        elif q_type in ["short_answer", "fill_blank"]:
            opt_html = '<div class="print-short-ans"><em>Đáp số của thí sinh:</em> ........................................................................................</div>'
            answer_keys.append((q_num, str(ans_raw)))
        elif q_type == "essay":
            opt_html = '<div class="print-essay-space"><div class="print-dots"></div></div>'
            answer_keys.append((q_num, "Theo barem"))

        questions_html.append(f"""
        <div class="print-question">
          <div class="print-q-title"><strong>Câu {q_num}:</strong> {prompt}</div>
          {opt_html}
        </div>
        """)

    # Bảng đáp án ở cuối
    key_rows = "".join([f'<div class="key-cell"><strong>{k}:</strong> {v}</div>' for k, v in answer_keys])

    html_content = f"""<!DOCTYPE html>
<html lang="vi">
<head>
  <meta charset="UTF-8">
  <title>{exam.title} - Đề Thi Chuẩn In Ấn</title>
  <!-- KaTeX for math rendering -->
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css">
  <script src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js"></script>
  <style>
    @page {{
      size: A4;
      margin: 15mm 15mm 15mm 15mm;
    }}
    body {{
      font-family: 'Times New Roman', Times, serif;
      font-size: 13pt;
      line-height: 1.45;
      color: #000;
      background: #fff;
      margin: 0;
      padding: 10px;
    }}
    .print-header {{
      display: flex;
      justify-content: space-between;
      border-bottom: 2px solid #000;
      padding-bottom: 8px;
      margin-bottom: 15px;
    }}
    .header-left, .header-right {{
      width: 48%;
      text-align: center;
    }}
    .header-left h3, .header-right h3 {{
      margin: 0 0 4px 0;
      font-size: 12pt;
      font-weight: bold;
    }}
    .exam-title-box {{
      text-align: center;
      margin: 15px 0;
    }}
    .exam-title-box h1 {{
      font-size: 16pt;
      margin: 0 0 5px 0;
      text-transform: uppercase;
    }}
    .exam-meta {{
      font-style: italic;
      font-size: 11pt;
    }}
    .candidate-info-box {{
      border: 1px dashed #444;
      padding: 8px 12px;
      margin-bottom: 18px;
      font-size: 11pt;
      display: flex;
      justify-content: space-between;
    }}
    .print-question {{
      margin-bottom: 12px;
      page-break-inside: avoid;
    }}
    .print-q-title {{
      margin-bottom: 4px;
      text-align: justify;
    }}
    .print-opts-grid {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 4px 20px;
      padding-left: 15px;
    }}
    .print-tf-table {{
      width: 100%;
      border-collapse: collapse;
      margin-top: 6px;
      font-size: 11pt;
    }}
    .print-tf-table th, .print-tf-table td {{
      border: 1px solid #000;
      padding: 4px 8px;
    }}
    .print-short-ans {{
      margin-top: 6px;
      padding-left: 15px;
    }}
    .print-essay-space {{
      margin-top: 8px;
      min-height: 80px;
      border: 1px dotted #888;
      border-radius: 4px;
    }}
    .page-break {{
      page-break-before: always;
    }}
    .keys-section {{
      margin-top: 30px;
      border-top: 2px solid #000;
      padding-top: 15px;
    }}
    .keys-grid {{
      display: grid;
      grid-template-columns: repeat(6, 1fr);
      gap: 6px;
      font-size: 10pt;
    }}
    .key-cell {{
      border: 1px solid #ccc;
      padding: 3px 6px;
      text-align: center;
    }}
    .no-print {{
      background: #4f46e5;
      color: #fff;
      padding: 10px 20px;
      position: sticky;
      top: 0;
      text-align: center;
      margin-bottom: 15px;
      border-radius: 6px;
      box-shadow: 0 4px 10px rgba(0,0,0,0.15);
    }}
    .btn-print {{
      background: #10b981;
      color: #fff;
      border: none;
      padding: 8px 18px;
      font-size: 14px;
      font-weight: bold;
      border-radius: 4px;
      cursor: pointer;
      margin-left: 15px;
    }}
    @media print {{
      .no-print {{ display: none; }}
      body {{ padding: 0; }}
    }}
  </style>
</head>
<body>
  <div class="no-print">
    <span>🖨️ Chế độ In Đề Thi Chuẩn Khảo Thí (A4 Printable Layout)</span>
    <button class="btn-print" onclick="window.print()">In Đề Thi / Lưu PDF</button>
  </div>

  <div class="print-header">
    <div class="header-left">
      <h3>{univ_header}</h3>
      <div>HỘI ĐỒNG KHẢO THÍ CHUẨN HÓA</div>
      <div style="font-weight: bold; margin-top: 4px;">MÃ ĐỀ THI: {exam.id[-4:].upper()}</div>
    </div>
    <div class="header-right">
      <h3>CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM</h3>
      <div style="text-decoration: underline;">Độc lập - Tự do - Hạnh phúc</div>
      <div style="font-style: italic; margin-top: 4px;">Ngày thi: ...../...../2026</div>
    </div>
  </div>

  <div class="exam-title-box">
    <h1>{exam.title}</h1>
    <div class="exam-meta">
      Thời gian làm bài: <strong>{exam.duration_minutes} phút</strong> (Không kể thời gian phát đề) • Số lượng: <strong>{exam.total_questions} câu hỏi</strong>
    </div>
  </div>

  <div class="candidate-info-box">
    <div>Họ và tên thí sinh: ............................................................................</div>
    <div>Số báo danh: .................................</div>
    <div>Phòng thi: ....................</div>
  </div>

  <div class="questions-container">
    {''.join(questions_html)}
  </div>

  <div class="page-break"></div>

  <div class="keys-section">
    <h3 style="text-align: center; text-transform: uppercase;">BẢNG ĐÁP ÁN CHUẨN KHẢO THÍ (DÀNH CHO GIÁO VIÊN / CHẤM THI)</h3>
    <div class="keys-grid">
      {key_rows}
    </div>
  </div>

  <script>
    document.addEventListener("DOMContentLoaded", function() {{
      if (typeof renderMathInElement === 'function') {{
        renderMathInElement(document.body, {{
          delimiters: [
            {{ left: '$$', right: '$$', display: true }},
            {{ left: '$', right: '$', display: false }}
          ]
        }});
      }}
    }});
  </script>
</body>
</html>
"""
    return HTMLResponse(content=html_content)

@app.get("/api/history")
def get_submission_history(user_id: Optional[str] = None, candidate_name: Optional[str] = None, db: Session = Depends(get_db)):
    """
    Lấy danh sách lịch sử nộp bài thi để vẽ biểu đồ tiến bộ năng lực.
    CÔ LẬP DỮ LIỆU: Nếu truyền user_id hoặc candidate_name, chỉ trả về bài thi của chính học sinh đó!
    """
    query = db.query(SubmissionModel)
    if user_id:
        query = query.filter(SubmissionModel.user_id == user_id)
    elif candidate_name:
        query = query.filter(SubmissionModel.candidate_name == candidate_name)
    
    subs = query.order_by(SubmissionModel.submitted_at.desc()).limit(30).all()
    history = []
    for s in subs:
        exam = db.query(ExamModel).filter(ExamModel.id == s.exam_id).first()
        exam_title = exam.title if exam else "Bài thi ĐGNL"
        max_s = exam.max_score if (exam and exam.max_score) else (10.0 if (exam and exam.exam_type == "spt") else 1200.0)
        history.append({
            "id": s.id,
            "user_id": s.user_id,
            "candidate_name": s.candidate_name,
            "exam_id": s.exam_id,
            "exam_title": exam_title,
            "submitted_at": s.submitted_at.strftime("%d/%m/%Y %H:%M") if s.submitted_at else "",
            "total_score": s.total_score,
            "max_score": max_s,
            "percentage": round(s.total_score / max_s * 100.0, 1) if max_s > 0 else 0,
            "time_spent_seconds": s.time_spent_seconds
        })
    return {"history": history}

class AskTutorRequest(BaseModel):
    prompt: str
    user_answer: Optional[Any] = None
    correct_answer: Optional[Any] = None
    explanation: Optional[str] = None
    question_type: Optional[str] = "multiple_choice"
    student_query: Optional[str] = None

@app.post("/api/exams/ask-tutor")
def ask_ai_tutor(req: AskTutorRequest):
    """
    Gia sư AI Sư phạm (Interactive Pedagogical AI Tutor):
    Giải thích cặn kẽ câu hỏi, phân tích lý do học sinh chọn sai, và gợi ý phương pháp giải thông minh.
    """
    from backend.agent_council.gemini_rotator import gemini_rotator

    system_prompt = f"""Bạn là Thầy/Cô Gia Sư Khảo Thí giàu kinh nghiệm sư phạm, kiên nhẫn, gần gũi và truyền cảm hứng.
Học sinh vừa làm một câu hỏi trong đề thi thử Đánh giá năng lực và muốn được thầy/cô giải đáp cặn kẽ.

THÔNG TIN CÂU HỎI:
- Nội dung câu hỏi: {req.prompt}
- Dạng câu hỏi: {req.question_type}
- Câu trả lời của học sinh: {req.user_answer}
- Đáp án chính xác: {req.correct_answer}
- Hướng dẫn giải chuẩn: {req.explanation}

CÂU HỎI / THẮC MẮC CỦA HỌC SINH:
{req.student_query or "Thầy/Cô hãy giải thích tại sao câu này lại chọn đáp án như vậy và con bị sai ở bước tư duy nào ạ?"}

HƯỚNG DẪN TRẢ LỜI:
1. Thân thiện, khen ngợi tinh thần học hỏi của học sinh.
2. Phân tích rõ ràng: Vì sao học sinh chọn {req.user_answer} là bị bẫy ở đâu (lỗi kiến thức hay lỗi đọc đề).
3. Hướng dẫn từng bước tư duy để tìm ra đáp án đúng {req.correct_answer}.
4. Đưa ra 1 mẹo (Tip) làm bài nhanh cho dạng câu này để lần sau không mắc lại.
Định dạng câu trả lời bằng Markdown rõ ràng, dùng KaTeX LaTeX cho công thức toán ($...$).
"""

    try:
        success, reply, key_mask = gemini_rotator.generate_content(prompt=system_prompt)
        if success and reply:
            return {"tutor_reply": reply}
    except Exception as e:
        print(f"Error calling AI tutor: {e}")

    return {
        "tutor_reply": f"**Gia sư AI Sư phạm:**\n\nChào bạn! Câu hỏi này có đáp án chính xác là **{req.correct_answer}**.\n\n**Hướng dẫn giải chi tiết:**\n{req.explanation or 'Hãy chú ý đọc kỹ dữ kiện đề bài và áp dụng đúng công thức cơ bản.'}\n\n*💡 Mẹo khảo thí:* Hãy gạch chân từ khóa chính trong câu hỏi để tránh các phương án gây nhiễu nhé!"
    }

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
    Kích hoạt Hội đồng Tác tử LangGraph sinh đề:
    BẢO MẬT PHÂN QUYỀN: Chỉ tài khoản Admin mới có quyền tạo đề thi mới!
    Học sinh chỉ có quyền xem đề và làm bài.
    """
    # Kiểm tra quyền Admin
    if req.role != "admin":
        # Xác minh trong database nếu có user_id
        is_admin = False
        if req.user_id:
            u = db.query(UserModel).filter(UserModel.id == req.user_id).first()
            if u and (u.role == "admin" or u.username == "admin"):
                is_admin = True
        if not is_admin:
            raise HTTPException(status_code=403, detail="Chỉ Quản trị viên (Admin) mới có quyền tạo đề thi mới. Học sinh chỉ được phép làm bài thi!")

    mode = (req.mode or "vact_full").strip()
    title_raw = (req.title or "").strip()
    theme_raw = (req.theme or "").strip()

    from backend.agent_council.full_exam_generator import SPT_CONFIGS, full_exam_generator

    if mode in SPT_CONFIGS:
        cfg = SPT_CONFIGS[mode]
        final_title = title_raw or f"Đề Tham Khảo SPT ĐH Sư Phạm Hà Nội - Môn {cfg['name']}"
    else:
        mode = "vact_full"
        final_title = resolve_next_exam_title(title_raw, db)

    task_id = full_exam_generator.generate_full_exam_async(
        exam_title=final_title,
        topic_theme=theme_raw or "Chương trình GDPT 2018",
        mode=mode
    )
    return {"status": "started", "task_id": task_id, "resolved_title": final_title, "mode": mode}

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
        "gemini_model": gemini_rotator.model or os.getenv("GEMINI_MODEL", "gemini-flash-lite-latest"),
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

    # Nạp lại keys và model cho rotator
    from backend.agent_council.gemini_rotator import gemini_rotator
    if req.gemini_model:
        gemini_rotator.model = req.gemini_model
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
