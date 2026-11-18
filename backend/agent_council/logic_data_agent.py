import time
import random
from pathlib import Path
from typing import Dict, Any, List
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from backend.config import CHARTS_DIR

class LogicDataAgent:
    """
    Logic & Data Agent:
    Tác tử này sử dụng Python (matplotlib) để:
    1. Sinh ngẫu nhiên các bộ dữ liệu bảng thực tế (doanh thu, nông nghiệp, năng lượng...).
    2. Tự động vẽ và xuất ra file ảnh biểu đồ (cột, tròn, đường) chất lượng cao.
    3. Sinh các câu hỏi phân tích dữ liệu dựa trên chính hình ảnh và số liệu đó.
    4. Sinh các bài toán tư duy logic (sắp xếp vị trí, mệnh đề, suy luận logic).
    """
    def __init__(self):
        CHARTS_DIR.mkdir(parents=True, exist_ok=True)

    def generate_chart_and_question(self, chart_type: str = "bar") -> Dict[str, Any]:
        """
        Sinh dữ liệu ngẫu nhiên, vẽ biểu đồ với matplotlib,
        lưu ảnh vào static/charts và trả về câu hỏi trắc nghiệm tương ứng.
        """
        timestamp = int(time.time() * 1000)
        filename = f"chart_gen_{chart_type}_{timestamp}.png"
        file_path = CHARTS_DIR / filename
        web_path = f"/static/charts/{filename}"

        if chart_type == "bar":
            categories = ["Hà Nội", "TP.HCM", "Đà Nẵng", "Cần Thơ", "Hải Phòng"]
            # Tạo số liệu ngẫu nhiên hợp lý (Tỷ VNĐ)
            base = random.randint(120, 250)
            data_2023 = [base + random.randint(-30, 80) for _ in categories]
            data_2024 = [d + random.randint(15, 60) for d in data_2023]
            
            # Vẽ biểu đồ cột nhóm
            fig, ax = plt.subplots(figsize=(7, 4.2))
            x = range(len(categories))
            width = 0.35
            ax.bar([i - width/2 for i in x], data_2023, width, label="Năm 2023", color="#3b82f6")
            ax.bar([i + width/2 for i in x], data_2024, width, label="Năm 2024", color="#10b981")
            ax.set_ylabel("Doanh thu (Tỷ đồng)", fontsize=10)
            ax.set_title("DOANH THU BÁN LẺ DỊCH VỤ TẠI CÁC ĐÔ THỊ", fontsize=11, weight="bold")
            ax.set_xticks(x)
            ax.set_xticklabels(categories, fontsize=9)
            ax.legend()
            ax.grid(axis='y', linestyle='--', alpha=0.6)
            plt.tight_layout()
            plt.savefig(file_path, dpi=120)
            plt.close(fig)

            # Tạo câu hỏi tính toán trên dữ liệu thật
            target_city = "TP.HCM"
            idx = categories.index(target_city)
            val_23 = data_2023[idx]
            val_24 = data_2024[idx]
            growth = round(((val_24 - val_23) / val_23) * 100, 1)
            
            # Sinh 3 distractors
            distractors = [
                round(growth + random.choice([3.5, 6.2, -4.1, -7.3]), 1)
                for _ in range(3)
            ]
            all_opts = [growth] + distractors
            random.shuffle(all_opts)
            labels = ["A", "B", "C", "D"]
            correct_lbl = labels[all_opts.index(growth)]

            return {
                "domain": "data_analysis",
                "section_id": "section_2_logic_data",
                "difficulty": "medium",
                "chart_image": web_path,
                "passage": f"Quan sát biểu đồ cột đôi thể hiện doanh thu bán lẻ dịch vụ tại 5 đô thị năm 2023 và 2024 để trả lời câu hỏi.",
                "prompt": f"Dựa vào biểu đồ, tốc độ tăng trưởng doanh thu của {target_city} năm 2024 so với năm 2023 đạt xấp xỉ bao nhiêu phần trăm?",
                "options": {
                    labels[i]: f"{all_opts[i]}%" for i in range(4)
                },
                "correct_answer": correct_lbl,
                "explanation": f"Năm 2023 đạt {val_23} tỷ, năm 2024 đạt {val_24} tỷ. Tốc độ tăng trưởng = (({val_24} - {val_23}) / {val_23}) * 100% = {growth}%."
            }

        elif chart_type == "pie":
            sectors = ["Nông - Lâm - Thủy sản", "Công nghiệp - Xây dựng", "Dịch vụ", "Thuế sản phẩm"]
            vals = [random.randint(12, 18), random.randint(35, 42), random.randint(38, 45), random.randint(6, 10)]
            total = sum(vals)
            percents = [round(v / total * 100, 1) for v in vals]
            # Sửa phần tử cuối để tổng đúng 100%
            percents[-1] = round(100.0 - sum(percents[:-1]), 1)

            fig, ax = plt.subplots(figsize=(6.5, 4.5))
            colors = ["#10b981", "#3b82f6", "#f59e0b", "#8b5cf6"]
            ax.pie(percents, labels=sectors, autopct='%1.1f%%', colors=colors, startangle=140)
            ax.set_title("CƠ CẤU TỔNG SẢN PHẨM NỘI ĐỊA (GDP) THEO NGÀNH", fontsize=11, weight="bold")
            plt.tight_layout()
            plt.savefig(file_path, dpi=120)
            plt.close(fig)

            combined = round(percents[1] + percents[2], 1)
            distractors = [round(combined + d, 1) for d in [-8.5, 6.4, -14.2]]
            all_opts = [combined] + distractors
            random.shuffle(all_opts)
            labels = ["A", "B", "C", "D"]
            correct_lbl = labels[all_opts.index(combined)]

            return {
                "domain": "data_analysis",
                "section_id": "section_2_logic_data",
                "difficulty": "medium",
                "chart_image": web_path,
                "passage": "Quan sát biểu đồ hình tròn cơ cấu GDP theo ngành kinh tế để trả lời câu hỏi.",
                "prompt": "Dựa vào biểu đồ tròn, tổng tỷ trọng của hai ngành 'Công nghiệp - Xây dựng' và 'Dịch vụ' chiếm bao nhiêu phần trăm trong cơ cấu GDP?",
                "options": {
                    labels[i]: f"{all_opts[i]}%" for i in range(4)
                },
                "correct_answer": correct_lbl,
                "explanation": f"Tỷ trọng Công nghiệp - Xây dựng ({percents[1]}%) + Dịch vụ ({percents[2]}%) = {combined}%."
            }

        else: # logic puzzle
            return self.generate_logic_puzzle()

    def generate_logic_puzzle(self) -> Dict[str, Any]:
        """Sinh bài toán tư duy suy luận logic"""
        names = ["An", "Bình", "Châu", "Dương", "Hà"]
        random.shuffle(names)
        p1, p2, p3, p4, p5 = names

        passage = f"Năm bạn học sinh gồm {', '.join(names)} tham gia một cuộc thi chạy tiếp sức và về đích ở 5 thứ hạng từ 1 đến 5 (không có hai bạn nào đồng hạng). Biết rằng:\n- {p1} về đích trước {p2}.\n- {p3} về đích ngay sau {p4}.\n- {p5} về đích ở vị trí thứ 3."
        prompt = f"Nếu {p2} về đích ở vị trí thứ 2, thì ai chắc chắn về đích ở vị trí thứ 1?"
        
        # Nếu p2 ở vị trí 2, mà p1 trước p2 => p1 phải ở vị trí 1
        correct_person = p1
        distractors = [p3, p4, p5]
        all_opts = [correct_person] + distractors
        random.shuffle(all_opts)
        labels = ["A", "B", "C", "D"]
        correct_lbl = labels[all_opts.index(correct_person)]

        return {
            "domain": "logic",
            "section_id": "section_2_logic_data",
            "difficulty": "medium",
            "passage": passage,
            "prompt": prompt,
            "options": {
                labels[i]: all_opts[i] for i in range(4)
            },
            "correct_answer": correct_lbl,
            "explanation": f"Vì {p1} về đích trước {p2}, mà {p2} về đích ở vị trí thứ 2, nên vị trí duy nhất phía trước {p2} là vị trí thứ 1, do đó {p1} chắc chắn về đích thứ 1."
        }
