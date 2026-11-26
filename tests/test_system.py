import sys
import os

sys.stdout.reconfigure(encoding='utf-8')
sys.stderr.reconfigure(encoding='utf-8')

# Thêm thư mục gốc vào PYTHONPATH
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from backend.config import MAX_TOTAL_SCORE, SCORE_DISTRIBUTION
from backend.exam_engine.benchmark_exam import BENCHMARK_QUESTIONS
from backend.exam_engine.grader import calculate_question_weights, grade_submission
from backend.exam_engine.analytics import generate_radar_chart_base64, calculate_competency_insights
from backend.exam_engine.advisor import generate_personalized_advice
from backend.agent_council.graph import run_agent_council_pipeline

def test_benchmark_structure():
    assert len(BENCHMARK_QUESTIONS) == 120, f"Expected 120 questions, got {len(BENCHMARK_QUESTIONS)}"
    
    # Check sections
    sec1 = [q for q in BENCHMARK_QUESTIONS if q["question_number"] <= 40]
    sec2 = [q for q in BENCHMARK_QUESTIONS if 41 <= q["question_number"] <= 70]
    sec3 = [q for q in BENCHMARK_QUESTIONS if q["question_number"] > 70]

    assert len(sec1) == 40, f"Section 1 should have 40 questions, got {len(sec1)}"
    assert len(sec2) == 30, f"Section 2 should have 30 questions, got {len(sec2)}"
    assert len(sec3) == 50, f"Section 3 should have 50 questions, got {len(sec3)}"

def test_irt_weights_and_1200_point_scale():
    weights = calculate_question_weights(BENCHMARK_QUESTIONS)
    assert len(weights) == 120, "Should have weights for all 120 questions"

    sec1_sum = sum(weights[q["question_number"]] for q in BENCHMARK_QUESTIONS if q["question_number"] <= 40)
    sec2_sum = sum(weights[q["question_number"]] for q in BENCHMARK_QUESTIONS if 41 <= q["question_number"] <= 70)
    sec3_sum = sum(weights[q["question_number"]] for q in BENCHMARK_QUESTIONS if q["question_number"] > 70)
    total_sum = sec1_sum + sec2_sum + sec3_sum

    assert round(sec1_sum, 1) == 400.0, f"Section 1 sum should be 400.0, got {sec1_sum}"
    assert round(sec2_sum, 1) == 300.0, f"Section 2 sum should be 300.0, got {sec2_sum}"
    assert round(sec3_sum, 1) == 500.0, f"Section 3 sum should be 500.0, got {sec3_sum}"
    assert round(total_sum, 1) == 1200.0, f"Total sum should be 1200.0, got {total_sum}"

def test_grading_perfect_score():
    # User selects all correct answers
    perfect_answers = {str(q["question_number"]): q["correct_answer"] for q in BENCHMARK_QUESTIONS}
    report = grade_submission(BENCHMARK_QUESTIONS, perfect_answers)

    assert report["total_score"] == 1200.0, f"Perfect score should be 1200.0, got {report['total_score']}"
    assert report["correct_count"] == 120
    assert report["wrong_count"] == 0
    assert report["unanswered_count"] == 0
    assert report["sec1_score"] == 400.0
    assert report["sec2_score"] == 300.0
    assert report["sec3_score"] == 500.0

def test_radar_chart_and_analytics():
    # Grade partial score
    answers = {str(q["question_number"]): q["correct_answer"] for q in BENCHMARK_QUESTIONS[:80]}
    report = grade_submission(BENCHMARK_QUESTIONS, answers)

    # Test radar image generation
    radar_base64 = generate_radar_chart_base64(report["domain_stats"])
    assert radar_base64.startswith("data:image/png;base64,")
    assert len(radar_base64) > 1000, "Base64 image should have valid content"

    # Test insights
    insights = calculate_competency_insights(report["domain_stats"], report["total_score"])
    assert "strong_areas" in insights
    assert "weak_areas" in insights
    assert 1.0 <= insights["estimated_percentile"] <= 99.9

    # Test AI advice
    advice = generate_personalized_advice(report["domain_stats"], report["total_score"])
    assert len(advice) > 200, "Personalized advice should provide substantial guidance"

def test_langgraph_pipeline():
    result = run_agent_council_pipeline(
        topic="Sóng cơ và giao thoa sóng",
        section_target="problem_solving",
        count=1,
        difficulty="medium"
    )
    assert "final_questions" in result
    assert len(result["final_questions"]) == 1
    assert result["ragas_faithfulness"] > 0.6
    assert result["ragas_relevance"] > 0.6
    assert len(result["agent_logs"]) >= 3

if __name__ == "__main__":
    print("Running system test suite...")
    test_benchmark_structure()
    print("✅ test_benchmark_structure passed!")
    test_irt_weights_and_1200_point_scale()
    print("✅ test_irt_weights_and_1200_point_scale passed (Exact 1200.0 points: 400-300-500)!")
    test_grading_perfect_score()
    print("✅ test_grading_perfect_score passed!")
    test_radar_chart_and_analytics()
    print("✅ test_radar_chart_and_analytics passed!")
    test_langgraph_pipeline()
    print("✅ test_langgraph_pipeline passed!")
    print("\n🎉 ALL 5 COMPREHENSIVE TESTS PASSED SUCCESSFULLY!")
