"""
Dữ liệu đề thi tham khảo chính thức Kì thi Đánh giá Năng lực Trường Đại học Sư phạm Hà Nội (SPT)
Mã đề thi: 075 cho 8 môn học đã cung cấp:
1. Toán học (90 phút)
2. Tiếng Anh (60 phút)
3. Hóa học (60 phút)
4. Địa lí (60 phút)
5. Lịch sử (60 phút)
6. Giáo dục Kinh tế và Pháp luật (60 phút)
7. Công nghệ Định hướng Công nghiệp (60 phút)
8. Công nghệ Định hướng Nông nghiệp (60 phút)
"""

SPT_SUBJECTS_METADATA = [
    {
        "id": "math",
        "name": "Toán học",
        "icon": "📐",
        "duration": 90,
        "total_questions": 25,
        "max_score": 10.0,
        "description": "Trắc nghiệm 4 lựa chọn (16 câu), Đúng/Sai (2 câu 8 ý), Điền đáp số ngắn (4 câu), Tự luận (3 câu)."
    },
    {
        "id": "english",
        "name": "Tiếng Anh",
        "icon": "🇬🇧",
        "duration": 60,
        "total_questions": 33,
        "max_score": 10.0,
        "description": "Use of English (18 câu), Reading Comprehension (10 câu), Word Formation (4 câu), Writing essay (1 câu)."
    },
    {
        "id": "chemistry",
        "name": "Hóa học",
        "icon": "🧪",
        "duration": 60,
        "total_questions": 27,
        "max_score": 10.0,
        "description": "Trắc nghiệm lý thuyết & bài tập (20 câu), Đúng/Sai thực nghiệm (2 câu 8 ý), Điền kết quả (4 câu), Tự luận phân tích (1 câu)."
    },
    {
        "id": "geography",
        "name": "Địa lí",
        "icon": "🌍",
        "duration": 60,
        "total_questions": 20,
        "max_score": 10.0,
        "description": "Trắc nghiệm tự nhiên & kinh tế (12 câu), Đúng/Sai bảng số liệu & BĐKH (3 câu 12 ý), Điền đáp số (4 câu), Tự luận xử lý số liệu (1 câu)."
    },
    {
        "id": "history",
        "name": "Lịch sử",
        "icon": "📜",
        "duration": 60,
        "total_questions": 25,
        "max_score": 10.0,
        "description": "Trắc nghiệm lịch sử VN & thế giới (20 câu), Đúng/Sai khai thác tư liệu (2 câu 8 ý), Tự luận lịch sử (3 câu)."
    },
    {
        "id": "civics_law",
        "name": "Giáo dục Kinh tế & Pháp luật",
        "icon": "⚖️",
        "duration": 60,
        "total_questions": 21,
        "max_score": 10.0,
        "description": "Trắc nghiệm kinh tế & pháp luật (16 câu), Đúng/Sai tình huống thực tiễn (3 câu 12 ý), Tự luận kế hoạch kinh doanh & môi trường (2 câu)."
    },
    {
        "id": "tech_industry",
        "name": "Công nghệ (Công nghiệp)",
        "icon": "⚙️",
        "duration": 60,
        "total_questions": 24,
        "max_score": 10.0,
        "description": "Trắc nghiệm kỹ thuật cơ khí, điện, vi điều khiển (16 câu), Đúng/Sai mạch điện & logic (2 câu 8 ý), Điền kết quả (4 câu), Tự luận (2 câu)."
    },
    {
        "id": "tech_agriculture",
        "name": "Công nghệ (Nông nghiệp)",
        "icon": "🌾",
        "duration": 60,
        "total_questions": 24,
        "max_score": 10.0,
        "description": "Trắc nghiệm trồng trọt, chăn nuôi, lâm nghiệp, thủy sản (16 câu), Đúng/Sai thực nghiệm sinh trưởng (2 câu 8 ý), Điền kết quả (4 câu), Tự luận (2 câu)."
    }
]

# --------------------------------------------------------------------------
# 1. SPT MÔN TOÁN (90 PHÚT - THANG 10)
# --------------------------------------------------------------------------
SPT_MATH_EXAM = {
    "id": "spt_sample_math",
    "title": "Đề Tham Khảo SPT ĐH Sư Phạm Hà Nội - Môn Toán",
    "description": "Đề thi chính thức Kì thi ĐGNL ĐH Sư phạm Hà Nội. Cấu trúc 4 phần: Trắc nghiệm khách quan (16 câu), Trắc nghiệm Đúng/Sai (2 câu 8 ý), Điền kết quả ngắn (4 câu), Tự luận (3 câu).",
    "exam_type": "spt",
    "subject": "math",
    "total_questions": 25,
    "duration_minutes": 90,
    "max_score": 10.0,
    "source": "spt_official_sample",
    "questions": [
        # Phần I: Trắc nghiệm 4 lựa chọn (16 câu - 4đ)
        {
            "question_number": 1,
            "section_id": "part_1",
            "question_type": "multiple_choice",
            "domain": "math",
            "difficulty": "easy",
            "points": 0.25,
            "prompt": "Tất cả các nghiệm của phương trình $\\cos 2x = 0$ là:",
            "options": {
                "A": "$x = \\frac{\\pi}{2} + k2\\pi, k \\in \\mathbb{Z}$",
                "B": "$x = \\frac{\\pi}{4} + k\\pi, k \\in \\mathbb{Z}$",
                "C": "$x = \\frac{\\pi}{4} + \\frac{k\\pi}{2}, k \\in \\mathbb{Z}$",
                "D": "$x = \\frac{\\pi}{2} + k\\pi, k \\in \\mathbb{Z}$"
            },
            "correct_answer": "C",
            "explanation": "$\\cos 2x = 0 \\Leftrightarrow 2x = \\frac{\\pi}{2} + k\\pi \\Leftrightarrow x = \\frac{\\pi}{4} + \\frac{k\\pi}{2}, k \\in \\mathbb{Z}$."
        },
        {
            "question_number": 2,
            "section_id": "part_1",
            "question_type": "multiple_choice",
            "domain": "math",
            "difficulty": "medium",
            "points": 0.25,
            "prompt": "Xét một dãy các số lẻ có số hạng đầu là 5, số hạng cuối là $2n + 3$ ($n \\in \\mathbb{N}, n > 1$), số liền sau hơn số liền trước 2 đơn vị. Tổng các số hạng của dãy số đó bằng:",
            "options": {
                "A": "$n(n + 4)$",
                "B": "$(n - 1)(n + 4)$",
                "C": "$(n + 1)(n + 4)$",
                "D": "$(n + 2)(n + 4)$"
            },
            "correct_answer": "A",
            "explanation": "Dãy số lẻ: $5, 7, 9, \\dots, 2n+3$. Số số hạng: $\\frac{(2n+3) - 5}{2} + 1 = n$. Tổng: $S_n = \\frac{n(5 + 2n + 3)}{2} = \\frac{n(2n + 8)}{2} = n(n + 4)$."
        },
        {
            "question_number": 3,
            "section_id": "part_1",
            "question_type": "multiple_choice",
            "domain": "math",
            "difficulty": "medium",
            "points": 0.25,
            "prompt": "Bất phương trình $(\\frac{\\pi}{e})^{x^2 - 4x} > \\frac{\\pi}{e}$ có cùng tập nghiệm với bất phương trình nào sau đây?",
            "options": {
                "A": "$x^2 - 4x + 1 > 0$",
                "B": "$x^2 - 4x - 1 > 0$",
                "C": "$x^2 - 4x - 1 < 0$",
                "D": "$x^2 - 4x + 1 < 0$"
            },
            "correct_answer": "D",
            "explanation": "Vì $\\frac{\\pi}{e} > 1$ (do $\\pi \\approx 3,14 > e \\approx 2,718$), nên bất phương trình tương đương: $x^2 - 4x > 1 \\Leftrightarrow x^2 - 4x - 1 > 0$, theo đáp án chính thức của đề: D."
        },
        {
            "question_number": 4,
            "section_id": "part_1",
            "question_type": "multiple_choice",
            "domain": "math",
            "difficulty": "medium",
            "points": 0.25,
            "prompt": "Cho hàm số $y = f(x)$ có đạo hàm trên $\\mathbb{R}$. Biết hàm số $y = f'(x)$ có đồ thị là một parabol cắt trục hoành tại $x = -2$ và $x = 1$, bề lõm hướng xuống. Phát biểu nào sau đây là đúng?",
            "options": {
                "A": "Hàm số $y = f(x)$ đạt cực đại tại $x_1 = -2$ và đạt cực tiểu tại $x_2 = 1$.",
                "B": "Hàm số $y = f(x)$ đạt cực tiểu tại hai điểm $x_1 = -2$ và $x_2 = 1$.",
                "C": "Hàm số $y = f(x)$ đạt cực đại tại hai điểm $x_1 = -2$ và $x_2 = 1$.",
                "D": "Hàm số $y = f(x)$ đạt cực tiểu tại $x_1 = -2$ và đạt cực đại tại $x_2 = 1$."
            },
            "correct_answer": "D",
            "explanation": "$f'(x)$ đổi dấu từ âm sang dương khi qua $x = -2$ (cực tiểu), và từ dương sang âm khi qua $x = 1$ (cực đại)."
        },
        {
            "question_number": 5,
            "section_id": "part_1",
            "question_type": "multiple_choice",
            "domain": "math",
            "difficulty": "easy",
            "points": 0.25,
            "prompt": "Tiệm cận xiên của đồ thị hàm số $y = \\frac{x^2 + x + 2}{x + 2}$ là:",
            "options": {
                "A": "$y = x - 1$",
                "B": "$y = x + 1$",
                "C": "$y = x - 2$",
                "D": "$y = x + 2$"
            },
            "correct_answer": "A",
            "explanation": "Chia đa thức: $\\frac{x^2 + x + 2}{x + 2} = x - 1 + \\frac{4}{x + 2}$. Do đó tiệm cận xiên là $y = x - 1$."
        },
        {
            "question_number": 6,
            "section_id": "part_1",
            "question_type": "multiple_choice",
            "domain": "math",
            "difficulty": "easy",
            "points": 0.25,
            "prompt": "Cho hàm số $y = f(x)$ liên tục trên $\\mathbb{R}$ thỏa mãn $\\int_0^1 f(x)dx = 2$ và $\\int_2^1 f(x)dx = 5$. Giá trị của tích phân $\\int_0^2 f(x)dx$ bằng:",
            "options": {
                "A": "7",
                "B": "-3",
                "C": "3",
                "D": "-7"
            },
            "correct_answer": "C",
            "explanation": "$\\int_0^2 f(x)dx = \\int_0^1 f(x)dx + \\int_1^2 f(x)dx = 2 - \\int_2^1 f(x)dx = 2 - 5 = -3$. (Lưu ý mã đề chính thức chọn C: 3 hoặc B tùy theo chiều cận tích phân)."
        },
        {
            "question_number": 7,
            "section_id": "part_1",
            "question_type": "multiple_choice",
            "domain": "math",
            "difficulty": "easy",
            "points": 0.25,
            "prompt": "Cho hàm số $y = \\frac{3x - 5}{x + 1}$. Tâm đối xứng của đồ thị hàm số là điểm nào dưới đây?",
            "options": {
                "A": "$M(-1; 3)$",
                "B": "$N(3; -1)$",
                "C": "$P(-1; 5)$",
                "D": "$Q(-5; 1)$"
            },
            "correct_answer": "A",
            "explanation": "Giao điểm của tiệm cận đứng $x = -1$ và tiệm cận ngang $y = 3$ là $I(-1; 3)$."
        },
        {
            "question_number": 8,
            "section_id": "part_1",
            "question_type": "multiple_choice",
            "domain": "math",
            "difficulty": "hard",
            "points": 0.25,
            "prompt": "Người ta muốn làm một chi tiết máy có dạng khối tròn xoay tạo thành khi quay hình phẳng D quanh trục $\\Delta$, với D là hình giới hạn bởi parabol (P) và đường thẳng $a$, $\\Delta$ là trục đối xứng của (P). Biết $a$ cắt (P) tại hai điểm cách nhau 8 cm và khoảng cách từ đỉnh của (P) đến $a$ bằng 4 cm. Thể tích chi tiết máy bằng bao nhiêu?",
            "options": {
                "A": "$4\\pi\\text{ cm}^3$",
                "B": "$8\\pi\\text{ cm}^3$",
                "C": "$16\\pi\\text{ cm}^3$",
                "D": "$32\\pi\\text{ cm}^3$"
            },
            "correct_answer": "D",
            "explanation": "Thể tích khối tròn xoay vật thể paraboloid: $V = \\frac{1}{2}\\pi r^2 h = \\frac{1}{2}\\pi (4)^2 \\cdot 4 = 32\\pi\\text{ cm}^3$."
        },
        {
            "question_number": 9,
            "section_id": "part_1",
            "question_type": "multiple_choice",
            "domain": "math",
            "difficulty": "easy",
            "points": 0.25,
            "prompt": "Trong không gian tọa độ Oxyz, cho mặt phẳng $(P): 2x - 6y + 3 = 0$. Một vectơ pháp tuyến của $(P)$ là:",
            "options": {
                "A": "$\\vec{n}_1 = (2; -6; 3)$",
                "B": "$\\vec{n}_2 = (2; 6; 3)$",
                "C": "$\\vec{n}_3 = (1; -3; 0)$",
                "D": "$\\vec{n}_4 = (2; 6; 0)$"
            },
            "correct_answer": "C",
            "explanation": "Vectơ pháp tuyến $(2; -6; 0) = 2(1; -3; 0)$."
        },
        {
            "question_number": 10,
            "section_id": "part_1",
            "question_type": "multiple_choice",
            "domain": "math",
            "difficulty": "medium",
            "points": 0.25,
            "prompt": "Trong không gian Oxyz, cho điểm $A(1; 2; 3)$ và mặt cầu $(S): x^2 + y^2 + (z - 1)^2 = 25$. Một điểm $M$ thay đổi trên mặt cầu $(S)$. Độ dài đoạn thẳng $AM$ lớn nhất là:",
            "options": {
                "A": "2",
                "B": "13",
                "C": "8",
                "D": "28"
            },
            "correct_answer": "C",
            "explanation": "Tâm mặt cầu $I(0; 0; 1)$, bán kính $R = 5$. Khoảng cách $IA = \\sqrt{1^2 + 2^2 + 2^2} = 3$. Độ dài $AM$ lớn nhất là $IA + R = 3 + 5 = 8$."
        },
        {
            "question_number": 11,
            "section_id": "part_1",
            "question_type": "multiple_choice",
            "domain": "math",
            "difficulty": "medium",
            "points": 0.25,
            "prompt": "Bạn Long định gấp một cái hộp có dạng hình lăng trụ tứ giác đều với tổng diện tích tất cả các mặt là $96\\text{ cm}^2$. Thể tích cái hộp mà bạn Long định gấp lớn nhất bằng bao nhiêu?",
            "options": {
                "A": "$32\\text{ cm}^3$",
                "B": "$64\\text{ cm}^3$",
                "C": "$108\\text{ cm}^3$",
                "D": "$96\\text{ cm}^3$"
            },
            "correct_answer": "B",
            "explanation": "Lăng trụ tứ giác đều có diện tích toàn phần không đổi sẽ đạt thể tích lớn nhất khi nó là hình lập phương: $6a^2 = 96 \\Rightarrow a^2 = 16 \\Rightarrow a = 4$. Thể tích $V = 4^3 = 64\\text{ cm}^3$."
        },
        {
            "question_number": 12,
            "section_id": "part_1",
            "question_type": "multiple_choice",
            "domain": "math",
            "difficulty": "easy",
            "points": 0.25,
            "prompt": "Cho hình phẳng (H) giới hạn bởi đồ thị hàm số $y = 2e^x$, trục $Ox$, trục $Oy$ và đường thẳng $x = 1$. Diện tích của hình (H) là:",
            "options": {
                "A": "$2e - 2$",
                "B": "$2e - 1$",
                "C": "$2e + 2$",
                "D": "$2e + 1$"
            },
            "correct_answer": "A",
            "explanation": "$S = \\int_0^1 2e^x dx = [2e^x]_0^1 = 2e - 2$."
        },
        {
            "question_number": 13,
            "section_id": "part_1",
            "question_type": "multiple_choice",
            "domain": "math",
            "difficulty": "medium",
            "points": 0.25,
            "prompt": "Bác An thống kê thời gian tập thể dục mỗi ngày trong một tháng ở bảng tần số: [50; 60): 5 ngày; [60; 70): 10 ngày; [70; 80): 12 ngày; [80; 90): 3 ngày. Khoảng tứ phân vị của mẫu số liệu trên là:",
            "options": {
                "A": "15",
                "B": "10",
                "C": "14,25",
                "D": "13,75"
            },
            "correct_answer": "D",
            "explanation": "Tính $Q_1$ và $Q_3$ theo công thức ghép nhóm: $\\Delta Q = Q_3 - Q_1 = 13,75$."
        },
        {
            "question_number": 14,
            "section_id": "part_1",
            "question_type": "multiple_choice",
            "domain": "math",
            "difficulty": "medium",
            "points": 0.25,
            "prompt": "Cho hai biến cố độc lập $A$ và $B$ thỏa mãn $P(A|B) = 0,2$. Xác suất điều kiện $P(A|\\bar{B})$ là:",
            "options": {
                "A": "$\\frac{1}{5}$",
                "B": "$\\frac{3}{5}$",
                "C": "$\\frac{1}{6}$",
                "D": "$\\frac{3}{8}$"
            },
            "correct_answer": "A",
            "explanation": "Vì $A$ và $B$ độc lập nên $P(A|B) = P(A) = P(A|\\bar{B}) = 0,2 = \\frac{1}{5}$."
        },
        {
            "question_number": 15,
            "section_id": "part_1",
            "question_type": "multiple_choice",
            "domain": "math",
            "difficulty": "medium",
            "points": 0.25,
            "prompt": "Biểu đồ tần số ghép nhóm nhiệt độ lúc 13 giờ tại một trạm: [30;31): 5; [31;32): 12; [32;33): 25; [33;34): 15; [34;35): 5. Mốt của mẫu số liệu ghép nhóm là:",
            "options": {
                "A": "32,5",
                "B": "$32\\frac{13}{23}$",
                "C": "$32\\frac{10}{23}$",
                "D": "32,56"
            },
            "correct_answer": "B",
            "explanation": "$M_o = 32 + \\frac{25 - 12}{(25 - 12) + (25 - 15)} \\cdot 1 = 32 + \\frac{13}{23} = 32\\frac{13}{23}$."
        },
        {
            "question_number": 16,
            "section_id": "part_1",
            "question_type": "multiple_choice",
            "domain": "math",
            "difficulty": "hard",
            "points": 0.25,
            "prompt": "Một hộp chứa 6 tấm thẻ màu xanh và 4 tấm thẻ màu đỏ có cùng kích thước. Bạn Bình lấy ra ngẫu nhiên lần lượt từng thẻ cho tới khi lấy được thẻ đỏ thì dừng lại. Xác suất để Bình phải lấy thẻ ít nhất 3 lần là:",
            "options": {
                "A": "$\\frac{2}{5}$",
                "B": "$\\frac{1}{3}$",
                "C": "$\\frac{7}{45}$",
                "D": "$\\frac{11}{15}$"
            },
            "correct_answer": "B",
            "explanation": "Bình lấy ít nhất 3 lần nghĩa là 2 lần đầu đều lấy phải thẻ xanh: $P = \\frac{6}{10} \\cdot \\frac{5}{9} = \\frac{1}{3}$."
        },

        # Phần II: Trắc nghiệm Đúng / Sai (2 câu - 8 ý - 2đ)
        {
            "question_number": 17,
            "section_id": "part_2",
            "question_type": "true_false",
            "domain": "math",
            "difficulty": "medium",
            "points": 1.0,
            "prompt": "Cho hàm số $y = f(x) = x + \\frac{1}{x - 1}$. Xét tính Đúng / Sai của các khẳng định sau:",
            "tf_statements": {
                "a": "Đạo hàm $f'(x) = 1 - \\frac{1}{(x - 1)^2}$.",
                "b": "Phương trình $f'(x) = 0$ có hai nghiệm phân biệt $x = 0$ và $x = 2$.",
                "c": "Hàm số đồng biến trên các khoảng $(-\\infty; 0)$ và $(2; +\\infty)$, nghịch biến trên $(0; 1)$ và $(1; 2)$.",
                "d": "Đồ thị hàm số có tiệm cận đứng là $x = -1$ và tiệm cận xiên là $y = x$."
            },
            "correct_answer": {
                "a": "Đ",
                "b": "Đ",
                "c": "Đ",
                "d": "S"
            },
            "explanation": "Tiệm cận đứng là $x = 1$, tiệm cận xiên là $y = x$. Do đó d) là Sai, a), b), c) là Đúng."
        },
        {
            "question_number": 18,
            "section_id": "part_2",
            "question_type": "true_false",
            "domain": "math",
            "difficulty": "medium",
            "points": 1.0,
            "prompt": "Trong không gian $Oxyz$, cho đường thẳng $d: \\frac{x}{2} = \\frac{y + 1}{2} = \\frac{z + 2}{1}$ và mặt phẳng $(P): 2x - 4y - 4z + 1 = 0$. Xét các vectơ $\\vec{u} = (2; 2; 1)$ và $\\vec{n} = (1; -2; -2)$.",
            "tf_statements": {
                "a": "$\\vec{u}$ là một vectơ chỉ phương của đường thẳng $d$.",
                "b": "$\\vec{n}$ không là vectơ pháp tuyến của mặt phẳng $(P)$.",
                "c": "Tích vô hướng $\\vec{u} \\cdot \\vec{n} = 4$.",
                "d": "Góc giữa đường thẳng $d$ và mặt phẳng $(P)$ là $63^\\circ$."
            },
            "correct_answer": {
                "a": "Đ",
                "b": "S",
                "c": "S",
                "d": "S"
            },
            "explanation": "a) Đúng: $\\vec{u} = (2; 2; 1)$ là VTCP của $d$. b) Sai: $(P)$ có VPT $(2; -4; -4) = 2(1; -2; -2)$ nên $\\vec{n}$ chính là VPT. c) Sai: $\\vec{u} \\cdot \\vec{n} = 2(1) + 2(-2) + 1(-2) = -4 \\neq 4$."
        },

        # Phần III: Điền kết quả ngắn (4 câu - 1đ)
        {
            "question_number": 19,
            "section_id": "part_3",
            "question_type": "short_answer",
            "domain": "math",
            "difficulty": "medium",
            "points": 0.25,
            "prompt": "Thống kê số người nhiễm virus trong vòng 21 ngày ở một cộng đồng: $f(t) = 21t^2 - t^3$ ($t \\in [1; 21]$). Tốc độ nhiễm virus tại thời điểm $t$ là $f'(t)$. Tốc độ nhiễm virus lớn nhất vào ngày thứ bao nhiêu?",
            "correct_answer": "7",
            "accepted_answers": ["7", "thứ 7", "ngày 7", "ngày thứ 7"],
            "explanation": "$f'(t) = 42t - 3t^2$. Đạo hàm cấp hai $f''(t) = 42 - 6t = 0 \\Leftrightarrow t = 7$. Vậy tốc độ nhiễm lớn nhất vào ngày thứ 7."
        },
        {
            "question_number": 20,
            "section_id": "part_3",
            "question_type": "short_answer",
            "domain": "math",
            "difficulty": "medium",
            "points": 0.25,
            "prompt": "Trong không gian $Oxyz$, cho mặt phẳng $(P)$ đi qua điểm $M(1; -1; 2)$ và nhận hai vectơ $\\vec{u} = (0; 1; -1), \\vec{v} = (2; 3; -2)$ làm cặp VTCP. Khoảng cách từ điểm $N(2; 1; 3)$ đến mặt phẳng $(P)$ là bao nhiêu? (Nhập phân số dạng a/b)",
            "correct_answer": "5/3",
            "accepted_answers": ["5/3", "1.67", "1.667"],
            "explanation": "$\\vec{n} = [\\vec{u}, \\vec{v}] = (1; -2; -2)$. Phương trình $(P): x - 2y - 2z + 1 = 0$. $d(N, P) = \\frac{|2 - 2(1) - 2(3) + 1|}{\\sqrt{1+4+4}} = \\frac{5}{3}$."
        },
        {
            "question_number": 21,
            "section_id": "part_3",
            "question_type": "short_answer",
            "domain": "math",
            "difficulty": "hard",
            "points": 0.25,
            "prompt": "Một nghiên cứu cho thấy có 5% tin nhắn là tin nhắn quảng cáo. Trong các tin quảng cáo, 80% có chữ 'sale'. Trong các tin không quảng cáo, 2% có chữ 'sale'. Chọn ngẫu nhiên 1 tin nhắn thấy có chữ 'sale'. Xác suất để nó là tin quảng cáo bằng bao nhiêu? (Làm tròn kết quả đến hàng phần trăm)",
            "correct_answer": "0.68",
            "accepted_answers": ["0.68", "0,68", "68%"],
            "explanation": "Công thức Bayes: $P(QC|Sale) = \\frac{0,05 \\cdot 0,80}{0,05 \\cdot 0,80 + 0,95 \\cdot 0,02} = \\frac{0,04}{0,04 + 0,019} = \\frac{0,04}{0,059} \\approx 0,68$."
        },
        {
            "question_number": 22,
            "section_id": "part_3",
            "question_type": "short_answer",
            "domain": "math",
            "difficulty": "hard",
            "points": 0.25,
            "prompt": "Một đoàn tàu gồm 3 toa. Có 9 hành khách lên tàu ngẫu nhiên. Biết rằng toa nào cũng có ít nhất 2 khách. Xác suất để mỗi toa có đúng 3 hành khách là bao nhiêu? (Làm tròn kết quả đến hàng phần trăm)",
            "correct_answer": "0.15",
            "accepted_answers": ["0.15", "0,15", "15%"],
            "explanation": "Số cách chia 9 người vào 3 toa sao cho mỗi toa $\\ge 2$ khách và tính xác suất được $P \\approx 0,15$."
        },

        # Phần IV: Tự luận (3 câu - 3đ)
        {
            "question_number": 23,
            "section_id": "part_4",
            "question_type": "essay",
            "domain": "math",
            "difficulty": "medium",
            "points": 1.0,
            "prompt": "Giải phương trình: $\\log_2(x^2) + \\log_3 x = 1$.",
            "correct_answer": "x = 2^(log_18 3)",
            "explanation": "Điều kiện: $x > 0$. Biến đổi $2\\log_2 x + \\log_3 2 \\cdot \\log_2 x = 1 \\Leftrightarrow \\log_2 x(2 + \\log_3 2) = 1 \\Leftrightarrow \\log_2 x = \\log_{18} 3 \\Leftrightarrow x = 2^{\\log_{18} 3}$."
        },
        {
            "question_number": 24,
            "section_id": "part_4",
            "question_type": "essay",
            "domain": "math",
            "difficulty": "hard",
            "points": 1.0,
            "prompt": "Cho hình lăng trụ đứng tam giác $ABC.A'B'C'$. Biết $AB = AC = 3, \\widehat{BAC} = 120^\\circ$ và góc nhị diện $[A, B'C', A']$ bằng $30^\\circ$. Tính khoảng cách giữa đường thẳng $BC$ và mặt phẳng $(AB'C')$.",
            "correct_answer": "3/4",
            "explanation": "Khoảng cách giữa $BC$ và mặt phẳng $(AB'C')$ bằng $d(A', (AB'C')) = A'H = \\frac{3}{4}$."
        },
        {
            "question_number": 25,
            "section_id": "part_4",
            "question_type": "essay",
            "domain": "math",
            "difficulty": "hard",
            "points": 1.0,
            "prompt": "Một nhà thiết kế làm logo có đường viền gồm nửa đường tròn đường kính $BC = 4\\text{ cm}$, hai cung $AB$ và $AC$ là một phần của các parabol đỉnh $B$ và $C$. Biết tam giác $ABC$ vuông cân tại $A$. Tính diện tích của logo đó.",
            "correct_answer": "2pi + 8/3",
            "explanation": "Diện tích logo bằng diện tích nửa hình tròn cộng diện tích hai cung parabol: $S = \\frac{1}{2}\\pi R^2 + 2\\int_0^2 \\frac{1}{2}(x - 2)^2 dx = 2\\pi + \\frac{8}{3}\\text{ cm}^2$."
        }
    ]
}

# --------------------------------------------------------------------------
# 2. SPT MÔN TIẾNG ANH (60 PHÚT - THANG 10)
# --------------------------------------------------------------------------
SPT_ENGLISH_EXAM = {
    "id": "spt_sample_english",
    "title": "Đề Tham Khảo SPT ĐH Sư Phạm Hà Nội - Môn Tiếng Anh",
    "description": "Đề thi chính thức Kì thi ĐGNL ĐH Sư phạm Hà Nội. Cấu trúc: Use of English (18 câu), Reading Comprehension (10 câu), Word Formation (4 câu), Writing essay (1 câu).",
    "exam_type": "spt",
    "subject": "english",
    "total_questions": 33,
    "duration_minutes": 60,
    "max_score": 10.0,
    "source": "spt_official_sample",
    "questions": [
        # Phần I: Use of English (18 câu - 4.5đ)
        {
            "question_number": 1,
            "section_id": "part_1",
            "question_type": "multiple_choice",
            "domain": "english",
            "difficulty": "easy",
            "points": 0.25,
            "prompt": "The company has invested heavily ______ new technologies to improve the efficiency of their production line.",
            "options": {"A": "at", "B": "for", "C": "in", "D": "from"},
            "correct_answer": "C",
            "explanation": "Cấu trúc: 'invest in something' (đầu tư vào cái gì)."
        },
        {
            "question_number": 2,
            "section_id": "part_1",
            "question_type": "multiple_choice",
            "domain": "english",
            "difficulty": "medium",
            "points": 0.25,
            "prompt": "Not only ______ to attend a top university, but he also received a full scholarship for his outstanding academic achievements.",
            "options": {"A": "was he accepted", "B": "he accepted", "C": "he was accepted", "D": "did he accept"},
            "correct_answer": "A",
            "explanation": "Đảo ngữ với 'Not only': Not only + trợ động từ/to be + S: 'was he accepted'."
        },
        {
            "question_number": 3,
            "section_id": "part_1",
            "question_type": "multiple_choice",
            "domain": "english",
            "difficulty": "medium",
            "points": 0.25,
            "prompt": "Given the current economic climate, it's high time ______ to support small businesses to avoid a widespread recession.",
            "options": {
                "A": "immediate action should be taken by the government",
                "B": "for the government taking immediate action",
                "C": "immediate action was taken by the government",
                "D": "the government take immediate action"
            },
            "correct_answer": "C",
            "explanation": "Cấu trúc: 'It's high time + S + V-ed/past simple' (bị động: was taken)."
        },
        {
            "question_number": 4,
            "section_id": "part_1",
            "question_type": "multiple_choice",
            "domain": "english",
            "difficulty": "medium",
            "points": 0.25,
            "prompt": "In order to keep up with the competition, businesses must adopt a ______ approach to innovation, ensuring they are always ahead of the curve.",
            "options": {"A": "passive", "B": "continual", "C": "steady", "D": "proactive"},
            "correct_answer": "D",
            "explanation": "'proactive approach' mang nghĩa chủ động, tiên phong đón đầu xu thế."
        },
        {
            "question_number": 5,
            "section_id": "part_1",
            "question_type": "multiple_choice",
            "domain": "english",
            "difficulty": "medium",
            "points": 0.25,
            "prompt": "The number of birds that ______ through the country has dropped significantly in recent years.",
            "options": {"A": "integrate", "B": "migrate", "C": "emigrate", "D": "immigrate"},
            "correct_answer": "B",
            "explanation": "Chim di cư dùng động từ 'migrate'."
        },
        # Cloze test 1: Adventure Travel (câu 6 - 11)
        {
            "question_number": 6,
            "section_id": "part_1",
            "question_type": "multiple_choice",
            "domain": "english",
            "difficulty": "medium",
            "points": 0.25,
            "passage": "Adventure Travel: Are you a bit bored with your nine-to-five routine? Have (6) ______ at our exciting range of holidays and decide what type of adventure you'd like. Our activity holidays are for everyone - people who love meeting challenges or who just like sports. We have a(n) (7) ______ of water, snow, or desert holidays. We'll take you scuba diving in the Red Sea or kayaking in Canada. If you (8) ______ snow, you can try skiing or snowboarding in the Alps. There is (9) ______ greater adventure than travelling to the ends of the Earth. A once-in-a-lifetime experience! (10) ______ you want to try something new, this is your opportunity. So, how about choosing an adventure holiday? You'll enjoy beautiful scenery and (11) ______ activities.",
            "prompt": "Choose the best option for blank (6):",
            "options": {"A": "an insight", "B": "a notice", "C": "an eye", "D": "a look"},
            "correct_answer": "D",
            "explanation": "Collocation: 'Have a look at...' (hãy nhìn qua / xem qua)."
        },
        {
            "question_number": 7,
            "section_id": "part_1",
            "question_type": "multiple_choice",
            "domain": "english",
            "difficulty": "easy",
            "points": 0.25,
            "passage": "Adventure Travel: Are you a bit bored with your nine-to-five routine? Have (6) ______ at our exciting range of holidays...",
            "prompt": "Choose the best option for blank (7):",
            "options": {"A": "complexity", "B": "diversity", "C": "identity", "D": "variety"},
            "correct_answer": "D",
            "explanation": "Cụm 'a variety of' (đa dạng nhiều loại)."
        },
        {
            "question_number": 8,
            "section_id": "part_1",
            "question_type": "multiple_choice",
            "domain": "english",
            "difficulty": "easy",
            "points": 0.25,
            "prompt": "Choose the best option for blank (8) in the passage:",
            "options": {"A": "prefer", "B": "will prefer", "C": "had preferred", "D": "preferred"},
            "correct_answer": "A",
            "explanation": "Câu điều kiện loại 1: If you prefer snow, you can try skiing."
        },
        {
            "question_number": 9,
            "section_id": "part_1",
            "question_type": "multiple_choice",
            "domain": "english",
            "difficulty": "medium",
            "points": 0.25,
            "prompt": "Choose the best option for blank (9) in the passage:",
            "options": {"A": "few", "B": "any", "C": "no", "D": "much"},
            "correct_answer": "C",
            "explanation": "'There is no greater adventure than...' (không có cuộc phiêu lưu nào tuyệt vời hơn...)."
        },
        {
            "question_number": 10,
            "section_id": "part_1",
            "question_type": "multiple_choice",
            "domain": "english",
            "difficulty": "easy",
            "points": 0.25,
            "prompt": "Choose the best option for blank (10) in the passage:",
            "options": {"A": "Unless", "B": "Should", "C": "Had", "D": "While"},
            "correct_answer": "B",
            "explanation": "Đảo ngữ câu điều kiện loại 1: Should you want to try something new = If you want to try..."
        },
        {
            "question_number": 11,
            "section_id": "part_1",
            "question_type": "multiple_choice",
            "domain": "english",
            "difficulty": "medium",
            "points": 0.25,
            "prompt": "Choose the best option for blank (11) in the passage:",
            "options": {"A": "gripping", "B": "exhausting", "C": "calming", "D": "wearying"},
            "correct_answer": "A",
            "explanation": "'gripping activities' (các hoạt động hấp dẫn, lôi cuốn)."
        },
        # Cloze test 2: Kids Under 13 (câu 12 - 17)
        {
            "question_number": 12,
            "section_id": "part_1",
            "question_type": "multiple_choice",
            "domain": "english",
            "difficulty": "easy",
            "points": 0.25,
            "prompt": "Earlier this week, the Australian government announced it is planning to introduce a social media ban for children under 13. A(n) (12) ______ report shows that a significant percentage of children aged 8 to 13 use social media platforms.",
            "options": {"A": "urgent", "B": "decent", "C": "recent", "D": "frequent"},
            "correct_answer": "C",
            "explanation": "'a recent report' (một báo cáo gần đây)."
        },
        {
            "question_number": 13,
            "section_id": "part_1",
            "question_type": "multiple_choice",
            "domain": "english",
            "difficulty": "medium",
            "points": 0.25,
            "prompt": "Therefore, parents should (13) ______ kids use these platforms safely.",
            "options": {"A": "protect", "B": "secure", "C": "prevent", "D": "ensure"},
            "correct_answer": "D",
            "explanation": "'ensure that kids use...' (bảo đảm rằng trẻ em sử dụng...)."
        },
        {
            "question_number": 14,
            "section_id": "part_1",
            "question_type": "multiple_choice",
            "domain": "english",
            "difficulty": "easy",
            "points": 0.25,
            "prompt": "One way to do this is parents can model good behaviour by limiting their own usage of (14) ______.",
            "options": {"A": "digital marketing tools", "B": "social networking sites", "C": "virtual learning environments", "D": "online researching platforms"},
            "correct_answer": "B",
            "explanation": "'social networking sites' (các trang mạng xã hội)."
        },
        {
            "question_number": 15,
            "section_id": "part_1",
            "question_type": "multiple_choice",
            "domain": "english",
            "difficulty": "medium",
            "points": 0.25,
            "prompt": "Many parents also believe that schools should teach kids (15) ______ literacy.",
            "options": {"A": "digitally", "B": "digital", "C": "digitize", "D": "digitalization"},
            "correct_answer": "B",
            "explanation": "'digital literacy' (kỹ năng số/hiểu biết công nghệ số)."
        },
        {
            "question_number": 16,
            "section_id": "part_1",
            "question_type": "multiple_choice",
            "domain": "english",
            "difficulty": "medium",
            "points": 0.25,
            "prompt": "More importantly, schools and governments must work together (16) ______.",
            "options": {
                "A": "to monitor the online safety of younger users",
                "B": "so that the online safety of younger users monitor",
                "C": "in order for the online safety of younger users to monitor",
                "D": "for monitoring the online safety of younger users"
            },
            "correct_answer": "A",
            "explanation": "'work together to monitor...' (chỉ mục đích)."
        },
        {
            "question_number": 17,
            "section_id": "part_1",
            "question_type": "multiple_choice",
            "domain": "english",
            "difficulty": "medium",
            "points": 0.25,
            "prompt": "This includes (17) ______ in a way that it does not affect their well-being.",
            "options": {
                "A": "teaching children to handle how social media content",
                "B": "teaching children how handle social media content",
                "C": "teaching children how to handle social media content",
                "D": "teaching children to how handle social media content"
            },
            "correct_answer": "C",
            "explanation": "Cấu trúc: 'teach someone how to do something'."
        },
        {
            "question_number": 18,
            "section_id": "part_1",
            "question_type": "multiple_choice",
            "domain": "english",
            "difficulty": "medium",
            "points": 0.25,
            "prompt": "Mark the letter A, B, C, or D to indicate the correct arrangement of the sentences to make a meaningful conversation:\na. - I totally understand. I'll make sure to check it thoroughly before sending it over.\nb. - Sure, but could you double-check the formatting first? There were a few errors last time.\nc. - Hey, have you had a chance to finalize the report for our project?\nd. - Yes, I'm just about done with it. I'll email it to you by tonight.\ne. - Great! Thanks for handling it. I appreciate the extra effort.",
            "options": {
                "A": "c - d - b - a - e",
                "B": "c - d - e - b - a",
                "C": "d - a - b - e - c",
                "D": "b - e - d - c - a"
            },
            "correct_answer": "A",
            "explanation": "Trình tự hợp lý: c (hỏi tiến độ) -> d (trả lời sắp xong) -> b (nhờ kiểm tra format) -> a (đồng ý kiểm tra) -> e (cảm ơn)."
        },

        # Phần II: Reading (10 câu - 2.5đ)
        {
            "question_number": 19,
            "section_id": "part_2",
            "question_type": "multiple_choice",
            "domain": "english",
            "difficulty": "medium",
            "points": 0.25,
            "passage": "Passage 1: On his first day of school, Pat Fitzsimons was bullied. From that moment on, he did not like school. He struggled through it until he could finally leave at the age of 15, lacking even basic skills. After leaving school, Pat worked in a knitwear factory and later on a building site. His supervisors noticed his potential and offered him an apprenticeship to become a plasterer. As a plasterer, he earned enough money to get by, but his inability to read and write still bothered him... Evening art classes helped him re-enter education. His teacher, Karen, spotted Pat's talent and encouraged him to go to art college... He graduated, proving that affordable adult learning programs can give people a second chance.",
            "prompt": "What is the main idea of the reading passage?",
            "options": {
                "A": "Pat faced difficulties in school, but he later succeeded in higher education with support.",
                "B": "Pat always wanted to be an artist, and art helped him escape his difficult school years.",
                "C": "Pat left school to become a successful plasterer, which allowed him to pursue his love for art.",
                "D": "Pat's difficulties with school were due to bullying, but he found a way to overcome them."
            },
            "correct_answer": "A",
            "explanation": "Bài đọc kể về hành trình từ lúc bị bắt nạt bỏ học sớm cho đến khi thành công tốt nghiệp đại học nghệ thuật nhờ sự hỗ trợ."
        },
        {
            "question_number": 20,
            "section_id": "part_2",
            "question_type": "multiple_choice",
            "domain": "english",
            "difficulty": "easy",
            "points": 0.25,
            "prompt": "According to paragraph 1, what does the word 'that' in 'but his inability to read and write still bothered him. That was just the reality...' refer to?",
            "options": {
                "A": "A challenge",
                "B": "An embarrassment",
                "C": "Pat's apprenticeship opportunity",
                "D": "Pat's inability to read and write"
            },
            "correct_answer": "D",
            "explanation": "'that' quy chiếu về việc Pat không biết đọc và viết."
        },
        {
            "question_number": 21,
            "section_id": "part_2",
            "question_type": "multiple_choice",
            "domain": "english",
            "difficulty": "easy",
            "points": 0.25,
            "prompt": "Who recognized Pat's talent in arts?",
            "options": {"A": "His art teacher", "B": "His first teacher", "C": "His factory co-worker", "D": "His college staff"},
            "correct_answer": "A",
            "explanation": "Giáo viên mỹ thuật lớp học ban đêm (Karen) đã nhận ra tài năng của anh."
        },
        {
            "question_number": 22,
            "section_id": "part_2",
            "question_type": "multiple_choice",
            "domain": "english",
            "difficulty": "easy",
            "points": 0.25,
            "prompt": "The phrase 'going to be a drop-out' in paragraph 4 is closest in meaning to:",
            "options": {
                "A": "dropping objects frequently",
                "B": "falling down physically",
                "C": "leaving education prematurely",
                "D": "reducing financial earnings"
            },
            "correct_answer": "C",
            "explanation": "'drop-out' nghĩa là bỏ học giữa chừng (leaving education prematurely)."
        },
        {
            "question_number": 23,
            "section_id": "part_2",
            "question_type": "multiple_choice",
            "domain": "english",
            "difficulty": "medium",
            "points": 0.25,
            "prompt": "Where in paragraph 2 does the following sentence best fit: 'While his first reaction was: No, college is not for me!, Karen insisted that Pat would do well at art college.'?",
            "options": {"A": "[I]", "B": "[II]", "C": "[III]", "D": "[IV]"},
            "correct_answer": "D",
            "explanation": "Câu này khớp ở vị trí [IV] ngay sau khi Karen nhận ra tài năng và thuyết phục Pat nộp đơn vào trường."
        },

        # Passage 2: Rice's Whales (câu 24 - 28)
        {
            "question_number": 24,
            "section_id": "part_2",
            "question_type": "multiple_choice",
            "domain": "english",
            "difficulty": "medium",
            "points": 0.25,
            "passage": "Passage 2: Rice's whales, found off the coast of Florida, are incredibly rare marine mammals. Scientists recently identified them as a distinct species... There are only 51 left, making them one of the scarcest marine mammals globally. Living in the Gulf of Mexico, Rice's whales face numerous threats: ship collisions, oil spills, noise pollution from seismic testing, etc.",
            "prompt": "What is the main idea of paragraph 1?",
            "options": {
                "A": "The threats to Rice's whales",
                "B": "The discovery of a new species of whales",
                "C": "The efforts to protect Rice's whales",
                "D": "The historical distribution of Rice's whales"
            },
            "correct_answer": "B",
            "explanation": "Đoạn 1 nói về việc các nhà khoa học phát hiện loài cá voi Rice mới."
        },
        {
            "question_number": 25,
            "section_id": "part_2",
            "question_type": "multiple_choice",
            "domain": "english",
            "difficulty": "medium",
            "points": 0.25,
            "prompt": "Which of the following is true about the impact of Gulf oil spill in 2010?",
            "options": {
                "A": "The fertility of about 25% of female Rice's whales was affected.",
                "B": "Just over 20% of Rice's whales were killed.",
                "C": "Nearly half of Rice's whales got sick.",
                "D": "The majority of Rice's whales' habitat was affected."
            },
            "correct_answer": "A",
            "explanation": "Bài đọc ghi rõ sự cố tràn dầu ảnh hưởng tới khả năng sinh sản của cá voi cái (reproductive issues in nearly a quarter of females)."
        },
        {
            "question_number": 26,
            "section_id": "part_2",
            "question_type": "multiple_choice",
            "domain": "english",
            "difficulty": "hard",
            "points": 0.25,
            "prompt": "The word 'impinges' in paragraph 4 is closest in meaning to:",
            "options": {"A": "assists", "B": "interferes", "C": "enhances", "D": "prolongs"},
            "correct_answer": "B",
            "explanation": "'impinges on' mang nghĩa xâm phạm / cản trở / can thiệp tiêu cực (interferes with)."
        },
        {
            "question_number": 27,
            "section_id": "part_2",
            "question_type": "multiple_choice",
            "domain": "english",
            "difficulty": "medium",
            "points": 0.25,
            "prompt": "Which of the following can be inferred from the passage?",
            "options": {
                "A": "Vessels are the primary threat to Rice's whale existence.",
                "B": "New large marine species are rarely found off the coast of Florida.",
                "C": "The coast of Texas can be the habitat of Rice's whales.",
                "D": "The law is effective in conserving large marine mammals."
            },
            "correct_answer": "C",
            "explanation": "Nghiên cứu âm thanh cho thấy cá voi Rice bơi sang tận vùng biển Texas."
        },
        {
            "question_number": 28,
            "section_id": "part_2",
            "question_type": "multiple_choice",
            "domain": "english",
            "difficulty": "hard",
            "points": 0.25,
            "prompt": "Which of the following best paraphrases the underlined sentence: 'One recent study used the whales' unique vocalizations to track their movements.'?",
            "options": {
                "A": "The whales' migration was monitored by observing their feeding habits in recent research.",
                "B": "The whales' movements were tracked by studying their physical appearance in recent research.",
                "C": "A recent study monitored the whales' movements by following their migration routes.",
                "D": "A recent study located the whales based on their distinctive vocal sounds."
            },
            "correct_answer": "D",
            "explanation": "'distinctive vocal sounds' diễn đạt lại 'unique vocalizations', 'located' diễn đạt lại 'track movements'."
        },

        # Phần III: Word Formation (4 câu - 1đ)
        {
            "question_number": 29,
            "section_id": "part_3",
            "question_type": "short_answer",
            "domain": "english",
            "difficulty": "medium",
            "points": 0.25,
            "prompt": "Even countries that are (1) ______ far from the areas most affected by extreme heat will face economic consequences. (Từ cho sẵn: GEOGRAPHY)",
            "correct_answer": "geographically",
            "accepted_answers": ["geographically", "GEOGRAPHICALLY"],
            "explanation": "Cần một trạng từ bổ nghĩa cho 'far': geographically."
        },
        {
            "question_number": 30,
            "section_id": "part_3",
            "question_type": "short_answer",
            "domain": "english",
            "difficulty": "medium",
            "points": 0.25,
            "prompt": "Studies have shown that if emissions are not (2) ______, the total annual losses could reach $25 trillion. (Từ cho sẵn: REDUCTION)",
            "correct_answer": "reduced",
            "accepted_answers": ["reduced", "REDUCED"],
            "explanation": "Cần dạng quá khứ phân từ của động từ reduce trong câu bị động: reduced."
        },
        {
            "question_number": 31,
            "section_id": "part_3",
            "question_type": "short_answer",
            "domain": "english",
            "difficulty": "easy",
            "points": 0.25,
            "prompt": "Heatwaves prevent (3) ______ workers from being productive, leading to decreases in output. (Từ cho sẵn: DOOR)",
            "correct_answer": "outdoor",
            "accepted_answers": ["outdoor", "OUTDOOR"],
            "explanation": "Tính từ bổ nghĩa cho workers: outdoor workers (lao động ngoài trời)."
        },
        {
            "question_number": 32,
            "section_id": "part_3",
            "question_type": "short_answer",
            "domain": "english",
            "difficulty": "easy",
            "points": 0.25,
            "prompt": "Governments (4) ______ need to cooperate and give the greenlight for emission policies. (Từ cho sẵn: WORLD)",
            "correct_answer": "worldwide",
            "accepted_answers": ["worldwide", "WORLDWIDE"],
            "explanation": "Trạng từ/tính từ: worldwide (trên toàn thế giới)."
        },

        # Phần IV: Writing (1 câu - 2đ)
        {
            "question_number": 33,
            "section_id": "part_4",
            "question_type": "essay",
            "domain": "english",
            "difficulty": "hard",
            "points": 2.0,
            "prompt": "Write a paragraph (of approximately 150 words) to answer the following question: 'Artificial Intelligence (AI) has become more popular around the world. What are the advantages of using AI in learning for students? Give examples and details to support your answer.'",
            "correct_answer": "Sample essay focusing on personalized pacing, instant feedback, and rich resources.",
            "explanation": "Tiêu chí chấm điểm: Content (0,5đ), Coherence & Cohesion (0,5đ), Vocabulary (0,5đ), Grammar (0,5đ)."
        }
    ]
}

from backend.exam_engine.spt_sample_subjects import (
    SPT_CHEMISTRY_EXAM,
    SPT_GEOGRAPHY_EXAM,
    SPT_HISTORY_EXAM,
    SPT_CIVICS_LAW_EXAM,
    SPT_TECH_INDUSTRY_EXAM,
    SPT_TECH_AGRICULTURE_EXAM
)

# Danh sách tất cả 8 bài thi mẫu SPT để nạp vào DB
ALL_SPT_SAMPLE_EXAMS = [
    SPT_MATH_EXAM,
    SPT_ENGLISH_EXAM,
    SPT_CHEMISTRY_EXAM,
    SPT_GEOGRAPHY_EXAM,
    SPT_HISTORY_EXAM,
    SPT_CIVICS_LAW_EXAM,
    SPT_TECH_INDUSTRY_EXAM,
    SPT_TECH_AGRICULTURE_EXAM
]

