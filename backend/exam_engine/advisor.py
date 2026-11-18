import os
from typing import Dict, Any, List
from backend.config import OPENAI_API_KEY, GEMINI_API_KEY, OPENAI_MODEL, OPENAI_BASE_URL

DOMAIN_ADVICE_CATALOG = {
    "vietnamese": {
        "title": "Phần Tiếng Việt (Ngữ pháp, Đọc hiểu & Phong cách ngôn ngữ)",
        "tips": [
            "Tập trung ôn luyện các biện pháp tu từ (ẩn dụ, hoán dụ, điệp từ, chêm xen) và phong cách chức năng ngôn ngữ (báo chí, chính luận, nghệ thuật, khoa học).",
            "Đọc kỹ đề bài để phân biệt lỗi sai dùng từ (lỗi kết hợp từ, lỗi lẫn lộn từ gần âm, lỗi lặp từ vô nghĩa).",
            "Khi làm đoạn văn đọc hiểu, hãy áp dụng kỹ thuật gạch chân từ khóa trung tâm (keywords) và nắm bắt thái độ/giọng điệu của tác giả."
        ]
    },
    "english": {
        "title": "Phần Tiếng Anh (Ngữ pháp, Từ vựng & Đọc hiểu đoạn văn)",
        "tips": [
            "Củng cố các chủ điểm ngữ pháp trọng tâm: Câu điều kiện hỗn hợp, Mệnh đề quan hệ rút gọn, Đảo ngữ, Cấu trúc câu giả định và Giới từ đi kèm cụm động từ (Phrasal Verbs).",
            "Đối với bài đọc dài, không nên dịch từng từ một; hãy dùng kỹ năng Skimming để nắm ý chính (Main Idea) và Scanning để tìm số liệu/thông tin cụ thể trả lời câu hỏi chi tiết.",
            "Lưu ý các câu hỏi từ đồng nghĩa/trái nghĩa trong ngữ cảnh (Contextual clues)."
        ]
    },
    "math": {
        "title": "Phần Toán học (Đại số & Hình học THPT)",
        "tips": [
            "Nắm vững các dạng toán thực tế ứng dụng hàm số (cực trị thực tế, bài toán tối ưu chi phí, lãi suất ngân hàng).",
            "Ôn tập kỹ phần Xác suất - Thống kê và Tổ hợp/Chỉnh hợp - đây là nội dung chiếm tỷ trọng quan trọng trong đề ĐGNL.",
            "Rèn luyện kỹ năng bấm máy tính Casio để tối ưu hóa thời gian tính toán cho các bài tích phân và hình giải tích Oxyz."
        ]
    },
    "logic": {
        "title": "Phần Tư duy Logic (Suy luận quy nạp, Sắp xếp & Mệnh đề)",
        "tips": [
            "Tuyệt đối không giải nhẩm; hãy vẽ bảng ma trận hoặc sơ đồ thứ tự (ví dụ: vẽ 6 vị trí ghế ngồi từ 1 đến 6) để điền các dữ kiện cố định trước.",
            "Nhận diện điều kiện 'Nếu... thì...' (mệnh đề kéo theo P -> Q tương đương phủ định ~Q -> ~P).",
            "Phát hiện các dữ kiện liên kết then chốt nối giữa 2 hoặc nhiều giả thiết để loại trừ ngay lập tức các phương án vô lý."
        ]
    },
    "data_analysis": {
        "title": "Phần Phân tích Số liệu (Biểu đồ tròn, cột, đường & Bảng số liệu)",
        "tips": [
            "Quan sát kỹ đơn vị đo trên hai trục tung/trục hoành và ghi chú của biểu đồ (ví dụ: tỷ USD, triệu tấn, phần trăm).",
            "Thành thạo công thức tính tốc độ tăng trưởng: ((Năm sau - Năm trước) / Năm trước) * 100% thay vì chỉ nhìn vào độ tăng tuyệt đối.",
            "Ước lượng nhanh (Mental Math) bằng cách làm tròn số có quy luật để loại trừ các đáp án chênh lệch lớn mà không cần bấm máy tính quá nhiều bước."
        ]
    },
    "chemistry": {
        "title": "Phần Hóa học (Giải quyết vấn đề & Thực nghiệm)",
        "tips": [
            "Đề thi ĐGNL chú trọng câu hỏi dạng thí nghiệm thực hành: nhận biết hiện tượng kết tủa, bay hơi, đổi màu chất chỉ thị.",
            "Rèn luyện khả năng đọc hiểu các đoạn văn mô tả quy trình sản xuất hóa học công nghiệp hoặc xử lý môi trường để trích xuất phương trình phản ứng."
        ]
    },
    "physics": {
        "title": "Phần Vật lý (Hiện tượng thực tế & Tư duy định tính)",
        "tips": [
            "Chú trọng các hiện tượng quang học, điện xoay chiều và sóng cơ học gắn liền với đời sống (radar, siêu âm, truyền tải điện năng).",
            "Tập trung hiểu rõ bản chất vật lý của các đại lượng thay vì chỉ học thuộc công thức toán học rời rạc."
        ]
    },
    "biology": {
        "title": "Phần Sinh học (Cơ chế di truyền, Tiến hóa & Sinh thái)",
        "tips": [
            "Đọc kỹ các đoạn văn mô tả sơ đồ phả hệ hoặc thí nghiệm di truyền phân tử mới; xác định quy luật di truyền chi phối.",
            "Hệ thống hóa kiến thức chu trình sinh địa hóa và mối quan hệ giữa các loài trong quần xã sinh vật."
        ]
    },
    "history": {
        "title": "Phần Lịch sử (Tư duy liên hệ & Nguyên nhân - Kết quả)",
        "tips": [
            "ĐGNL không hỏi ngày tháng cụ thể mà hỏi về ý nghĩa lịch sử, bài học kinh nghiệm, và mối liên hệ giữa lịch sử Việt Nam với bối cảnh quốc tế.",
            "Phân tích kỹ ngữ liệu đoạn trích tuyên ngôn, nghị quyết, trích dẫn văn kiện để rút ra nhận định đúng."
        ]
    },
    "geography": {
        "title": "Phần Địa lý (Khai thác số liệu, Bản đồ & Chuyển dịch kinh tế)",
        "tips": [
            "Nắm vững các quy luật phân hóa tự nhiên theo Bắc - Nam, Đông - Tây và theo đai cao của Việt Nam.",
            "Phân tích xu hướng chuyển dịch cơ cấu ngành kinh tế và khai thác thế mạnh của từng vùng kinh tế trọng điểm."
        ]
    }
}

def generate_personalized_advice(domain_stats: Dict[str, Any], total_score: float) -> str:
    """
    Sinh lời khuyên ôn tập cá nhân hóa.
    Nếu có API Key (OpenAI hoặc Gemini), gọi LLM để viết lời khuyên sâu sắc.
    Nếu không, sử dụng heuristic engine tư vấn sư phạm chuyên sâu.
    """
    weak_keys = [k for k, v in domain_stats.items() if v.get("percentage", 0) < 60.0]
    strong_keys = [k for k, v in domain_stats.items() if v.get("percentage", 0) >= 75.0]

    # Kiểm tra xem có Gemini hoặc OpenAI để gọi AI trực tiếp không
    from backend.agent_council.gemini_rotator import gemini_rotator
    summary_stats = "\n".join([f"- {v['name']}: {v['percentage']}% ({v['correct']}/{v['total']} câu)" for k, v in domain_stats.items()])
    prompt = f"""Bạn là Chuyên gia Khảo thí và Luyện thi Đánh giá Năng lực (ĐGNL) ĐHQG hàng đầu.
Học sinh vừa hoàn thành bài thi thử ĐGNL với kết quả:
- Tổng điểm: {total_score}/1200 điểm
- Chi tiết từng phần:
{summary_stats}

Hãy viết một báo cáo tư vấn và lộ trình ôn tập cá nhân hóa dành riêng cho học sinh này:
1. Đánh giá tổng quan phong độ và phân vị điểm số.
2. Phân tích cụ thể các lỗ hổng tư duy và kiến thức tại các môn yếu nhất.
3. Kế hoạch hành động 4 tuần tập trung để bứt phá 150 - 200 điểm.
4. Lời khuyên chiến thuật phân bổ thời gian trong phòng thi (150 phút cho 120 câu).
Viết bằng tiếng Việt với văn phong truyền cảm hứng, ngắn gọn, khoa học và giàu tính định hướng thực chiến."""

    if gemini_rotator.keys:
        ok, text_res, _ = gemini_rotator.generate_content(
            prompt=prompt,
            system_instruction="Bạn là chuyên gia cố vấn khảo thí kỳ thi ĐGNL ĐHQG."
        )
        if ok and len(text_res) > 100:
            return text_res

    if OPENAI_API_KEY:
        try:
            from openai import OpenAI
            client = OpenAI(api_key=OPENAI_API_KEY, base_url=OPENAI_BASE_URL)
            response = client.chat.completions.create(
                model=OPENAI_MODEL,
                messages=[
                    {"role": "system", "content": "Bạn là chuyên gia cố vấn khảo thí kỳ thi ĐGNL ĐHQG."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.7,
                max_tokens=1000
            )
            return response.choices[0].message.content
        except Exception as e:
            print(f"LLM Advice API error: {e}, falling back to pedagogical heuristic engine.")

    # Rule-based Pedagogical Advisory Engine
    advice_lines = []
    advice_lines.append(f"### 🎯 ĐÁNH GIÁ TỔNG THỂ KẾT QUẢ THI ({total_score}/1200 ĐIỂM)")
    if total_score >= 850:
        advice_lines.append("Chúc mừng bạn! Điểm số của bạn đang nằm trong top thí sinh có năng lực tư duy xuất sắc. Bạn đã có nền tảng vững vàng ở hầu hết các phân môn.")
    elif total_score >= 700:
        advice_lines.append("Kết quả của bạn rất khả quan và đạt trên mức điểm trung bình kỳ thi ĐGNL. Bạn hoàn toàn có tiềm năng chạm mốc 850 - 900+ nếu khắc phục một số điểm mù tư duy.")
    else:
        advice_lines.append("Bạn đã hoàn thành bài thi 120 câu đầy thử thách. Điểm số hiện tại cho thấy bạn cần một chiến lược ôn tập trọng tâm và điều chỉnh lại tốc độ làm bài để tối ưu hóa điểm số.")

    if strong_keys:
        strong_names = ", ".join([domain_stats[k]["name"] for k in strong_keys])
        advice_lines.append(f"\n**🌟 Điểm mạnh nổi trội:** Bạn làm rất tốt ở các môn: **{strong_names}**. Hãy duy trì phong độ này bằng cách luyện các đề nâng cao định kỳ.")

    if weak_keys:
        weak_names = ", ".join([domain_stats[k]["name"] for k in weak_keys])
        advice_lines.append(f"\n**⚠️ Miền năng lực cần tập trung cải thiện cấp tốc:** **{weak_names}**")
        advice_lines.append("\n#### 📋 Lộ trình bứt phá chi tiết theo từng chuyên đề:")
        for k in weak_keys[:4]: # Lấy tối đa 4 môn yếu nhất
            catalog = DOMAIN_ADVICE_CATALOG.get(k)
            if catalog:
                advice_lines.append(f"\n**{catalog['title']}** (Đạt {domain_stats[k]['percentage']}%):")
                for tip in catalog["tips"]:
                    advice_lines.append(f"- {tip}")

    advice_lines.append("\n#### ⏱️ Chiến thuật Quản trị Thời gian 150 phút (120 câu):")
    advice_lines.append("- **Vòng 1 (70 phút đầu):** Giải quyết tất cả các câu Nhận biết - Thông hiểu trong 3 phần (nhắm mục tiêu đạt chắc 60 - 70 câu đúng). Câu nào đọc quá 60 giây chưa ra hướng thì đánh dấu cờ (Flag) và bỏ qua ngay.")
    advice_lines.append("- **Vòng 2 (55 phút tiếp theo):** Xử lý các bài đọc hiểu dài, bài toán tư duy logic bảng biểu và phân tích số liệu.")
    advice_lines.append("- **Vòng 3 (25 phút cuối):** Giải quyết các câu Vận dụng cao đã gắn cờ, sau đó kiểm tra chắc chắn đã tô đủ 120 câu hỏi (tuyệt đối không để trống).")

    return "\n".join(advice_lines)
