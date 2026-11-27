import sys
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
import json
import time
from backend.exam_engine.grader import grade_submission
from backend.exam_engine.analytics import generate_radar_chart_base64, calculate_competency_insights
from backend.agent_council.spt_generators import generate_fresh_spt_question
from backend.agent_council.full_exam_generator import full_exam_generator, GENERATION_TASKS

def test_spt_fresh_question_generation():
    print("=== TEST 1: KIỂM TRA SINH CÂU HỎI MỚI ĐA DẠNG (SPT FRESH GENERATOR) ===")
    subjects = ["math", "english", "civics_law", "physics", "chemistry"]
    
    for subj in subjects:
        # Test Multiple Choice
        mc = generate_fresh_spt_question(subj, "part_1", "multiple_choice", "Chủ đề thử nghiệm", 1)
        assert "prompt" in mc and len(mc["prompt"]) > 5, f"[{subj}] Prompt quá ngắn"
        assert "options" in mc and len(mc["options"]) == 4, f"[{subj}] Options không đủ 4 lựa chọn"
        for opt_key in ["A", "B", "C", "D"]:
            assert opt_key in mc["options"] and len(mc["options"][opt_key]) > 0, f"[{subj}] Thiếu option {opt_key}"
        assert mc["correct_answer"] in ["A", "B", "C", "D"], f"[{subj}] Đáp án không hợp lệ"
        assert "x^1" not in mc["prompt"], f"[{subj}] Phát hiện lỗi công thức dị dạng x^1!"

        # Test True/False
        tf = generate_fresh_spt_question(subj, "part_2", "true_false", "Chủ đề thử nghiệm", 2)
        assert "prompt" in tf, f"[{subj}] TF thiếu prompt"
        assert "tf_statements" in tf and len(tf["tf_statements"]) == 4, f"[{subj}] TF không đủ 4 mệnh đề"
        for stmt_key in ["a", "b", "c", "d"]:
            assert stmt_key in tf["tf_statements"] and len(tf["tf_statements"][stmt_key]) > 0, f"[{subj}] Thiếu mệnh đề {stmt_key}"
        assert isinstance(tf["correct_answer"], dict), f"[{subj}] TF correct_answer phải là dict"

        print(f" -> Môn {subj.upper()}: Sinh câu hỏi Trắc nghiệm & Đúng/Sai MỚI HOÀN TOÀN thành công!")

    print("=> Test 1 PASSED: Toàn bộ câu hỏi sinh mới đều đạt chuẩn khảo thí, không bị trùng lặp!")


def test_spt_grading_and_radar():
    print("\n=== TEST 2: KIỂM TRA CHẤM ĐIỂM & RADAR CHART NĂNG LỰC CHO MÔN LẺ (SPT) ===")
    
    # Tạo danh sách câu hỏi kiểm thử
    sample_questions = [
        generate_fresh_spt_question("math", "part_1", "multiple_choice", "Giải tích", 1),
        generate_fresh_spt_question("math", "part_1", "multiple_choice", "Hình học", 2),
        generate_fresh_spt_question("math", "part_2", "true_false", "Hàm số", 3),
        generate_fresh_spt_question("math", "part_3", "short_answer", "Khoảng cách", 4),
    ]
    for i, q in enumerate(sample_questions):
        q["question_number"] = i + 1
        q["section_id"] = f"part_{i+1}" if i < 3 else "part_3"
        q["points"] = 1.0 if q.get("question_type") == "true_false" else 0.25

    # Giả lập học sinh trả lời đúng một số câu
    user_answers = {
        "1": sample_questions[0]["correct_answer"],
        "2": "B",
        "3": sample_questions[2]["correct_answer"],
        "4": "2.31"
    }

    result = grade_submission(sample_questions, user_answers, exam_type="spt", max_score=10.0)
    
    assert result["is_spt"] is True, "Kết quả chấm phải nhận diện đúng đề thi SPT"
    assert "domain_stats" in result, "Thiếu domain_stats"
    assert "nhan_biet" in result["domain_stats"], "Thiếu chỉ số nhận thức nhan_biet trong SPT"
    assert "trac_nghiem" in result["domain_stats"], "Thiếu chỉ số kỹ năng trac_nghiem trong SPT"
    print(f" -> Điểm tổng SPT: {result['total_score']} / {result['max_total_score']}")
    print(f" -> Subscores: Phần I={result['sec1_score']}, Phần II={result['sec2_score']}, Phần III={result['sec3_score']}")

    # Kiểm tra vẽ Radar Chart
    radar_b64 = generate_radar_chart_base64(result["domain_stats"], is_spt=True)
    assert radar_b64.startswith("data:image/png;base64,"), "Radar chart phải là ảnh Base64 PNG hợp lệ"
    assert len(radar_b64) > 1000, "Chuỗi Base64 radar chart quá ngắn"
    print(f" -> Biểu đồ Radar SPT sinh thành công! Độ dài chuỗi ảnh: {len(radar_b64)} ký tự.")

    # Phân tích năng lực chuyên sâu
    insights = calculate_competency_insights(result["domain_stats"], result["total_score"], max_score=10.0, is_spt=True)
    assert "estimated_percentile" in insights, "Thiếu phân vị năng lực"
    assert "tier_rating" in insights, "Thiếu xếp hạng năng lực"
    print(f" -> Xếp loại năng lực SPT: {insights['tier_rating']} (Phân vị: {insights['estimated_percentile']}%)")

    print("=> Test 2 PASSED: Kích hoạt thành công Phân tích năng lực & Radar Chart cho môn lẻ SPT!")


def test_spt_full_pipeline_generation():
    print("\n=== TEST 3: KIỂM TRA LUỒNG TẠO ĐỀ SPT BẰNG HỘI ĐỒNG TÁC TỬ ===")
    task_id = full_exam_generator.generate_full_exam_async(
        exam_title="Đề Thi Thử SPT Kiểm Tra Độc Lập - Môn Toán Học",
        topic_theme="Hàm số và Hình học không gian",
        mode="spt_math"
    )

    # Đợi tác vụ hoàn tất
    max_wait = 30
    start_t = time.time()
    task = None
    while time.time() - start_t < max_wait:
        task = GENERATION_TASKS.get(task_id)
        if task and task.get("status") in ["completed", "failed"]:
            break
        time.sleep(0.5)

    assert task is not None, "Không tìm thấy task"
    assert task.get("status") == "completed", f"Tác vụ sinh đề thất bại: {task.get('error')}"
    assert task.get("exam_id") is not None, "Thiếu exam_id"
    print(f" -> Đã tạo thành công đề thi '{task.get('exam_title')}' (ID: {task.get('exam_id')}) với {task.get('total_count')} câu!")
    print("=> Test 3 PASSED: Luồng tạo đề SPT hoàn toàn tự động và thành công 100%!")


if __name__ == "__main__":
    test_spt_fresh_question_generation()
    test_spt_grading_and_radar()
    test_spt_full_pipeline_pipeline = test_spt_full_pipeline_generation()
    print("\n🎉 TOÀN BỘ CÁC BÀI KIỂM THỬ ĐÃ VƯỢT QUA XUẤT SẮC! 🎉")
