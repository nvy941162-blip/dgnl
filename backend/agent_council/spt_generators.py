import random
import math
from typing import Dict, Any, List, Optional

def generate_fresh_spt_question(
    subject: str,
    sec_id: str,
    q_type: str,
    topic_theme: str = "",
    index: int = 1
) -> Dict[str, Any]:
    """
    Sinh câu hỏi MỚI TOÀN DIỆN, độc lập 100% với đề mẫu.
    Đảm bảo chuẩn CT GDPT 2018 và quy cách khảo thí ĐH Sư Phạm Hà Nội.
    """
    subject = (subject or "math").lower()

    if subject == "math":
        return _generate_fresh_math(sec_id, q_type, index)
    elif subject == "english":
        return _generate_fresh_english(sec_id, q_type, index)
    elif subject in ["civics_law", "economics_law", "gdktpl"]:
        return _generate_fresh_civics_law(sec_id, q_type, index)
    elif subject == "physics":
        return _generate_fresh_physics(sec_id, q_type, index)
    elif subject == "chemistry":
        return _generate_fresh_chemistry(sec_id, q_type, index)
    elif subject == "biology":
        return _generate_fresh_biology(sec_id, q_type, index)
    elif subject == "history":
        return _generate_fresh_history(sec_id, q_type, index)
    elif subject == "geography":
        return _generate_fresh_geography(sec_id, q_type, index)
    else:
        return _generate_fresh_general(subject, sec_id, q_type, index)


# =============================================================================
# 1. MÔN TOÁN HỌC (MATHEMATICS)
# =============================================================================
def _generate_fresh_math(sec_id: str, q_type: str, idx: int) -> Dict[str, Any]:
    seed = (idx * 17 + random.randint(1, 99)) % 100

    if q_type == "multiple_choice":
        templates = [
            # Dạng 1: Đạo hàm & Khảo sát hàm phân thức
            lambda: {
                "prompt": f"Cho hàm số $y = \\frac{{2x - {random.randint(1, 5)}}}{{x + {random.randint(1, 4)}}}$. Đồ thị hàm số có các đường tiệm cận đứng và tiệm cận ngang lần lượt là:",
                "options": {
                    "A": "Tiệm cận đứng $x = -2$, tiệm cận ngang $y = 2$.",
                    "B": "Tiệm cận đứng $x = 2$, tiệm cận ngang $y = -2$.",
                    "C": "Tiệm cận đứng $x = -1$, tiệm cận ngang $y = 1$.",
                    "D": "Tiệm cận đứng $x = 1$, tiệm cận ngang $y = 2$."
                },
                "correct_answer": "A",
                "explanation": "Đồ thị hàm phân thức $y = \\frac{ax+b}{cx+d}$ có tiệm cận đứng là nghiệm mẫu số $cx+d=0 \\Leftrightarrow x = -d/c$ và tiệm cận ngang $y = \\lim_{x\\to \\pm\\infty} y = a/c = 2$."
            },
            # Dạng 2: Cực trị hàm đa thức bậc 3
            lambda: {
                "prompt": f"Điểm cực đại của đồ thị hàm số $y = -x^3 + 3x^2 + {random.randint(1, 6)}$ là điểm nào sau đây?",
                "options": {
                    "A": "$(2; 5)$",
                    "B": "$(0; 1)$",
                    "C": "$(-1; 3)$",
                    "D": "$(1; 4)$"
                },
                "correct_answer": "A",
                "explanation": "Đạo hàm $y' = -3x^2 + 6x = -3x(x - 2)$. Nghiệm $x = 0$ (cực tiểu) và $x = 2$ (cực đại vì $y'$ đổi dấu từ dương sang âm qua $x=2$). Tọa độ điểm cực đại là $(2; 5)$."
            },
            # Dạng 3: Tích phân đổi biến / từng phần
            lambda: {
                "prompt": "Biết $\\int_0^1 (2x + 1) e^x dx = a \\cdot e + b$ với $a, b \\in \\mathbb{Z}$. Tính giá trị của biểu thức $T = a + b$.",
                "options": {
                    "A": "$T = 2$",
                    "B": "$T = 1$",
                    "C": "$T = 0$",
                    "D": "$T = -1$"
                },
                "correct_answer": "A",
                "explanation": "Đặt $u = 2x+1 \\Rightarrow du = 2dx$; $dv = e^x dx \\Rightarrow v = e^x$. Ta có: $\\int_0^1 (2x+1)e^x dx = [(2x+1)e^x]_0^1 - \\int_0^1 2e^x dx = 3e - 1 - 2(e - 1) = e + 1$. Do đó $a = 1, b = 1 \\Rightarrow T = 2$."
            },
            # Dạng 4: Tọa độ không gian Oxyz - Mặt phẳng
            lambda: {
                "prompt": "Trong không gian $Oxyz$, cho điểm $A(1; -2; 3)$ và vectơ pháp tuyến $\\vec{n} = (2; -1; 4)$. Phương trình tổng quát của mặt phẳng đi qua $A$ và nhận $\\vec{n}$ làm VTPT là:",
                "options": {
                    "A": "$2x - y + 4z - 16 = 0$",
                    "B": "$2x - y + 4z + 16 = 0$",
                    "C": "$x - 2y + 3z - 16 = 0$",
                    "D": "$2x + y - 4z + 8 = 0$"
                },
                "correct_answer": "A",
                "explanation": "Phương trình mặt phẳng: $2(x - 1) - 1(y + 2) + 4(z - 3) = 0 \\Leftrightarrow 2x - y + 4z - 16 = 0$."
            },
            # Dạng 5: Thống kê & Xác suất có điều kiện (GDPT 2018)
            lambda: {
                "prompt": "Một hộp có 6 quả cầu đỏ và 4 quả cầu xanh. Lấy ngẫu nhiên liên tiếp 2 quả cầu (không hoàn lại). Xác suất để quả thứ hai màu đỏ biết rằng quả thứ nhất màu xanh là:",
                "options": {
                    "A": "$\\frac{2}{3}$",
                    "B": "$\\frac{3}{5}$",
                    "C": "$\\frac{1}{2}$",
                    "D": "$\\frac{4}{9}$"
                },
                "correct_answer": "A",
                "explanation": "Sau khi lấy quả thứ nhất màu xanh, trong hộp còn lại 9 quả cầu gồm 6 quả đỏ và 3 quả xanh. Xác suất lấy tiếp được quả đỏ có điều kiện là $P(Đ_2|X_1) = \\frac{6}{9} = \\frac{2}{3}$."
            },
            # Dạng 6: Bất phương trình logarit
            lambda: {
                "prompt": "Tập nghiệm $S$ của bất phương trình $\\log_3(2x - 1) \\le 2$ là:",
                "options": {
                    "A": "$S = \\left( \\frac{1}{2}; 5 \\right]$",
                    "B": "$S = [1; 5]$",
                    "C": "$S = (-\\infty; 5]$",
                    "D": "$S = \\left( \\frac{1}{2}; 10 \\right]$"
                },
                "correct_answer": "A",
                "explanation": "Điều kiện xác định: $2x - 1 > 0 \\Leftrightarrow x > \\frac{1}{2}$. Vì cơ số $3 > 1$ nên bất phương trình tương đương: $2x - 1 \\le 3^2 = 9 \\Leftrightarrow 2x \\le 10 \\Leftrightarrow x \\le 5$. Kết hợp điều kiện ta có $S = \\left( \\frac{1}{2}; 5 \\right]$."
            }
        ]
        chosen = templates[seed % len(templates)]()
        return {
            "prompt": chosen["prompt"],
            "options": chosen["options"],
            "correct_answer": chosen["correct_answer"],
            "explanation": chosen["explanation"],
            "difficulty": "medium",
            "question_type": "multiple_choice"
        }

    elif q_type == "true_false":
        tf_templates = [
            lambda: {
                "prompt": "Cho hàm số $f(x) = x^3 - 3x^2 + 2$ có đồ thị là đường cong $(C)$. Xét tính đúng/sai của các mệnh đề sau:",
                "tf_statements": {
                    "a": "Hàm số đồng biến trên khoảng $(-\\infty; 0)$ và $(2; +\\infty)$.",
                    "b": "Hàm số đạt cực đại tại điểm $x = 2$.",
                    "c": "Điểm uốn của đồ thị $(C)$ là $I(1; 0)$.",
                    "d": "Phương trình tiếp tuyến của $(C)$ tại điểm có hoành độ $x_0 = 1$ có hệ số góc bằng $k = -3$."
                },
                "correct_answer": {"a": "Đ", "b": "S", "c": "Đ", "d": "Đ"},
                "explanation": "Đạo hàm $f'(x) = 3x^2 - 6x = 3x(x - 2)$. Ta có $f'(x) > 0 \\Leftrightarrow x \\in (-\\infty; 0) \\cup (2; +\\infty)$ nên mệnh đề (a) đúng. Hàm số đạt cực đại tại $x = 0$ và cực tiểu tại $x = 2$, nên mệnh đề (b) sai. Đạo hàm cấp hai $f''(x) = 6x - 6 = 0 \\Leftrightarrow x = 1 \\Rightarrow y(1) = 0$, điểm uốn là $(1; 0)$ nên (c) đúng. Hệ số góc $k = f'(1) = 3(1)^2 - 6(1) = -3$ nên (d) đúng."
            },
            lambda: {
                "prompt": "Trong không gian $Oxyz$, cho mặt cầu $(S): x^2 + y^2 + z^2 - 2x + 4y - 6z - 11 = 0$ và mặt phẳng $(P): 2x - 2y + z + 1 = 0$. Xét tính đúng/sai của các mệnh đề sau:",
                "tf_statements": {
                    "a": "Mặt cầu $(S)$ có tâm $I(1; -2; 3)$ và bán kính $R = 5$.",
                    "b": "Khoảng cách từ tâm $I$ của mặt cầu đến mặt phẳng $(P)$ bằng $d(I, (P)) = 4$.",
                    "c": "Mặt phẳng $(P)$ cắt mặt cầu $(S)$ theo một đường tròn có bán kính $r = 3$.",
                    "d": "Điểm $M(0; 0; -1)$ thuộc cả mặt phẳng $(P)$ và mặt cầu $(S)$."
                },
                "correct_answer": {"a": "Đ", "b": "Đ", "c": "Đ", "d": "S"},
                "explanation": "Tâm $I(1; -2; 3)$, $R = \\sqrt{1^2 + (-2)^2 + 3^2 - (-11)} = \\sqrt{25} = 5$ (mệnh đề a đúng). Khoảng cách $d = \\frac{|2(1) - 2(-2) + 3 + 1|}{\\sqrt{2^2 + (-2)^2 + 1^2}} = \\frac{10 + 2}{3} = 4$ (mệnh đề b đúng). Bán kính đường tròn giao tuyến $r = \\sqrt{R^2 - d^2} = \\sqrt{5^2 - 4^2} = 3$ (mệnh đề c đúng). Thay $M(0; 0; -1)$ vào $(P)$: $2(0) - 2(0) + (-1) + 1 = 0$ (thuộc $(P)$), nhưng thay vào $(S)$: $0 + 0 + 1 - 0 + 0 + 6 - 11 = -4 \\ne 0$ (không thuộc $(S)$) nên (d) sai."
            }
        ]
        chosen = tf_templates[seed % len(tf_templates)]()
        return {
            "prompt": chosen["prompt"],
            "tf_statements": chosen["tf_statements"],
            "correct_answer": chosen["correct_answer"],
            "explanation": chosen["explanation"],
            "difficulty": "hard",
            "question_type": "true_false"
        }

    elif q_type == "short_answer":
        sa_templates = [
            {
                "prompt": "Cho hình lập phương $ABCD.A'B'C'D'$ có cạnh bằng $a = 4\\text{ cm}$. Tính khoảng cách từ điểm $B$ đến mặt phẳng $(A'BD)$. (Nhập kết quả dưới dạng số làm tròn đến 2 chữ số thập phân hoặc căn thức, ví dụ: 2.31)",
                "correct_answer": "2.31",
                "explanation": "Khoảng cách từ $B$ đến $(A'BD)$ bằng chiều cao $h$ kẻ từ đỉnh $B$ của tứ diện vuông $BAA'D$. Ta có $\\frac{1}{h^2} = \\frac{1}{BA^2} + \\frac{1}{BD^2} + \\frac{1}{BA'^2} \\Rightarrow h = \\frac{a}{\\sqrt{3}} = \\frac{4}{\\sqrt{3}} \\approx 2.31\\text{ cm}$."
            },
            {
                "prompt": "Một bể bơi hình chữ nhật có chu vi $P = 60\\text{ m}$. Hỏi chiều dài của bể bơi bằng bao nhiêu mét để diện tích mặt nước của bể bơi đạt giá trị lớn nhất?",
                "correct_answer": "15",
                "explanation": "Nửa chu vi là $x + y = 30 \\Rightarrow y = 30 - x$. Diện tích $S(x) = x(30 - x) = -x^2 + 30x$. Đạt cực đại tại đỉnh parabol $x = 15\\text{ m}$ (hình vuông)."
            }
        ]
        chosen = sa_templates[seed % len(sa_templates)]
        return {
            **chosen,
            "difficulty": "hard",
            "question_type": "short_answer"
        }

    else: # essay
        return {
            "prompt": "Một doanh nghiệp sản xuất một loại sản phẩm công nghệ với hàm chi phí tổng cộng $C(x) = 0.02x^3 - 1.2x^2 + 30x + 500$ (triệu đồng), trong đó $x$ là số lượng sản phẩm ($x \\in [10; 80]$). Giá bán mỗi sản phẩm trên thị trường là $p(x) = 60 - 0.2x$ (triệu đồng). Hãy tìm số lượng sản phẩm $x$ cần sản xuất để doanh nghiệp thu được lợi nhuận tối đa và tính giá trị lợi nhuận tối đa đó.",
            "correct_answer": "Lợi nhuận tối đa đạt được khi x = 40 sản phẩm, lợi nhuận cực đại bằng 780 triệu đồng.",
            "explanation": "Hàm doanh thu $R(x) = x \\cdot p(x) = 60x - 0.2x^2$. Hàm lợi nhuận $P(x) = R(x) - C(x) = -0.02x^3 + x^2 + 30x - 500$. Đạo hàm $P'(x) = -0.06x^2 + 2x + 30 = 0 \\Leftrightarrow x = 40$ hoặc $x = -12.5$ (loại). Lập bảng biến thiên trên đoạn $[10; 80]$ suy ra $P(x)$ đạt cực đại tại $x = 40$. Lợi nhuận tối đa là $P(40) = 780$ triệu đồng.",
            "difficulty": "very_hard",
            "question_type": "essay"
        }


# =============================================================================
# 2. MÔN TIẾNG ANH (ENGLISH)
# =============================================================================
def _generate_fresh_english(sec_id: str, q_type: str, idx: int) -> Dict[str, Any]:
    seed = (idx * 23 + random.randint(1, 99)) % 100

    if q_type == "multiple_choice":
        templates = [
            {
                "prompt": "Not only _______ the national science competition, but she also secured a full scholarship to Cambridge University.",
                "options": {
                    "A": "did she win",
                    "B": "she won",
                    "C": "has she won",
                    "D": "she had won"
                },
                "correct_answer": "A",
                "explanation": "Inversion structure with 'Not only': Not only + auxiliary verb + S + main verb..., but S + also + V."
            },
            {
                "prompt": "_______ for the prompt intervention of the firefighter team, the chemical explosion would have caused catastrophic damage.",
                "options": {
                    "A": "Had it not been",
                    "B": "Were it not",
                    "C": "If it were not",
                    "D": "Should it not be"
                },
                "correct_answer": "A",
                "explanation": "Inversion of third conditional expressing an unreal condition in the past: Had it not been for + Noun phrase, S + would have + V3/ed."
            },
            {
                "prompt": "The headmaster recommended that all senior students _______ an intensive academic writing seminar before taking the national examination.",
                "options": {
                    "A": "attend",
                    "B": "attended",
                    "C": "must attend",
                    "D": "attending"
                },
                "correct_answer": "A",
                "explanation": "Subjunctive mood after verbs of recommendation/demand (recommend, suggest, require): S + recommend + that + S + (should) bare infinitive."
            },
            {
                "prompt": "Due to the economic downturn, several multinational corporations had to _______ their scheduled branch expansion plans until next year.",
                "options": {
                    "A": "call off",
                    "B": "look into",
                    "C": "take after",
                    "D": "get round"
                },
                "correct_answer": "A",
                "explanation": "'Call off' means to cancel or postpone an event or plan. 'Look into' means investigate; 'take after' means resemble."
            },
            {
                "prompt": "Scientists have recently made a significant _______ in quantum computing that could revolutionize data encryption.",
                "options": {
                    "A": "breakthrough",
                    "B": "breakdown",
                    "C": "breakout",
                    "D": "breakaway"
                },
                "correct_answer": "A",
                "explanation": "Collocation: 'make a breakthrough' means to make an important discovery or sudden advance in knowledge or technology."
            }
        ]
        chosen = templates[seed % len(templates)]
        return {
            **chosen,
            "difficulty": "medium",
            "question_type": "multiple_choice"
        }

    elif q_type == "true_false":
        return {
            "passage": "Artificial intelligence (AI) has rapidly transformed modern pedagogy by offering adaptive learning platforms that tailor educational materials to each student's pacing and proficiency. Recent empirical studies conducted in Southeast Asian high schools indicate that learners utilizing intelligent tutoring systems achieved a 22% higher retention rate compared to traditional classroom settings. Nevertheless, educational sociologists emphasize that automated algorithms cannot replace the fundamental social and emotional mentoring provided by human instructors.",
            "prompt": "Read the passage above and decide whether each of the following statements is True (Đ) or False (S):",
            "tf_statements": {
                "a": "Adaptive learning platforms adjust educational content according to an individual learner's pace.",
                "b": "Students using intelligent tutoring systems demonstrated lower knowledge retention than traditional students.",
                "c": "The passage suggests that AI tutoring systems should completely replace human teachers in high schools.",
                "d": "Educational sociologists highlight the irreplaceable emotional and social mentoring role of teachers."
            },
            "correct_answer": {"a": "Đ", "b": "S", "c": "S", "d": "Đ"},
            "explanation": "Statement (a) is explicitly mentioned in sentence 1 ('tailor materials to each student's pacing'). Statement (b) is False because retention was 22% higher, not lower. Statement (c) is False because the text states automated algorithms cannot replace human mentoring. Statement (d) is True based on the concluding sentence.",
            "difficulty": "hard",
            "question_type": "true_false"
        }

    elif q_type == "short_answer":
        sa_templates = [
            {
                "prompt": "Give the correct form of the word in brackets: 'The rapid development of renewable energy is expected to ensure long-term environmental _______.' [SUSTAIN]",
                "correct_answer": "sustainability",
                "explanation": "After the adjective 'environmental', we need a noun. The noun form of 'sustain' is 'sustainability' (tính bền vững)."
            },
            {
                "prompt": "Give the correct form of the word in brackets: 'She delivered an exceptionally _______ presentation that persuaded all members of the board.' [CONVINCE]",
                "correct_answer": "convincing",
                "explanation": "Before the noun 'presentation', an adjective is required to describe the quality of the speech: 'convincing' (thuyết phục)."
            }
        ]
        chosen = sa_templates[seed % len(sa_templates)]
        return {
            **chosen,
            "difficulty": "hard",
            "question_type": "short_answer"
        }

    else:
        return {
            "prompt": "Write an academic paragraph of 150-180 words addressing the following prompt: 'Some educators argue that high school students should be taught coding and artificial intelligence literacy as compulsory subjects. To what extent do you agree or disagree with this view?'",
            "correct_answer": "Bài luận cần có cấu trúc 3 phần rõ ràng: Topic sentence, 2 luận điểm dẫn chứng kèm phản biện và Concluding sentence. Tiêu chí chấm: Task response (0.3đ), Coherence & Cohesion (0.25đ), Lexical Resource (0.25đ), Grammatical Range (0.2đ).",
            "explanation": "Tiêu chí chấm chuẩn khảo thí: Luận điểm thuyết phục, vốn từ phong phú chuẩn học thuật C1/B2, sử dụng linh hoạt câu phức và liên từ mạch lạc.",
            "difficulty": "very_hard",
            "question_type": "essay"
        }


# =============================================================================
# 3. MÔN GIÁO DỤC KINH TẾ & PHÁP LUẬT (GDKT&PL)
# =============================================================================
def _generate_fresh_civics_law(sec_id: str, q_type: str, idx: int) -> Dict[str, Any]:
    seed = (idx * 31 + random.randint(1, 99)) % 100

    if q_type == "multiple_choice":
        templates = [
            {
                "prompt": "Theo quy luật cung - cầu trong nền kinh tế thị trường, khi giá cả của một loại hàng hóa giảm xuống trong khi các yếu tố khác không đổi thì:",
                "options": {
                    "A": "Lượng cầu về hàng hóa đó thường có xu hướng tăng lên.",
                    "B": "Lượng cung về hàng hóa đó sẽ tăng đột biến.",
                    "C": "Lượng cầu về hàng hóa đó lập tức giảm mạnh.",
                    "D": "Cung và cầu luôn giữ nguyên ở trạng thái cân bằng tuyệt đối."
                },
                "correct_answer": "A",
                "explanation": "Theo quy luật cầu, khi giá cả giảm, khả năng chi trả của người tiêu dùng tăng lên, do đó lượng cầu về hàng hóa đó có xu hướng tăng."
            },
            {
                "prompt": "Loại hình thất nghiệp nào phát sinh do sự mất cân đối giữa kỹ năng của người lao động với yêu cầu công việc mới xuất hiện từ chuyển đổi số và công nghệ?",
                "options": {
                    "A": "Thất nghiệp cơ cấu.",
                    "B": "Thất nghiệp chu kỳ.",
                    "C": "Thất nghiệp tạm thời.",
                    "D": "Thất nghiệp tự nguyện."
                },
                "correct_answer": "A",
                "explanation": "Thất nghiệp cơ cấu xảy ra khi có sự mất cân xứng lâu dài giữa cơ cấu ngành nghề đào tạo, kỹ năng của người lao động với cơ cấu nhu cầu tuyển dụng của nền kinh tế."
            },
            {
                "prompt": "Hành vi nào sau đây vi phạm quyền bất khả xâm phạm về thân thể của công dân theo quy định của Hiến pháp nước Cộng hòa XHCN Việt Nam?",
                "options": {
                    "A": "Bắt giữ và giam người vì nghi ngờ lấy cắp tài sản khi chưa có lệnh hợp pháp của cơ quan có thẩm quyền.",
                    "B": "Công an tạm giữ người đang thực hiện hành vi phạm tội quả tang.",
                    "C": "Cảnh sát áp giải đối tượng có lệnh truy nã toàn quốc về trụ sở.",
                    "D": "Kiểm tra nồng độ cồn người điều khiển phương tiện tham gia giao thông theo chuyên đề."
                },
                "correct_answer": "A",
                "explanation": "Không ai bị bắt nếu không có quyết định của Tòa án nhân dân, quyết định hoặc phê chuẩn của Viện kiểm sát nhân dân, trừ trường hợp phạm tội quả tang. Việc tự ý giam giữ người vì nghi ngờ là xâm phạm quyền bất khả xâm phạm về thân thể."
            },
            {
                "prompt": "Trong các chính sách tài khóa của Nhà nước, việc tăng chi tiêu đầu tư công cho hệ thống đường cao tốc và hạ tầng logistics nhằm mục đích trực tiếp nào sau đây?",
                "options": {
                    "A": "Kích thích tổng cầu và thúc đẩy tăng trưởng kinh tế dài hạn.",
                    "B": "Triệt tiêu ngay lập tức hiện tượng cạnh tranh giữa các doanh nghiệp.",
                    "C": "Xóa bỏ hoàn toàn việc thu thuế thu nhập doanh nghiệp.",
                    "D": "Hạn chế sự lưu thông của dòng vốn đầu tư nước ngoài (FDI)."
                },
                "correct_answer": "A",
                "explanation": "Chi tiêu đầu tư công là một bộ phận của tổng cầu ($AD$). Khi nhà nước đầu tư hạ tầng giao thông sẽ trực tiếp kích thích tổng cầu, tạo việc làm và gia tăng năng lực sản xuất của nền kinh tế."
            }
        ]
        chosen = templates[seed % len(templates)]
        return {
            **chosen,
            "difficulty": "medium",
            "question_type": "multiple_choice"
        }

    elif q_type == "true_false":
        return {
            "prompt": "Công ty cổ phần Chế biến Nông sản An Phú do ông H làm Giám đốc ký hợp đồng lao động 2 năm với anh M vào vị trí kỹ sư vận hành máy. Sau 6 tháng, do giá nông sản giảm, ông H tự ý đơn phương ra quyết định chấm dứt hợp đồng lao động với anh M mà không báo trước và không có lý do chính đáng được pháp luật thừa nhận. Đồng thời, công ty giữ lại sổ bảo hiểm xã hội của anh M. Xét tính đúng/sai của các nhận định pháp lý sau:",
            "tf_statements": {
                "a": "Hành vi của ông H đã vi phạm quy định của Bộ luật Lao động về nghĩa vụ báo trước khi đơn phương chấm dứt hợp đồng.",
                "b": "Anh M có quyền khiếu nại hoặc khởi kiện trực tiếp ra Tòa án nhân dân có thẩm quyền để bảo vệ quyền lợi hợp pháp của mình.",
                "c": "Công ty An Phú có quyền giữ sổ bảo hiểm xã hội của anh M cho đến khi công ty tìm được kỹ sư mới thay thế.",
                "d": "Theo quy định, người sử dụng lao động đơn phương chấm dứt hợp đồng trái luật phải nhận người lao động trở lại làm việc và bồi thường tiền lương những ngày không được làm việc."
            },
            "correct_answer": {"a": "Đ", "b": "Đ", "c": "S", "d": "Đ"},
            "explanation": "Nhận định (a) đúng vì ông H chấm dứt hợp đồng không báo trước theo thời hạn luật định (ít nhất 30 ngày đối với HĐLĐ xác định thời hạn). Nhận định (b) đúng vì anh M là chủ thể quyền lao động bị xâm hại. Nhận định (c) sai vì pháp luật cấm giữ giấy tờ tùy thân và sổ BHXH của người lao động. Nhận định (d) đúng theo Điều 41 Bộ luật Lao động 2019."
        }

    elif q_type == "short_answer":
        return {
            "prompt": "Thuật ngữ kinh tế học nào chỉ hiện tượng mức giá chung của nền kinh tế liên tục giảm trong một khoảng thời gian dài, thường đi kèm với đình trệ sản xuất và gia tăng thất nghiệp?",
            "correct_answer": "giảm phát",
            "explanation": "Giảm phát (Deflation) là sự suy giảm liên tục trong mức giá chung của hàng hóa và dịch vụ, đối lập với lạm phát (Inflation).",
            "difficulty": "hard",
            "question_type": "short_answer"
        }

    else:
        return {
            "prompt": "Hãy phân tích vai trò của pháp luật về sở hữu trí tuệ đối với việc thúc đẩy các doanh nghiệp khởi nghiệp đổi mới sáng tạo (startup) tại Việt Nam trong bối cảnh cuộc Cách mạng công nghiệp lần thứ tư.",
            "correct_answer": "Barem chấm: Nêu được khái niệm quyền SHTT (0.25đ); Phân tích vai trò bảo vệ thành quả nghiên cứu, tạo động lực sáng tạo (0.25đ); Vai trò thu hút vốn đầu tư mạo hiểm và thương mại hóa (0.25đ); Liên hệ thực tiễn doanh nghiệp công nghệ Việt Nam (0.25đ).",
            "explanation": "Đánh giá tư duy pháp lý và liên hệ thực tiễn kinh tế thị trường hiện đại.",
            "difficulty": "very_hard",
            "question_type": "essay"
        }


# =============================================================================
# 4. MÔN VẬT LÝ, HÓA HỌC, SINH HỌC, LỊCH SỬ, ĐỊA LÝ
# =============================================================================
def _generate_fresh_physics(sec_id: str, q_type: str, idx: int) -> Dict[str, Any]:
    seed = (idx * 13 + random.randint(1, 99)) % 100
    if q_type == "multiple_choice":
        templates = [
            {
                "prompt": "Một con lắc lò xo gồm vật nhỏ khối lượng $m = 100\\text{ g}$ và lò xo nhẹ có độ cứng $k = 40\\text{ N/m}$. Tần số góc dao động điều hòa của con lắc là:",
                "options": {
                    "A": "$\\omega = 20\\text{ rad/s}$",
                    "B": "$\\omega = 10\\text{ rad/s}$",
                    "C": "$\\omega = 400\\text{ rad/s}$",
                    "D": "$\\omega = 2\\pi\\text{ rad/s}$"
                },
                "correct_answer": "A",
                "explanation": "Tần số góc $\\omega = \\sqrt{\\frac{k}{m}} = \\sqrt{\\frac{40}{0.1}} = \\sqrt{400} = 20\\text{ rad/s}$."
            },
            {
                "prompt": "Hiện tượng tán sắc ánh sáng của lăng kính xảy ra chủ yếu là do:",
                "options": {
                    "A": "Chiết suất của thủy tinh lăng kính đối với các ánh sáng đơn sắc khác nhau là khác nhau.",
                    "B": "Vận tốc ánh sáng trong chân không phụ thuộc vào tần số sóng.",
                    "C": "Góc chiết quang của lăng kính thay đổi liên tục khi ánh sáng đi qua.",
                    "D": "Lăng kính hấp thụ hoàn toàn ánh sáng màu đỏ."
                },
                "correct_answer": "A",
                "explanation": "Chiết suất của môi trường trong suốt phụ thuộc vào tần số ánh sáng (nhỏ nhất đối với ánh sáng đỏ và lớn nhất đối với ánh sáng tím), dẫn đến góc khúc xạ khác nhau và gây ra hiện tượng tán sắc."
            }
        ]
        chosen = templates[seed % len(templates)]
        return {**chosen, "difficulty": "medium", "question_type": "multiple_choice"}
    elif q_type == "true_false":
        return {
            "prompt": "Một mạch dao động $LC$ lí tưởng gồm cuộn cảm thuần có độ tự cảm $L = 50\\text{ mH}$ và tụ điện có điện dung $C = 5\\mu\\text{F}$. Điện áp cực đại giữa hai bản tụ điện là $U_0 = 12\\text{ V}$. Xét tính đúng/sai của các phát biểu sau:",
            "tf_statements": {
                "a": "Chu kỳ dao động riêng của mạch là $T = \\pi \\cdot 10^{-3}\\text{ s}$.",
                "b": "Năng lượng điện từ toàn phần của mạch bằng $W = 3.6 \\cdot 10^{-4}\\text{ J}$.",
                "c": "Cường độ dòng điện cực đại qua cuộn cảm bằng $I_0 = 0.12\\text{ A}$.",
                "d": "Khi điện áp giữa hai bản tụ là $6\\text{ V}$ thì năng lượng từ trường bằng một nửa năng lượng điện từ toàn phần."
            },
            "correct_answer": {"a": "Đ", "b": "Đ", "c": "Đ", "d": "S"},
            "explanation": "Chu kỳ $T = 2\\pi\\sqrt{LC} = 2\\pi\\sqrt{50\\cdot 10^{-3}\\cdot 5\\cdot 10^{-6}} = \\pi \\cdot 10^{-3}\\text{ s}$ (a đúng). Năng lượng $W = \\frac{1}{2}CU_0^2 = \\frac{1}{2}(5\\cdot 10^{-6})(144) = 3.6\\cdot 10^{-4}\\text{ J}$ (b đúng). $I_0 = U_0\\sqrt{C/L} = 12\\sqrt{5\\cdot 10^{-6} / (50\\cdot 10^{-3})} = 0.12\\text{ A}$ (c đúng). Khi $u = U_0/2 = 6\\text{ V}$ thì $W_C = W/4$, do đó năng lượng từ trường $W_L = \\frac{3}{4}W$ chứ không phải một nửa (d sai)."
        }
    else:
        return {
            "prompt": "Một chất phóng xạ có chu kỳ bán rã $T = 138\\text{ ngày}$. Ban đầu có $m_0 = 20\\text{ mg}$ chất này. Hỏi sau bao nhiêu ngày thì khối lượng chất phóng xạ còn lại đúng $2.5\\text{ mg}$?",
            "correct_answer": "414",
            "explanation": "Ta có $m(t) = m_0 \\cdot 2^{-t/T} \\Rightarrow 2.5 = 20 \\cdot 2^{-t/138} \\Rightarrow 2^{-t/138} = \\frac{1}{8} = 2^{-3} \\Rightarrow t = 3 \\times 138 = 414\\text{ ngày}$."
        }

def _generate_fresh_chemistry(sec_id: str, q_type: str, idx: int) -> Dict[str, Any]:
    seed = (idx * 29 + random.randint(1, 99)) % 100
    if q_type == "multiple_choice":
        templates = [
            {
                "prompt": "Chất nào sau đây khi thủy phân trong môi trường kiềm (đun nóng) tạo ra muối của axit cacboxylic và ancol etylic?",
                "options": {
                    "A": "Etyl axetat ($\\text{CH}_3\\text{COOC}_2\\text{H}_5$).",
                    "B": "Metyl fomat ($\\text{HCOOCH}_3$).",
                    "C": "Phenyl axetat ($\\text{CH}_3\\text{COOC}_6\\text{H}_5$).",
                    "D": "Tripanmitin ($(\\text{C}_{15}\\text{H}_{31}\\text{COO})_3\\text{C}_3\\text{H}_5$)."
                },
                "correct_answer": "A",
                "explanation": "Phương trình phản ứng xà phòng hóa: $\\text{CH}_3\\text{COOC}_2\\text{H}_5 + \\text{NaOH} \\rightarrow \\text{CH}_3\\text{COONa} + \\text{C}_2\\text{H}_5\\text{OH}$ (ancol etylic)."
            },
            {
                "prompt": "Kim loại nào sau đây có tính khử mạnh nhất trong dãy điện hóa của kim loại?",
                "options": {
                    "A": "Mg (Magie).",
                    "B": "Fe (Sắt).",
                    "C": "Cu (Đồng).",
                    "D": "Ag (Bạc)."
                },
                "correct_answer": "A",
                "explanation": "Theo thứ tự dãy điện hóa: $\\text{Mg} > \\text{Al} > \\text{Zn} > \\text{Fe} > \\text{Cu} > \\text{Ag}$. Do đó Magie có tính khử mạnh nhất trong các kim loại trên."
            }
        ]
        chosen = templates[seed % len(templates)]
        return {**chosen, "difficulty": "medium", "question_type": "multiple_choice"}
    elif q_type == "true_false":
        return {
            "prompt": "Tiến hành thí nghiệm lên men glucozơ thành ancol etylic và dẫn toàn bộ khí sinh ra vào dung dịch nước vôi trong dư. Xét tính đúng/sai của các nhận định hóa học sau:",
            "tf_statements": {
                "a": "Quá trình lên men glucozơ xảy ra nhờ xúc tác men do nấm men sinh ra.",
                "b": "Khí sinh ra trong phản ứng lên men là khí $\\text{CO}_2$ làm vẩn đục dung dịch nước vôi trong.",
                "c": "Khối lượng kết tủa thu được tỉ lệ mol 1:1 với lượng glucozơ đã tham gia phản ứng.",
                "d": "Nếu hiệu suất lên men là 80% thì từ 1 mol glucozơ sẽ thu được tối đa 1.6 mol ancol etylic."
            },
            "correct_answer": {"a": "Đ", "b": "Đ", "c": "S", "d": "Đ"},
            "explanation": "Phương trình: $\\text{C}_6\\text{H}_{12}\\text{O}_6 \\rightarrow 2\\text{C}_2\\text{H}_5\\text{OH} + 2\\text{CO}_2$. Khí $\\text{CO}_2 + \\text{Ca(OH)}_2 \\rightarrow \\text{CaCO}_3\\downarrow + \\text{H}_2\\text{O}$. Tỉ lệ mol giữa kết tủa $\\text{CaCO}_3$ và glucozơ phản ứng là 2:1 chứ không phải 1:1 (c sai). Với $H=80\\%$, số mol ancol thu được $= 1 \\times 2 \\times 0.8 = 1.6\\text{ mol}$ (d đúng)."
        }
    else:
        return {
            "prompt": "Hòa tan hoàn toàn $5.4\\text{ gam}$ Al vào dung dịch $\\text{HNO}_3$ loãng dư, thu được $V$ lít khí NO (sản phẩm khử duy nhất ở đktc). Tính giá trị của $V$ (lít).",
            "correct_answer": "4.48",
            "explanation": "Số mol Al $= 5.4 / 27 = 0.2\\text{ mol}$. Bảo toàn electron: $3 \\times n_{\\text{Al}} = 3 \\times n_{\\text{NO}} \\Rightarrow n_{\\text{NO}} = 0.2\\text{ mol}$. Thể tích khí $V = 0.2 \\times 22.4 = 4.48\\text{ lít}$."
        }

def _generate_fresh_biology(sec_id: str, q_type: str, idx: int) -> Dict[str, Any]:
    return {
        "prompt": "Ở một loài thực vật lưỡng bội, gen A quy định thân cao trội hoàn toàn so với alen a quy định thân thấp; gen B quy định hoa đỏ trội hoàn toàn so với alen b quy định hoa trắng. Hai cặp gen phân li độc lập. Cho cây dị hợp 2 cặp gen tự thụ phấn, tỉ lệ kiểu hình thân cao, hoa trắng ở đời con $F_1$ là:",
        "options": {
            "A": "$\\frac{3}{16}$",
            "B": "$\\frac{9}{16}$",
            "C": "$\\frac{1}{16}$",
            "D": "$\\frac{3}{8}$"
        },
        "correct_answer": "A",
        "explanation": "Phép lai $AaBb \\times AaBb$. Tỉ lệ kiểu hình thân cao, hoa trắng ($A\\_bb$) $= \\frac{3}{4} (A\\_) \\times \\frac{1}{4} (bb) = \\frac{3}{16}$."
    }

def _generate_fresh_history(sec_id: str, q_type: str, idx: int) -> Dict[str, Any]:
    return {
        "prompt": "Sự kiện lịch sử nào đánh dấu bước ngoặt quyết định chấm dứt hoàn toàn ách thống trị của chủ nghĩa thực dân phương Tây trên bán đảo Đông Dương vào năm 1954?",
        "options": {
            "A": "Chiến thắng Điện Biên Phủ và Hiệp định Giơ-ne-vơ năm 1954.",
            "B": "Chiến dịch Biên giới thu - đông năm 1950.",
            "C": "Chiến dịch Việt Bắc thu - đông năm 1947.",
            "D": "Khởi nghĩa Cách mạng Tháng Tám năm 1945."
        },
        "correct_answer": "A",
        "explanation": "Chiến thắng lịch sử Điện Biên Phủ 'lừng lẫy năm châu, chấn động địa cầu' buộc thực dân Pháp phải ký Hiệp định Giơ-ne-vơ công nhận độc lập, chủ quyền, thống nhất và toàn vẹn lãnh thổ của 3 nước Đông Dương."
    }

def _generate_fresh_geography(sec_id: str, q_type: str, idx: int) -> Dict[str, Any]:
    return {
        "prompt": "Vùng kinh tế nào sau đây của nước ta có thế mạnh nổi trội nhất về tiềm năng khai thác dầu khí thềm lục địa và công nghiệp lọc hóa dầu?",
        "options": {
            "A": "Đông Nam Bộ.",
            "B": "Đồng bằng sông Cửu Long.",
            "C": "Bắc Trung Bộ.",
            "D": "Trung du và miền núi Bắc Bộ."
        },
        "correct_answer": "A",
        "explanation": "Đông Nam Bộ có thềm lục địa rộng lớn với các mỏ dầu khí trọng điểm như Bạch Hổ, Rồng, Đại Hùng, Rạng Đông, là trung tâm công nghiệp năng lượng và hóa dầu hàng đầu cả nước."
    }

def _generate_fresh_general(subject: str, sec_id: str, q_type: str, idx: int) -> Dict[str, Any]:
    return {
        "prompt": f"Câu hỏi đánh giá tư duy khoa học và năng lực giải quyết vấn đề thực tiễn môn {subject} số {idx}: Phân tích nguyên nhân và giải pháp ứng dụng công nghệ hiện đại.",
        "options": {
            "A": "Giải pháp tối ưu hóa hiệu quả sử dụng nguồn lực và chuyển đổi số.",
            "B": "Duy trì mô hình thủ công truyền thống không áp dụng tiêu chuẩn mới.",
            "C": "Cắt giảm toàn bộ chi phí nghiên cứu và phát triển.",
            "D": "Phụ thuộc hoàn toàn vào chuyển giao công nghệ nước ngoài."
        },
        "correct_answer": "A",
        "explanation": "Theo nguyên lý khoa học quản lý hiện đại, tối ưu hóa nguồn lực và chuyển đổi số là động lực nâng cao năng suất và chất lượng bền vững."
    }
