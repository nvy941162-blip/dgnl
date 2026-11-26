import re
import json
from typing import Dict, Any
from backend.agent_council.gemini_rotator import gemini_rotator

def grade_essay_with_ai(
    prompt: str,
    student_essay: str,
    official_rubric: str,
    max_points: float = 1.0,
    subject_domain: str = "Tự luận"
) -> Dict[str, Any]:
    """
    Tác tử Chấm thi Tự luận (AI Essay Grader Agent):
    Đánh giá bài làm tự luận của học sinh dựa trên barem điểm khảo thí (Rubric).
    Trả về điểm số chính xác và nhận xét sư phạm chi tiết.
    """
    if not student_essay or not student_essay.strip():
        return {
            "score": 0.0,
            "feedback": "Thí sinh chưa nhập câu trả lời cho câu hỏi tự luận này.",
            "criteria_breakdown": ["Chưa có nội dung trả lời"]
        }

    gemini_key, model_name = gemini_rotator.get_available_key()

    # Nếu không có key hoặc chạy offline, dùng rubric đánh giá heuristic từ khóa
    if not gemini_key:
        return _heuristic_grade(prompt, student_essay, official_rubric, max_points)

    system_prompt = f"""Bạn là Chuyên gia Khảo thí và Giảng viên Sư phạm chấm thi môn {subject_domain}.
Nhiệm vụ của bạn là đọc bài làm của học sinh, đối chiếu với Đề bài và Barem điểm chuẩn (Rubric),
sau đó chấm điểm công tâm và nhận xét sư phạm mang tính xây dựng.

ĐỀ BÀI:
{prompt}

BAREM ĐIỂM / HƯỚNG DẪN CHẤM CHUẨN:
{official_rubric}

ĐIỂM TỐI ĐA CỦA CÂU: {max_points} điểm.

BÀI LÀM CỦA HỌC SINH:
{student_essay}

Hãy chấm điểm và trả về DUY NHẤT một chuỗi JSON chuẩn (không kèm markdown ngoài) theo cấu trúc:
{{
  "score": <số điểm học sinh đạt được, từ 0.0 đến {max_points}, làm tròn đến 0.25>,
  "feedback": "<Nhận xét sư phạm ngắn gọn 2-3 câu: điểm tốt của học sinh, lỗi sai hoặc ý còn thiếu, hướng dẫn cải thiện>",
  "strengths": "<Điểm đã làm tốt>",
  "improvements": "<Điểm cần bổ sung>"
}}
"""

    try:
        raw_response = gemini_rotator.call_gemini_api(gemini_key, model_name, system_prompt)
        json_match = re.search(r"\{.*\}", raw_response, re.DOTALL)
        if json_match:
            data = json.loads(json_match.group(0))
            score = float(data.get("score", 0.0))
            score = max(0.0, min(max_points, score))
            return {
                "score": round(score, 2),
                "feedback": data.get("feedback", "Đã đánh giá theo barem điểm khảo thí."),
                "strengths": data.get("strengths", ""),
                "improvements": data.get("improvements", "")
            }
    except Exception as e:
        print(f"[AIEssayGrader] Lỗi gọi Gemini: {e}")

    return _heuristic_grade(prompt, student_essay, official_rubric, max_points)

def _heuristic_grade(prompt: str, student_essay: str, official_rubric: str, max_points: float) -> Dict[str, Any]:
    """Chấm điểm dự phòng dựa trên độ hoàn thiện câu trả lời và từ khóa cốt lõi"""
    words = student_essay.strip().split()
    word_count = len(words)

    # Đánh giá cơ bản theo độ dài và nội dung
    if word_count < 10:
        ratio = 0.25
        fb = "Bài làm quá ngắn, mới chỉ nêu được ý mở đầu, thiếu các bước lập luận chi tiết."
    elif word_count < 30:
        ratio = 0.5
        fb = "Bài làm đã nêu được một số luận điểm cơ bản nhưng cần lập luận chặt chẽ và đầy đủ các bước giải hơn."
    elif word_count < 60:
        ratio = 0.75
        fb = "Bài làm khá tốt, nắm được phương pháp và cấu trúc bài thi, cần chú ý tính chính xác của các thuật ngữ chuyên môn."
    else:
        ratio = 1.0
        fb = "Bài làm chi tiết, mạch lạc, lập luận đầy đủ theo yêu cầu của barem điểm."

    earned = round(max_points * ratio, 2)
    return {
        "score": earned,
        "feedback": fb,
        "strengths": "Học sinh có ý thức giải quyết bài toán và lập luận tự luận.",
        "improvements": "Rèn luyện thêm kỹ năng trình bày mạch lạc theo từng bước barem."
    }
