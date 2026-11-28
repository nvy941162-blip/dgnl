# -*- coding: utf-8 -*-
"""
CẬP NHẬT CÁC CÂU HỎI CÓ HÌNH VẼ & BIỂU ĐỒ TRỰC QUAN VÀO DATABASE VÀ DỮ LIỆU ĐỀ THI
"""
import json
import sqlite3
from pathlib import Path

from backend.config import DB_PATH
from backend.exam_engine.diagram_generator import (
    draw_orthographic_projection,
    draw_smart_greenhouse_diagram,
    draw_hydroponics_nft_diagram,
    draw_nanosilver_chart,
    draw_climate_chart,
    draw_gdp_structure_chart,
    draw_math_cubic_graph,
    draw_math_rational_graph,
    draw_math_spatial_pyramid,
    draw_telecom_network
)

def apply_diagrams_to_db():
    print(f"Connecting to database: {DB_PATH}")
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Pre-generate diagrams to avoid duplicate computation
    print("Generating base64 diagrams...")
    img_ortho = draw_orthographic_projection()
    img_greenhouse = draw_smart_greenhouse_diagram()
    img_hydroponics = draw_hydroponics_nft_diagram()
    img_nanosilver = draw_nanosilver_chart()
    img_climate = draw_climate_chart("Trạm Khí tượng Hà Nội")
    img_gdp = draw_gdp_structure_chart()
    img_math_cubic = draw_math_cubic_graph()
    img_math_rational = draw_math_rational_graph()
    img_math_pyramid = draw_math_spatial_pyramid()
    img_telecom = draw_telecom_network()
    print("All diagrams generated successfully.")

    cursor.execute("SELECT id, title, data_json FROM exams")
    rows = cursor.fetchall()
    updated_count = 0

    for exam_id, title, data_json in rows:
        if not data_json:
            continue
        try:
            questions = json.loads(data_json)
        except Exception:
            continue

        changed = False

        for q in questions:
            prompt = q.get("prompt", "")
            q_num = q.get("question_number", 0)

            # 1. Công nghệ Công nghiệp: Hình chiếu vuông góc & trục đo
            if "hình chiếu vuông góc của vật thể" in prompt.lower():
                q["chart_image"] = img_ortho
                q["passage"] = "Quan sát hình vẽ vật thể mẫu (Isometric 3D) và 4 phương án hình chiếu 3 hướng (Hình a, Hình b, Hình c, Hình d) ở khung bên trái."
                changed = True
            elif "hình chiếu trục đo của vật thể" in prompt.lower():
                q["chart_image"] = img_ortho
                q["passage"] = "Quan sát bản vẽ các hình chiếu vuông góc và hình chiếu trục đo ở khung bên trái."
                changed = True

            # 2. Công nghệ Nông nghiệp: Nhà kính thông minh, Thủy canh NFT, Đồ thị nano bạc
            elif "thủy canh" in prompt.lower() and ("sắp xếp các bước" in prompt.lower() or "dinh dưỡng" in prompt.lower()):
                q["chart_image"] = img_hydroponics
                q["passage"] = "Quan sát sơ đồ hệ thống trồng rau thủy canh hồi lưu NFT (Nutrient Film Technique) ở khung bên trái."
                changed = True
            elif "nhà kính" in prompt.lower() or "trồng trọt" in prompt.lower() and q_num == 1 and "tech_agriculture" in str(q.get("domain")):
                q["chart_image"] = img_greenhouse
                q["passage"] = "Quan sát sơ đồ mô hình nhà kính thông minh công nghệ cao (Smart IoT Greenhouse) ở khung bên trái."
                changed = True
            elif "nano bạc" in prompt.lower() and "florfenicol" in prompt.lower():
                q["chart_image"] = img_nanosilver
                q["passage"] = "Quan sát đồ thị biểu diễn tỉ lệ sống (%) của cá nheo Mỹ sau 7 ngày thử nghiệm điều trị ở khung bên trái."
                changed = True

            # 3. Địa lí: Biểu đồ khí hậu nhiệt độ & lượng mưa, Biểu đồ cơ cấu GDP
            elif "trạm khí tượng" in prompt.lower() or ("nhiệt độ" in prompt.lower() and "lượng mưa" in prompt.lower() and "khí hậu" in prompt.lower()):
                q["chart_image"] = img_climate
                q["passage"] = "Quan sát biểu đồ khí hậu kết hợp nhiệt độ và lượng mưa của trạm khí tượng ở khung bên trái."
                changed = True
            elif "cơ cấu gdp" in prompt.lower() and "2010" in prompt.lower():
                q["chart_image"] = img_gdp
                q["passage"] = "Quan sát biểu đồ chuyển dịch cơ cấu GDP nước ta giai đoạn 2010 - 2022 (%) ở khung bên trái."
                changed = True

            # 4. Toán học: Đồ thị hàm số, hình không gian
            elif "y = f(x) = x +" in prompt or "tiệm cận" in prompt.lower() and q_num == 1:
                q["chart_image"] = img_math_rational
                q["passage"] = "Quan sát đồ thị hàm phân thức và các đường tiệm cận đứng, tiệm cận ngang ở khung bên trái."
                changed = True
            elif "đồ thị là đường cong (c)" in prompt.lower() or ("hàm số" in prompt.lower() and "cực trị" in prompt.lower() and q_num in [1, 2, 17]):
                q["chart_image"] = img_math_cubic
                q["passage"] = "Quan sát đồ thị hàm số bậc ba (C) trên mặt phẳng tọa độ Oxy ở khung bên trái."
                changed = True
            elif "hình chóp $s.abc$" in prompt.lower() or "hình chóp s.abc" in prompt.lower():
                q["chart_image"] = img_math_pyramid
                q["passage"] = "Quan sát hình vẽ hình chóp S.ABC có SA ⊥ (ABC) và đáy vuông tại B ở khung bên trái."
                changed = True

            # 5. V-ACT: Sơ đồ mạng lưới viễn thông
            elif "sáu thị trấn" in prompt.lower() or "tuyến cáp" in prompt.lower() and "chi phí" in prompt.lower():
                q["chart_image"] = img_telecom
                q["passage"] = "Quan sát sơ đồ mạng lưới các tuyến cáp nối và chi phí giữa sáu thị trấn A, B, C, D, E, F ở khung bên trái."
                changed = True

        if changed:
            new_data_json = json.dumps(questions, ensure_ascii=False)
            cursor.execute("UPDATE exams SET data_json = ? WHERE id = ?", (new_data_json, exam_id))
            updated_count += 1
            print(f"Updated diagrams for exam: {title} ({exam_id})")

    conn.commit()
    conn.close()
    print(f"Successfully applied diagrams to {updated_count} exams in SQLite database!")

if __name__ == "__main__":
    apply_diagrams_to_db()
