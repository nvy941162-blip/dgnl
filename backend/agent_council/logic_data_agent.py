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

    def generate_logic_puzzle(self, idx: int = 0) -> Dict[str, Any]:
        """Sinh 12 bài toán tư duy suy luận logic độc lập, 100% không trùng lặp"""
        puzzles = [
            # 1. Chạy tiếp sức
            {
                "passage": "Năm bạn học sinh gồm An, Bình, Châu, Dương, Hà tham gia cuộc thi chạy và về đích ở 5 thứ hạng từ 1 đến 5 (không có ai đồng hạng). Biết: An về đích trước Bình; Châu về đích ngay sau Dương; Hà về đích ở vị trí thứ 3.",
                "prompt": "Nếu Bình về đích ở vị trí thứ 2, thì ai chắc chắn về đích ở vị trí thứ 1?",
                "options": {"A": "An", "B": "Châu", "C": "Dương", "D": "Hà"},
                "correct_answer": "A",
                "explanation": "Vì An về đích trước Bình, mà Bình về đích thứ 2 nên vị trí duy nhất trước Bình là vị trí thứ 1, do đó An về đích thứ 1."
            },
            # 2. Xếp hàng ngang
            {
                "passage": "Năm bạn gồm Minh, Nam, Phong, Quân, Sơn xếp thành một hàng dọc từ trước ra sau (vị trí 1 đến 5). Biết rằng: Sơn đứng ngay sau Minh; Nam đứng trước Quân nhưng sau Phong; Minh đứng ở vị trí số 1.",
                "prompt": "Bạn nào đứng ở vị trí số 2 trong hàng?",
                "options": {"A": "Sơn", "B": "Nam", "C": "Phong", "D": "Quân"},
                "correct_answer": "A",
                "explanation": "Minh đứng ở vị trí số 1, mà Sơn đứng ngay sau Minh nên Sơn đứng ở vị trí số 2."
            },
            # 3. Phân công trực nhật
            {
                "passage": "Lịch trực nhật từ thứ Hai đến thứ Sáu của lớp được phân công cho 5 bạn: Mai, Lan, Cúc, Trúc, Đào (mỗi người trực đúng 1 ngày). Biết rằng: Lan trực vào thứ Ba; Cúc trực sau Đào đúng 2 ngày; Mai trực ngay trước ngày của Lan.",
                "prompt": "Bạn nào là người được phân công trực nhật vào ngày thứ Hai?",
                "options": {"A": "Mai", "B": "Cúc", "C": "Trúc", "D": "Đào"},
                "correct_answer": "A",
                "explanation": "Lan trực vào thứ Ba, Mai trực ngay trước Lan nên Mai trực vào ngày thứ Hai."
            },
            # 4. Tầng chung cư
            {
                "passage": "Một tòa nhà 5 tầng (tầng 1 đến tầng 5) là nơi sinh sống của 5 gia đình: bác Hải, bác Lâm, bác Phúc, bác Quý, bác Tâm. Biết rằng: Bác Lâm ở tầng 1; Bác Phúc ở ngay trên tầng của bác Lâm; Bác Quý ở tầng cao nhất; Bác Hải ở tầng cao hơn bác Tâm.",
                "prompt": "Bác Tâm sinh sống ở tầng mấy của tòa nhà?",
                "options": {"A": "Tầng 3", "B": "Tầng 2", "C": "Tầng 4", "D": "Tầng 5"},
                "correct_answer": "A",
                "explanation": "Bác Lâm ở tầng 1, bác Phúc ở tầng 2, bác Quý ở tầng 5. Còn lại tầng 3 và 4 chia cho bác Hải và bác Tâm. Do bác Hải ở cao hơn bác Tâm nên bác Hải ở tầng 4, bác Tâm ở tầng 3."
            },
            # 5. Nói thật - Nói dối
            {
                "passage": "Trên một hòn đảo có hai bộ tộc: người tộc Thật luôn nói thật và người tộc Dối luôn nói dối. Gặp hai người A và B, A nói: 'Ít nhất một người trong chúng tôi là người tộc Dối'.",
                "prompt": "Kết luận nào sau đây là hoàn toàn chính xác về A và B?",
                "options": {
                    "A": "A là người tộc Thật, B là người tộc Dối",
                    "B": "Cả A và B đều là người tộc Dối",
                    "C": "Cả A và B đều là người tộc Thật",
                    "D": "A là người tộc Dối, B là người tộc Thật"
                },
                "correct_answer": "A",
                "explanation": "Nếu A là người tộc Dối, mệnh đề của A là dối => không có ai là tộc Dối (cả hai là tộc Thật), mâu thuẫn vì A là tộc Dối. Vậy A nói thật (A thuộc tộc Thật). Do mệnh đề đúng nên có ít nhất một người tộc Dối, suy ra B phải thuộc tộc Dối."
            },
            # 6. Phủ định mệnh đề
            {
                "passage": None,
                "prompt": "Mệnh đề phủ định của mệnh đề 'Mọi hình thoi đều là hình bình hành' là:",
                "options": {
                    "A": "Tồn tại ít nhất một hình thoi không phải là hình bình hành",
                    "B": "Mọi hình thoi đều không phải là hình bình hành",
                    "C": "Tồn tại một hình bình hành không phải là hình thoi",
                    "D": "Mọi hình bình hành đều là hình thoi"
                },
                "correct_answer": "A",
                "explanation": "Phủ định của mệnh đề chứa lượng từ 'Với mọi' ($\\forall$) là mệnh đề chứa lượng từ 'Tồn tại' ($\\exists$) kèm theo phủ định vị ngữ."
            },
            # 7. Tương đương logic
            {
                "passage": None,
                "prompt": "Mệnh đề nào sau đây tương đương logic với mệnh đề kéo theo 'Nếu trời mưa thì đường ướt'?",
                "options": {
                    "A": "Nếu đường không ướt thì trời không mưa",
                    "B": "Nếu đường ướt thì trời mưa",
                    "C": "Nếu trời không mưa thì đường không ướt",
                    "D": "Đường ướt khi và chỉ khi trời mưa"
                },
                "correct_answer": "A",
                "explanation": "Mệnh đề đảo phản đề $\\neg Q \\Rightarrow \\neg P$ luôn có cùng chân trị logic với mệnh đề gốc $P \\Rightarrow Q$."
            },
            # 8. Chọn đội tuyển
            {
                "passage": "Thầy giáo chọn 3 học sinh từ nhóm 5 học sinh gồm A, B, C, D, E vào đội tuyển cờ vua theo quy tắc: Nếu chọn A thì phải chọn B; C và D không thể cùng được chọn; B và E luôn cùng được chọn hoặc cùng không được chọn.",
                "prompt": "Nếu bạn C được chọn, thì danh sách 3 bạn trong đội tuyển là:",
                "options": {"A": "C, B, E", "B": "C, A, B", "C": "C, D, E", "D": "C, A, D"},
                "correct_answer": "A",
                "explanation": "C được chọn => D bị loại. Còn lại 4 bạn A, B, C, E để chọn thêm 2 bạn. Nếu chọn A => phải chọn B, mà chọn B thì phải chọn E => thành 4 bạn (loại). Do đó A bị loại, chọn thêm B và E."
            },
            # 9. So sánh độ cao
            {
                "passage": "Năm ngọn núi P, Q, R, S, T có độ cao khác nhau. Biết rằng: Núi P cao hơn núi Q nhưng thấp hơn núi R; Núi S cao hơn núi R; Núi T thấp hơn núi Q.",
                "prompt": "Ngọn núi nào có độ cao đứng thứ nhì trong năm ngọn núi?",
                "options": {"A": "Núi R", "B": "Núi S", "C": "Núi P", "D": "Núi Q"},
                "correct_answer": "A",
                "explanation": "Thứ tự độ cao từ lớn đến bé: S > R > P > Q > T. Do đó ngọn núi cao thứ nhì là núi R."
            },
            # 10. Bàn tròn
            {
                "passage": "Năm bạn gồm Anh, Bắc, Cường, Dũng, Em ngồi quanh một bàn tròn 5 ghế xếp đều nhau. Biết rằng: Anh ngồi cạnh Bắc và Cường; Dũng không ngồi cạnh Bắc.",
                "prompt": "Bạn nào ngồi đối diện (hoặc ngồi cạnh) bạn Dũng trong các khẳng định sau?",
                "options": {
                    "A": "Dũng ngồi cạnh Cường và Em",
                    "B": "Dũng ngồi cạnh Anh",
                    "C": "Dũng ngồi cạnh Bắc",
                    "D": "Em ngồi giữa Anh và Bắc"
                },
                "correct_answer": "A",
                "explanation": "Vì Anh ngồi cạnh Bắc và Cường nên thứ tự là Bắc - Anh - Cường. Hai ghế còn lại dành cho Dũng và Em. Do Dũng không cạnh Bắc nên Dũng phải cạnh Cường, suy ra Dũng ngồi cạnh Cường và Em."
            },
            # 11. Nhạc cụ sở thích
            {
                "passage": "Bốn bạn Giáp, Ất, Bính, Đinh mỗi người biết chơi một loại nhạc cụ khác nhau gồm: Piano, Guitar, Violin, Trống. Biết rằng: Giáp không biết chơi Piano và Trống; Bính là tay chơi Guitar xuất sắc; Ất không biết chơi Trống.",
                "prompt": "Bạn nào là người chơi Trống trong nhóm?",
                "options": {"A": "Đinh", "B": "Ất", "C": "Giáp", "D": "Bính"},
                "correct_answer": "A",
                "explanation": "Bính chơi Guitar. Giáp và Ất đều không chơi Trống. Vậy người duy nhất còn lại chơi Trống là Đinh."
            },
            # 12. Suy luận quy nạp
            {
                "passage": "Cho dãy số suy luận logic: 2, 6, 12, 20, 30, ...",
                "prompt": "Số hạng tiếp theo trong dãy số logic trên là:",
                "options": {"A": "42", "B": "40", "C": "36", "D": "48"},
                "correct_answer": "A",
                "explanation": "Quy luật: $1 \\times 2 = 2, 2 \\times 3 = 6, 3 \\times 4 = 12, 4 \\times 5 = 20, 5 \\times 6 = 30$. Số tiếp theo là $6 \\times 7 = 42$."
            }
        ]
        chosen = puzzles[idx % len(puzzles)]
        return {
            "domain": "logic",
            "section_id": "section_2_logic_data",
            "difficulty": "medium",
            **chosen
        }
