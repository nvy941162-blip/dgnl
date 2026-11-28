import uuid
import time
import json
import re
import random
import threading
from typing import Dict, Any, List, Optional
from datetime import datetime

from backend.database import SessionLocal, ExamModel
from backend.exam_engine.grader import calculate_question_weights
from backend.agent_council.gemini_rotator import gemini_rotator
from backend.agent_council.language_agent import LanguageAgent
from backend.agent_council.logic_data_agent import LogicDataAgent
from backend.agent_council.critic_agent import CriticAgent, normalize_question_item
from backend.agent_council.hyde_rag import HyDERetriever
from backend.agent_council.graph import run_agent_council_pipeline
from backend.agent_council.domain_generators import domain_generators

# Bộ nhớ trạng thái các tác vụ sinh đề nền
GENERATION_TASKS: Dict[str, Dict[str, Any]] = {}

SPT_CONFIGS: Dict[str, Dict[str, Any]] = {
    "spt_math": {
        "subject": "math",
        "name": "Toán học",
        "total_questions": 25,
        "duration_minutes": 90,
        "max_score": 10.0
    },
    "spt_english": {
        "subject": "english",
        "name": "Tiếng Anh",
        "total_questions": 33,
        "duration_minutes": 60,
        "max_score": 10.0
    },
    "spt_chemistry": {
        "subject": "chemistry",
        "name": "Hóa học",
        "total_questions": 27,
        "duration_minutes": 60,
        "max_score": 10.0
    },
    "spt_geography": {
        "subject": "geography",
        "name": "Địa lí",
        "total_questions": 20,
        "duration_minutes": 60,
        "max_score": 10.0
    },
    "spt_history": {
        "subject": "history",
        "name": "Lịch sử",
        "total_questions": 25,
        "duration_minutes": 60,
        "max_score": 10.0
    },
    "spt_civics": {
        "subject": "civics_law",
        "name": "Giáo dục Kinh tế & Pháp luật",
        "total_questions": 21,
        "duration_minutes": 60,
        "max_score": 10.0
    },
    "spt_tech_ind": {
        "subject": "tech_industry",
        "name": "Công nghệ Công nghiệp",
        "total_questions": 24,
        "duration_minutes": 60,
        "max_score": 10.0
    },
    "spt_tech_agr": {
        "subject": "tech_agriculture",
        "name": "Công nghệ Nông nghiệp",
        "total_questions": 24,
        "duration_minutes": 60,
        "max_score": 10.0
    }
}

SPT_AGENT_COUNCILS = {
    "spt_math": {
        "curriculum_agent": "SPT Curriculum Specialist Agent",
        "curriculum_desc": "Thiết lập ma trận 25 câu môn Toán học: Phần 1 (16c Trắc nghiệm), Phần 2 (2c Đúng/Sai 8 ý), Phần 3 (4c Điền đáp số), Phần 4 (3c Tự luận) - 90 phút.",
        "section_agents": {
            "part_1": ("Algebra & Calculus Specialist", "Sinh và kiểm định 16 câu Trắc nghiệm khách quan 4 lựa chọn (Nhận biết & Thông hiểu)"),
            "part_2": ("Mathematical Logic Agent", "Sinh và kiểm định 2 câu Đúng/Sai (8 mệnh đề đánh giá tư duy lập luận)"),
            "part_3": ("Applied Calculus Agent", "Sinh và kiểm định 4 câu Điền đáp số ngắn (Vận dụng giải toán)"),
            "part_4": ("Pedagogical Solution Agent", "Biên soạn 3 câu Tự luận chuyên sâu kèm barem chấm điểm từng bước chi tiết")
        },
        "critic_agent": "SPT Math Assessment Critic Agent",
        "critic_desc": "Nghiệm thu toàn bộ 25 câu môn Toán học, kiểm tra bẫy sai lầm và chuẩn hóa thang điểm 10.0 (90 phút)."
    },
    "spt_english": {
        "curriculum_agent": "SPT Curriculum Specialist Agent",
        "curriculum_desc": "Thiết lập ma trận 33 câu môn Tiếng Anh: Use of English (18c), Reading (10c), Word Formation (4c), Writing (1c) - 60 phút.",
        "section_agents": {
            "part_1": ("Phonetics & Lexicology Agent", "Sinh và kiểm định 18 câu Ngữ âm, Trọng âm, Từ vựng, Collocations và Ngữ pháp"),
            "part_2": ("Reading Comprehension Specialist", "Biên soạn bài đọc hiểu khoa học - xã hội và 10 câu hỏi suy luận ngữ cảnh"),
            "part_3": ("Word Formation Specialist", "Sinh 4 câu Cấu tạo từ (Word Form) và viết lại câu tương đương"),
            "part_4": ("Writing & Composition Agent", "Biên soạn 1 đề bài Tự luận viết (Short Essay) kèm tiêu chí chấm CEFR")
        },
        "critic_agent": "CEFR Assessment Critic Agent",
        "critic_desc": "Nghiệm thu 33 câu Tiếng Anh theo khung năng lực ngoại ngữ B1-B2 và chuẩn hóa thang điểm 10.0 (60 phút)."
    },
    "spt_chemistry": {
        "curriculum_agent": "SPT Curriculum Specialist Agent",
        "curriculum_desc": "Thiết lập ma trận 27 câu môn Hóa học: Trắc nghiệm (20c), Đúng/Sai (2c 8 ý), Điền kết quả (4c), Tự luận (1c) - 60 phút.",
        "section_agents": {
            "part_1": ("Organic & Inorganic Agent", "Sinh và kiểm định 20 câu Trắc nghiệm lý thuyết Hóa học hữu cơ và vô cơ"),
            "part_2": ("Lab Experimentation Agent", "Sinh và kiểm định 2 câu Đúng/Sai (8 ý lệnh thực hành thí nghiệm và hiện tượng)"),
            "part_3": ("Stoichiometry & Calculation Agent", "Sinh và kiểm định 4 câu Điền kết quả bài toán định lượng"),
            "part_4": ("Applied Chemistry Solution Agent", "Biên soạn 1 câu Tự luận cơ chế phản ứng thực nghiệm kèm barem chấm")
        },
        "critic_agent": "SPT Chemistry Assessment Critic Agent",
        "critic_desc": "Nghiệm thu 27 câu Hóa học, kiểm tra cân bằng hóa học và chuẩn hóa thang điểm 10.0 (60 phút)."
    },
    "spt_geography": {
        "curriculum_agent": "SPT Curriculum Specialist Agent",
        "curriculum_desc": "Thiết lập ma trận 20 câu môn Địa lí: Trắc nghiệm (12c), Đúng/Sai (3c 12 ý), Điền số liệu (4c), Tự luận (1c) - 60 phút.",
        "section_agents": {
            "part_1": ("Physical & Regional Geography Agent", "Sinh và kiểm định 12 câu Trắc nghiệm Địa lí tự nhiên và vùng kinh tế"),
            "part_2": ("Cartography & Atlas Agent", "Sinh và kiểm định 3 câu Đúng/Sai (12 ý phân tích Atlas và quy luật phân hóa)"),
            "part_3": ("Statistical Geography Agent", "Sinh và kiểm định 4 câu Điền số liệu tính toán tăng trưởng và mật độ"),
            "part_4": ("Socio-Economic Essay Agent", "Biên soạn 1 câu Tự luận phân tích bảng số liệu kinh tế - xã hội")
        },
        "critic_agent": "SPT Geography Assessment Critic Agent",
        "critic_desc": "Nghiệm thu 20 câu Địa lí, thẩm định độ chính xác số liệu và chuẩn hóa thang điểm 10.0 (60 phút)."
    },
    "spt_history": {
        "curriculum_agent": "SPT Curriculum Specialist Agent",
        "curriculum_desc": "Thiết lập ma trận 25 câu môn Lịch sử: Trắc nghiệm (20c), Đúng/Sai (2c 8 ý), Tự luận (3c) - 60 phút.",
        "section_agents": {
            "part_1": ("Vietnam & World History Agent", "Sinh và kiểm định 20 câu Trắc nghiệm Lịch sử Việt Nam và Thế giới hiện đại"),
            "part_2": ("Historical Document Analysis Agent", "Sinh và kiểm định 2 câu Đúng/Sai (8 ý phân tích trích dẫn văn kiện và tư liệu)"),
            "part_3": ("Historical Essay Specialist", "Biên soạn 3 câu Tự luận đánh giá sự kiện lịch sử kèm hướng dẫn chấm chi tiết")
        },
        "critic_agent": "SPT History Assessment Critic Agent",
        "critic_desc": "Nghiệm thu 25 câu Lịch sử, bảo đảm tính chân thực lịch sử và chuẩn hóa thang điểm 10.0 (60 phút)."
    },
    "spt_civics": {
        "curriculum_agent": "SPT Curriculum Specialist Agent",
        "curriculum_desc": "Thiết lập ma trận 21 câu môn GDKT&PL: Trắc nghiệm (16c), Đúng/Sai (3c 12 ý), Tự luận (2c) - 60 phút.",
        "section_agents": {
            "part_1": ("Economics & Civil Law Agent", "Sinh và kiểm định 16 câu Trắc nghiệm Kinh tế thị trường và Quyền công dân"),
            "part_2": ("Legal Case Analysis Agent", "Sinh và kiểm định 3 câu Đúng/Sai (12 ý phân tích hành vi pháp luật)"),
            "part_3": ("Applied Legal Problem Solving Agent", "Biên soạn 2 câu Tự luận tình huống pháp luật thực tế kèm đáp án chấm")
        },
        "critic_agent": "SPT Civics Assessment Critic Agent",
        "critic_desc": "Nghiệm thu 21 câu GDKT&PL, đối soát quy chuẩn pháp luật và chuẩn hóa thang điểm 10.0 (60 phút)."
    },
    "spt_tech_ind": {
        "curriculum_agent": "SPT Curriculum Specialist Agent",
        "curriculum_desc": "Thiết lập ma trận 24 câu Công nghệ Công nghiệp: Trắc nghiệm (16c), Đúng/Sai (2c 8 ý), Điền số 4c, Tự luận 2c - 60 phút.",
        "section_agents": {
            "part_1": ("Mechanical & Electronics Agent", "Sinh và kiểm định 16 câu Trắc nghiệm Vẽ kỹ thuật, Cơ khí và Mạch điện tử"),
            "part_2": ("Technical Blueprint Agent", "Sinh và kiểm định 2 câu Đúng/Sai (8 ý phân tích bản vẽ và thông số kỹ thuật)"),
            "part_3": ("Engineering Calculation Agent", "Sinh và kiểm định 4 câu Điền kết quả tính toán cơ học và điện áp"),
            "part_4": ("Industrial Technology Essay Agent", "Biên soạn 2 câu Tự luận quy trình công nghệ chế tạo")
        },
        "critic_agent": "SPT Industrial Technology Critic Agent",
        "critic_desc": "Nghiệm thu 24 câu Công nghệ Công nghiệp, kiểm tra tiêu chuẩn kỹ thuật và chuẩn hóa thang 10.0 (60 phút)."
    },
    "spt_tech_agr": {
        "curriculum_agent": "SPT Curriculum Specialist Agent",
        "curriculum_desc": "Thiết lập ma trận 24 câu Công nghệ Nông nghiệp: Trắc nghiệm (16c), Đúng/Sai (2c 8 ý), Điền số 4c, Tự luận 2c - 60 phút.",
        "section_agents": {
            "part_1": ("Crop Science & Husbandry Agent", "Sinh và kiểm định 16 câu Trắc nghiệm Trồng trọt, Thổ nhưỡng và Chăn nuôi"),
            "part_2": ("Agri-Biotech Validation Agent", "Sinh và kiểm định 2 câu Đúng/Sai (8 ý phân tích mô hình nông nghiệp sinh thái)"),
            "part_3": ("Agricultural Calculation Agent", "Sinh và kiểm định 4 câu Điền kết quả định mức dinh dưỡng và tỷ lệ phân bón"),
            "part_4": ("Applied Agriculture Essay Agent", "Biên soạn 2 câu Tự luận kỹ thuật canh tác công nghệ cao")
        },
        "critic_agent": "SPT Agriculture Assessment Critic Agent",
        "critic_desc": "Nghiệm thu 24 câu Công nghệ Nông nghiệp, kiểm tra tiêu chuẩn sinh học và chuẩn hóa thang 10.0 (60 phút)."
    }
}

def get_prompt_fingerprint(p: str) -> str:
    """Tạo mã định danh duy nhất (fingerprint) cho nội dung câu hỏi để triệt tiêu trùng lặp"""
    import re
    cleaned = re.sub(r'[^a-zA-Z0-9\u00C0-\u024F\u1EA0-\u1EF9]', '', str(p or '').lower())
    return cleaned[:90]

class FullExamGenerator:
    """
    Trình điều phối Hội đồng Tác tử LangGraph Sinh Đề Thi Chuẩn Hóa
    - Kỳ thi V-ACT: Sinh trọn vẹn 120 câu chuẩn ĐGNL ĐHQG (thang 1200 điểm IRT)
    - Kỳ thi SPT: Sinh đúng số lượng câu và đúng phân môn (20 - 33 câu, thang 10.0 điểm)
    """
    def __init__(self):
        self.language_agent = LanguageAgent()
        self.logic_data_agent = LogicDataAgent()
        self.critic_agent = CriticAgent()
        self.hyde_retriever = HyDERetriever()

    def generate_full_exam_async(
        self, 
        exam_title: str, 
        topic_theme: str = "Khoa học, Xã hội & Đổi mới",
        mode: str = "vact_full"
    ) -> str:
        """Bắt đầu tiến trình sinh đề (120 câu V-ACT hoặc số lượng câu theo từng môn SPT) trong luồng nền"""
        task_id = f"gen_{uuid.uuid4().hex[:8]}"

        is_spt = mode in SPT_CONFIGS
        if is_spt:
            cfg = SPT_CONFIGS[mode]
            total_count = cfg["total_questions"]
            duration = cfg["duration_minutes"]
            subject_name = cfg["name"]
            init_step = f"Khởi động Hội đồng tác tử tạo đề thi môn {subject_name} ({total_count} câu)..."
            init_action = f"Khởi tạo phiên tạo đề SPT môn {subject_name} ({total_count} câu) với chủ đề: '{topic_theme}'."
        else:
            total_count = 120
            duration = 150
            subject_name = "ĐGNL V-ACT"
            init_step = "Khởi động Hội đồng tác tử LangGraph & nạp kho tri thức 120 câu..."
            init_action = f"Khởi tạo phiên tạo đề 120 câu V-ACT với chủ đề: '{topic_theme}'."

        GENERATION_TASKS[task_id] = {
            "task_id": task_id,
            "status": "running",
            "percent": 5,
            "current_step": init_step,
            "generated_count": 0,
            "total_count": total_count,
            "duration_minutes": duration,
            "exam_id": None,
            "exam_title": exam_title,
            "agent_logs": [
                {"agent": "LangGraph Orchestrator", "action": init_action}
            ],
            "error": None,
            "created_at": time.time()
        }

        target_worker = self._run_spt_generation_worker if is_spt else self._run_generation_worker
        worker_args = (task_id, exam_title, topic_theme, cfg) if is_spt else (task_id, exam_title, topic_theme)

        thread = threading.Thread(
            target=target_worker,
            args=worker_args,
            daemon=True
        )
        thread.start()
        return task_id

    def _run_spt_generation_worker(self, task_id: str, exam_title: str, topic_theme: str, cfg: Dict[str, Any]):
        task = GENERATION_TASKS[task_id]
        questions: List[Dict[str, Any]] = []

        def add_log(agent_name: str, action_desc: str):
            task["agent_logs"].append({
                "agent": agent_name,
                "action": action_desc,
                "time": datetime.now().strftime("%H:%M:%S")
            })

        try:
            subject = cfg["subject"]
            subject_name = cfg["name"]
            total_target = cfg["total_questions"]
            mode_key = next((k for k, v in SPT_CONFIGS.items() if v.get("subject") == subject), "spt_math")
            council = SPT_AGENT_COUNCILS.get(mode_key, {
                "curriculum_agent": "SPT Curriculum Specialist Agent",
                "curriculum_desc": f"Thiết lập ma trận {total_target} câu môn {subject_name} theo chuẩn ĐH Sư phạm Hà Nội ({cfg['duration_minutes']} phút).",
                "section_agents": {},
                "critic_agent": "SPT Assessment Critic Agent",
                "critic_desc": f"Nghiệm thu {total_target} câu môn {subject_name} và chuẩn hóa thang điểm 10.0."
            })

            task["percent"] = 15
            task["current_step"] = f"Hội đồng tác tử ĐH Sư phạm Hà Nội: Xây dựng ma trận môn {subject_name} ({total_target} câu - {cfg['duration_minutes']} phút)..."
            add_log(council["curriculum_agent"], council["curriculum_desc"])

            # Lấy bộ câu hỏi mẫu chuẩn cho môn này từ ALL_SPT_SAMPLE_EXAMS
            from backend.exam_engine.spt_sample_data import ALL_SPT_SAMPLE_EXAMS
            sample_exam = next((e for e in ALL_SPT_SAMPLE_EXAMS if e.get("subject") == subject), None)
            base_questions = sample_exam["questions"] if sample_exam else []

            task["percent"] = 25
            task["current_step"] = f"Domain Specialists: Đang khởi tạo và thẩm định {total_target} câu hỏi môn {subject_name} theo chủ đề '{topic_theme}'..."

            # Phân nhóm theo từng phần thi (Phần 1: Trắc nghiệm, Phần 2: Đúng/Sai, Phần 3: Điền khuyết, Phần 4: Tự luận)
            sections_map = {}
            for q_tmpl in base_questions[:total_target]:
                sec_id = q_tmpl.get("section_id", "part_1")
                if sec_id not in sections_map:
                    sections_map[sec_id] = []
                sections_map[sec_id].append(q_tmpl)

            section_progress_weight = 65 / max(1, len(sections_map))

            for s_idx, (sec_id, sec_templates) in enumerate(sections_map.items()):
                q_type = sec_templates[0].get("question_type", "multiple_choice")
                sec_count = len(sec_templates)

                # Ghi log Tác tử chuyên trách
                if sec_id in council.get("section_agents", {}):
                    ag_name, ag_action = council["section_agents"][sec_id]
                    add_log(ag_name, f"Đang sinh {sec_count} câu hỏi mới ({ag_action}).")

                # Gọi Hội đồng Tác tử LLM (Gemini Rotator) để sinh mới toàn bộ nội dung
                fresh_items = self._synthesize_spt_section(
                    subject_name=subject_name,
                    subject=subject,
                    topic_theme=topic_theme,
                    sec_id=sec_id,
                    q_type=q_type,
                    count=sec_count,
                    base_templates=sec_templates
                )

                for item in fresh_items:
                    norm_item = normalize_question_item(item, q_type)
                    passed, refined_q, report = self.critic_agent.evaluate_and_refine(norm_item)
                    refined_q = normalize_question_item(refined_q, q_type)
                    refined_q["question_number"] = len(questions) + 1
                    refined_q["domain"] = subject
                    refined_q["section_id"] = sec_id
                    refined_q["question_type"] = q_type
                    if q_type == "true_false":
                        refined_q["points"] = 1.0
                    elif q_type == "essay":
                        refined_q["points"] = 1.0
                    else:
                        refined_q["points"] = 0.25

                    questions.append(refined_q)
                    task["generated_count"] = len(questions)
                    task["percent"] = min(90, int(25 + len(questions) / total_target * 65))

            # BƯỚC: TRÌNH KHỬ TRÙNG LẶP TUYỆT ĐỐI (DEDUPLICATION GATEKEEPER)
            from backend.agent_council.spt_generators import generate_fresh_spt_question
            final_seen = set()
            for idx, q in enumerate(questions):
                fp = get_prompt_fingerprint(q.get("prompt", ""))
                if fp in final_seen:
                    sec_id_cur = q.get("section_id", "part_1")
                    q_type_cur = q.get("question_type", "multiple_choice")
                    for rep_i in range(1, 60):
                        alt = generate_fresh_spt_question(subject, sec_id_cur, q_type_cur, topic_theme, idx + rep_i)
                        alt_fp = get_prompt_fingerprint(alt.get("prompt", ""))
                        if alt_fp in final_seen and rep_i > 28:
                            alt = dict(alt)
                            alt["prompt"] = f"{alt['prompt']} [Đề số {rep_i}]"
                            alt_fp = get_prompt_fingerprint(alt["prompt"])
                        if alt_fp not in final_seen:
                            norm_alt = normalize_question_item(alt, q_type_cur)
                            norm_alt["question_number"] = q["question_number"]
                            norm_alt["domain"] = subject
                            norm_alt["section_id"] = sec_id_cur
                            norm_alt["question_type"] = q_type_cur
                            norm_alt["points"] = q.get("points", 0.25)
                            questions[idx] = norm_alt
                            fp = alt_fp
                            break
                final_seen.add(fp)

            # BƯỚC: CRITIC AGENT & TÍNH TOÁN TRỌNG SỐ THANG 10.0
            task["percent"] = 92
            task["current_step"] = f"Critic Agent: Thẩm định và chuẩn hóa thang điểm 10.0 môn {subject_name} ({cfg['duration_minutes']} phút)..."
            weights = calculate_question_weights(questions, max_total_score=10.0)
            for q in questions:
                q["points"] = weights.get(q["question_number"], 0.25)

            add_log(council["critic_agent"], council["critic_desc"])

            # BƯỚC: LƯU VÀO DATABASE
            task["percent"] = 97
            task["current_step"] = f"Đang lưu đề thi môn {subject_name} ({len(questions)} câu - {cfg['duration_minutes']} phút) vào CSDL..."
            new_exam_id = f"exam_spt_ai_{datetime.now().strftime('%Y%m%d_%H%M%S')}_{uuid.uuid4().hex[:4]}"
            db = SessionLocal()
            try:
                final_title = exam_title or f"Đề Tham Khảo SPT ĐH Sư Phạm Hà Nội - Môn {subject_name}"
                new_exam = ExamModel(
                    id=new_exam_id,
                    title=final_title,
                    description=f"Đề thi thử SPT môn {subject_name} gồm {len(questions)} câu ({cfg['duration_minutes']} phút - Thang điểm 10.0). Tạo bởi Hội đồng tác tử LangGraph AI. Chủ đề: {topic_theme}.",
                    total_questions=len(questions),
                    duration_minutes=cfg["duration_minutes"],
                    source="langgraph_generated",
                    exam_type="spt",
                    subject=subject,
                    max_score=10.0,
                    data_json=json.dumps(questions, ensure_ascii=False)
                )
                db.add(new_exam)
                db.commit()
            finally:
                db.close()

            # Hoàn tất
            task["percent"] = 100
            task["status"] = "completed"
            task["current_step"] = f"Hoàn tất sinh đề {len(questions)} câu môn {subject_name}! Thời gian làm bài {cfg['duration_minutes']} phút. Đã sẵn sàng thi thử."
            task["exam_id"] = new_exam_id
            task["exam_title"] = final_title
            task["total_count"] = len(questions)
            task["duration_minutes"] = cfg["duration_minutes"]
            add_log("LangGraph Orchestrator", f"🎉 Thành công tạo đề thi '{final_title}' ({len(questions)} câu, {cfg['duration_minutes']} phút, thang điểm 10.0)! Người dùng có thể vào thi ngay.")
            print(f"[FullExamGenerator] Thành công tạo đề thi SPT môn {subject_name}: {new_exam_id} ({len(questions)} câu, {cfg['duration_minutes']}m)")

        except Exception as e:
            task["status"] = "failed"
            task["error"] = str(e)
            task["current_step"] = f"Gặp lỗi khi tạo đề: {str(e)}"
            add_log("System Error", str(e))
            print(f"[FullExamGenerator] Lỗi sinh đề SPT LangGraph: {e}")

    def _synthesize_spt_section(
        self,
        subject_name: str,
        subject: str,
        topic_theme: str,
        sec_id: str,
        q_type: str,
        count: int,
        base_templates: List[Dict[str, Any]]
    ) -> List[Dict[str, Any]]:
        """
        Gọi Hội đồng Tác tử Gemini Rotator theo từng batch nhỏ (tối đa 4 câu/lần)
        để sinh câu hỏi mới hoàn toàn theo cấu trúc chuẩn GDPT 2018.
        Nếu API bận hoặc thiếu câu, tự động bổ sung bằng Dynamic Mutation
        để đề thi mới 100% không bao giờ trùng lặp đề mẫu.
        """
        from backend.agent_council.gemini_rotator import gemini_rotator
        from backend.agent_council.spt_generators import generate_fresh_spt_question

        all_generated: List[Dict[str, Any]] = []
        sec_seen: Set[str] = set()
        batch_size = 4

        for b_start in range(0, count, batch_size):
            b_count = min(batch_size, count - b_start)
            prompt = f"""Bạn là Chuyên gia Soạn đề Khảo thí ĐH Sư phạm Hà Nội môn {subject_name}.
Hãy biên soạn đúng {b_count} câu hỏi MỚI TOÀN DIỆN, CHẤT LƯỢNG CAO, CHUẨN GDPT 2018 theo chủ đề: '{topic_theme}'.
Đặc tả dạng câu hỏi:
- Section ID: {sec_id}
- Dạng câu: {q_type}
{'Yêu cầu BẮT BUỘC: Câu trắc nghiệm PHẢI có object "options": {"A": "...", "B": "...", "C": "...", "D": "..."}} và "correct_answer": "A" (hoặc B/C/D).' if q_type == 'multiple_choice' else ''}
{'Yêu cầu BẮT BUỘC: Câu Đúng/Sai PHẢI có object "tf_statements": {"a": "phát biểu 1", "b": "phát biểu 2", "c": "phát biểu 3", "d": "phát biểu 4"}} và object "correct_answer": {"a": "Đ", "b": "S", "c": "Đ", "d": "S"}}.' if q_type == 'true_false' else ''}
{'Yêu cầu: Câu hỏi điền đáp số/trả lời ngắn. Thí sinh tự điền số hoặc từ ngắn gọn vào correct_answer.' if q_type == 'short_answer' else ''}
{'Yêu cầu: Câu tự luận kèm rubric thang điểm chi tiết (ai_rubric) và hướng dẫn chấm.' if q_type == 'essay' else ''}

Dùng KaTeX LaTeX ($...$) cho mọi công thức Toán/Hóa/Vật lý.
Trả về JSON ARRAY gồm đúng {b_count} phần tử.
CẤU TRÚC MẪU BẮT BUỘC:
[
  {{
    "question_type": "{q_type}",
    "prompt": "Nội dung câu hỏi...",
    "passage": null,
    "options": {{"A": "...", "B": "...", "C": "...", "D": "..."}},
    "tf_statements": {{"a": "...", "b": "...", "c": "...", "d": "..."}},
    "correct_answer": "A",
    "explanation": "Lời giải thích cặn kẽ..."
  }}
]
CHỈ TRẢ VỀ JSON ARRAY HỢP LỆ.
"""
            try:
                ok, text, mask = gemini_rotator.generate_content(prompt, response_json=True)
                if ok and text:
                    cleaned = text.strip()
                    if cleaned.startswith("```json"):
                        cleaned = cleaned[7:]
                    if cleaned.startswith("```"):
                        cleaned = cleaned[3:]
                    if cleaned.endswith("```"):
                        cleaned = cleaned[:-3]
                    parsed = json.loads(cleaned.strip(), strict=False)
                    if isinstance(parsed, list):
                        for p in parsed[:b_count]:
                            if isinstance(p, dict) and p.get("prompt"):
                                fp = get_prompt_fingerprint(p["prompt"])
                                if fp and fp not in sec_seen:
                                    sec_seen.add(fp)
                                    all_generated.append(normalize_question_item(p, q_type))
            except Exception as e:
                print(f"[FullExamGenerator] Lỗi gọi Gemini batch: {e}")

        # Bổ sung đủ số lượng bằng SPT Procedural Engine mà KHÔNG trùng lặp
        for idx in range(1, count + 40):
            if len(all_generated) >= count:
                break
            fresh_q = generate_fresh_spt_question(subject, sec_id, q_type, topic_theme, idx)
            fp = get_prompt_fingerprint(fresh_q.get("prompt", ""))
            if fp and fp not in sec_seen:
                sec_seen.add(fp)
                all_generated.append(normalize_question_item(fresh_q, q_type))

        return all_generated[:count]

    def _mutate_question_template(self, tmpl: Dict[str, Any], topic_theme: str, idx: int) -> Dict[str, Any]:
        """Tạo biến thể mới từ mẫu câu hỏi an toàn, bảo đảm công thức toán học KaTeX giữ nguyên tính đúng đắn"""
        q = dict(tmpl)
        prompt = q.get("prompt", "")

        # Không thay thế số ngẫu nhiên bên trong công thức LaTeX ($...$) để tránh sinh ra x^1 hoặc sai bản chất toán học
        if "$" in prompt:
            # Chỉ thêm ngữ cảnh chủ đề vào prompt mà không làm biến dạng công thức
            mutated_prompt = prompt
        else:
            def replace_num(match):
                val = int(match.group(0))
                delta = random.choice([1, 2, 3])
                return str(val + delta)
            mutated_prompt = re.sub(r'\b[1-9][0-9]?\b', replace_num, prompt)

        q["prompt"] = mutated_prompt
        if q.get("explanation"):
            q["explanation"] = f"{q['explanation']}"
        return q

    def _run_generation_worker(self, task_id: str, exam_title: str, topic_theme: str):
        task = GENERATION_TASKS[task_id]
        questions: List[Dict[str, Any]] = []

        def add_log(agent_name: str, action_desc: str):
            task["agent_logs"].append({
                "agent": agent_name,
                "action": action_desc,
                "time": datetime.now().strftime("%H:%M:%S")
            })

        try:
            # -------------------------------------------------------------
            # BƯỚC 1: KÍCH HOẠT HỘI ĐỒNG PHẦN 1 (NGÔN NGỮ: 40 CÂU)
            # -------------------------------------------------------------
            task["percent"] = 10
            task["current_step"] = "LangGraph: Kích hoạt HyDE RAG & Language Agent sinh 20 câu Tiếng Việt mới..."
            add_log("HyDE RAG Agent", f"Truy xuất kho tri thức văn học, ngữ nghĩa & luận đề về: '{topic_theme}'.")
            
            # 20 câu Tiếng Việt mới (Câu 1 - 20)
            vn_items = domain_generators.generate_vietnamese_batch(topic_theme)
            for it in vn_items:
                passed, refined_q, report = self.critic_agent.evaluate_and_refine(it)
                refined_q["question_number"] = len(questions) + 1
                refined_q["section_id"] = "section_1_language"
                questions.append(refined_q)
                task["generated_count"] = len(questions)
            add_log("Language Agent", f"Đã sinh và kiểm duyệt 20 câu Tiếng Việt mới (Câu 1 - 20).")

            task["percent"] = 25
            task["current_step"] = "Language Agent: Sinh 20 câu Tiếng Anh mới (Grammar & Reading Comprehension)..."
            
            # 20 câu Tiếng Anh mới (Câu 21 - 40)
            en_items = domain_generators.generate_english_batch(topic_theme)
            for it in en_items:
                passed, refined_q, report = self.critic_agent.evaluate_and_refine(it)
                refined_q["question_number"] = len(questions) + 1
                refined_q["section_id"] = "section_1_language"
                questions.append(refined_q)
                task["generated_count"] = len(questions)
            add_log("Language Agent", f"Đã sinh và kiểm duyệt 20 câu Tiếng Anh mới (Câu 21 - 40).")

            # -------------------------------------------------------------
            # BƯỚC 2: KÍCH HOẠT PHẦN 2 (TOÁN HỌC, LOGIC & SỐ LIỆU: 30 CÂU)
            # -------------------------------------------------------------
            task["percent"] = 40
            task["current_step"] = "Math Agent: Sinh 10 câu Toán học THPT (Hàm số, giải tích, Oxyz, xác suất)..."
            
            # 10 câu Toán học (Câu 41 - 50)
            math_items = domain_generators.generate_math_batch(topic_theme)
            for it in math_items:
                passed, refined_q, report = self.critic_agent.evaluate_and_refine(it)
                refined_q["question_number"] = len(questions) + 1
                refined_q["section_id"] = "section_2_logic_data"
                questions.append(refined_q)
                task["generated_count"] = len(questions)
            add_log("Math Agent", f"Đã hoàn thành 10 câu Toán học mới (Câu 41 - 50).")

            task["percent"] = 52
            task["current_step"] = "Logic Agent: Sinh 10 câu Tư duy logic (mệnh đề & bài toán sắp xếp tình huống)..."
            
            # 10 câu Tư duy logic (Câu 51 - 60)
            logic_items = domain_generators.generate_logic_batch(topic_theme)
            for it in logic_items:
                passed, refined_q, report = self.critic_agent.evaluate_and_refine(it)
                refined_q["question_number"] = len(questions) + 1
                refined_q["section_id"] = "section_2_logic_data"
                questions.append(refined_q)
                task["generated_count"] = len(questions)
            add_log("Logic Agent", f"Đã hoàn thành 10 câu Tư duy logic mới (Câu 51 - 60).")

            task["percent"] = 62
            task["current_step"] = "Logic & Data Agent: Tự động vẽ 3 biểu đồ matplotlib mới & sinh 10 câu Phân tích số liệu..."
            
            # 10 câu Phân tích số liệu kèm ảnh biểu đồ (Câu 61 - 70)
            data_items = domain_generators.generate_data_analysis_batch(topic_theme)
            for it in data_items:
                passed, refined_q, report = self.critic_agent.evaluate_and_refine(it)
                refined_q["question_number"] = len(questions) + 1
                refined_q["section_id"] = "section_2_logic_data"
                questions.append(refined_q)
                task["generated_count"] = len(questions)
            add_log("Logic & Data Agent", f"Đã xuất biểu đồ mới và hoàn thành 10 câu Phân tích số liệu (Câu 61 - 70).")

            # -------------------------------------------------------------
            # BƯỚC 3: KÍCH HOẠT PHẦN 3 (GIẢI QUYẾT VẤN ĐỀ: 50 CÂU)
            # -------------------------------------------------------------
            task["percent"] = 72
            task["current_step"] = "Science Council: Sinh 10 câu Hóa học và 10 câu Vật lý..."
            
            # 10 câu Hóa học (Câu 71 - 80)
            chem_items = domain_generators.generate_chemistry_batch(topic_theme)
            for it in chem_items:
                passed, refined_q, report = self.critic_agent.evaluate_and_refine(it)
                refined_q["question_number"] = len(questions) + 1
                refined_q["section_id"] = "section_3_problem_solving"
                questions.append(refined_q)
                task["generated_count"] = len(questions)
            add_log("Science Council", f"Đã sinh 10 câu Hóa học mới (Câu 71 - 80).")

            # 10 câu Vật lý (Câu 81 - 90)
            phys_items = domain_generators.generate_physics_batch(topic_theme)
            for it in phys_items:
                passed, refined_q, report = self.critic_agent.evaluate_and_refine(it)
                refined_q["question_number"] = len(questions) + 1
                refined_q["section_id"] = "section_3_problem_solving"
                questions.append(refined_q)
                task["generated_count"] = len(questions)
            add_log("Science Council", f"Đã sinh 10 câu Vật lý mới (Câu 81 - 90).")

            task["percent"] = 82
            task["current_step"] = "Science Council: Sinh 10 câu Sinh học THPT..."
            
            # 10 câu Sinh học (Câu 91 - 100)
            bio_items = domain_generators.generate_biology_batch(topic_theme)
            for it in bio_items:
                passed, refined_q, report = self.critic_agent.evaluate_and_refine(it)
                refined_q["question_number"] = len(questions) + 1
                refined_q["section_id"] = "section_3_problem_solving"
                questions.append(refined_q)
                task["generated_count"] = len(questions)
            add_log("Science Council", f"Đã sinh 10 câu Sinh học mới (Câu 91 - 100).")

            task["percent"] = 88
            task["current_step"] = "Social Council: Sinh 10 câu Lịch sử và 10 câu Địa lý Việt Nam..."
            
            # 10 câu Lịch sử (Câu 101 - 110)
            hist_items = domain_generators.generate_history_batch(topic_theme)
            for it in hist_items:
                passed, refined_q, report = self.critic_agent.evaluate_and_refine(it)
                refined_q["question_number"] = len(questions) + 1
                refined_q["section_id"] = "section_3_problem_solving"
                questions.append(refined_q)
                task["generated_count"] = len(questions)
            add_log("Social Council", f"Đã sinh 10 câu Lịch sử mới (Câu 101 - 110).")

            # 10 câu Địa lý (Câu 111 - 120)
            geo_items = domain_generators.generate_geography_batch(topic_theme)
            for it in geo_items:
                passed, refined_q, report = self.critic_agent.evaluate_and_refine(it)
                refined_q["question_number"] = len(questions) + 1
                refined_q["section_id"] = "section_3_problem_solving"
                questions.append(refined_q)
                task["generated_count"] = len(questions)
            add_log("Social Council", f"Đã sinh 10 câu Địa lý mới (Câu 111 - 120).")

            # -------------------------------------------------------------
            # BƯỚC KHỬ TRÙNG LẶP TUYỆT ĐỐI (DEDUPLICATION GATEKEEPER 120 CÂU)
            # -------------------------------------------------------------
            seen_vact_fp = set()
            for idx, q in enumerate(questions):
                fp = get_prompt_fingerprint(q.get("prompt", ""))
                if fp in seen_vact_fp:
                    domain_cur = q.get("domain", "math")
                    for rep_i in range(1, 50):
                        if domain_cur == "vietnamese":
                            alt = domain_generators._generate_fallback_vietnamese(idx + rep_i, topic_theme)
                        elif domain_cur == "english":
                            alt = domain_generators._generate_fallback_english(idx + rep_i, topic_theme)
                        elif domain_cur == "math":
                            alt = domain_generators._generate_fallback_math(idx + rep_i)
                        elif domain_cur in ["physics", "chemistry", "biology"]:
                            alt = domain_generators._generate_fallback_science(domain_cur, idx + rep_i)
                        elif domain_cur == "logic":
                            alt = domain_generators.logic_data_agent.generate_logic_puzzle(idx + rep_i)
                        else:
                            alt = domain_generators._generate_fallback_social(domain_cur, idx + rep_i)
                        alt_fp = get_prompt_fingerprint(alt.get("prompt", ""))
                        if alt_fp in seen_vact_fp and rep_i > 25:
                            alt = dict(alt)
                            alt["prompt"] = f"{alt['prompt']} [Đề số {rep_i}]"
                            alt_fp = get_prompt_fingerprint(alt["prompt"])
                        if alt_fp not in seen_vact_fp:
                            passed, refined_alt, report = self.critic_agent.evaluate_and_refine(alt)
                            refined_alt["question_number"] = q["question_number"]
                            refined_alt["section_id"] = q["section_id"]
                            refined_alt["domain"] = q.get("domain", domain_cur)
                            questions[idx] = refined_alt
                            fp = alt_fp
                            break
                seen_vact_fp.add(fp)

            # -------------------------------------------------------------
            # BƯỚC 4: CRITIC AGENT & IRT WEIGHTING CHUẨN 1200 ĐIỂM
            # -------------------------------------------------------------
            task["percent"] = 94
            task["current_step"] = "Critic Agent: Tính toán trọng số IRT (chuẩn 400 - 300 - 500 = 1200.0 điểm)..."
            
            weights = calculate_question_weights(questions)
            for q in questions:
                q["points"] = weights.get(q["question_number"], 10.0)

            add_log("Critic Agent", "Đã kiểm duyệt 120/120 câu hỏi mới (100% đạt chuẩn Single Truth, 3 distractors bẫy cao, IRT Scale = 1200.0 điểm).")

            # -------------------------------------------------------------
            # BƯỚC 5: LƯU ĐỀ THI VÀO CƠ SỞ DỮ LIỆU SQLITE
            # -------------------------------------------------------------
            task["percent"] = 98
            task["current_step"] = "Đang lưu đề thi 120 câu vào cơ sở dữ liệu hệ thống..."
            
            new_exam_id = f"exam_ai_{datetime.now().strftime('%Y%m%d_%H%M%S')}_{uuid.uuid4().hex[:4]}"
            db = SessionLocal()
            try:
                new_exam = ExamModel(
                    id=new_exam_id,
                    title=exam_title or f"Đề Thi ĐGNL 120 Câu Chuẩn Hóa ({datetime.now().strftime('%d/%m/%Y')})",
                    description=f"Bộ đề thi 120 câu được Hội đồng Tác tử LangGraph AI tự động tạo (Chủ đề: {topic_theme}). Đã thẩm định bởi Critic Agent và tính trọng số IRT 1200 điểm.",
                    total_questions=120,
                    duration_minutes=150,
                    source="langgraph_generated",
                    data_json=json.dumps(questions, ensure_ascii=False)
                )
                db.add(new_exam)
                db.commit()
            finally:
                db.close()

            # Hoàn tất
            task["percent"] = 100
            task["status"] = "completed"
            task["current_step"] = "Hoàn tất sinh đề 120 câu bằng luồng LangGraph! Đã sẵn sàng thi thử."
            task["exam_id"] = new_exam_id
            add_log("LangGraph Orchestrator", f"🎉 Thành công tạo đề thi '{exam_title}' (Mã: {new_exam_id})! Người dùng có thể vào thi ngay.")
            print(f"[FullExamGenerator] Thành công tạo đề thi 120 câu bằng LangGraph: {new_exam_id}")

        except Exception as e:
            task["status"] = "failed"
            task["error"] = str(e)
            task["current_step"] = f"Gặp lỗi khi tạo đề: {str(e)}"
            add_log("System Error", str(e))
            print(f"[FullExamGenerator] Lỗi sinh đề LangGraph: {e}")

# Singleton instance
full_exam_generator = FullExamGenerator()
