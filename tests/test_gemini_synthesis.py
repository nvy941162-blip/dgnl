import json, os, sys
sys.path.insert(0, ".")

from backend.agent_council.gemini_rotator import gemini_rotator

prompt = """Bạn là Trưởng ban Đề thi Chuyên gia Khảo thí ĐH Sư phạm Hà Nội.
Hãy tạo 3 CÂU HỎI MỚI TOÀN DIỆN môn Toán học chuẩn GDPT 2018 theo chủ đề: 'Hàm số, Tích phân và Hình không gian'.
Mỗi câu hỏi phải có số liệu mới, hoàn toàn khác các đề mẫu có sẵn.

Định dạng JSON trả về dạng mảng:
[
  {
    "question_type": "multiple_choice",
    "prompt": "Câu hỏi dùng KaTeX LaTeX...",
    "options": ["A. ...", "B. ...", "C. ...", "D. ..."],
    "correct_answer": "A",
    "explanation": "Lời giải chi tiết...",
    "points": 0.25
  }
]
CHỈ TRẢ VỀ JSON HỢP LỆ, KHÔNG KÈM GIẢI THÍCH NGOÀI.
"""

ok, text, mask = gemini_rotator.generate_content(prompt, response_json=True)
print('Success:', ok, 'Mask:', mask)
if ok:
    try:
        data = json.loads(text)
        print('Generated', len(data), 'fresh questions!')
        for i, q in enumerate(data):
            print(f"Q{i+1}: {q['prompt'][:80]} | Correct: {q['correct_answer']}")
    except Exception as e:
        print('JSON error:', e, text[:300])
