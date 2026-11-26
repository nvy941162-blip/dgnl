import json, random, re, os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from backend.agent_council.gemini_rotator import gemini_rotator

def synthesize_spt_section(subject_name, subject, topic_theme, sec_id, q_type, count, base_templates):
    prompt = f"""Bạn là Chuyên gia Soạn đề Khảo thí ĐH Sư phạm Hà Nội môn {subject_name}.
Hãy biên soạn đúng {count} câu hỏi MỚI TOÀN DIỆN, CHẤT LƯỢNG CAO, CHUẨN GDPT 2018 theo chủ đề: '{topic_theme}'.
Đặc tả dạng câu hỏi:
- Section ID: {sec_id}
- Dạng câu: {q_type}
{'Yêu cầu: Mỗi câu hỏi trắc nghiệm có 4 phương án A, B, C, D và đúng 1 đáp án đúng (A/B/C/D).' if q_type == 'multiple_choice' else ''}
{'Yêu cầu: Câu hỏi Đúng/Sai gồm ngữ cảnh và 4 mệnh đề nhỏ (a, b, c, d). tf_statements: [{\"id\": \"a\", \"text\": \"...\", \"correct\": true}, ...], correct_answer: {\"a\": true, \"b\": false, \"c\": true, \"d\": false}.' if q_type == 'true_false' else ''}
{'Yêu cầu: Câu hỏi điền đáp số/trả lời ngắn. Thí sinh tự điền số hoặc từ ngắn gọn vào correct_answer.' if q_type == 'short_answer' else ''}
{'Yêu cầu: Câu tự luận kèm rubric thang điểm chi tiết (ai_rubric) và hướng dẫn chấm.' if q_type == 'essay' else ''}

Dùng KaTeX LaTeX ($...$) cho mọi công thức Toán/Hóa/Vật lý.
Trả về JSON ARRAY gồm đúng {count} phần tử:
[
  {{
    "question_type": "{q_type}",
    "prompt": "...",
    "passage": null,
    "options": ["A. ...", "B. ...", "C. ...", "D. ..."],
    "tf_statements": [],
    "correct_answer": "...",
    "explanation": "..."
  }}
]
CHỈ TRẢ VỀ JSON ARRAY HỢP LỆ.
"""
    ok, text, mask = gemini_rotator.generate_content(prompt, response_json=True)
    if ok and text:
        try:
            # Clean possible markdown wrap
            cleaned = text.strip()
            if cleaned.startswith("```json"):
                cleaned = cleaned[7:]
            if cleaned.startswith("```"):
                cleaned = cleaned[3:]
            if cleaned.endswith("```"):
                cleaned = cleaned[:-3]
            parsed = json.loads(cleaned.strip())
            if isinstance(parsed, list) and len(parsed) > 0:
                return parsed[:count]
        except Exception as e:
            print(f"Error parsing Gemini generated questions: {e}")

    # Fallback to intelligent dynamic mutations if API fails
    mutated = []
    for idx in range(count):
        tmpl = dict(base_templates[idx % len(base_templates)]) if base_templates else {}
        q = dict(tmpl)
        q["prompt"] = mutate_prompt(q.get("prompt", ""), topic_theme, idx)
        mutated.append(q)
    return mutated

def mutate_prompt(text, theme, idx):
    # Thay đổi số và tham số để câu hỏi không bao giờ trùng lặp
    def replace_num(match):
        val = int(match.group(0))
        delta = random.choice([-3, -2, -1, 1, 2, 3, 5])
        return str(max(1, val + delta))
    mut = re.sub(r'\b[1-9][0-9]?\b', replace_num, text)
    if mut == text:
        mut += f" (Biến thể số {idx+1} theo chủ đề: {theme})"
    return mut

if __name__ == '__main__':
    res = synthesize_spt_section("Toán học", "Toán học", "Hàm số & Tích phân", "part_1", "multiple_choice", 2, [])
    print("Result count:", len(res))
    print("Q1 prompt:", res[0].get("prompt")[:100])
    print("Q1 options:", res[0].get("options"))
    print("Q1 correct:", res[0].get("correct_answer"))
