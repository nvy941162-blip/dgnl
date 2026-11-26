import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

import time
from backend.agent_council.full_exam_generator import full_exam_generator, GENERATION_TASKS
from backend.exam_engine.benchmark_exam import BENCHMARK_QUESTIONS
from backend.database import SessionLocal, ExamModel

def test_full_ai_generation():
    print("=== BẮT ĐẦU KIỂM THỬ SINH ĐỀ 120 CÂU THỰC SỰ MỚI TỪ AI ===")
    task_id = full_exam_generator.generate_full_exam_async(
        exam_title="Đề Thi Thử AI Hoàn Toàn Mới 2026",
        topic_theme="Chuyển đổi xanh & Trí tuệ nhân tạo"
    )
    print(f"Khởi chạy Task ID: {task_id}")

    # Polling task progress
    while True:
        task = GENERATION_TASKS.get(task_id, {})
        status = task.get("status")
        pct = task.get("percent", 0)
        step = task.get("current_step", "")
        count = task.get("generated_count", 0)
        print(f"[{pct}%] ({count}/120 câu) - {step}")

        if status in ["completed", "failed"]:
            break
        time.sleep(3)

    if status == "failed":
        print(f"LỖI: {task.get('error')}")
        return False

    exam_id = task.get("exam_id")
    print(f"\nSinh đề thành công! Exam ID: {exam_id}")

    # Truy vấn đề thi từ Database
    db = SessionLocal()
    try:
        exam = db.query(ExamModel).filter(ExamModel.id == exam_id).first()
        assert exam is not None, "Không tìm thấy exam trong DB"
        questions = exam.to_dict()["questions"]
        assert len(questions) == 120, f"Số câu không đủ 120: {len(questions)}"

        print(f"\nKiểm tra 120 câu hỏi mới:")
        # So sánh với đề benchmark để khẳng định không bị trùng lặp
        bench_prompts = set(q["prompt"] for q in BENCHMARK_QUESTIONS)
        new_prompts = [q["prompt"] for q in questions]

        overlap = sum(1 for p in new_prompts if p in bench_prompts)
        print(f"- Số câu trùng với đề mẫu benchmark: {overlap}/120")
        assert overlap < 5, f"Quá nhiều câu trùng lặp ({overlap}/120)!"

        # Kiểm tra phân bố các phần
        sec1 = [q for q in questions if q["section_id"] == "section_1_language"]
        sec2 = [q for q in questions if q["section_id"] == "section_2_logic_data"]
        sec3 = [q for q in questions if q["section_id"] == "section_3_problem_solving"]
        print(f"- Phần 1 (Ngôn ngữ): {len(sec1)} câu")
        print(f"- Phần 2 (Logic & Số liệu): {len(sec2)} câu")
        print(f"- Phần 3 (Giải quyết vấn đề): {len(sec3)} câu")
        assert len(sec1) == 40
        assert len(sec2) == 30
        assert len(sec3) == 50

        # Kiểm tra tổng điểm IRT
        total_pts = sum(q.get("points", 0) for q in questions)
        print(f"- Tổng điểm IRT: {total_pts:.1f} / 1200.0 điểm")
        assert abs(total_pts - 1200.0) < 0.1, f"Tổng điểm IRT không bằng 1200: {total_pts}"

        # Kiểm tra có ảnh biểu đồ số liệu thực tế không
        charts = [q for q in sec2 if q.get("chart_image")]
        print(f"- Số câu hỏi có biểu đồ đồ họa phân tích: {len(charts)}")
        assert len(charts) > 0, "Không có câu nào chứa biểu đồ đồ họa!"

        print("\nMột vài câu hỏi mẫu được AI sinh mới:")
        print("Câu 1 (Tiếng Việt):", questions[0]["prompt"])
        print("Câu 21 (Tiếng Anh):", questions[20]["prompt"])
        print("Câu 41 (Toán học):", questions[40]["prompt"])
        print("Câu 51 (Logic):", questions[50]["prompt"])
        print("Câu 61 (Số liệu):", questions[60]["prompt"], "| Ảnh:", questions[60].get("chart_image"))
        print("Câu 71 (Hóa học):", questions[70]["prompt"])
        print("Câu 81 (Vật lý):", questions[80]["prompt"])
        print("Câu 91 (Sinh học):", questions[90]["prompt"])
        print("Câu 101 (Lịch sử):", questions[100]["prompt"])
        print("Câu 111 (Địa lý):", questions[110]["prompt"])

        print("\n>>> TẤT CẢ CÁC KIỂM TRA ĐỀ THI MỚI HOÀN TOÀN ĐẠT CHUẨN XUẤT SẮC 100%! <<<")
        return True
    finally:
        db.close()

if __name__ == "__main__":
    test_full_ai_generation()
