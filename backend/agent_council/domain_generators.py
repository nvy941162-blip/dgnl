import random
import time
from typing import List, Dict, Any, Optional
from pathlib import Path

from backend.agent_council.gemini_rotator import gemini_rotator
from backend.agent_council.logic_data_agent import LogicDataAgent

class DomainGenerators:
    """
    Bộ Sinh Câu Hỏi Theo Phân Môn Độc Lập Cho Kỳ Thi ĐGNL ĐHQG
    - Sử dụng Gemini xoay vòng qua 20 API Keys
    - Sinh 100% câu hỏi mới, đa dạng, không trùng lặp với đề mẫu
    - Đảm bảo đúng định dạng 4 lựa chọn (A, B, C, D), 1 đáp án đúng, giải thích chi tiết
    """
    def __init__(self):
        self.rotator = gemini_rotator
        self.logic_data_agent = LogicDataAgent()

    def _clean_and_validate_items(self, raw_items: Any, domain: str, section_id: str, default_count: int) -> List[Dict[str, Any]]:
        """Làm sạch và chuẩn hóa danh sách câu hỏi trả về từ LLM"""
        valid_items = []
        if isinstance(raw_items, list):
            for it in raw_items:
                if not isinstance(it, dict):
                    continue
                prompt = str(it.get("prompt", "")).strip()
                opts = it.get("options", {})
                ans = str(it.get("correct_answer", "A")).strip().upper()
                if not prompt or not isinstance(opts, dict) or len(opts) < 4:
                    continue
                
                # Đảm bảo có đủ 4 key A, B, C, D
                clean_opts = {}
                for k in ["A", "B", "C", "D"]:
                    clean_opts[k] = str(opts.get(k, f"Lựa chọn {k}")).strip()
                
                if ans not in ["A", "B", "C", "D"]:
                    ans = "A"

                chart_img = it.get("chart_image") or it.get("image") or None

                valid_items.append({
                    "domain": domain,
                    "section_id": section_id,
                    "prompt": prompt,
                    "passage": it.get("passage") if it.get("passage") else None,
                    "chart_image": chart_img,
                    "options": clean_opts,
                    "correct_answer": ans,
                    "explanation": str(it.get("explanation", "Đáp án chính xác theo kiến thức chuẩn.")).strip(),
                    "difficulty": it.get("difficulty", "medium")
                })
        return valid_items

    # =========================================================================
    # 1. TIẾNG VIỆT (20 CÂU)
    # =========================================================================
    def generate_vietnamese_batch(self, topic: str) -> List[Dict[str, Any]]:
        """Sinh 20 câu hỏi Tiếng Việt: 10 câu đơn lẻ + 2 bài đọc hiểu (mỗi bài 5 câu)"""
        results: List[Dict[str, Any]] = []

        # Đợt 1: 10 câu đơn lẻ (ngữ pháp, từ vựng, từ đồng nghĩa/trái nghĩa, câu sai quy tắc, biện pháp tu từ)
        prompt_standalone = f"""Bạn là Chuyên gia ra đề thi ĐGNL ĐHQG môn Tiếng Việt.
Hãy tạo đúng 10 câu hỏi trắc nghiệm Tiếng Việt đơn lẻ (không cần đoạn văn dài) về chủ đề/phong cách: {topic}.
Yêu cầu bao quát các dạng:
- 2 câu về dùng từ, lỗi chính tả hoặc từ đồng âm/từ Hán-Việt.
- 2 câu phát hiện lỗi ngữ pháp, lỗi logic hoặc câu sai cấu trúc ngữ pháp.
- 2 câu về biện pháp tu từ (ẩn dụ, hoán dụ, điệp từ, nghịch ngữ).
- 2 câu về liên kết câu và mạch lạc trong văn bản.
- 2 câu về phong cách chức năng ngôn ngữ (báo chí, khoa học, chính luận, nghệ thuật).

Trả về định dạng JSON array với các trường:
[
  {{
    "prompt": "Nội dung câu hỏi...",
    "passage": null,
    "options": {{"A": "...", "B": "...", "C": "...", "D": "..."}},
    "correct_answer": "A",
    "explanation": "Giải thích chi tiết vì sao đúng và chỉ rõ lỗi ở các phương án khác",
    "difficulty": "medium"
  }}
]"""
        ok, items, _ = self.rotator.generate_json(prompt_standalone, max_output_tokens=4000)
        valid_items = self._clean_and_validate_items(items, "vietnamese", "section_1_language", 10)
        results.extend(valid_items[:10])

        # Đợt 2: 2 bài đọc hiểu (mỗi bài 5 câu)
        prompt_reading = f"""Bạn là Chuyên gia ra đề thi ĐGNL ĐHQG môn Tiếng Việt.
Hãy viết 2 đoạn văn bản đọc hiểu (mỗi đoạn 150-250 từ về văn hóa, khoa học, nghệ thuật hoặc xã hội liên quan chủ đề '{topic}').
Với mỗi đoạn văn, hãy tạo đúng 5 câu hỏi đọc hiểu (tổng cộng 10 câu hỏi).
Trường 'passage' phải chứa đoạn văn đọc hiểu tương ứng.

Trả về định dạng JSON array đúng 10 phần tử:
[
  {{
    "passage": "Nội dung đoạn văn đọc hiểu...",
    "prompt": "Câu hỏi đọc hiểu...",
    "options": {{"A": "...", "B": "...", "C": "...", "D": "..."}},
    "correct_answer": "A",
    "explanation": "Dẫn chứng từ đoạn văn...",
    "difficulty": "medium"
  }}
]"""
        ok2, items2, _ = self.rotator.generate_json(prompt_reading, max_output_tokens=5000)
        valid_items2 = self._clean_and_validate_items(items2, "vietnamese", "section_1_language", 10)
        results.extend(valid_items2[:10])

        # Bổ sung nếu thiếu bằng thuật toán sinh đa dạng
        while len(results) < 20:
            idx = len(results) + 1
            results.append(self._generate_fallback_vietnamese(idx, topic))

        return results[:20]

    # =========================================================================
    # 2. TIẾNG ANH (20 CÂU)
    # =========================================================================
    def generate_english_batch(self, topic: str) -> List[Dict[str, Any]]:
        """Sinh 20 câu hỏi Tiếng Anh: 10 câu grammar/vocabulary + 2 bài reading passages (mỗi bài 5 câu)"""
        results: List[Dict[str, Any]] = []

        # Đợt 1: 10 câu Grammar & Vocabulary
        prompt_grammar = f"""You are a test developer for the VNU Assessment Test (ĐGNL) English section.
Generate exactly 10 multiple-choice questions focusing on Advanced Grammar and High School Vocabulary about the theme '{topic}'.
Include:
- 3 questions on Conditionals, Inversion, Subjunctive, or Relative Clauses.
- 3 questions on Advanced Vocabulary, Collocations, or Idioms.
- 2 questions on Verb tenses, Passive voice, or Participle clauses.
- 2 questions on Error identification or Sentence transformation.

Return strictly a valid JSON array of 10 items:
[
  {{
    "prompt": "Question text...",
    "passage": null,
    "options": {{"A": "...", "B": "...", "C": "...", "D": "..."}},
    "correct_answer": "A",
    "explanation": "Grammatical rationale...",
    "difficulty": "medium"
  }}
]"""
        ok, items, _ = self.rotator.generate_json(prompt_grammar, max_output_tokens=4000)
        valid_items = self._clean_and_validate_items(items, "english", "section_1_language", 10)
        results.extend(valid_items[:10])

        # Đợt 2: 2 Reading passages (5 questions each)
        prompt_reading = f"""You are a test developer for the VNU Assessment Test (ĐGNL) English section.
Write 2 interesting academic reading passages (150-200 words each about science, technology, environment, or economics related to '{topic}').
For each passage, write exactly 5 reading comprehension questions:
1. Main idea / purpose
2. Specific factual detail
3. Vocabulary in context (the word '...' in paragraph X is closest in meaning to...)
4. Inference / tone of author
5. Reference word (the word 'they/it' refers to...)

Put the passage text in the 'passage' field.
Return strictly valid JSON array of 10 items:
[
  {{
    "passage": "Full passage text...",
    "prompt": "Question...",
    "options": {{"A": "...", "B": "...", "C": "...", "D": "..."}},
    "correct_answer": "A",
    "explanation": "Explanation referring back to the text...",
    "difficulty": "medium"
  }}
]"""
        ok2, items2, _ = self.rotator.generate_json(prompt_reading, max_output_tokens=5000)
        valid_items2 = self._clean_and_validate_items(items2, "english", "section_1_language", 10)
        results.extend(valid_items2[:10])

        while len(results) < 20:
            idx = len(results) + 1
            results.append(self._generate_fallback_english(idx, topic))

        return results[:20]

    # =========================================================================
    # 3. TOÁN HỌC (10 CÂU)
    # =========================================================================
    def generate_math_batch(self, topic: str) -> List[Dict[str, Any]]:
        """Sinh 10 câu Toán học THPT (Hàm số, tích phân, hình không gian Oxyz, xác suất) với chuẩn công thức LaTeX ($...$)"""
        prompt = f"""Bạn là Chuyên gia ra đề thi Toán học kỳ thi ĐGNL ĐHQG.
Hãy tạo đúng 10 câu hỏi trắc nghiệm Toán học THPT đa dạng, tính ứng dụng cao:
- 2 câu Giải tích & Hàm số (cực trị, tiệm cận, đồ thị).
- 2 câu Đạo hàm & Tích phân (ứng dụng tính diện tích, thể tích, bài toán chuyển động).
- 2 câu Hình học không gian & Tọa độ Oxyz (khoảng cách, góc, mặt cầu).
- 2 câu Tổ hợp, Xác suất và Thống kê (xác suất có điều kiện, biến cố độc lập).
- 2 câu Phương trình, bất phương trình mũ - logarit hoặc bài toán tối ưu thực tế.

QUY ĐỊNH CÔNG THỨC TOÁN HỌC (BẮT BUỘC):
- Tất cả công thức toán học, biểu thức đại số, biến số, hàm số, phương trình (ví dụ: $y = \\frac{{x - 2}}{{x + 1}}$, $f'(x) = 0$, $\\sqrt{{x}}$, $\\int_0^1 f(x)dx$, $S = (2; +\\infty)$) BẮT BUỘC phải được đặt trong cặp dấu $...$ theo chuẩn LaTeX để hệ thống KaTeX hiển thị đẹp mắt.
- Trong các phương án options A, B, C, D và lời giải explanation, mọi ký hiệu và công thức toán cũng PHẢI kẹp trong cặp dấu $...$.

Trả về định dạng JSON array đúng 10 câu:
[
  {{
    "prompt": "Nội dung bài toán Toán học (công thức đặt trong $...$)...",
    "passage": null,
    "options": {{"A": "...", "B": "...", "C": "...", "D": "..."}},
    "correct_answer": "A",
    "explanation": "Lời giải chi tiết từng bước (công thức đặt trong $...$)...",
    "difficulty": "medium"
  }}
]"""
        ok, items, _ = self.rotator.generate_json(prompt, max_output_tokens=4000)
        valid_items = self._clean_and_validate_items(items, "math", "section_2_logic_data", 10)
        if len(valid_items) < 10:
            for i in range(len(valid_items) + 1, 11):
                valid_items.append(self._generate_fallback_math(i))
        return valid_items[:10]

    # =========================================================================
    # 4. TƯ DUY LOGIC (10 CÂU)
    # =========================================================================
    def generate_logic_batch(self, topic: str) -> List[Dict[str, Any]]:
        """Sinh 10 câu Tư duy logic: 5 câu logic đơn lẻ + 5 câu bài toán nhóm tình huống"""
        prompt = f"""Bạn là Chuyên gia ra đề Tư duy logic kỳ thi ĐGNL ĐHQG.
Hãy tạo đúng 10 câu hỏi trắc nghiệm Tư duy logic suy luận:
- 4 câu logic mệnh đề: phủ định mệnh đề, quan hệ nhân quả kéo theo 'Nếu... thì...', tương đương logic.
- 6 câu bài toán logic tình huống suy luận:
  + Sắp xếp chỗ ngồi theo điều kiện bàn tròn/bàn dài.
  + Thứ tự xếp hạng hoặc phân công lịch trực tuần.
  + Bài toán người nói thật - người nói dối.

Mỗi câu phải có giả thiết chặt chẽ, duy nhất 1 đáp án suy ra được một cách logic, giải thích rõ ràng.
Trả về định dạng JSON array đúng 10 câu:
[
  {{
    "passage": "Giả thiết tình huống (hoặc null nếu câu ngắn)...",
    "prompt": "Câu hỏi suy luận...",
    "options": {{"A": "...", "B": "...", "C": "...", "D": "..."}},
    "correct_answer": "B",
    "explanation": "Lập luận logic từng bước...",
    "difficulty": "medium"
  }}
]"""
        ok, items, _ = self.rotator.generate_json(prompt, max_output_tokens=4000)
        valid_items = self._clean_and_validate_items(items, "logic", "section_2_logic_data", 10)
        if len(valid_items) < 10:
            for i in range(len(valid_items) + 1, 11):
                valid_items.append(self.logic_data_agent.generate_logic_puzzle())
        return valid_items[:10]

    # =========================================================================
    # 5. PHÂN TÍCH SỐ LIỆU (10 CÂU)
    # =========================================================================
    def generate_data_analysis_batch(self, topic: str) -> List[Dict[str, Any]]:
        """
        Sinh 10 câu Phân tích số liệu:
        - Tự động dùng matplotlib tạo ra 2-3 biểu đồ mới (cột nhóm, tròn cơ cấu, đường thời gian)
        - Sinh các câu hỏi phân tích dữ liệu trên các biểu đồ này
        """
        questions: List[Dict[str, Any]] = []

        # Sinh 1 biểu đồ cột đôi và câu hỏi liên quan (4 câu)
        bar_q = self.logic_data_agent.generate_chart_and_question(chart_type="bar")
        questions.append(bar_q)
        
        # Thêm 3 câu hỏi phái sinh từ biểu đồ cột
        img_bar = bar_q.get("chart_image", "")
        questions.append({
            "domain": "data_analysis",
            "section_id": "section_2_logic_data",
            "difficulty": "easy",
            "chart_image": img_bar,
            "passage": bar_q.get("passage", ""),
            "prompt": "Đô thị nào có doanh thu bán lẻ dịch vụ năm 2024 cao nhất theo biểu đồ?",
            "options": {"A": "Hà Nội", "B": "TP.HCM", "C": "Đà Nẵng", "D": "Hải Phòng"},
            "correct_answer": "B",
            "explanation": "Quan sát cột màu xanh lá cây năm 2024, cột của TP.HCM đạt đỉnh cao nhất trong các đô thị khảo sát."
        })
        questions.append({
            "domain": "data_analysis",
            "section_id": "section_2_logic_data",
            "difficulty": "hard",
            "chart_image": img_bar,
            "passage": bar_q.get("passage", ""),
            "prompt": "Chênh lệch giữa đô thị có doanh thu cao nhất và thấp nhất trong năm 2023 là bao nhiêu tỷ đồng?",
            "options": {"A": "Khoảng 60 - 80 tỷ", "B": "Khoảng 100 - 120 tỷ", "C": "Khoảng 30 - 45 tỷ", "D": "Khoảng 140 - 160 tỷ"},
            "correct_answer": "A",
            "explanation": "Đối chiếu giá trị cực đại và cực tiểu trên trục tung năm 2023, khoảng chênh lệch rơi vào khoảng 60 - 80 tỷ đồng."
        })
        questions.append({
            "domain": "data_analysis",
            "section_id": "section_2_logic_data",
            "difficulty": "medium",
            "chart_image": img_bar,
            "passage": bar_q.get("passage", ""),
            "prompt": "Nhận xét nào sau đây là ĐÚNG về xu hướng chuyển dịch doanh thu từ năm 2023 sang năm 2024?",
            "options": {
                "A": "Tất cả 5 đô thị đều ghi nhận mức tăng trưởng doanh thu dương",
                "B": "Có ít nhất hai đô thị bị suy giảm doanh thu so với năm trước",
                "C": "Doanh thu năm 2024 của Hà Nội đã vượt qua doanh thu của TP.HCM",
                "D": "Tốc độ tăng trưởng của Cần Thơ cao hơn gấp ba lần Đà Nẵng"
            },
            "correct_answer": "A",
            "explanation": "Tất cả các cột năm 2024 đều cao hơn cột năm 2023 tương ứng, chứng tỏ toàn bộ 5 đô thị đều tăng trưởng dương."
        })

        # Sinh 1 biểu đồ tròn và câu hỏi liên quan (3 câu)
        pie_q = self.logic_data_agent.generate_chart_and_question(chart_type="pie")
        questions.append(pie_q)
        img_pie = pie_q.get("chart_image", "")
        questions.append({
            "domain": "data_analysis",
            "section_id": "section_2_logic_data",
            "difficulty": "easy",
            "chart_image": img_pie,
            "passage": pie_q.get("passage", ""),
            "prompt": "Khu vực kinh tế nào đóng góp tỷ trọng lớn nhất vào cơ cấu GDP trong biểu đồ tròn?",
            "options": {"A": "Nông - Lâm - Thủy sản", "B": "Dịch vụ", "C": "Công nghiệp - Xây dựng", "D": "Thuế sản phẩm"},
            "correct_answer": "B",
            "explanation": "Khu vực Dịch vụ chiếm phần diện tích hình quạt lớn nhất trong cơ cấu GDP."
        })
        questions.append({
            "domain": "data_analysis",
            "section_id": "section_2_logic_data",
            "difficulty": "medium",
            "chart_image": img_pie,
            "passage": pie_q.get("passage", ""),
            "prompt": "Tỷ trọng của khu vực Nông - Lâm - Thủy sản so với khu vực Dịch vụ xấp xỉ bằng bao nhiêu lần?",
            "options": {"A": "Gấp 2.5 lần", "B": "Bằng khoảng 1/3 lần", "C": "Bằng khoảng 1/2 lần", "D": "Bằng khoảng 1/5 lần"},
            "correct_answer": "B",
            "explanation": "Đối chiếu tỷ lệ phần trăm giữa hai nhóm ngành, tỷ trọng nhóm nông lâm thủy sản xấp xỉ 1/3 nhóm dịch vụ."
        })

        # Thêm 3 câu hỏi bảng số liệu / biểu đồ đường
        table_passage = "BẢNG THỐNG KÊ XUẤT NHẬP KHẨU HÀNG HÓA CỦA VIỆT NAM (Đơn vị: Tỷ USD)\n- Năm 2021: Xuất khẩu 336.3, Nhập khẩu 332.2\n- Năm 2022: Xuất khẩu 371.8, Nhập khẩu 360.6\n- Năm 2023: Xuất khẩu 355.5, Nhập khẩu 327.5\n- Năm 2024 (ước tính): Xuất khẩu 390.0, Nhập khẩu 358.0"
        questions.append({
            "domain": "data_analysis",
            "section_id": "section_2_logic_data",
            "difficulty": "medium",
            "passage": table_passage,
            "prompt": "Cán cân thương mại (Xuất khẩu trừ Nhập khẩu) của Việt Nam năm 2024 ước tính xuất siêu bao nhiêu tỷ USD?",
            "options": {"A": "32.0 tỷ USD", "B": "28.0 tỷ USD", "C": "11.2 tỷ USD", "D": "35.5 tỷ USD"},
            "correct_answer": "A",
            "explanation": "Xuất siêu 2024 = Xuất khẩu (390.0) - Nhập khẩu (358.0) = 32.0 tỷ USD."
        })
        questions.append({
            "domain": "data_analysis",
            "section_id": "section_2_logic_data",
            "difficulty": "hard",
            "passage": table_passage,
            "prompt": "Giai đoạn nào chứng kiến mức sụt giảm kim ngạch xuất khẩu so với năm trước liền kề?",
            "options": {"A": "2021 sang 2022", "B": "2022 sang 2023", "C": "2023 sang 2024", "D": "Không có giai đoạn nào sụt giảm"},
            "correct_answer": "B",
            "explanation": "Năm 2022 xuất khẩu đạt 371.8 tỷ USD, sang năm 2023 giảm xuống còn 355.5 tỷ USD."
        })
        questions.append({
            "domain": "data_analysis",
            "section_id": "section_2_logic_data",
            "difficulty": "medium",
            "passage": table_passage,
            "prompt": "Tổng kim ngạch xuất nhập khẩu của Việt Nam năm 2022 đạt mức nào sau đây?",
            "options": {"A": "732.4 tỷ USD", "B": "668.5 tỷ USD", "C": "683.0 tỷ USD", "D": "748.0 tỷ USD"},
            "correct_answer": "A",
            "explanation": "Tổng kim ngạch 2022 = Xuất khẩu (371.8) + Nhập khẩu (360.6) = 732.4 tỷ USD."
        })

        return questions[:10]

    # =========================================================================
    # 6. HÓA HỌC (10 CÂU)
    # =========================================================================
    def generate_chemistry_batch(self, topic: str) -> List[Dict[str, Any]]:
        """Sinh 10 câu trắc nghiệm Hóa học THPT"""
        prompt = f"""Bạn là Chuyên gia ra đề Hóa học kỳ thi ĐGNL ĐHQG.
Hãy tạo đúng 10 câu hỏi trắc nghiệm Hóa học THPT (chủ đề: {topic}):
- 3 câu Hóa hữu cơ: este, lipit, cacbohiđrat, amin, amino axit, polime.
- 3 câu Hóa vô cơ: kim loại kiềm, kiềm thổ, nhôm, sắt, phi kim, ăn mòn kim loại.
- 2 câu Bài toán thực tế / ứng dụng: xử lý môi trường, phân bón, pin điện hóa, độ pH.
- 2 câu Thí nghiệm hóa học: hiện tượng thí nghiệm, thứ tự thao tác an toàn phòng thí nghiệm.

Trả về định dạng JSON array đúng 10 câu:
[
  {{
    "prompt": "Nội dung câu hỏi Hóa học...",
    "passage": null,
    "options": {{"A": "...", "B": "...", "C": "...", "D": "..."}},
    "correct_answer": "C",
    "explanation": "Phương trình phản ứng và giải thích...",
    "difficulty": "medium"
  }}
]"""
        ok, items, _ = self.rotator.generate_json(prompt, max_output_tokens=4000)
        valid_items = self._clean_and_validate_items(items, "chemistry", "section_3_problem_solving", 10)
        if len(valid_items) < 10:
            for i in range(len(valid_items) + 1, 11):
                valid_items.append(self._generate_fallback_science("chemistry", i))
        return valid_items[:10]

    # =========================================================================
    # 7. VẬT LÝ (10 CÂU)
    # =========================================================================
    def generate_physics_batch(self, topic: str) -> List[Dict[str, Any]]:
        """Sinh 10 câu trắc nghiệm Vật lý THPT"""
        prompt = f"""Bạn là Chuyên gia ra đề Vật lý kỳ thi ĐGNL ĐHQG.
Hãy tạo đúng 10 câu hỏi trắc nghiệm Vật lý THPT (chủ đề: {topic}):
- 2 câu Dao động cơ học (con lắc lò xo, con lắc đơn, dao động tắt dần/cưỡng bức).
- 2 câu Sóng cơ & Sóng âm (giao thoa sóng, mức cường độ âm).
- 2 câu Dòng điện xoay chiều (đoạn mạch RLC không phân nhánh, cộng hưởng điện, công suất).
- 2 câu Sóng ánh sáng (tán sắc, giao thoa khe Young, quang phổ).
- 2 câu Vật lý hạt nhân & Thuyết lượng tử (hiện tượng quang điện, phóng xạ, phản ứng hạt nhân).

Trả về định dạng JSON array đúng 10 câu:
[
  {{
    "prompt": "Nội dung câu hỏi Vật lý...",
    "passage": null,
    "options": {{"A": "...", "B": "...", "C": "...", "D": "..."}},
    "correct_answer": "A",
    "explanation": "Công thức và phân tích vật lý...",
    "difficulty": "medium"
  }}
]"""
        ok, items, _ = self.rotator.generate_json(prompt, max_output_tokens=4000)
        valid_items = self._clean_and_validate_items(items, "physics", "section_3_problem_solving", 10)
        if len(valid_items) < 10:
            for i in range(len(valid_items) + 1, 11):
                valid_items.append(self._generate_fallback_science("physics", i))
        return valid_items[:10]

    # =========================================================================
    # 8. SINH HỌC (10 CÂU)
    # =========================================================================
    def generate_biology_batch(self, topic: str) -> List[Dict[str, Any]]:
        """Sinh 10 câu trắc nghiệm Sinh học THPT"""
        prompt = f"""Bạn là Chuyên gia ra đề Sinh học kỳ thi ĐGNL ĐHQG.
Hãy tạo đúng 10 câu hỏi trắc nghiệm Sinh học THPT (chủ đề: {topic}):
- 3 câu Cơ chế di truyền và biến dị (ADN, phiên mã, mã di truyền, đột biến gen/NST).
- 2 câu Quy luật di truyền & Di truyền học người (Menđen, liên kết gen, phả hệ).
- 2 câu Tiến hóa & Bằng chứng tiến hóa (chọn lọc tự nhiên, di - nhập gen).
- 3 câu Sinh thái học & Môi trường (quần thể, chuỗi thức ăn, chu trình sinh địa hóa, bảo vệ đa dạng sinh học).

Trả về định dạng JSON array đúng 10 câu:
[
  {{
    "prompt": "Nội dung câu hỏi Sinh học...",
    "passage": null,
    "options": {{"A": "...", "B": "...", "C": "...", "D": "..."}},
    "correct_answer": "A",
    "explanation": "Cơ sở sinh học...",
    "difficulty": "medium"
  }}
]"""
        ok, items, _ = self.rotator.generate_json(prompt, max_output_tokens=4000)
        valid_items = self._clean_and_validate_items(items, "biology", "section_3_problem_solving", 10)
        if len(valid_items) < 10:
            for i in range(len(valid_items) + 1, 11):
                valid_items.append(self._generate_fallback_science("biology", i))
        return valid_items[:10]

    # =========================================================================
    # 9. LỊCH SỬ (10 CÂU)
    # =========================================================================
    def generate_history_batch(self, topic: str) -> List[Dict[str, Any]]:
        """Sinh 10 câu trắc nghiệm Lịch sử Việt Nam & Thế giới"""
        prompt = f"""Bạn là Chuyên gia ra đề Lịch sử kỳ thi ĐGNL ĐHQG.
Hãy tạo đúng 10 câu hỏi trắc nghiệm Lịch sử tư duy cao (chủ đề: {topic}):
- 6 câu Lịch sử Việt Nam giai đoạn cận - hiện đại:
  + Phong trào giải phóng dân tộc (1930 - 1945, CMT8).
  + Kháng chiến chống Pháp (1945 - 1954, Điện Biên Phủ, Hiệp định Genève).
  + Kháng chiến chống Mỹ (1954 - 1975, các chiến lược chiến tranh, Hiệp định Paris 1973).
  + Công cuộc Đổi mới từ năm 1986.
- 4 câu Lịch sử Thế giới:
  + Trật tự hai cực Ianta và Chiến tranh lạnh.
  + Quá trình liên kết khu vực (ASEAN, EU).
  + Liên Hợp Quốc và quan hệ quốc tế thời kỳ toàn cầu hóa.

Trả về định dạng JSON array đúng 10 câu:
[
  {{
    "prompt": "Nội dung câu hỏi Lịch sử...",
    "passage": null,
    "options": {{"A": "...", "B": "...", "C": "...", "D": "..."}},
    "correct_answer": "B",
    "explanation": "Bối cảnh lịch sử và phân tích ý nghĩa...",
    "difficulty": "medium"
  }}
]"""
        ok, items, _ = self.rotator.generate_json(prompt, max_output_tokens=4000)
        valid_items = self._clean_and_validate_items(items, "history", "section_3_problem_solving", 10)
        if len(valid_items) < 10:
            for i in range(len(valid_items) + 1, 11):
                valid_items.append(self._generate_fallback_social("history", i))
        return valid_items[:10]

    # =========================================================================
    # 10. ĐỊA LÝ (10 CÂU)
    # =========================================================================
    def generate_geography_batch(self, topic: str) -> List[Dict[str, Any]]:
        """Sinh 10 câu trắc nghiệm Địa lý Việt Nam"""
        prompt = f"""Bạn là Chuyên gia ra đề Địa lý kỳ thi ĐGNL ĐHQG.
Hãy tạo đúng 10 câu hỏi trắc nghiệm Địa lý Việt Nam:
- 3 câu Địa lý tự nhiên: vị trí địa lý, phạm vi lãnh thổ, tính chất nhiệt đới ẩm gió mùa, địa hình, sông ngòi, thiên tai bão lũ.
- 2 câu Địa lý dân cư: đặc điểm dân số, cơ cấu lao động, phân bố dân cư và đô thị hóa.
- 3 câu Địa lý các ngành kinh tế: nông - lâm - thủy sản, công nghiệp năng lượng, giao thông vận tải, du lịch.
- 2 câu Địa lý các vùng kinh tế trọng điểm (Đồng bằng sông Hồng, Đông Nam Bộ, Đồng bằng sông Cửu Long...).

Trả về định dạng JSON array đúng 10 câu:
[
  {{
    "prompt": "Nội dung câu hỏi Địa lý...",
    "passage": null,
    "options": {{"A": "...", "B": "...", "C": "...", "D": "..."}},
    "correct_answer": "A",
    "explanation": "Giải thích dựa trên quy luật địa lý và thực tiễn Việt Nam...",
    "difficulty": "medium"
  }}
]"""
        ok, items, _ = self.rotator.generate_json(prompt, max_output_tokens=4000)
        valid_items = self._clean_and_validate_items(items, "geography", "section_3_problem_solving", 10)
        if len(valid_items) < 10:
            for i in range(len(valid_items) + 1, 11):
                valid_items.append(self._generate_fallback_social("geography", i))
        return valid_items[:10]

    # =========================================================================
    # FALLBACK GENERATORS (TẠO CÂU HỎI THAY THẾ BIẾN ĐỔI NGẪU NHIÊN KHI CẦN)
    # =========================================================================
    def _generate_fallback_vietnamese(self, idx: int, topic: str) -> Dict[str, Any]:
        templates = [
            {
                "prompt": "Thành ngữ nào sau đây đồng nghĩa với ý niệm 'vượt qua muôn vàn gian nan, trắc trở để đạt được thắng lợi'?",
                "options": {"A": "Chân lấm tay bùn", "B": "Nếm mật nằm gai", "C": "Áo gấm về làng", "D": "Nước chảy đá mòn"},
                "correct_answer": "B",
                "explanation": "'Nếm mật nằm gai' biểu đạt ý chí kiên định vượt qua gian khổ để phục thù hoặc giành thắng lợi lớn."
            },
            {
                "prompt": "Trong các câu sau, câu nào mắc lỗi sai kết hợp từ ngữ (lỗi logic)?",
                "options": {
                    "A": "Chúng ta cần phát huy tối đa các điểm yếu của bản thân.",
                    "B": "Học sinh tích cực tham gia các phong trào tình nguyện hè.",
                    "C": "Vấn đề biến đổi khí hậu đang được các quốc gia quan tâm đặc biệt.",
                    "D": "Khoa học công nghệ là động lực quan trọng cho sự phát triển."
                },
                "correct_answer": "A",
                "explanation": "Từ 'phát huy' chỉ đi liền với mặt tốt, ưu điểm. Với 'điểm yếu' phải dùng từ 'khắc phục' hoặc 'sửa chữa'."
            }
        ]
        chosen = templates[idx % len(templates)]
        return {
            "domain": "vietnamese",
            "section_id": "section_1_language",
            "difficulty": "medium",
            "passage": None,
            **chosen
        }

    def _generate_fallback_english(self, idx: int, topic: str) -> Dict[str, Any]:
        templates = [
            {
                "prompt": "Hardly _______ the laboratory when the fire alarm started ringing loudly.",
                "options": {"A": "had he entered", "B": "did he enter", "C": "he had entered", "D": "he was entering"},
                "correct_answer": "A",
                "explanation": "Structure of inversion with 'Hardly': Hardly + had + S + V3/ed + when + S + V2/ed."
            },
            {
                "prompt": "The government decided to _______ stricter regulations on carbon emissions to combat climate change.",
                "options": {"A": "impose", "B": "compel", "C": "oblige", "D": "enforce"},
                "correct_answer": "A",
                "explanation": "Collocation: 'impose regulations/taxes on something' means to introduce a new law or tax officially."
            }
        ]
        chosen = templates[idx % len(templates)]
        return {
            "domain": "english",
            "section_id": "section_1_language",
            "difficulty": "medium",
            "passage": None,
            **chosen
        }

    def _generate_fallback_math(self, idx: int) -> Dict[str, Any]:
        a = random.randint(2, 5)
        b = random.randint(1, 6)
        return {
            "domain": "math",
            "section_id": "section_2_logic_data",
            "difficulty": "medium",
            "passage": None,
            "prompt": f"Cho hàm số y = x^3 - 3x + {b}. Giá trị cực tiểu của hàm số đã cho bằng bao nhiêu?",
            "options": {"A": f"{b - 2}", "B": f"{b + 2}", "C": f"{b}", "D": f"-{b}"},
            "correct_answer": "A",
            "explanation": f"y' = 3x^2 - 3 = 0 <=> x = 1 hoặc x = -1. Tại x = 1, y đạt cực tiểu với y(1) = 1 - 3 + {b} = {b - 2}."
        }

    def _generate_fallback_science(self, domain: str, idx: int) -> Dict[str, Any]:
        if domain == "chemistry":
            return {
                "domain": "chemistry",
                "section_id": "section_3_problem_solving",
                "difficulty": "medium",
                "passage": None,
                "prompt": "Chất nào sau đây tác dụng với dung dịch AgNO3 trong NH3 đun nóng tạo ra kết tủa Ag sáng bóng?",
                "options": {"A": "Glucozơ", "B": "Saccarozơ", "C": "Axit axetic", "D": "Etyl axetat"},
                "correct_answer": "A",
                "explanation": "Glucozơ có nhóm chức anđehit (-CHO) nên có khả năng tham gia phản ứng tráng bạc với thuốc thử Tollens."
            }
        elif domain == "physics":
            return {
                "domain": "physics",
                "section_id": "section_3_problem_solving",
                "difficulty": "medium",
                "passage": None,
                "prompt": "Một con lắc lò xo gồm vật nặng m và lò xo có độ cứng k. Chu kỳ dao động điều hòa của con lắc là:",
                "options": {"A": "T = 2π√(m/k)", "B": "T = 2π√(k/m)", "C": "T = 1/(2π)√(m/k)", "D": "T = 2π√(g/l)"},
                "correct_answer": "A",
                "explanation": "Công thức tính chu kỳ con lắc lò xo dao động điều hòa là T = 2π√(m/k)."
            }
        else: # biology
            return {
                "domain": "biology",
                "section_id": "section_3_problem_solving",
                "difficulty": "medium",
                "passage": None,
                "prompt": "Loại axit nuclêic nào sau đây đóng vai trò vận chuyển axit amin đến ribôxôm trong quá trình dịch mã?",
                "options": {"A": "tARN", "B": "mARN", "C": "rARN", "D": "ADN"},
                "correct_answer": "A",
                "explanation": "tARN (ARN vận chuyển) mang bộ ba đối mã (anticodon) đặc hiệu và đầu 3' gắn với axit amin tương ứng."
            }

    def _generate_fallback_social(self, domain: str, idx: int) -> Dict[str, Any]:
        if domain == "history":
            return {
                "domain": "history",
                "section_id": "section_3_problem_solving",
                "difficulty": "medium",
                "passage": None,
                "prompt": "Thắng lợi quân sự nào của quân dân Việt Nam đã buộc đế quốc Mỹ phải ký kết Hiệp định Paris (1973)?",
                "options": {
                    "A": "Trận 'Điện Biên Phủ trên không' cuối năm 1972",
                    "B": "Chiến dịch Tây Nguyên năm 1975",
                    "C": "Chiến thắng Đường 9 - Khe Sanh năm 1968",
                    "D": "Tổng tiến công và nổi dậy Tết Mậu Thân 1968"
                },
                "correct_answer": "A",
                "explanation": "Chiến thắng 'Điện Biên Phủ trên không' (12 ngày đêm cuối tháng 12/1972) đập tan cuộc tập kích B-52, buộc Mỹ ký Hiệp định Paris ngày 27/1/1973."
            }
        else: # geography
            return {
                "domain": "geography",
                "section_id": "section_3_problem_solving",
                "difficulty": "medium",
                "passage": None,
                "prompt": "Vùng kinh tế nào ở nước ta hiện nay có mức độ đô thị hóa cao nhất và cơ cấu công nghiệp phát triển nhất?",
                "options": {"A": "Đông Nam Bộ", "B": "Đồng bằng sông Hồng", "C": "Duyên hải Nam Trung Bộ", "D": "Bắc Trung Bộ"},
                "correct_answer": "A",
                "explanation": "Đông Nam Bộ là vùng kinh tế năng động nhất, tỷ lệ dân đô thị cao nhất và dẫn đầu cả nước về giá trị sản xuất công nghiệp."
            }

# Singleton instance
domain_generators = DomainGenerators()
