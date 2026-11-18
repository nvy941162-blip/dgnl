import json
import re
from typing import List, Dict, Any, Optional
from backend.config import OPENAI_API_KEY, OPENAI_BASE_URL, OPENAI_MODEL
from backend.agent_council.gemini_rotator import gemini_rotator

class LanguageAgent:
    """
    Language Agent:
    Chuyên phụ trách sinh đoạn văn bản đọc hiểu và các câu hỏi Tiếng Việt / Tiếng Anh
    chuẩn cấu trúc khảo thí ĐGNL Phần 1 (Sử dụng ngôn ngữ).
    Tích hợp xoay vòng Gemini Key (Rotator) và OpenAI.
    """
    def __init__(self):
        pass

    def _call_llm_json(self, prompt: str, system_prompt: str = "") -> Optional[Dict[str, Any]]:
        """Ưu tiên gọi Gemini với key xoay vòng, sau đó đến OpenAI"""
        # 1. Thử gọi qua Gemini Key Rotator
        if gemini_rotator.keys:
            ok, text_res, used_key = gemini_rotator.generate_content(
                prompt=prompt,
                system_instruction=system_prompt,
                response_json=True
            )
            if ok:
                try:
                    # Clean markdown fence if any
                    clean_text = re.sub(r"^```json\s*|\s*```$", "", text_res.strip(), flags=re.MULTILINE)
                    return json.loads(clean_text)
                except Exception as e:
                    print(f"[LanguageAgent] JSON parse error from Gemini: {e}")

        # 2. Thử gọi qua OpenAI
        if OPENAI_API_KEY:
            try:
                from openai import OpenAI
                client = OpenAI(api_key=OPENAI_API_KEY, base_url=OPENAI_BASE_URL)
                res = client.chat.completions.create(
                    model=OPENAI_MODEL,
                    messages=[
                        {"role": "system", "content": system_prompt or "You are a professional exam generator."},
                        {"role": "user", "content": prompt}
                    ],
                    temperature=0.7,
                    response_format={"type": "json_object"}
                )
                return json.loads(res.choices[0].message.content)
            except Exception as e:
                print(f"[LanguageAgent] OpenAI call error: {e}")

        return None

    def generate_vietnamese_item(self, topic: str, difficulty: str, context: str = "") -> Dict[str, Any]:
        """Sinh một câu hỏi trắc nghiệm Tiếng Việt kèm bài đọc hoặc ngữ cảnh"""
        prompt = f"""Bạn là Tác tử Ngôn ngữ (Language Agent) chuyên gia khảo thí Tiếng Việt kỳ thi ĐGNL ĐHQG.
Hãy tạo 1 câu hỏi trắc nghiệm Tiếng Việt chuẩn xác:
- Chủ đề/Ngữ liệu: {topic}
- Tư liệu tham khảo: {context}
- Độ khó: {difficulty} (easy, medium, hard, very_hard)

Yêu cầu định dạng JSON chính xác:
{{
  "prompt": "Nội dung câu hỏi...",
  "passage": "Đoạn văn đọc hiểu hoặc ngữ liệu kèm theo (nếu có, không có thì để null)",
  "options": {{
    "A": "Lựa chọn A",
    "B": "Lựa chọn B",
    "C": "Lựa chọn C",
    "D": "Lựa chọn D"
  }},
  "correct_answer": "A",
  "explanation": "Giải thích chi tiết tại sao đúng và các đáp án bẫy sai ở điểm nào"
}}"""

        data = self._call_llm_json(prompt, "Bạn là chuyên gia ra đề thi môn Tiếng Việt kỳ thi ĐGNL.")
        if data and "options" in data and "correct_answer" in data:
            data["domain"] = "vietnamese"
            data["section_id"] = "section_1_language"
            data["difficulty"] = difficulty
            return data

        # Procedural fallback generator for Vietnamese
        return {
            "domain": "vietnamese",
            "section_id": "section_1_language",
            "difficulty": difficulty,
            "passage": f"Trong tiểu luận phê bình văn học, nhà văn nhận định: 'Văn chương không chỉ tái hiện hiện thực khách quan một cách thụ động, mà còn phản quang tư tưởng, tâm tư và khát vọng nhân đạo sâu xa của thời đại. Một tác phẩm chỉ thực sự sống mãi khi nó chạm tới nỗi đau và niềm tin bất diệt của con người trước nghịch cảnh.'",
            "prompt": f"Theo đoạn văn về {topic}, giá trị trường tồn của một tác phẩm văn chương bắt nguồn từ yếu tố nào?",
            "options": {
                "A": "Sự sao chép nguyên xi mọi chi tiết của hiện thực cuộc sống hằng ngày",
                "B": "Khả năng chạm đến nỗi đau, tư tưởng và khát vọng nhân đạo bất diệt của con người",
                "C": "Dung lượng đồ sộ và ngôn từ hoa mỹ cầu kỳ",
                "D": "Tính chất giải trí thuần túy giúp người đọc thoát ly thực tại"
            },
            "correct_answer": "B",
            "explanation": "Văn bản nêu rõ: 'Một tác phẩm chỉ thực sự sống mãi khi nó chạm tới nỗi đau và niềm tin bất diệt của con người trước nghịch cảnh', chứng minh đáp án B chính xác."
        }

    def generate_english_item(self, topic: str, difficulty: str, context: str = "") -> Dict[str, Any]:
        """Sinh một câu hỏi trắc nghiệm Tiếng Anh kèm bài đọc hoặc ngữ pháp/từ vựng"""
        prompt = f"""You are the Language Agent specializing in the English section of Vietnam National University Competency Exam (ĐGNL).
Generate 1 high-quality multiple choice question in English:
- Topic: {topic}
- Context: {context}
- Difficulty: {difficulty} (easy, medium, hard, very_hard)

Return strictly valid JSON:
{{
  "prompt": "Question stem...",
  "passage": "Reading passage if applicable, or null",
  "options": {{
    "A": "Option A",
    "B": "Option B",
    "C": "Option C",
    "D": "Option D"
  }},
  "correct_answer": "B",
  "explanation": "Detailed explanation of correct answer and distractors"
}}"""

        data = self._call_llm_json(prompt, "You are an English exam test item designer for standardized exams.")
        if data and "options" in data and "correct_answer" in data:
            data["domain"] = "english"
            data["section_id"] = "section_1_language"
            data["difficulty"] = difficulty
            return data

        # Procedural fallback generator for English
        return {
            "domain": "english",
            "section_id": "section_1_language",
            "difficulty": difficulty,
            "passage": "Renewable energy adoption has accelerated significantly over the past decade. However, the intermittent nature of wind and solar sources necessitates advanced grid storage systems to prevent blackouts during peak demand periods.",
            "prompt": "According to the passage, why are advanced grid storage systems required for renewable energy?",
            "options": {
                "A": "Because renewable energy sources generate too much permanent pollution.",
                "B": "Because solar and wind power generation can be intermittent and unpredictable.",
                "C": "Because the electrical grid cannot transmit renewable power under any circumstances.",
                "D": "Because fossil fuel power plants are completely dismantled worldwide."
            },
            "correct_answer": "B",
            "explanation": "The text states: 'the intermittent nature of wind and solar sources necessitates advanced grid storage systems to prevent blackouts'."
        }
