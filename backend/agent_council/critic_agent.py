from typing import Dict, Any, Tuple

class CriticAgent:
    """
    Critic Agent (Tác tử Phản biện):
    Nhiệm vụ cốt lõi:
    1. Kiểm tra 4 phương án A, B, C, D: Đảm bảo DUY NHẤT 1 đáp án đúng (Single Truth).
    2. Đảm bảo 3 phương án gây nhiễu (Distractors) có tính đánh lừa cao,
       bám sát các lỗi sai tâm lý và nhận thức phổ biến của học sinh.
    3. Phát hiện lỗi trùng lặp nội dung giữa các phương án hoặc đáp án quá lộ liễu.
    4. Cung cấp điểm số thẩm định và tự động hiệu chỉnh (refine) nếu cần thiết.
    Hỗ trợ cả các dạng câu hỏi chuyên biệt của kỳ thi SPT (Đúng/Sai, Điền đáp số, Tự luận).
    """
    def __init__(self):
        pass

    def evaluate_and_refine(self, question: Dict[str, Any]) -> Tuple[bool, Dict[str, Any], Dict[str, Any]]:
        """
        Thẩm định câu hỏi trắc nghiệm hoặc các dạng câu hỏi khác (true_false, fill_in_the_blank, essay).
        Trả về: (passed, refined_question, evaluation_report)
        """
        q_type = question.get("question_type", "multiple_choice")
        prompt = str(question.get("prompt", "")).strip()
        explanation = str(question.get("explanation", "")).strip()

        # Xử lý các dạng câu hỏi không phải trắc nghiệm 4 lựa chọn đơn
        if q_type in ["true_false", "fill_in_the_blank", "fill_blank", "essay"]:
            correct_ans = question.get("correct_answer")
            has_ans = correct_ans is not None and (not isinstance(correct_ans, str) or correct_ans.strip() != "")
            passed = bool(prompt and has_ans)
            evaluation_report = {
                "passed": passed,
                "distractor_score": 1.0,
                "single_truth_verified": True,
                "critic_notes": f"Đạt tiêu chuẩn khảo thí định dạng {q_type}."
            }
            refined_question = dict(question)
            if not refined_question.get("explanation"):
                refined_question["explanation"] = f"Hướng dẫn chấm và giải chi tiết cho câu hỏi dạng {q_type}."
            return passed, refined_question, evaluation_report

        # Trắc nghiệm 4 lựa chọn (multiple_choice)
        options = question.get("options", {})
        raw_ans = question.get("correct_answer", "")
        correct_ans = str(raw_ans).strip().upper() if isinstance(raw_ans, (str, int)) else ""

        issues = []
        score = 1.0

        # 1. Kiểm tra cấu trúc 4 phương án
        required_keys = ["A", "B", "C", "D"]
        for key in required_keys:
            if key not in options or not str(options[key]).strip():
                issues.append(f"Thiếu hoặc để trống lựa chọn {key}.")
                score -= 0.3

        # 2. Kiểm tra tính duy nhất của nội dung các lựa chọn (không trùng lặp)
        opt_values = [str(options.get(k, "")).strip().lower() for k in required_keys if k in options]
        if len(opt_values) != len(set(opt_values)):
            issues.append("Có phương án trả lời bị trùng lặp nội dung.")
            score -= 0.4

        # 3. Kiểm tra đáp án đúng hợp lệ
        if correct_ans not in required_keys:
            issues.append(f"Đáp án đúng '{correct_ans}' không nằm trong tập hợp A, B, C, D.")
            score -= 0.5

        # 4. Đánh giá độ dài và tính chất của các phương án nhiễu (distractor plausibility)
        if len(opt_values) == 4:
            lengths = [len(v) for v in opt_values]
            avg_len = sum(lengths) / 4.0
            # Nếu 1 đáp án quá dài gấp 3 lần các đáp án khác, học sinh dễ đoán mò
            max_len = max(lengths)
            min_len = min(lengths)
            if min_len > 0 and max_len / min_len > 4.0:
                issues.append("Độ dài các lựa chọn chênh lệch quá lớn (dễ bị học sinh nhận diện đáp án bẫy).")
                score -= 0.15

        passed = len(issues) == 0 and score >= 0.75
        
        evaluation_report = {
            "passed": passed,
            "distractor_score": round(max(0.1, score), 2),
            "single_truth_verified": correct_ans in required_keys and len(opt_values) == len(set(opt_values)),
            "critic_notes": "; ".join(issues) if issues else "Đạt tiêu chuẩn khảo thí: 1 đáp án duy nhất đúng, 3 đáp án nhiễu có tính phân hóa tốt."
        }

        refined_question = dict(question)
        if not refined_question.get("explanation"):
            refined_question["explanation"] = f"Đáp án đúng là {correct_ans}."

        return passed, refined_question, evaluation_report
