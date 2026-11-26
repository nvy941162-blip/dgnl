import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

from backend.exam_engine.spt_sample_data import SPT_MATH_EXAM, ALL_SPT_SAMPLE_EXAMS
from backend.exam_engine.grader import grade_submission, calculate_question_weights
from backend.exam_engine.analytics import calculate_competency_insights, generate_radar_chart_base64
from backend.exam_engine.advisor import generate_personalized_advice

def test_spt_sample_exams_structure():
    assert len(ALL_SPT_SAMPLE_EXAMS) == 8, f"Expected 8 SPT sample exams, got {len(ALL_SPT_SAMPLE_EXAMS)}"
    for spt in ALL_SPT_SAMPLE_EXAMS:
        assert spt["exam_type"] == "spt"
        assert spt["max_score"] == 10.0
        assert len(spt["questions"]) == spt["total_questions"]
        print(f"  ✓ Đề {spt['title']}: {len(spt['questions'])} câu, thang {spt['max_score']}đ")

def test_spt_math_weights():
    weights = calculate_question_weights(SPT_MATH_EXAM["questions"], max_total_score=10.0)
    assert len(weights) == len(SPT_MATH_EXAM["questions"])
    total_weights = sum(weights.values())
    print(f"SPT Math total weights: {total_weights:.2f}")
    assert abs(total_weights - 10.0) < 0.1, f"Expected total 10.0, got {total_weights}"

def test_spt_grading_and_analytics():
    questions = SPT_MATH_EXAM["questions"]
    
    # Giả lập trả lời: câu 1 đúng, câu 2 đúng, ...
    user_answers = {}
    for q in questions[:15]:
        q_num = str(q["question_number"])
        if q["question_type"] == "multiple_choice":
            user_answers[q_num] = q.get("correct_answer", "A")
        elif q["question_type"] == "true_false":
            user_answers[q_num] = q.get("correct_answer", {"a": "Đ", "b": "S", "c": "S", "d": "Đ"})
        elif q["question_type"] == "short_answer":
            user_answers[q_num] = q.get("correct_answer", "1")

    report = grade_submission(questions, user_answers, exam_type="spt", max_score=10.0)
    assert report["is_spt"] == True
    assert report["max_total_score"] == 10.0
    assert 0.0 <= report["total_score"] <= 10.0
    print(f"SPT Grade total score: {report['total_score']} / {report['max_total_score']}")

    # Kiểm tra phân tích năng lực SPT
    comp = calculate_competency_insights(
        report["domain_stats"],
        report["total_score"],
        max_score=10.0,
        is_spt=True
    )
    assert "tier_rating" in comp
    assert "estimated_percentile" in comp
    assert 1.0 <= comp["estimated_percentile"] <= 99.9
    print(f"SPT Tier: {comp['tier_rating']}")
    print(f"SPT Percentile: {comp['estimated_percentile']}%")

    # Kiểm tra lời khuyên ôn tập SPT
    advice = generate_personalized_advice(
        report["domain_stats"],
        report["total_score"],
        max_score=10.0,
        is_spt=True,
        exam_title=SPT_MATH_EXAM["title"]
    )
    assert len(advice) > 100
    assert "10" in advice or "SPT" in advice
    print("SPT Personalized Advice generated successfully!")

if __name__ == "__main__":
    print("=== KIỂM THỬ KHẢO THÍ ĐỀ THI SPT (ĐH SƯ PHẠM HÀ NỘI) ===")
    test_spt_sample_exams_structure()
    test_spt_math_weights()
    test_spt_grading_and_analytics()
    print("\n✅ TẤT CẢ KIỂM THỬ KHẢO THÍ SPT ĐÃ VƯỢT QUA 100%!")
