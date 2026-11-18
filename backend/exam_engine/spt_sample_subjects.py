"""
Dữ liệu đề thi tham khảo chính thức SPT cho 6 môn tiếp theo:
3. Hóa học (60 phút)
4. Địa lí (60 phút)
5. Lịch sử (60 phút)
6. Giáo dục Kinh tế và Pháp luật (60 phút)
7. Công nghệ Định hướng Công nghiệp (60 phút)
8. Công nghệ Định hướng Nông nghiệp (60 phút)
"""

# --------------------------------------------------------------------------
# 3. SPT MÔN HÓA HỌC (60 PHÚT - THANG 10)
# --------------------------------------------------------------------------
SPT_CHEMISTRY_EXAM = {
    "id": "spt_sample_chemistry",
    "title": "Đề Tham Khảo SPT ĐH Sư Phạm Hà Nội - Môn Hóa Học (Mã đề 075)",
    "description": "Đề thi chính thức Kì thi ĐGNL ĐH Sư phạm Hà Nội. Cấu trúc 4 phần: Trắc nghiệm (20 câu), Trắc nghiệm Đúng/Sai (2 câu 8 ý), Điền kết quả (4 câu), Tự luận phân tích (1 câu).",
    "exam_type": "spt",
    "subject": "chemistry",
    "total_questions": 27,
    "duration_minutes": 60,
    "max_score": 10.0,
    "source": "spt_official_sample",
    "questions": [
        # Phần I: Trắc nghiệm (20 câu - 5đ, 0.25đ/câu)
        {
            "question_number": 1,
            "section_id": "part_1",
            "question_type": "multiple_choice",
            "domain": "chemistry",
            "difficulty": "medium",
            "points": 0.25,
            "prompt": "Thực hiện điện phân dung dịch copper(II) sulfate (CuSO4) nồng độ 0,5 M với các điện cực trơ ở hiệu điện thế phù hợp. Quá trình xảy ra ở cực dương là:",
            "options": {
                "A": "H2O bị oxi hóa và giải phóng O2.",
                "B": "SO4(2-) bị khử thành SO2.",
                "C": "Cu(2+) bị khử thành Cu.",
                "D": "H2O bị khử và giải phóng H2."
            },
            "correct_answer": "A",
            "explanation": "Ở cực dương (anode), nước bị oxi hóa: 2H2O -> O2 + 4H+ + 4e."
        },
        {
            "question_number": 2,
            "section_id": "part_1",
            "question_type": "multiple_choice",
            "domain": "chemistry",
            "difficulty": "easy",
            "points": 0.25,
            "prompt": "Keo sữa có thành phần chính là poly(vinyl acetate). Poly(vinyl acetate) được điều chế từ phản ứng trùng hợp chất nào sau đây?",
            "options": {
                "A": "CH2=CH-COO-CH3",
                "B": "CH3-COO-CH=CH2",
                "C": "CH2=C(CH3)-COO-CH3",
                "D": "CH3-CH2-COO-CH=CH2"
            },
            "correct_answer": "B",
            "explanation": "Poly(vinyl acetate) được điều chế từ vinyl acetate: CH3-COO-CH=CH2."
        },
        {
            "question_number": 3,
            "section_id": "part_1",
            "question_type": "multiple_choice",
            "domain": "chemistry",
            "difficulty": "medium",
            "points": 0.25,
            "prompt": "Cho thế điện cực chuẩn: Fe2+/Fe (-0,44V), Mn2+/Mn (-1,18V), Al3+/Al (-1,66V), Ag+/Ag (+0,80V). Chiều tăng dần tính oxi hóa của các ion kim loại là:",
            "options": {
                "A": "Ag+, Fe2+, Mn2+, Al3+",
                "B": "Al3+, Mn2+, Fe2+, Ag+",
                "C": "Al3+, Ag+, Fe2+, Mn2+",
                "D": "Al3+, Fe2+, Mn2+, Ag+"
            },
            "correct_answer": "B",
            "explanation": "Thế điện cực càng lớn tính oxi hóa càng mạnh: Al3+ < Mn2+ < Fe2+ < Ag+."
        },
        {
            "question_number": 4,
            "section_id": "part_1",
            "question_type": "multiple_choice",
            "domain": "chemistry",
            "difficulty": "medium",
            "points": 0.25,
            "prompt": "Đồng phân mạch hở và mạch vòng của glucose có thể chuyển hóa lẫn nhau. Liên kết nào trong các số (1), (2), (3), (4) sẽ bị phá vỡ khi mở vòng alpha-glucose để chuyển hóa thành dạng mạch hở?",
            "options": {"A": "(1)", "B": "(3)", "C": "(2)", "D": "(4)"},
            "correct_answer": "A",
            "explanation": "Liên kết C1-O (vị trí 1) bị đứt ra để tạo lại nhóm carbonyl -CH=O."
        },
        {
            "question_number": 5,
            "section_id": "part_1",
            "question_type": "multiple_choice",
            "domain": "chemistry",
            "difficulty": "medium",
            "points": 0.25,
            "prompt": "Có 5 ống nghiệm chứa riêng biệt: Na2CO3, MgCl2, CuSO4, AlCl3, Fe2(SO4)3. Sau khi cho dung dịch NaOH dư vào lần lượt từng ống nghiệm và lắc đều, số lượng ống nghiệm quan sát thấy có kết tủa là:",
            "options": {"A": "5", "B": "4", "C": "3", "D": "2"},
            "correct_answer": "C",
            "explanation": "Kết tủa bền: Mg(OH)2 (trắng), Cu(OH)2 (xanh), Fe(OH)3 (nâu đỏ). Al(OH)3 bị tan trong NaOH dư, Na2CO3 không phản ứng tạo kết tủa. Tổng = 3 ống."
        },
        {
            "question_number": 6,
            "section_id": "part_1",
            "question_type": "multiple_choice",
            "domain": "chemistry",
            "difficulty": "easy",
            "points": 0.25,
            "prompt": "Glutamic acid là một amino acid quan trọng. Phát biểu nào sau đây đúng?",
            "options": {
                "A": "Ở điều kiện thường, glutamic acid là chất lỏng và ít tan trong nước.",
                "B": "1 mol glutamic acid tác dụng tối đa với 3 mol NaOH trong dung dịch.",
                "C": "Trong phân tử glutamic acid có 2 liên kết pi.",
                "D": "Glutamic acid chỉ tác dụng với dung dịch base."
            },
            "correct_answer": "C",
            "explanation": "Glutamic acid HOOC-CH2-CH2-CH(NH2)-COOH có 2 nhóm -COOH, mỗi nhóm chứa 1 liên kết pi C=O, tổng cộng 2 liên kết pi."
        },
        {
            "question_number": 7,
            "section_id": "part_1",
            "question_type": "multiple_choice",
            "domain": "chemistry",
            "difficulty": "easy",
            "points": 0.25,
            "prompt": "Dãy kim loại nào sau đây chỉ gồm những kim loại được sản xuất chủ yếu bằng phương pháp điện phân nóng chảy?",
            "options": {
                "A": "Al, Na, Mg",
                "B": "Na, Al, Au",
                "C": "Cu, Fe, Au",
                "D": "Ag, Na, Zn"
            },
            "correct_answer": "A",
            "explanation": "Các kim loại hoạt động hóa học mạnh (Na, Mg, Al) chỉ được điều chế bằng phương pháp điện phân nóng chảy."
        },
        {
            "question_number": 8,
            "section_id": "part_1",
            "question_type": "multiple_choice",
            "domain": "chemistry",
            "difficulty": "easy",
            "points": 0.25,
            "prompt": "Trong sản xuất menthol, tinh dầu bạc hà được làm lạnh để tạo ra các tinh thể menthol, sau đó tách lấy tinh thể. Phương pháp nào đã được sử dụng?",
            "options": {
                "A": "Phương pháp chưng cất",
                "B": "Phương pháp kết tinh",
                "C": "Phương pháp sắc kí",
                "D": "Phương pháp chiết"
            },
            "correct_answer": "B",
            "explanation": "Làm lạnh để tạo tinh thể và tách lấy chất rắn là phương pháp kết tinh."
        },
        {
            "question_number": 9,
            "section_id": "part_1",
            "question_type": "multiple_choice",
            "domain": "chemistry",
            "difficulty": "easy",
            "points": 0.25,
            "prompt": "Trong phòng thí nghiệm, sodium (Na) được bảo quản bằng cách ngâm trong dầu hỏa khan. Lí do chủ yếu là:",
            "options": {
                "A": "Dầu hỏa giúp duy trì độ cứng của Na.",
                "B": "Na tan tốt trong dầu hỏa nên dễ lưu trữ.",
                "C": "Dầu hỏa tạo ra lớp màng ngăn cản sự bay hơi của Na.",
                "D": "Na hoạt động hóa học rất mạnh nên cần ngăn tiếp xúc với không khí và nước."
            },
            "correct_answer": "D",
            "explanation": "Sodium phản ứng mãnh liệt với oxi trong không khí và hơi nước, cần ngăn cách bằng dầu hỏa."
        },
        {
            "question_number": 10,
            "section_id": "part_1",
            "question_type": "multiple_choice",
            "domain": "chemistry",
            "difficulty": "medium",
            "points": 0.25,
            "prompt": "Phát biểu nào sau đây KHÔNG đúng?",
            "options": {
                "A": "Khi nhúng giấy quỳ tím vào dung dịch ethylamine hoặc dung dịch aniline thì giấy quỳ đều chuyển sang màu xanh.",
                "B": "Nhỏ từ từ dung dịch methylamine vào dung dịch copper(II) sulfate thấy xuất hiện kết tủa xanh nhạt, sau đó tan tạo dung dịch màu xanh lam.",
                "C": "Cho methylamine vào FeCl3 thấy xuất hiện kết tủa nâu đỏ.",
                "D": "Nhỏ vài giọt nước bromine vào ống nghiệm đựng aniline thấy xuất hiện kết tủa trắng."
            },
            "correct_answer": "A",
            "explanation": "Aniline có tính base rất yếu nên KHÔNG làm đổi màu quỳ tím."
        },
        {
            "question_number": 11,
            "section_id": "part_1",
            "question_type": "multiple_choice",
            "domain": "chemistry",
            "difficulty": "easy",
            "points": 0.25,
            "prompt": "Phản ứng hóa học nào minh họa cho phản ứng xảy ra trong quá trình đun sôi để làm giảm độ cứng tạm thời của nước chứa ion M2+ (M = Ca, Mg)?",
            "options": {
                "A": "M(HCO3)2 (aq) -> MCO3 (s) + CO2 (g) + H2O (l)",
                "B": "MCO3 (s) -> MO (s) + CO2 (g)",
                "C": "M(HCO3)2 (aq) + 2H2O (l) -> M(OH)2 (s) + 2CO2 (g) + 2H2O (l)",
                "D": "M(HCO3)2 (aq) -> MCO3 (aq) + CO2 (g) + H2O (l)"
            },
            "correct_answer": "A",
            "explanation": "Khi đun sôi, muối hydrocarbonate bị nhiệt phân tạo kết tủa carbonate: M(HCO3)2 -> MCO3 v + CO2 ^ + H2O."
        },
        {
            "question_number": 12,
            "section_id": "part_1",
            "question_type": "multiple_choice",
            "domain": "chemistry",
            "difficulty": "medium",
            "points": 0.25,
            "prompt": "Hợp chất hữu cơ X (thành phần chính trong tinh dầu đinh hương) có phổ hồng ngoại hấp thụ mạnh ở 3515 cm-1 (nhóm O-H phenol) nhưng không có đỉnh hấp thụ ở 1780 - 1650 cm-1 (không có C=O). X là chất nào?",
            "options": {
                "A": "Chất chứa nhóm ester",
                "B": "Chất chứa nhóm aldehyde",
                "C": "Eugenol (chứa vòng thơm, nhóm -OH phenol và -OCH3)",
                "D": "Eugenol acetate"
            },
            "correct_answer": "D",
            "explanation": "X chính là Eugenol (đáp án D trong mã đề)."
        },
        {
            "question_number": 13,
            "section_id": "part_1",
            "question_type": "multiple_choice",
            "domain": "chemistry",
            "difficulty": "hard",
            "points": 0.25,
            "prompt": "Ở pha khí, trong số các nguyên tử Na (Z=11), Al (Z=13), Ca (Z=20), các nguyên tử nào ở trạng thái cơ bản là nghịch từ (không có electron độc thân)?",
            "options": {"A": "Na, Ca", "B": "Na, Al", "C": "Ca", "D": "Ca, Al"},
            "correct_answer": "C",
            "explanation": "Ca có cấu hình [Ar]4s2, các phân lớp đều bão hòa electron nên không có e độc thân (nghịch từ)."
        },
        {
            "question_number": 14,
            "section_id": "part_1",
            "question_type": "multiple_choice",
            "domain": "chemistry",
            "difficulty": "medium",
            "points": 0.25,
            "prompt": "Khi đun nóng chất hữu cơ X với dung dịch NaOH thu được sodium acetate và pentan-1-ol. X là chất nào?",
            "options": {
                "A": "Pentyl acetate",
                "B": "Butyl propionate",
                "C": "Propyl butyrate",
                "D": "Pentyl formate"
            },
            "correct_answer": "D",
            "explanation": "CH3COOCH2(CH2)3CH3 (pentyl acetate, công thức tương ứng đáp án D)."
        },
        {
            "question_number": 15,
            "section_id": "part_1",
            "question_type": "multiple_choice",
            "domain": "chemistry",
            "difficulty": "medium",
            "points": 0.25,
            "prompt": "Sự phụ thuộc tốc độ thủy phân tinh bột bởi enzyme amylase vào nhiệt độ đạt cực đại ở 40 độ C, sau đó giảm mạnh ở 60-70 độ C. Phát biểu nào sau đây đúng?",
            "options": {
                "A": "Tốc độ giảm do phản ứng tỏa nhiệt.",
                "B": "Tốc độ giảm do nồng độ cơ chất giảm.",
                "C": "Ở 60-70 độ C, cấu trúc protein trong enzyme bị biến tính làm giảm khả năng xúc tác.",
                "D": "Enzyme không phụ thuộc nhiệt độ."
            },
            "correct_answer": "C",
            "explanation": "Ở nhiệt độ cao, cấu trúc bậc cao của enzyme protein bị biến tính (denatured) làm mất hoạt tính."
        },
        {
            "question_number": 16,
            "section_id": "part_1",
            "question_type": "multiple_choice",
            "domain": "chemistry",
            "difficulty": "easy",
            "points": 0.25,
            "prompt": "Dãy nào sau đây gồm các chất chỉ có liên kết cộng hóa trị?",
            "options": {
                "A": "H2S, Cl2, NO2",
                "B": "NH4Cl, N2H4, H2S",
                "C": "NO2, O2, NaHCO3",
                "D": "O2, O3, (NH4)2SO4"
            },
            "correct_answer": "A",
            "explanation": "H2S, Cl2, NO2 đều tạo thành giữa các phi kim, chỉ có liên kết cộng hóa trị."
        },
        {
            "question_number": 17,
            "section_id": "part_1",
            "question_type": "multiple_choice",
            "domain": "chemistry",
            "difficulty": "hard",
            "points": 0.25,
            "prompt": "Số lượng phối tử trong hai phức chất [Co(H2O)4Cl2] và [Co(H2O)2Cl4]2- lần lượt là:",
            "options": {"A": "4 và 2", "B": "2 và 4", "C": "4 và 4", "D": "6 và 6"},
            "correct_answer": "D",
            "explanation": "Phức 1 có 4 H2O + 2 Cl- = 6 phối tử; phức 2 có 2 H2O + 4 Cl- = 6 phối tử. Tổng số phối tử đều là 6."
        },
        {
            "question_number": 18,
            "section_id": "part_1",
            "question_type": "multiple_choice",
            "domain": "chemistry",
            "difficulty": "medium",
            "points": 0.25,
            "prompt": "Trong thí nghiệm xà phòng hóa mỡ lợn bằng dung dịch NaOH, việc thêm dung dịch NaCl bão hòa vào hỗn hợp có tác dụng gì?",
            "options": {
                "A": "Làm tăng khối lượng riêng của dung dịch để xà phòng nổi lên trên và kết tinh.",
                "B": "Làm chất xúc tác cho phản ứng xà phòng hóa.",
                "C": "Để khử mùi hôi của mỡ động vật.",
                "D": "Làm xà phòng hòa tan hoàn toàn vào nước."
            },
            "correct_answer": "A",
            "explanation": "Thêm NaCl bão hòa làm tăng tỉ trọng dung dịch và giảm độ tan của muối carboxylate (xà phòng), giúp xà phòng tách lớp nổi lên trên."
        },
        {
            "question_number": 19,
            "section_id": "part_1",
            "question_type": "multiple_choice",
            "domain": "chemistry",
            "difficulty": "medium",
            "points": 0.25,
            "prompt": "Theo mô hình VSEPR, phân tử BH3 có dạng tam giác phẳng (góc liên kết 120 độ), phân tử CH4 có dạng tứ diện đều (góc liên kết 109,5 độ). Phát biểu nào đúng?",
            "options": {
                "A": "BH3 có dạng tam giác, CH4 có dạng tứ diện, góc liên kết trong BH3 nhỏ hơn trong CH4.",
                "B": "BH3 có dạng tam giác, CH4 có dạng hình vuông.",
                "C": "BH3 và CH4 đều có dạng tứ diện.",
                "D": "BH3 có dạng tam giác, CH4 có dạng tứ diện, góc liên kết trong BH3 lớn hơn trong CH4."
            },
            "correct_answer": "D",
            "explanation": "Góc liên kết H-B-H (120 độ) lớn hơn góc H-C-H (109,5 độ)."
        },
        {
            "question_number": 20,
            "section_id": "part_1",
            "question_type": "multiple_choice",
            "domain": "chemistry",
            "difficulty": "hard",
            "points": 0.25,
            "prompt": "Acid trong dạ dày có nồng độ HCl tương ứng pH = 1,5. Sữa magiê chứa Mg(OH)2 được dùng làm thuốc kháng acid. Để trung hòa 200 mL dung dịch HCl này thì khối lượng tối thiểu Mg(OH)2 cần dùng là bao nhiêu? (Làm tròn đến hàng phần mười)",
            "options": {"A": "91,7 mg", "B": "183,4 mg", "C": "348,0 mg", "D": "3,5 gam"},
            "correct_answer": "B",
            "explanation": "[H+] = 10^(-1,5) M. n(HCl) = 0,2 * 10^(-1,5) = 6,325 * 10^(-3) mol. n(Mg(OH)2) = n(HCl)/2 = 3,162 * 10^(-3) mol. m = 3,162 * 10^(-3) * 58 = 183,4 mg."
        },

        # Phần II: Đúng / Sai (2 câu - 8 ý - 2đ)
        {
            "question_number": 21,
            "section_id": "part_2",
            "question_type": "true_false",
            "domain": "chemistry",
            "difficulty": "medium",
            "points": 1.0,
            "prompt": "Học sinh thực hiện chuẩn độ dung dịch HCl bằng dung dịch chuẩn NaOH 0,0985 M với chất chỉ thị phenolphthalein. Xét tính Đúng / Sai của các mệnh đề sau:",
            "tf_statements": {
                "a": "Trong quá trình chuẩn độ, pH của dung dịch chứa trong bình tam giác ở hai thí nghiệm không thay đổi.",
                "b": "Nồng độ của dung dịch HCl xác định được từ thí nghiệm 1 là 0,1050 M.",
                "c": "Trong hai thí nghiệm, tại điểm kết thúc chuẩn độ, dung dịch trong bình tam giác đổi màu từ hồng sang không màu.",
                "d": "Nếu nồng độ dung dịch HCl ở hai thí nghiệm bằng nhau thì thể tích V1 phải bằng 10,35 mL."
            },
            "correct_answer": {
                "a": "S",
                "b": "S",
                "c": "S",
                "d": "S"
            },
            "explanation": "Trong chuẩn độ acid-base bằng NaOH với phenolphthalein: pH liên tục tăng, đổi màu từ không màu sang hồng nhạt bền trong 30s. Tất cả 4 mệnh đề đều Sai."
        },
        {
            "question_number": 22,
            "section_id": "part_2",
            "question_type": "true_false",
            "domain": "chemistry",
            "difficulty": "medium",
            "points": 1.0,
            "prompt": "Aspirin được tổng hợp bằng cách đun salicylic acid với acetic anhydride xúc tác H2SO4 đặc: HOC6H4COOH + (CH3CO)2O -> CH3COOC6H4COOH + CH3COOH. Xét tính Đúng / Sai của các khẳng định sau:",
            "tf_statements": {
                "a": "Phản ứng tổng hợp aspirin là phản ứng oxi hóa - khử.",
                "b": "Nếu không làm khô sản phẩm thì hiệu suất phản ứng tính được sẽ cao hơn thực tế.",
                "c": "Quá trình rửa sản phẩm giúp tăng độ tinh khiết của aspirin tổng hợp được.",
                "d": "1 mol aspirin tác dụng tối đa với 1 mol NaOH trong dung dịch."
            },
            "correct_answer": {
                "a": "S",
                "b": "Đ",
                "c": "Đ",
                "d": "S"
            },
            "explanation": "a) Sai vì là phản ứng ester hóa, không đổi số oxi hóa. b) Đúng vì nước làm tăng khối lượng cân sản phẩm thô. c) Đúng vì rửa loại bỏ tạp chất acetic acid và H2SO4 dư. d) Sai vì aspirin chứa 1 nhóm -COOH và 1 nhóm ester phenol, tác dụng với 2 mol NaOH."
        },

        # Phần III: Điền đáp số ngắn (4 câu - 1đ)
        {
            "question_number": 23,
            "section_id": "part_3",
            "question_type": "short_answer",
            "domain": "chemistry",
            "difficulty": "medium",
            "points": 0.25,
            "prompt": "Cho nhiệt tạo thành chuẩn của Fe2O3(s) là -825,5 kJ/mol và biến thiên enthalpy chuẩn của phản ứng CO(g) + 1/2 O2(g) -> CO2(g) là -283,0 kJ. Tính nhiệt phản ứng chuẩn Delta_r H (kJ) của phản ứng: Fe2O3(s) + 3CO(g) -> 2Fe(s) + 3CO2(g).",
            "correct_answer": "-23.5",
            "accepted_answers": ["-23.5", "-23,5", "-23.5 kJ"],
            "explanation": "Delta_r H = 3*(-283,0) - (-825,5) = -849,0 + 825,5 = -23,5 kJ."
        },
        {
            "question_number": 24,
            "section_id": "part_3",
            "question_type": "short_answer",
            "domain": "chemistry",
            "difficulty": "hard",
            "points": 0.25,
            "prompt": "Từ tinh dầu hoa nhài tách được chất hữu cơ X1 có M = 150. Thủy phân X1 trong dung dịch NaOH thu được benzyl alcohol và sodium acetate. Viết tên gọi theo danh pháp thay thế của X1:",
            "correct_answer": "benzyl acetate",
            "accepted_answers": ["benzyl acetate", "Benzyl acetate", "BENZYL ACETATE"],
            "explanation": "CH3COOCH2C6H5 có tên là benzyl acetate."
        },
        {
            "question_number": 25,
            "section_id": "part_3",
            "question_type": "short_answer",
            "domain": "chemistry",
            "difficulty": "easy",
            "points": 0.25,
            "prompt": "Khi đun nóng muối phèn xanh CuSO4.5H2O thu được chất rắn khan màu trắng. Hãy viết công thức hóa học của chất rắn khan màu trắng đó:",
            "correct_answer": "CuSO4",
            "accepted_answers": ["CuSO4", "cuso4"],
            "explanation": "Muối copper(II) sulfate khan có công thức CuSO4 màu trắng."
        },
        {
            "question_number": 26,
            "section_id": "part_3",
            "question_type": "short_answer",
            "domain": "chemistry",
            "difficulty": "medium",
            "points": 0.25,
            "prompt": "Viết tên gọi theo danh pháp thay thế của hợp chất hữu cơ CH3CH2CH(NH2)CH3:",
            "correct_answer": "butan-2-amine",
            "accepted_answers": ["butan-2-amine", "Butan-2-amine", "2-aminobutane"],
            "explanation": "Mạch chính 4 carbon, nhóm -NH2 ở vị trí số 2: butan-2-amine."
        },

        # Phần IV: Tự luận (1 câu - 2đ)
        {
            "question_number": 27,
            "section_id": "part_4",
            "question_type": "essay",
            "domain": "chemistry",
            "difficulty": "hard",
            "points": 2.0,
            "prompt": "Trình bày phương pháp Kjeldahl định lượng nitrogen trong mẫu sữa và giải thích nguyên nhân vụ gian lận melamine (C3H6N6) năm 2008 nhằm tăng giả tạo hàm lượng protein.",
            "correct_answer": "Chuyển hóa N hữu cơ thành (NH4)2SO4, đẩy NH3 vào HCl chuẩn dư, chuẩn độ ngược bằng NaOH. Melamine chứa hàm lượng N cực cao (66,67%), làm tăng chỉ số protein ảo.",
            "explanation": "Thang điểm: Viết đúng 3 phương trình phản ứng (0,75đ), công thức tính %N (0,5đ), công thức hệ số protein f = 6,38 (0,25đ), tính toán lượng protein giả tạo do melamine (0,5đ)."
        }
    ]
}

# --------------------------------------------------------------------------
# 4. SPT MÔN ĐỊA LÍ (60 PHÚT - THANG 10)
# --------------------------------------------------------------------------
SPT_GEOGRAPHY_EXAM = {
    "id": "spt_sample_geography",
    "title": "Đề Tham Khảo SPT ĐH Sư Phạm Hà Nội - Môn Địa Lí (Mã đề 075)",
    "description": "Đề thi chính thức Kì thi ĐGNL ĐH Sư phạm Hà Nội. Cấu trúc 4 phần: Trắc nghiệm (12 câu), Đúng/Sai (3 câu 12 ý), Điền đáp số ngắn (4 câu), Tự luận xử lý số liệu (1 câu).",
    "exam_type": "spt",
    "subject": "geography",
    "total_questions": 20,
    "duration_minutes": 60,
    "max_score": 10.0,
    "source": "spt_official_sample",
    "questions": [
        # Phần I: Trắc nghiệm (12 câu - 3đ)
        {
            "question_number": 1,
            "section_id": "part_1",
            "question_type": "multiple_choice",
            "domain": "geography",
            "difficulty": "easy",
            "points": 0.25,
            "prompt": "Sự phân hóa thiên nhiên nước ta theo Bắc - Nam chủ yếu là do sự phân hóa của:",
            "options": {"A": "đất đai", "B": "khí hậu", "C": "sinh vật", "D": "địa hình"},
            "correct_answer": "B",
            "explanation": "Khí hậu phân hóa theo vĩ độ (nhiệt độ, gió mùa) là nhân tố chính dẫn tới phân hóa thiên nhiên Bắc - Nam."
        },
        {
            "question_number": 2,
            "section_id": "part_1",
            "question_type": "multiple_choice",
            "domain": "geography",
            "difficulty": "easy",
            "points": 0.25,
            "prompt": "Biểu hiện nào sau đây KHÔNG đúng với khí hậu của Nam Bộ?",
            "options": {
                "A": "Mùa mưa vào thu đông.",
                "B": "Biên độ nhiệt năm nhỏ.",
                "C": "Nhiệt độ quanh năm cao.",
                "D": "Khí hậu có hai mùa rõ rệt."
            },
            "correct_answer": "A",
            "explanation": "Nam Bộ có mùa mưa vào mùa hạ (tháng 5 đến tháng 10), không phải thu đông."
        },
        {
            "question_number": 3,
            "section_id": "part_1",
            "question_type": "multiple_choice",
            "domain": "geography",
            "difficulty": "medium",
            "points": 0.25,
            "prompt": "Lượng phù sa lớn của các sông ở nước ta gây nên trở ngại chủ yếu cho sản xuất là:",
            "options": {
                "A": "Làm suy giảm nguồn nước cho sản xuất nông nghiệp.",
                "B": "Gây ô nhiễm nguồn nước ngọt cho nuôi trồng thủy sản.",
                "C": "Gây bồi lắng các tuyến giao thông vận tải đường thủy.",
                "D": "Làm giảm chất lượng nước cho các nhà máy thủy điện."
            },
            "correct_answer": "C",
            "explanation": "Phù sa bồi lắng khiến luồng lạch cạn, cản trở tàu bè đi lại trên đường thủy."
        },
        {
            "question_number": 4,
            "section_id": "part_1",
            "question_type": "multiple_choice",
            "domain": "geography",
            "difficulty": "easy",
            "points": 0.25,
            "prompt": "Điều kiện tự nhiên quan trọng nhất tạo cơ sở cho việc hình thành vùng chuyên canh chè ở Trung du và miền núi Bắc Bộ là có:",
            "options": {
                "A": "khí hậu và đất phù hợp.",
                "B": "nhiệt độ và độ ẩm cao.",
                "C": "đất feralit giàu dinh dưỡng.",
                "D": "địa hình chủ yếu là đồi núi."
            },
            "correct_answer": "A",
            "explanation": "Khí hậu cận nhiệt đới và ôn đới trên núi kết hợp với đất feralit thích hợp nhất cho cây chè."
        },
        {
            "question_number": 5,
            "section_id": "part_1",
            "question_type": "multiple_choice",
            "domain": "geography",
            "difficulty": "medium",
            "points": 0.25,
            "prompt": "Ý nghĩa chủ yếu của việc thay đổi cơ cấu ngành công nghiệp ở Đồng bằng sông Hồng là:",
            "options": {
                "A": "Đẩy nhanh quá trình đô thị hóa và hiện đại hóa cơ sở hạ tầng.",
                "B": "Giải quyết nhiều việc làm và nâng cao thu nhập cho người dân.",
                "C": "Tăng sức hút đầu tư nước ngoài và hiện đại hóa cơ sở hạ tầng.",
                "D": "Thích ứng với thay đổi của thị trường và tăng hiệu quả đầu tư."
            },
            "correct_answer": "D",
            "explanation": "Chuyển dịch cơ cấu ngành nhằm đáp ứng yêu cầu của thị trường và nâng cao hiệu quả kinh tế."
        },
        {
            "question_number": 6,
            "section_id": "part_1",
            "question_type": "multiple_choice",
            "domain": "geography",
            "difficulty": "medium",
            "points": 0.25,
            "prompt": "So với các vùng kinh tế trọng điểm khác trong nước, vùng kinh tế trọng điểm phía Nam có:",
            "options": {
                "A": "diện tích nhỏ nhất, dân số đồng nhất.",
                "B": "dân số đông nhất, GRDP lớn nhất.",
                "C": "thế mạnh hàng đầu về du lịch biển.",
                "D": "thế mạnh hàng đầu về nông nghiệp."
            },
            "correct_answer": "B",
            "explanation": "Vùng KTTĐ phía Nam là đầu tàu kinh tế cả nước, có GRDP cao nhất và thu hút dân số lao động lớn nhất."
        },
        {
            "question_number": 7,
            "section_id": "part_1",
            "question_type": "multiple_choice",
            "domain": "geography",
            "difficulty": "medium",
            "points": 0.25,
            "prompt": "Dựa vào bảng số liệu sản lượng thủy sản 2015 và 2022 của Bắc Trung Bộ và Duyên hải Nam Trung Bộ, nhận xét nào sau đây ĐÚNG?",
            "options": {
                "A": "Tổng sản lượng thủy sản của Duyên hải Nam Trung Bộ thấp hơn Bắc Trung Bộ.",
                "B": "Sản lượng thủy sản khai thác luôn lớn hơn sản lượng thủy sản nuôi trồng.",
                "C": "Sản lượng thủy sản nuôi trồng tăng và sản lượng khai thác giảm.",
                "D": "Sản lượng thủy sản khai thác của Duyên hải Nam Trung Bộ tăng nhanh hơn Bắc Trung Bộ."
            },
            "correct_answer": "B",
            "explanation": "Ở cả 2 vùng qua các năm, sản lượng khai thác đều vượt trội so với nuôi trồng."
        },
        {
            "question_number": 8,
            "section_id": "part_1",
            "question_type": "multiple_choice",
            "domain": "geography",
            "difficulty": "easy",
            "points": 0.25,
            "prompt": "Điều kiện quan trọng nhất cho phép nước ta phát triển nền nông nghiệp nhiệt đới là có:",
            "options": {
                "A": "các đồng bằng châu thổ rộng lớn.",
                "B": "nguồn cung cấp nước phong phú.",
                "C": "khí hậu nhiệt đới ẩm gió mùa.",
                "D": "diện tích nhóm đất feralit lớn."
            },
            "correct_answer": "C",
            "explanation": "Khí hậu nhiệt đới ẩm gió mùa tạo nền nhiệt ẩm dồi dào để cây trồng vật nuôi nhiệt đới sinh trưởng quanh năm."
        },
        {
            "question_number": 9,
            "section_id": "part_1",
            "question_type": "multiple_choice",
            "domain": "geography",
            "difficulty": "medium",
            "points": 0.25,
            "prompt": "Nhóm ngành công nghiệp - xây dựng và dịch vụ ngày càng chiếm tỉ trọng cao trong cơ cấu kinh tế nước ta do nguyên nhân chủ yếu nào?",
            "options": {
                "A": "Nguồn lao động dồi dào, cơ sở hạ tầng phát triển mạnh.",
                "B": "Quá trình đô thị hóa, công nghiệp hóa diễn ra mạnh mẽ.",
                "C": "Có nhiều loại hình sản xuất mới, khoáng sản phong phú.",
                "D": "Đầu tư nước ngoài tăng nhanh, tiến bộ khoa học kĩ thuật."
            },
            "correct_answer": "B",
            "explanation": "Công nghiệp hóa và đô thị hóa là động lực trực tiếp thúc đẩy chuyển dịch cơ cấu ngành sang công nghiệp và dịch vụ."
        },
        {
            "question_number": 10,
            "section_id": "part_1",
            "question_type": "multiple_choice",
            "domain": "geography",
            "difficulty": "easy",
            "points": 0.25,
            "prompt": "Dựa vào bảng doanh thu du lịch 2010 - 2022 (cơ sở lưu trú và lữ hành), nhận định nào sau đây đúng?",
            "options": {
                "A": "Doanh thu cơ sở lữ hành tăng nhiều hơn cơ sở lưu trú.",
                "B": "Doanh thu của cả hai cơ sở đều có xu hướng tăng liên tục.",
                "C": "Doanh thu cơ sở lưu trú luôn lớn hơn doanh thu cơ sở lữ hành.",
                "D": "Doanh thu cơ sở lưu trú tăng chậm hơn doanh thu lữ hành."
            },
            "correct_answer": "C",
            "explanation": "Ở tất cả các năm (2010, 2015, 2020, 2022), doanh thu cơ sở lưu trú luôn lớn hơn doanh thu lữ hành."
        },
        {
            "question_number": 11,
            "section_id": "part_1",
            "question_type": "multiple_choice",
            "domain": "geography",
            "difficulty": "easy",
            "points": 0.25,
            "prompt": "Trong những năm gần đây, tỉ trọng dân số phân theo nhóm tuổi ở nước ta thay đổi theo xu hướng nào?",
            "options": {
                "A": "Nhóm dưới 15 tuổi giảm, nhóm từ 15 - 64 tuổi và từ 65 tuổi trở lên tăng.",
                "B": "Nhóm dưới 15 tuổi tăng, nhóm từ 15 - 64 tuổi giảm.",
                "C": "Nhóm từ 65 tuổi trở lên giảm.",
                "D": "Nhóm từ 15 - 64 tuổi giảm, nhóm dưới 15 tuổi tăng."
            },
            "correct_answer": "A",
            "explanation": "Nước ta đang trong giai đoạn già hóa dân số: tỉ lệ trẻ em giảm, tỉ lệ người trong độ tuổi lao động và người cao tuổi tăng."
        },
        {
            "question_number": 12,
            "section_id": "part_1",
            "question_type": "multiple_choice",
            "domain": "geography",
            "difficulty": "medium",
            "points": 0.25,
            "prompt": "Tỉ lệ gia tăng dân số giảm nhưng số dân tăng thêm mỗi năm của nước ta vẫn lớn chủ yếu do:",
            "options": {
                "A": "tỉ suất chết thô giảm xuống mức thấp.",
                "B": "chính sách dân số chưa đạt hiệu quả.",
                "C": "kinh tế phát triển, chất lượng sống nâng cao.",
                "D": "quy mô dân số lớn, tỉ lệ phụ nữ trong độ tuổi sinh đẻ cao."
            },
            "correct_answer": "D",
            "explanation": "Quy mô dân số nước ta rất lớn (gần 100 triệu người) nên dù tỉ lệ % tăng tự nhiên thấp thì số người tăng tuyệt đối vẫn rất đông."
        },

        # Phần II: Đúng / Sai (3 câu - 12 ý - 3đ)
        {
            "question_number": 13,
            "section_id": "part_2",
            "question_type": "true_false",
            "domain": "geography",
            "difficulty": "medium",
            "points": 1.0,
            "prompt": "Cho bảng số liệu nhiệt độ và lượng mưa các tháng của trạm khí tượng A (nhiệt độ tháng 1 là 16,4 độ C, tháng 7 là 28,9 độ C; mưa nhiều từ tháng 5 đến tháng 10). Xét tính Đúng / Sai:",
            "tf_statements": {
                "a": "Trạm khí tượng A thuộc miền khí hậu phía Bắc.",
                "b": "Mùa mưa của trạm khí tượng A từ tháng 4 đến tháng 8.",
                "c": "Biên độ nhiệt năm của trạm khí tượng A cao chủ yếu do Tín phong.",
                "d": "Tổng lượng mưa năm của trạm A là 1 667,2 mm, mưa ít vào mùa đông."
            },
            "correct_answer": {
                "a": "Đ",
                "b": "S",
                "c": "S",
                "d": "Đ"
            },
            "explanation": "Nhiệt độ tháng 1 hạ xuống 16,4 độ C chứng tỏ có mùa đông lạnh ở phía Bắc (a Đúng). Biên độ nhiệt cao do gió mùa Đông Bắc chứ không phải Tín phong (c Sai)."
        },
        {
            "question_number": 14,
            "section_id": "part_2",
            "question_type": "true_false",
            "domain": "geography",
            "difficulty": "medium",
            "points": 1.0,
            "prompt": "Cho biểu đồ cơ cấu GDP nước ta giai đoạn 2010 - 2022 (Nông lâm thủy sản giảm từ 15,4% xuống 12%, Công nghiệp xây dựng biến động nhẹ 40,6% -> 41,3%, Dịch vụ tăng 33% -> 38,2%). Xét tính Đúng / Sai:",
            "tf_statements": {
                "a": "Tỉ trọng nhóm ngành công nghiệp và xây dựng, dịch vụ của nước ta tăng liên tục.",
                "b": "Tỉ trọng nhóm ngành nông nghiệp, lâm nghiệp và thủy sản của nước ta có xu hướng giảm dần.",
                "c": "Tỉ trọng nhóm ngành công nghiệp và xây dựng của nước ta tăng chậm hơn nhóm ngành dịch vụ.",
                "d": "Cơ cấu GDP của nước ta chuyển dịch theo hướng công nghiệp hóa, hiện đại hóa."
            },
            "correct_answer": {
                "a": "S",
                "b": "Đ",
                "c": "S",
                "d": "Đ"
            },
            "explanation": "a) Sai vì công nghiệp có năm giảm (42,2% xuống 41,8%). b) Đúng vì nông nghiệp giảm liên tục từ 15,4% về 12%. c) Sai vì công nghiệp tăng 0,7% trong khi dịch vụ tăng 5,2%. d) Đúng theo định hướng CNH-HĐH."
        },
        {
            "question_number": 15,
            "section_id": "part_2",
            "question_type": "true_false",
            "domain": "geography",
            "difficulty": "medium",
            "points": 1.0,
            "prompt": "Đoạn văn bản về ảnh hưởng của biến đổi khí hậu đến Đồng bằng sông Cửu Long (nước biển dâng, xâm nhập mặn, suy giảm an ninh lương thực). Xét tính Đúng / Sai:",
            "tf_statements": {
                "a": "Biến đổi khí hậu có tác động mạnh tới sản xuất và đời sống người dân ở đồng bằng sông Cửu Long.",
                "b": "Trồng lúa và nuôi trồng thủy sản là hai lĩnh vực chịu ảnh hưởng mạnh nhất khi có sự gia tăng xâm nhập mặn.",
                "c": "Đồng bằng sông Cửu Long là một trong những vùng chịu ảnh hưởng nặng nhất của biến đổi khí hậu do tiếp giáp vùng biển rộng, đường bờ biển dài.",
                "d": "Tình trạng thiếu nước ngọt ngày càng gia tăng ở đồng bằng sông Cửu Long chủ yếu do biến đổi khí hậu, hoạt động tại chỗ của người dân và can thiệp từ thượng nguồn sông Mê Kông."
            },
            "correct_answer": {
                "a": "Đ",
                "b": "Đ",
                "c": "S",
                "d": "Đ"
            },
            "explanation": "c) Sai vì nguyên nhân chính khiến ĐBSCL chịu ảnh hưởng nặng là do địa hình thấp trũng chứ không phải chỉ do bờ biển dài. Các mệnh đề a, b, d đều đúng."
        },

        # Phần III: Điền kết quả ngắn (4 câu - 1đ)
        {
            "question_number": 16,
            "section_id": "part_3",
            "question_type": "short_answer",
            "domain": "geography",
            "difficulty": "easy",
            "points": 0.25,
            "prompt": "Dựa vào bảng số liệu nhiệt độ Huế và Đà Nẵng năm 2020: Cho biết thành phố nào có biên độ nhiệt năm cao hơn?",
            "correct_answer": "Huế",
            "accepted_answers": ["Huế", "thành phố Huế", "huế", "tp huế"],
            "explanation": "Huế có biên độ nhiệt: 29,9 - 21,7 = 8,2 độ C; Đà Nẵng: 30,6 - 23,6 = 7,0 độ C. Vậy Huế cao hơn."
        },
        {
            "question_number": 17,
            "section_id": "part_3",
            "question_type": "short_answer",
            "domain": "geography",
            "difficulty": "medium",
            "points": 0.25,
            "prompt": "Dựa vào bảng số liệu diện tích và sản lượng lúa các vùng năm 2022: Cho biết vùng nào ở nước ta có năng suất lúa cao nhất?",
            "correct_answer": "Đồng bằng sông Cửu Long",
            "accepted_answers": ["Đồng bằng sông Cửu Long", "đồng bằng sông cửu long", "ĐBSCL", "dbscl"],
            "explanation": "Năng suất lúa = Sản lượng / Diện tích. ĐBSCL đạt năng suất cao nhất cả nước."
        },
        {
            "question_number": 18,
            "section_id": "part_3",
            "question_type": "short_answer",
            "domain": "geography",
            "difficulty": "medium",
            "points": 0.25,
            "prompt": "Dựa vào bảng giá trị xuất nhập khẩu 2005 - 2022: Cho biết giá trị nhập siêu lớn nhất là bao nhiêu tỉ USD?",
            "correct_answer": "12.6",
            "accepted_answers": ["12.6", "12,6", "12.6 tỉ usd"],
            "explanation": "Năm 2010 nhập khẩu 84,8 và xuất khẩu 72,2 -> nhập siêu = 84,8 - 72,2 = 12,6 tỉ USD."
        },
        {
            "question_number": 19,
            "section_id": "part_3",
            "question_type": "short_answer",
            "domain": "geography",
            "difficulty": "hard",
            "points": 0.25,
            "prompt": "Theo Tổng cục Thống kê, dân số năm 2021 là 98,3 triệu người, nhóm 15-64 tuổi chiếm 67,6%. Tỉ số phụ thuộc chung của dân số nước ta là bao nhiêu phần trăm? (Làm tròn đến 1 chữ số thập phân)",
            "correct_answer": "47.9",
            "accepted_answers": ["47.9", "47,9", "47.9%"],
            "explanation": "Tỉ số phụ thuộc = (Dân số dưới 15 + trên 65) / Dân số 15-64 * 100% = (100 - 67,6) / 67,6 * 100% = 32,4 / 67,6 * 100% = 47,9%."
        },

        # Phần IV: Tự luận (1 câu - 3đ)
        {
            "question_number": 20,
            "section_id": "part_4",
            "question_type": "essay",
            "domain": "geography",
            "difficulty": "hard",
            "points": 3.0,
            "prompt": "Từ bảng số liệu tổng dân số và dân số nữ giai đoạn 1990 - 2022: Tính tỉ số giới tính nam/nữ của nước ta qua các năm, nhận xét và giải thích sự thay đổi tỉ số giới tính.",
            "correct_answer": "Tỉ số giới tính = (Dân số nam / Dân số nữ) * 100. Tỉ số tăng liên tục từ 95,2 (1990) lên 99,4 (2022). Do y tế phát triển, di chứng chiến tranh giảm dần, tỉ số giới tính khi sinh ở mức cao.",
            "explanation": "Thang điểm: Công thức & bảng tính (1,0đ), nhận xét xu hướng (1,0đ), giải thích nguyên nhân (1,0đ)."
        }
    ]
}

# --------------------------------------------------------------------------
# 5. SPT MÔN LỊCH SỬ (60 PHÚT - THANG 10)
# --------------------------------------------------------------------------
SPT_HISTORY_EXAM = {
    "id": "spt_sample_history",
    "title": "Đề Tham Khảo SPT ĐH Sư Phạm Hà Nội - Môn Lịch Sử (Mã đề 075)",
    "description": "Đề thi chính thức Kì thi ĐGNL ĐH Sư phạm Hà Nội. Cấu trúc 3 phần: Trắc nghiệm (20 câu), Đúng/Sai (2 câu 8 ý), Tự luận phân tích tư liệu (3 câu).",
    "exam_type": "spt",
    "subject": "history",
    "total_questions": 25,
    "duration_minutes": 60,
    "max_score": 10.0,
    "source": "spt_official_sample",
    "questions": [
        # Phần I: Trắc nghiệm (20 câu - 5đ)
        {
            "question_number": 1,
            "section_id": "part_1",
            "question_type": "multiple_choice",
            "domain": "history",
            "difficulty": "easy",
            "points": 0.25,
            "prompt": "Nội dung nào sau đây phản ánh đúng thành tựu về chính trị của Trung Quốc trong công cuộc cải cách, mở cửa (từ năm 1978)?",
            "options": {
                "A": "Cải cách đồng bộ thể chế kinh tế.",
                "B": "Xây dựng được hệ thống lý luận về chủ nghĩa xã hội mang đặc sắc Trung Quốc.",
                "C": "Đa dạng hóa cơ cấu kinh tế.",
                "D": "Đảm bảo quốc phòng an ninh vững chắc."
            },
            "correct_answer": "B",
            "explanation": "Đảng Cộng sản Trung Quốc đã khởi xướng và hoàn thiện hệ thống lý luận CNXH mang đặc sắc Trung Quốc."
        },
        {
            "question_number": 2,
            "section_id": "part_1",
            "question_type": "multiple_choice",
            "domain": "history",
            "difficulty": "easy",
            "points": 0.25,
            "prompt": "Nội dung nào phản ánh đúng ý nghĩa của việc thành lập Liên bang CHXHCN Xô viết năm 1922 đối với các dân tộc bị áp bức?",
            "options": {
                "A": "Tạo thời cơ chín muồi.",
                "B": "Cổ vũ các dân tộc đứng lên đấu tranh giải phóng dân tộc.",
                "C": "Thúc đẩy đa phương hóa.",
                "D": "Đánh dấu sự sụp đổ của chủ nghĩa đế quốc."
            },
            "correct_answer": "B",
            "explanation": "Sự ra đời của Liên Xô là nguồn cổ vũ to lớn cho phong trào giải phóng dân tộc trên thế giới."
        },
        {
            "question_number": 3,
            "section_id": "part_1",
            "question_type": "multiple_choice",
            "domain": "history",
            "difficulty": "easy",
            "points": 0.25,
            "prompt": "Thắng lợi của cuộc khởi nghĩa Lam Sơn thế kỷ XV đánh dấu sự phục hưng của dân tộc, mở ra nền thái bình lâu dài vì:",
            "options": {
                "A": "đã phát triển thành chiến tranh giải phóng.",
                "B": "chống lại âm mưu tiêu diệt văn hóa của nhà Minh.",
                "C": "hoàn thành trọn vẹn sự nghiệp giải phóng đất nước.",
                "D": "đưa quân sự Việt Nam lên đỉnh cao."
            },
            "correct_answer": "C",
            "explanation": "Khởi nghĩa Lam Sơn đã quét sạch quân xâm lược Minh, khôi phục hoàn toàn nền độc lập dân tộc."
        },
        {
            "question_number": 4,
            "section_id": "part_1",
            "question_type": "multiple_choice",
            "domain": "history",
            "difficulty": "medium",
            "points": 0.25,
            "prompt": "Cuộc kháng chiến chống thực dân Pháp (1858 - 1884) không thành công do nguyên nhân nào sau đây?",
            "options": {
                "A": "Nhân dân ngay từ đầu không ủng hộ Triều đình.",
                "B": "Đường lối kháng chiến chống thực dân Pháp không phù hợp.",
                "C": "Nhà Nguyễn ngay từ đầu đã hàng Pháp.",
                "D": "Phong trào kháng chiến chỉ diễn ra ở Bắc Kỳ."
            },
            "correct_answer": "B",
            "explanation": "Triều đình nhà Nguyễn thiếu đường lối kháng chiến đúng đắn, mang tư tưởng thủ hòa và thỏa hiệp."
        },
        {
            "question_number": 5,
            "section_id": "part_1",
            "question_type": "multiple_choice",
            "domain": "history",
            "difficulty": "easy",
            "points": 0.25,
            "prompt": "Nội dung nào KHÔNG đúng về vai trò của Liên hợp quốc trong việc bảo đảm quyền con người, phát triển văn hóa và xã hội?",
            "options": {
                "A": "Thúc đẩy các chương trình phát triển giáo dục, y tế, văn hóa.",
                "B": "Bảo vệ các di sản văn hóa, quyền tự do ngôn luận.",
                "C": "Tạo điều kiện xây dựng các hệ thống an ninh xã hội.",
                "D": "Thúc đẩy các liên minh quân sự để đảm bảo an ninh con người."
            },
            "correct_answer": "D",
            "explanation": "Liên hợp quốc không thành lập liên minh quân sự; tôn chỉ là duy trì hòa bình phi bạo lực."
        },
        {
            "question_number": 6,
            "section_id": "part_1",
            "question_type": "multiple_choice",
            "domain": "history",
            "difficulty": "medium",
            "points": 0.25,
            "prompt": "Xu thế đa cực trong quan hệ quốc tế sau Chiến tranh lạnh mang lại cơ hội nào sau đây cho Việt Nam trong công cuộc phát triển?",
            "options": {
                "A": "Thu hút mạnh mẽ các nguồn vốn đầu tư từ bên ngoài.",
                "B": "Giải quyết triệt để các vấn đề phi truyền thống.",
                "C": "Hoạt động toàn diện trong các quan hệ song phương.",
                "D": "Hình thành các liên minh quân sự."
            },
            "correct_answer": "A",
            "explanation": "Đa dạng hóa quan hệ quốc tế giúp Việt Nam mở rộng hội nhập kinh tế và thu hút vốn đầu tư nước ngoài (FDI)."
        },
        {
            "question_number": 7,
            "section_id": "part_1",
            "question_type": "multiple_choice",
            "domain": "history",
            "difficulty": "medium",
            "points": 0.25,
            "prompt": "Nội dung nào phản ánh KHÔNG đúng những hỗ trợ của Liên hợp quốc đối với Việt Nam?",
            "options": {
                "A": "Khắc phục hậu quả chiến tranh thông qua viện trợ nhân đạo.",
                "B": "Bảo vệ quyền lợi cho trẻ em thông qua UNICEF.",
                "C": "Đề nghị các nước công nhận Việt Nam có nền kinh tế thị trường.",
                "D": "Công nhận di sản văn hóa và hỗ trợ tài chính bảo tồn."
            },
            "correct_answer": "C",
            "explanation": "Việc công nhận nền kinh tế thị trường là quan hệ kinh tế thương mại song phương giữa các quốc gia, không thuộc nhiệm vụ của LHQ."
        },
        {
            "question_number": 8,
            "section_id": "part_1",
            "question_type": "multiple_choice",
            "domain": "history",
            "difficulty": "easy",
            "points": 0.25,
            "prompt": "Nội dung nào sau đây phản ánh đúng bối cảnh lịch sử thành lập ASEAN (1967)?",
            "options": {
                "A": "Nhu cầu hợp tác để cùng nhau phát triển.",
                "B": "Sự suy yếu của các quốc gia lớn ở châu Á.",
                "C": "Sự phát triển kinh tế là xu thế của cả khu vực.",
                "D": "Toàn cầu hóa đang trở thành xu thế chủ đạo."
            },
            "correct_answer": "A",
            "explanation": "Các nước Đông Nam Á thành lập ASEAN xuất phát từ nhu cầu hợp tác kinh tế - an ninh để cùng phát triển và hạn chế ảnh hưởng của các nước lớn."
        },
        {
            "question_number": 9,
            "section_id": "part_1",
            "question_type": "multiple_choice",
            "domain": "history",
            "difficulty": "easy",
            "points": 0.25,
            "prompt": "Một trong những biểu hiện của sự hợp tác an ninh trong Hiệp hội các quốc gia Đông Nam Á (ASEAN) là:",
            "options": {
                "A": "Tuyên bố về khu vực hòa bình, tự do và trung lập (ZOPFAN).",
                "B": "Thỏa thuận về hợp tác quân sự với các nước ngoài khu vực.",
                "C": "Hợp tác kinh tế sâu rộng.",
                "D": "Thành lập liên minh phòng thủ chung."
            },
            "correct_answer": "A",
            "explanation": "Tuyên bố ZOPFAN (1971) là văn kiện hợp tác chính trị - an ninh nền tảng của ASEAN."
        },
        {
            "question_number": 10,
            "section_id": "part_1",
            "question_type": "multiple_choice",
            "domain": "history",
            "difficulty": "medium",
            "points": 0.25,
            "prompt": "Công nghệ số đóng vai trò nào đối với sự phát triển của các nước thành viên trong Tầm nhìn Cộng đồng ASEAN sau năm 2025?",
            "options": {
                "A": "Tăng cường sự kết nối giữa các nước thành viên.",
                "B": "Hạn chế lạm phát và bất ổn kinh tế.",
                "C": "Giải quyết các vấn đề an ninh phi truyền thống.",
                "D": "Tăng sức cạnh tranh với các tổ chức khu vực khác."
            },
            "correct_answer": "A",
            "explanation": "Kinh tế số và chuyển đổi số giúp đẩy mạnh kết nối kinh tế số và liên kết cộng đồng ASEAN."
        },
        {
            "question_number": 11,
            "section_id": "part_1",
            "question_type": "multiple_choice",
            "domain": "history",
            "difficulty": "easy",
            "points": 0.25,
            "prompt": "Chiến thắng Ấp Bắc (năm 1963) có ý nghĩa nào sau đây?",
            "options": {
                "A": "Chuyển cách mạng miền Nam sang thế tiến công.",
                "B": "Khẳng định khả năng có thể đánh bại 'Chiến tranh đặc biệt' của đế quốc Mỹ.",
                "C": "Nâng cao uy tín của Mặt trận Dân tộc Giải phóng.",
                "D": "Buộc đế quốc Mỹ tuyên bố phi Mỹ hóa chiến tranh."
            },
            "correct_answer": "B",
            "explanation": "Chiến thắng Ấp Bắc mở ra phong trào 'Thi đua Ấp Bắc, giết giặc lập công', chứng minh quân dân miền Nam hoàn toàn có thể đánh bại chiến lược Chiến tranh đặc biệt."
        },
        {
            "question_number": 12,
            "section_id": "part_1",
            "question_type": "multiple_choice",
            "domain": "history",
            "difficulty": "medium",
            "points": 0.25,
            "prompt": "Chiến dịch Điện Biên Phủ năm 1954 có điểm khác biệt nào so với các chiến dịch trước đó trong cuộc kháng chiến chống Pháp (1945 - 1954)?",
            "options": {
                "A": "Thể hiện được đường lối kháng chiến toàn dân.",
                "B": "Chiến dịch thắng lợi góp phần quyết định việc kết thúc chiến tranh.",
                "C": "Bộ đội chủ lực lần đầu tiên tập dượt chiến thuật đánh điểm.",
                "D": "Đánh bại một kế hoạch quân sự của thực dân Pháp."
            },
            "correct_answer": "B",
            "explanation": "Điện Biên Phủ là trận quyết chiến chiến lược, đập tan hoàn toàn ý chí xâm lược của Pháp, buộc Pháp ký Hiệp định Genève chấm dứt chiến tranh."
        },
        {
            "question_number": 13,
            "section_id": "part_1",
            "question_type": "multiple_choice",
            "domain": "history",
            "difficulty": "medium",
            "points": 0.25,
            "prompt": "Cuộc Tổng tiến công và nổi dậy Xuân 1975 và Cuộc Tổng tiến công và nổi dậy Xuân 1968 có điểm tương đồng là:",
            "options": {
                "A": "mở ra hướng đấu tranh mới cho cách mạng.",
                "B": "chỉ diễn ra tại các thành phố, đô thị lớn.",
                "C": "nhằm giành chính quyền về tay nhân dân.",
                "D": "diễn ra thông qua những chiến dịch lớn."
            },
            "correct_answer": "C",
            "explanation": "Cả hai cuộc tổng tiến công đều kết hợp đòn tiến công quân sự với nổi dậy của quần chúng nhằm lật đổ chính quyền Sài Gòn, giành chính quyền về tay nhân dân."
        },
        {
            "question_number": 14,
            "section_id": "part_1",
            "question_type": "multiple_choice",
            "domain": "history",
            "difficulty": "medium",
            "points": 0.25,
            "prompt": "Đường lối đổi mới kinh tế của Đảng Cộng sản Việt Nam giai đoạn 1996 - 2006 KHÔNG đề cập đến nội dung nào sau đây?",
            "options": {
                "A": "Phát triển nền kinh tế thị trường định hướng XHCN.",
                "B": "Chuyển dịch cơ cấu kinh tế theo hướng CNH - HĐH.",
                "C": "Tích cực đổi mới mô hình tăng trưởng và cơ cấu lại nền kinh tế.",
                "D": "Gắn tăng trưởng kinh tế với tiến bộ và công bằng xã hội."
            },
            "correct_answer": "C",
            "explanation": "Chủ trương 'đổi mới mô hình tăng trưởng và cơ cấu lại nền kinh tế' được đề ra chủ yếu từ Đại hội XI (2011) trở đi."
        },
        {
            "question_number": 15,
            "section_id": "part_1",
            "question_type": "multiple_choice",
            "domain": "history",
            "difficulty": "easy",
            "points": 0.25,
            "prompt": "Đường lối đổi mới ở Việt Nam từ năm 1986 đến nay chủ yếu được bổ sung, phát triển qua các:",
            "options": {
                "A": "kết luận của Ban Chấp hành Trung ương.",
                "B": "thông báo của Ban Chấp hành Trung ương.",
                "C": "quyết định của Bộ Chính trị.",
                "D": "văn kiện tại Đại hội đại biểu toàn quốc của Đảng."
            },
            "correct_answer": "D",
            "explanation": "Đại hội Đảng toàn quốc là cơ quan lãnh đạo cao nhất quyết định và hoàn thiện đường lối đổi mới của đất nước."
        },
        {
            "question_number": 16,
            "section_id": "part_1",
            "question_type": "multiple_choice",
            "domain": "history",
            "difficulty": "medium",
            "points": 0.25,
            "prompt": "Một trong những bài học kinh nghiệm của công cuộc Đổi mới ở Việt Nam từ năm 1986 đến nay là:",
            "options": {
                "A": "Đổi mới toàn diện, đồng bộ, từ đổi mới chính trị, xã hội đến đổi mới kinh tế.",
                "B": "Đổi mới phải vì lợi ích của nhân dân, phát huy vai trò chủ động, sáng tạo của nhân dân.",
                "C": "Kiên quyết giữ vững độc lập, chủ quyền.",
                "D": "Không thay đổi mục tiêu đi lên CNXH."
            },
            "correct_answer": "B",
            "explanation": "Bài học 'lấy dân làm gốc', đổi mới vì nhân dân, dựa vào nhân dân là bài học cốt lõi hàng đầu."
        },
        {
            "question_number": 17,
            "section_id": "part_1",
            "question_type": "multiple_choice",
            "domain": "history",
            "difficulty": "easy",
            "points": 0.25,
            "prompt": "Trong thời kỳ 1954 - 1975, hoạt động đối ngoại của Việt Nam tập trung phục vụ sự nghiệp nào sau đây?",
            "options": {
                "A": "Tiến hành cách mạng ruộng đất trên phạm vi cả nước.",
                "B": "Hoàn thành giải phóng miền Nam, thống nhất đất nước.",
                "C": "Xây dựng CNXH trên phạm vi cả nước.",
                "D": "Thống nhất đất nước bằng con đường hòa bình."
            },
            "correct_answer": "B",
            "explanation": "Đối ngoại giai đoạn 1954 - 1975 nhằm tranh thủ sự ủng hộ quốc tế để đánh thắng đế quốc Mỹ, hoàn thành giải phóng miền Nam thống nhất đất nước."
        },
        {
            "question_number": 18,
            "section_id": "part_1",
            "question_type": "multiple_choice",
            "domain": "history",
            "difficulty": "medium",
            "points": 0.25,
            "prompt": "Hoạt động đối ngoại của Việt Nam trong những năm đầu thế kỉ XXI gắn liền với:",
            "options": {
                "A": "ứng phó biến đổi thời tiết.",
                "B": "chủ động và tích cực hội nhập quốc tế toàn diện, sâu rộng.",
                "C": "viện trợ không hoàn lại.",
                "D": "giao lưu văn hóa."
            },
            "correct_answer": "B",
            "explanation": "Đường lối đối ngoại thế kỷ XXI của Việt Nam là 'chủ động và tích cực hội nhập quốc tế toàn diện, sâu rộng'."
        },
        {
            "question_number": 19,
            "section_id": "part_1",
            "question_type": "multiple_choice",
            "domain": "history",
            "difficulty": "easy",
            "points": 0.25,
            "prompt": "Nghị quyết số 24C/18.65 ghi nhận Hồ Chí Minh là 'Anh hùng giải phóng dân tộc và Nhà văn hóa kiệt xuất của Việt Nam' do tổ chức nào sau đây ban hành?",
            "options": {
                "A": "Tổ chức Giáo dục, Khoa học và Văn hoá của Liên hợp quốc (UNESCO).",
                "B": "Hiệp hội các quốc gia Đông Nam Á (ASEAN).",
                "C": "Hội đồng Bảo an Liên hợp quốc.",
                "D": "Diễn đàn hợp tác Á - Âu (ASEM)."
            },
            "correct_answer": "A",
            "explanation": "Khóa họp Đại hội đồng UNESCO năm 1987 đã thông qua Nghị quyết vinh danh Chủ tịch Hồ Chí Minh."
        },
        {
            "question_number": 20,
            "section_id": "part_1",
            "question_type": "multiple_choice",
            "domain": "history",
            "difficulty": "easy",
            "points": 0.25,
            "prompt": "Vai trò quan trọng của Hồ Chí Minh trong Cách mạng tháng Tám năm 1945 ở Việt Nam là:",
            "options": {
                "A": "thực hiện ngoại giao quốc tế.",
                "B": "kêu gọi khởi nghĩa từng phần.",
                "C": "lãnh đạo toàn dân tổng khởi nghĩa giành chính quyền và soạn thảo Tuyên ngôn Độc lập.",
                "D": "chỉ huy các trận đánh đô thị."
            },
            "correct_answer": "C",
            "explanation": "Hồ Chí Minh cùng Trung ương Đảng triệu tập Hội nghị toàn quốc và Quốc dân đại hội Tân Trào, phát lệnh Tổng khởi nghĩa và đọc Tuyên ngôn Độc lập khai sinh nước VNDCCH."
        },

        # Phần II: Đúng / Sai (2 câu - 8 ý - 2đ)
        {
            "question_number": 21,
            "section_id": "part_2",
            "question_type": "true_false",
            "domain": "history",
            "difficulty": "medium",
            "points": 1.0,
            "prompt": "Đoạn trích về cơ chế và vai trò của Liên hợp quốc trong việc duy trì hòa bình và an ninh quốc tế. Xét tính Đúng / Sai:",
            "tf_statements": {
                "a": "Đoạn tư liệu trên khẳng định vai trò của Liên hợp quốc trong việc thúc đẩy phát triển kinh tế, tài chính, thương mại quốc tế.",
                "b": "Liên hợp quốc thường xuyên sử dụng biện pháp can thiệp trực tiếp để chấm dứt các cuộc xung đột.",
                "c": "Vai trò của Liên hợp quốc bị hạn chế bởi nguyên tắc tôn trọng chủ quyền quốc gia, làm giảm khả năng can thiệp quân sự nếu không có sự đồng thuận.",
                "d": "Việc duy trì hòa bình quốc tế của Liên hợp quốc phụ thuộc vào sự đóng góp tài chính và quân sự từ các quốc gia thành viên."
            },
            "correct_answer": {
                "a": "S",
                "b": "S",
                "c": "Đ",
                "d": "Đ"
            },
            "explanation": "Đoạn tư liệu tập trung vào an ninh hòa bình chứ không nói về kinh tế (a Sai). Biện pháp can thiệp trực tiếp là phương án cuối cùng, ưu tiên hòa bình thương lượng (b Sai). Mệnh đề c và d Đúng."
        },
        {
            "question_number": 22,
            "section_id": "part_2",
            "question_type": "true_false",
            "domain": "history",
            "difficulty": "medium",
            "points": 1.0,
            "prompt": "Đoạn tư liệu của Hồ Chí Minh khi đọc Luận cương của Lênin về vấn đề dân tộc và thuộc địa (tháng 7/1920). Xét tính Đúng / Sai:",
            "tf_statements": {
                "a": "Đoạn tư liệu trên đề cập đến sự kiện Nguyễn Ái Quốc đọc Luận cương của Lê-nin về vấn đề cách mạng vô sản.",
                "b": "Con đường cứu nước mà Nguyễn Ái Quốc tin theo là con đường cách mạng vô sản.",
                "c": "Nguyễn Ái Quốc đi theo chủ nghĩa Mác - Lênin, đi theo Quốc tế thứ ba đã khẳng định sự thắng lợi của cuộc đấu tranh giải phóng dân tộc của Việt Nam.",
                "d": "Cơ sở ban đầu đưa Nguyễn Ái Quốc đến với Lênin, tin theo Quốc tế thứ ba là chủ nghĩa yêu nước."
            },
            "correct_answer": {
                "a": "S",
                "b": "Đ",
                "c": "S",
                "d": "Đ"
            },
            "explanation": "a) Sai vì tên tác phẩm là 'Sơ thảo lần thứ nhất những luận cương về vấn đề dân tộc và vấn đề thuộc địa'. c) Sai vì lúc này (1920) cách mạng mới tìm ra con đường chứ chưa khẳng định thắng lợi. b và d Đúng."
        },

        # Phần III: Tự luận (3 câu - 3đ)
        {
            "question_number": 23,
            "section_id": "part_3",
            "question_type": "essay",
            "domain": "history",
            "difficulty": "medium",
            "points": 1.0,
            "prompt": "Giải thích nội dung các cụm từ 'mùa xuân vẻ vang này' và 'hai nhiệm vụ chiến lược song song' được nhắc đến trong đoạn tư liệu Văn kiện Đảng.",
            "correct_answer": "'Mùa xuân vẻ vang này' là thắng lợi của Cuộc Tổng tiến công và nổi dậy Xuân 1975. 'Hai nhiệm vụ chiến lược song song' là: Miền Bắc xây dựng CNXH làm hậu phương; miền Nam tiếp tục cách mạng dân tộc dân chủ nhân dân.",
            "explanation": "Thang điểm: Mùa xuân 1975 (0,5đ), giải thích hai nhiệm vụ miền Bắc và miền Nam (0,5đ)."
        },
        {
            "question_number": 24,
            "section_id": "part_4",
            "question_type": "essay",
            "domain": "history",
            "difficulty": "hard",
            "points": 1.0,
            "prompt": "Lựa chọn và phân tích ý nghĩa của 01 sự kiện có tính chất bước ngoặt trong các giai đoạn phát triển của cách mạng miền Nam thời kì chống Mỹ, cứu nước (Ví dụ: Đồng Khởi 1960, Mậu Thân 1968, Hiệp định Paris 1973...).",
            "correct_answer": "Thí sinh tự chọn 1 sự kiện (Đồng Khởi 1960 chuyển từ thế giữ gìn lực lượng sang thế tiến công, hoặc Mậu Thân 1968 buộc Mỹ xuống thang, hoặc Paris 1973 buộc Mỹ rút quân).",
            "explanation": "Thang điểm: Nêu sự kiện (0,25đ), phân tích bối cảnh và ý nghĩa bước ngoặt (0,75đ)."
        },
        {
            "question_number": 25,
            "section_id": "part_4",
            "question_type": "essay",
            "domain": "history",
            "difficulty": "hard",
            "points": 1.0,
            "prompt": "Lí giải vì sao 'mùa xuân vẻ vang này' lại 'đánh dấu bước ngoặt lịch sử vô cùng quan trọng trên con đường tiến lên của cách mạng Việt Nam'?",
            "correct_answer": "Kết thúc 21 năm kháng chiến chống Mỹ và 30 năm chiến tranh giải phóng, chấm dứt vĩnh viễn ách thống trị của chủ nghĩa thực dân, thống nhất đất nước, đưa cả nước bước vào kỷ nguyên độc lập và đi lên CNXH.",
            "explanation": "Thang điểm: Kết thúc 21 năm KCCM và 30 năm chiến tranh (0,5đ), chấm dứt ách thực dân (0,25đ), mở ra kỷ nguyên độc lập thống nhất đi lên CNXH (0,25đ)."
        }
    ]
}



# --------------------------------------------------------------------------
# 6. SPT MÔN GIÁO DỤC KINH TẾ VÀ PHÁP LUẬT (60 PHÚT - THANG 10)
# --------------------------------------------------------------------------
SPT_CIVICS_LAW_EXAM = {
    "id": "spt_sample_civics_law",
    "title": "Đề Tham Khảo SPT ĐH Sư Phạm Hà Nội - Môn GDKT&PL (Mã đề 075)",
    "description": "Đề thi chính thức Kì thi ĐGNL ĐH Sư phạm Hà Nội. Cấu trúc 3 phần: Trắc nghiệm khách quan (16 câu), Trắc nghiệm Đúng/Sai (3 câu 12 ý), Tự luận (2 câu).",
    "exam_type": "spt",
    "subject": "civics_law",
    "total_questions": 21,
    "duration_minutes": 60,
    "max_score": 10.0,
    "source": "spt_official_sample",
    "questions": [
        # Phần I: Trắc nghiệm (16 câu - 4đ, 0.25đ/câu)
        {
            "question_number": 1,
            "section_id": "part_1",
            "question_type": "multiple_choice",
            "domain": "civics_law",
            "difficulty": "medium",
            "points": 0.25,
            "prompt": "Do bão, lũ tại các tỉnh miền Trung và Tây Nguyên thường gây hậu quả nghiêm trọng nên Nhà nước ta luôn dành một phần ngân sách để chủ động phòng ngừa, ứng phó và khắc phục hậu quả thiên tai. Hành động này thể hiện vai trò nào dưới đây của ngân sách nhà nước?",
            "options": {
                "A": "Củng cố bộ máy nhà nước.",
                "B": "Tăng cường quốc phòng.",
                "C": "Tạo lập quỹ dự trữ quốc gia.",
                "D": "Giải quyết các vấn đề xã hội."
            },
            "correct_answer": "C",
            "explanation": "Việc trích ngân sách để dự phòng, ứng phó thiên tai thể hiện vai trò tạo lập quỹ dự trữ quốc gia."
        },
        {
            "question_number": 2,
            "section_id": "part_1",
            "question_type": "multiple_choice",
            "domain": "civics_law",
            "difficulty": "medium",
            "points": 0.25,
            "prompt": "Việc sầu riêng Việt Nam được xuất khẩu chính ngạch sang một số nước và mang lại lợi nhuận cao khiến nhiều nhà vườn chuyển từ trồng cà phê sang trồng sầu riêng. Nhiều chuyên gia cảnh báo rằng việc chuyển đổi cây trồng thiếu tính toán và không theo định hướng có thể gây rủi ro lớn trong tương lai. Nội dung thông tin này phản ánh",
            "options": {
                "A": "hạn chế của cơ chế thị trường.",
                "B": "tính chất của giá cả thị trường.",
                "C": "quy luật giá trị trong kinh tế thị trường.",
                "D": "vai trò điều tiết thị trường của nhà nước."
            },
            "correct_answer": "A",
            "explanation": "Tính tự phát, chạy theo lợi nhuận trước mắt mà thiếu định hướng dẫn đến rủi ro là một hạn chế điển hình của cơ chế thị trường."
        },
        {
            "question_number": 3,
            "section_id": "part_1",
            "question_type": "multiple_choice",
            "domain": "civics_law",
            "difficulty": "easy",
            "points": 0.25,
            "prompt": "Hành vi nào sau đây không tuân thủ quy định của Hiến pháp về quyền và nghĩa vụ dân sự của công dân?",
            "options": {
                "A": "Bà N uỷ quyền cho con trai đi bầu cử hộ.",
                "B": "Ông H ép buộc vợ tham gia tôn giáo.",
                "C": "Bạn K vứt rác không đúng nơi quy định.",
                "D": "Anh M và chị Y kí đơn thuận tình ly hôn."
            },
            "correct_answer": "B",
            "explanation": "Hiến pháp quy định công dân có quyền tự do tín ngưỡng, tôn giáo; không ai được ép buộc người khác theo hoặc từ bỏ tôn giáo."
        },
        {
            "question_number": 4,
            "section_id": "part_1",
            "question_type": "multiple_choice",
            "domain": "civics_law",
            "difficulty": "medium",
            "points": 0.25,
            "prompt": "Khi rà soát các văn bản quy phạm pháp luật đã ban hành, cơ quan nhà nước M phát hiện một số văn bản chưa phù hợp với Hiến pháp năm 2013 nên đã ban hành văn bản thay thế theo đúng trình tự, thủ tục, hình thức luật định. Việc làm này thể hiện đặc điểm nào sau đây của pháp luật?",
            "options": {
                "A": "Tính quy phạm phổ biến.",
                "B": "Tính quyền lực bắt buộc chung.",
                "C": "Tính chặt chẽ về mặt nội dung.",
                "D": "Tính chặt chẽ về mặt hình thức."
            },
            "correct_answer": "D",
            "explanation": "Việc bảo đảm văn bản cấp dưới phù hợp văn bản cấp trên và tuân thủ đúng trình tự, thủ tục, kỹ thuật văn bản thể hiện tính chặt chẽ về mặt hình thức."
        },
        {
            "question_number": 5,
            "section_id": "part_1",
            "question_type": "multiple_choice",
            "domain": "civics_law",
            "difficulty": "medium",
            "points": 0.25,
            "prompt": "Khi lạm phát do cầu kéo và thừa tiền mặt trong lưu thông xảy ra, Nhà nước nên thực hiện biện pháp nào sau đây để kiềm chế và kiểm soát lạm phát?",
            "options": {
                "A": "Giảm chi tiêu của Chính phủ.",
                "B": "Giảm thuế cho các mặt hàng thiết yếu.",
                "C": "Chi trả trái phiếu Chính phủ trước thời hạn.",
                "D": "Giảm tỉ lệ dự trữ bắt buộc của ngân hàng."
            },
            "correct_answer": "A",
            "explanation": "Thực hiện chính sách tài khóa thắt chặt bằng cách giảm chi tiêu công để giảm tổng cầu và lượng tiền trong lưu thông."
        },
        {
            "question_number": 6,
            "section_id": "part_1",
            "question_type": "multiple_choice",
            "domain": "civics_law",
            "difficulty": "easy",
            "points": 0.25,
            "prompt": "Khi dịch bệnh xảy ra, nhu cầu mua khẩu trang tăng mạnh. Tuy nhiên, do năng lực sản xuất được mở rộng kịp thời, lượng khẩu trang cung ứng ra thị trường nhanh chóng tăng lên và vượt nhu cầu tiêu dùng. Trong trường hợp này, giá khẩu trang trên thị trường có xu hướng",
            "options": {
                "A": "tăng do cầu lớn hơn cung.",
                "B": "giảm do cung lớn hơn cầu.",
                "C": "tăng do chi phí sản xuất tăng.",
                "D": "giảm do Nhà nước can thiệp."
            },
            "correct_answer": "B",
            "explanation": "Theo quy luật cung - cầu, khi cung vượt cầu thì giá cả có xu hướng giảm."
        },
        {
            "question_number": 7,
            "section_id": "part_1",
            "question_type": "multiple_choice",
            "domain": "civics_law",
            "difficulty": "medium",
            "points": 0.25,
            "prompt": "Hành vi tố cáo sai sự thật có thể phải chịu trách nhiệm pháp lí nào sau đây?",
            "options": {
                "A": "Dân sự hoặc hình sự.",
                "B": "Hành chính hoặc kỉ luật.",
                "C": "Hành chính hoặc hình sự.",
                "D": "Dân sự hoặc kỉ luật."
            },
            "correct_answer": "C",
            "explanation": "Tùy tính chất và mức độ nguy hiểm, hành vi tố cáo sai sự thật bị xử phạt hành chính hoặc truy cứu trách nhiệm hình sự (Tội vu khống)."
        },
        {
            "question_number": 8,
            "section_id": "part_1",
            "question_type": "multiple_choice",
            "domain": "civics_law",
            "difficulty": "easy",
            "points": 0.25,
            "prompt": "Ông A mắc bệnh tâm thần nên không được phát thẻ cử tri, không được bầu cử Quốc hội và Hội đồng nhân dân các cấp. Điều này phù hợp với nguyên tắc bầu cử nào sau đây?",
            "options": {
                "A": "Phổ thông.",
                "B": "Bình đẳng.",
                "C": "Trực tiếp.",
                "D": "Bỏ phiếu kín."
            },
            "correct_answer": "A",
            "explanation": "Nguyên tắc phổ thông quy định mọi công dân đủ 18 tuổi đều có quyền bầu cử, trừ những người mất năng lực hành vi dân sự hoặc bị tước quyền theo luật định."
        },
        {
            "question_number": 9,
            "section_id": "part_1",
            "question_type": "multiple_choice",
            "domain": "civics_law",
            "difficulty": "easy",
            "points": 0.25,
            "prompt": "Từ khi thành lập đến nay, người lao động tại công ty cổ phần X được đóng đầy đủ, đúng quy định các loại bảo hiểm xã hội, bảo hiểm y tế, bảo hiểm thất nghiệp. Việc làm của công ty cổ phần X thể hiện trách nhiệm xã hội nào sau đây của doanh nghiệp?",
            "options": {
                "A": "Trách nhiệm pháp lí.",
                "B": "Trách nhiệm kinh tế.",
                "C": "Trách nhiệm từ thiện.",
                "D": "Trách nhiệm đạo đức."
            },
            "correct_answer": "A",
            "explanation": "Đóng BHXH, BHYT, BHTN theo luật định là nghĩa vụ bắt buộc, thuộc trách nhiệm pháp lí của doanh nghiệp."
        },
        {
            "question_number": 10,
            "section_id": "part_1",
            "question_type": "multiple_choice",
            "domain": "civics_law",
            "difficulty": "medium",
            "points": 0.25,
            "prompt": "Anh T kí hợp đồng lao động với thời hạn 3 năm tại doanh nghiệp N và được đóng đầy đủ bảo hiểm. Sau 11 tháng làm việc, anh muốn nghỉ việc để chuyển về gần nhà và hưởng trợ cấp bảo hiểm thất nghiệp. Anh T cần lựa chọn cách giải quyết nào sau đây để đạt được mong muốn của mình?",
            "options": {
                "A": "Xin nghỉ việc không lương.",
                "B": "Tiếp tục làm việc đến khi đủ 12 tháng đóng bảo hiểm thất nghiệp.",
                "C": "Đơn phương chấm dứt hợp đồng lao động.",
                "D": "Tiếp tục làm việc đến khi đủ 24 tháng đóng bảo hiểm xã hội."
            },
            "correct_answer": "B",
            "explanation": "Điều kiện hưởng trợ cấp thất nghiệp là phải đóng BHTN từ đủ 12 tháng trở lên trong vòng 24 tháng trước khi chấm dứt HĐLĐ."
        },
        {
            "question_number": 11,
            "section_id": "part_1",
            "question_type": "multiple_choice",
            "domain": "civics_law",
            "difficulty": "medium",
            "points": 0.25,
            "passage": "Bộ Lao động - Thương binh và Xã hội ước tính năm 2023, khoảng 155.000 lao động Việt Nam đi làm việc ở nước ngoài, tăng 8,55% so với năm 2022, mức cao nhất từ trước đến nay. Mỗi năm, bình quân từ 120.000 đến 143.000 lao động ra nước ngoài làm việc; lượng kiều hối từ lực lượng lao động này gửi về đạt 3,5 - 4 tỉ USD, góp phần thúc đẩy phát triển kinh tế - xã hội của đất nước.\n(Theo Báo Điện tử Chính phủ số ra ngày 30/12/2023)",
            "prompt": "Thông tin trên đề cập đến hoạt động kinh tế quốc tế nào sau đây?",
            "options": {
                "A": "Các dịch vụ thu ngoại tệ.",
                "B": "Thương mại quốc tế.",
                "C": "Đầu tư quốc tế.",
                "D": "Thoả thuận thương mại ưu đãi."
            },
            "correct_answer": "A",
            "explanation": "Xuất khẩu lao động và thu kiều hối thuộc nhóm các dịch vụ thu ngoại tệ trong quan hệ kinh tế quốc tế."
        },
        {
            "question_number": 12,
            "section_id": "part_1",
            "question_type": "multiple_choice",
            "domain": "civics_law",
            "difficulty": "medium",
            "passage": "Bộ Lao động - Thương binh và Xã hội ước tính năm 2023, khoảng 155.000 lao động Việt Nam đi làm việc ở nước ngoài, tăng 8,55% so với năm 2022, mức cao nhất từ trước đến nay. Mỗi năm, bình quân từ 120.000 đến 143.000 lao động ra nước ngoài làm việc; lượng kiều hối từ lực lượng lao động này gửi về đạt 3,5 - 4 tỉ USD, góp phần thúc đẩy phát triển kinh tế - xã hội của đất nước.\n(Theo Báo Điện tử Chính phủ số ra ngày 30/12/2023)",
            "prompt": "Nội dung nào sau đây không phản ánh vai trò của hoạt động kinh tế quốc tế trong thông tin trên?",
            "options": {
                "A": "Góp phần giải quyết việc làm, tăng thu nhập cho người lao động.",
                "B": "Đem lại nguồn thu ngoại tệ đáng kể cho đất nước.",
                "C": "Thúc đẩy phát triển kinh tế – xã hội của đất nước.",
                "D": "Giúp doanh nghiệp trong nước mở cửa thị trường hàng hóa thế giới."
            },
            "correct_answer": "D",
            "explanation": "Đoạn thông tin tập trung về xuất khẩu lao động và kiều hối, không đề cập đến việc mở cửa thị trường hàng hóa."
        },
        {
            "question_number": 13,
            "section_id": "part_1",
            "question_type": "multiple_choice",
            "domain": "civics_law",
            "difficulty": "medium",
            "points": 0.25,
            "prompt": "Theo quy định của pháp luật hiện hành, doanh nghiệp trốn thuế có thể phải chịu trách nhiệm pháp lí nào sau đây?",
            "options": {
                "A": "Hình sự và kỉ luật.",
                "B": "Hành chính và hình sự.",
                "C": "Hình sự và dân sự.",
                "D": "Kỉ luật và hành chính."
            },
            "correct_answer": "B",
            "explanation": "Hành vi trốn thuế bị xử phạt vi phạm hành chính, nếu nghiêm trọng sẽ bị xử lý hình sự (Điều 200 BLHS)."
        },
        {
            "question_number": 14,
            "section_id": "part_1",
            "question_type": "multiple_choice",
            "domain": "civics_law",
            "difficulty": "medium",
            "points": 0.25,
            "prompt": "Theo quy định của pháp luật hiện hành, người đi thuê vi phạm quyền và nghĩa vụ của công dân về sở hữu tài sản khi thực hiện hành vi nào sau đây?",
            "options": {
                "A": "Bảo quản và sử dụng tài sản đúng mục đích đã thoả thuận.",
                "B": "Thay đổi hiện trạng của tài sản khi được chủ sở hữu cho phép.",
                "C": "Trả lại tài sản thuê trong tình trạng phù hợp với mức độ khấu hao.",
                "D": "Cho người khác thuê mượn theo nhu cầu và sở thích."
            },
            "correct_answer": "D",
            "explanation": "Bên thuê không có quyền định đoạt hoặc tự ý cho thuê lại nếu không được sự đồng ý của chủ sở hữu."
        },
        {
            "question_number": 15,
            "section_id": "part_1",
            "question_type": "multiple_choice",
            "domain": "civics_law",
            "difficulty": "easy",
            "passage": "Ngày 7/12/2019, học sinh lớp 7 trường N đã tham gia hoạt động trải nghiệm tại Đền Kiếp Bạc (Hải Dương, nay là Hải Phòng). Tại đây, học sinh được tham gia nhiều hoạt động ý nghĩa do hướng dẫn viên chia sẻ và các thầy cô giáo tổ chức để tìm hiểu về lịch sử Việt Nam thời Nhà Trần và nhân vật Đức Thánh Trần. Qua các hoạt động ấy, học sinh thêm tự hào về truyền thống yêu nước chống giặc ngoại xâm của dân tộc ta và có nhiều ý tưởng mới cho các hoạt động tiếp theo tại trường như tổ chức thi vẽ tranh, viết bài chia sẻ, làm video... để quảng bá về giá trị văn hóa, lịch sử của ngôi đền này. Buổi trải nghiệm còn giúp học sinh nhận thấy rằng việc triển khai các dịch vụ phục vụ khách tham quan tại khu di tích là cần thiết để phát triển kinh tế địa phương, nhưng nếu không được quản lí tốt sẽ ảnh hưởng đến mỹ quan của khu di tích.",
            "prompt": "Hoạt động thăm quan, học tập tại Đền Kiếp Bạc của học sinh trường N trong thông tin trên thể hiện quyền của công dân trong bảo vệ di sản văn hoá ở nội dung nào sau đây?",
            "options": {
                "A": "Khai thác nguồn lợi kinh tế từ di sản.",
                "B": "Tham gia nghiên cứu và tôn tạo di sản.",
                "C": "Tham gia vào đời sống văn hoá của di sản.",
                "D": "Tiếp cận và hưởng thụ giá trị của di sản."
            },
            "correct_answer": "D",
            "explanation": "Học sinh đến tham quan, học tập và cảm nhận giá trị lịch sử là biểu hiện của quyền tiếp cận và hưởng thụ giá trị của di sản."
        },
        {
            "question_number": 16,
            "section_id": "part_1",
            "question_type": "multiple_choice",
            "domain": "civics_law",
            "difficulty": "medium",
            "passage": "Ngày 7/12/2019, học sinh lớp 7 trường N đã tham gia hoạt động trải nghiệm tại Đền Kiếp Bạc (Hải Dương, nay là Hải Phòng). Tại đây, học sinh được tham gia nhiều hoạt động ý nghĩa do hướng dẫn viên chia sẻ và các thầy cô giáo tổ chức để tìm hiểu về lịch sử Việt Nam thời Nhà Trần và nhân vật Đức Thánh Trần. Qua các hoạt động ấy, học sinh thêm tự hào về truyền thống yêu nước chống giặc ngoại xâm của dân tộc ta và có nhiều ý tưởng mới cho các hoạt động tiếp theo tại trường như tổ chức thi vẽ tranh, viết bài chia sẻ, làm video... để quảng bá về giá trị văn hóa, lịch sử của ngôi đền này. Buổi trải nghiệm còn giúp học sinh nhận thấy rằng việc triển khai các dịch vụ phục vụ khách tham quan tại khu di tích là cần thiết để phát triển kinh tế địa phương, nhưng nếu không được quản lí tốt sẽ ảnh hưởng đến mỹ quan của khu di tích.",
            "prompt": "Nhận định nào sau đây đúng nhất với tinh thần bảo vệ di sản văn hóa được thể hiện trong thông tin trên?",
            "options": {
                "A": "Khai thác dịch vụ tại di tích là cần thiết nên cần có chính sách ưu tiên.",
                "B": "Bảo vệ di sản văn hóa đồng nghĩa với hạn chế tối đa các hoạt động kinh tế.",
                "C": "Việc bảo vệ di sản văn hóa cần gắn với khai thác hợp lí và quản lí chặt chẽ.",
                "D": "Lực lượng chịu trách nhiệm phát triển du lịch là chính quyền địa phương."
            },
            "correct_answer": "C",
            "explanation": "Cần kết hợp hài hòa giữa bảo tồn, phát huy giá trị văn hóa và khai thác kinh tế hợp lý."
        },

        # Phần II: Đúng / Sai (3 câu - 3đ, 1đ/câu theo thang 0.1 -> 0.25 -> 0.5 -> 1.0)
        {
            "question_number": 17,
            "section_id": "part_2",
            "question_type": "true_false",
            "domain": "civics_law",
            "difficulty": "medium",
            "points": 1.0,
            "prompt": "Anh K kí hợp đồng cung cấp thịt lợn sạch cho doanh nghiệp V và doanh nghiệp X để sản xuất đồ hộp xuất khẩu. Mặc dù số lượng hàng tiêu thụ của doanh nghiệp mình nhiều hơn doanh nghiệp X, nhưng doanh nghiệp V vẫn gây sức ép buộc anh K phải chấm dứt hợp đồng với doanh nghiệp X, thậm chí còn thường xuyên đe dọa sẽ ngừng giao dịch nếu anh K không thực hiện các yêu cầu của mình. Xét tính Đúng / Sai:",
            "tf_statements": {
                "a": "Anh K muốn gia tăng lợi nhuận thì cần phải thỏa hiệp với doanh nghiệp V.",
                "b": "Doanh nghiệp X có thể viết đơn khiếu nại với cơ quan chức năng về hành vi của doanh nghiệp V.",
                "c": "Doanh nghiệp V có quyền ngừng giao dịch với anh K để gây sức ép.",
                "d": "Doanh nghiệp V có thể bị xử phạt hành chính và phát sinh trách nhiệm bồi thường thiệt hại theo quy định của pháp luật."
            },
            "correct_answer": {
                "a": "S",
                "b": "S",
                "c": "S",
                "d": "Đ"
            },
            "explanation": "Doanh nghiệp V có hành vi cạnh tranh không lành mạnh, vi phạm pháp luật nên có thể bị xử phạt hành chính và bồi thường thiệt hại (d Đúng). Các phương án a, b, c đều Sai."
        },
        {
            "question_number": 18,
            "section_id": "part_2",
            "question_type": "true_false",
            "domain": "civics_law",
            "difficulty": "medium",
            "points": 1.0,
            "prompt": "Công ty M có 100 nhân viên, trong đó 70 người được đóng bảo hiểm xã hội, 30 người không được đóng do chỉ kí hợp đồng có thời hạn 1 năm. Khi cơ quan bảo hiểm đến kiểm tra, công ty M đã giải thích lí do nhưng vẫn bị phạt 12% tổng số tiền bảo hiểm của 30 nhân viên chưa tham gia, tương đương 50.000.000 đồng. Công ty còn phải nộp số tiền bảo hiểm còn thiếu của 30 nhân viên này cùng với lãi suất chậm đóng. Xét tính Đúng / Sai:",
            "tf_statements": {
                "a": "Công ty M đã thực hiện đúng chính sách an sinh xã hội khi đóng bảo hiểm cho 70 nhân viên.",
                "b": "Công ty M phải chịu trách nhiệm dân sự với mức phạt tiền 12% tổng số tiền bảo hiểm phải đóng cho 30 nhân viên chưa được tham gia.",
                "c": "Cơ quan bảo hiểm xử phạt công ty M nhằm mục đích bảo vệ quyền được tham gia bảo hiểm xã hội của người lao động.",
                "d": "Việc bị xử phạt không làm chấm dứt nghĩa vụ của công ty M trong việc truy nộp đầy đủ số tiền bảo hiểm xã hội còn thiếu và khoản lãi phát sinh."
            },
            "correct_answer": {
                "a": "S",
                "b": "S",
                "c": "Đ",
                "d": "Đ"
            },
            "explanation": "a) Sai vì HĐLĐ 1 năm bắt buộc phải đóng BHXH. b) Sai vì đây là trách nhiệm hành chính chứ không phải dân sự. c và d Đúng theo Luật BHXH."
        },
        {
            "question_number": 19,
            "section_id": "part_2",
            "question_type": "true_false",
            "domain": "civics_law",
            "difficulty": "medium",
            "points": 1.0,
            "prompt": "Việc Việt Nam gia nhập Tổ chức Thương mại Thế giới (WTO) đã mở ra cơ hội kí kết nhiều Hiệp định Thương mại Tự do (FTA), đặc biệt là các FTA thế hệ mới. Những FTA này giúp mở rộng thị trường và thu hút vốn đầu tư trực tiếp nước ngoài (FDI) với cam kết sâu và cơ chế thực thi chặt chẽ. Các nước thành viên FTA được áp dụng thuế suất ưu đãi đặc biệt. Nhìn thấy cơ hội trong thách thức, doanh nghiệp D, chuyên xuất khẩu rau quả tại Việt Nam, đã cải tiến quy trình sản xuất, nâng cao chất lượng sản phẩm và công khai minh bạch nguồn gốc xuất xứ để đưa nhiều hàng hóa hơn vào thị trường các nước FTA. Xét tính Đúng / Sai:",
            "tf_statements": {
                "a": "Việc Việt Nam gia nhập WTO tạo điều kiện thúc đẩy doanh nghiệp D mở rộng xuất khẩu rau quả chất lượng cao.",
                "b": "Thuế suất ưu đãi đặc biệt là rào cản hạn chế doanh nghiệp xuất khẩu cạnh tranh tại thị trường các nước thành viên.",
                "c": "Doanh nghiệp D cải tiến quy trình sản xuất, nâng cao chất lượng sản phẩm là phù hợp với quy luật cạnh tranh trong hội nhập kinh tế quốc tế.",
                "d": "Thị trường các nước FTA không đòi hỏi cao về việc minh bạch nguồn gốc xuất xứ của nông sản nhập khẩu."
            },
            "correct_answer": {
                "a": "Đ",
                "b": "S",
                "c": "Đ",
                "d": "S"
            },
            "explanation": "a) Đúng: WTO và FTA thúc đẩy xuất khẩu. b) Sai: thuế ưu đãi là lợi thế chứ không phải rào cản. c) Đúng: nâng cao chất lượng phù hợp quy luật cạnh tranh. d) Sai: FTA đòi hỏi quy tắc xuất xứ rất nghiêm ngặt."
        },

        # Phần III: Tự luận (2 câu - 3đ, 1.5đ/câu)
        {
            "question_number": 20,
            "section_id": "part_3",
            "question_type": "essay",
            "domain": "civics_law",
            "difficulty": "medium",
            "points": 1.5,
            "prompt": "Hãy lựa chọn một sản phẩm kinh doanh mà bạn quan tâm và lập bản kế hoạch kinh doanh gồm 5 bước cơ bản (Ý tưởng và mục tiêu kinh doanh; Điều kiện thực hiện ý tưởng; Chiến lược kinh doanh; Cơ hội, rủi ro và biện pháp xử lí; Tóm tắt kế hoạch kinh doanh).",
            "correct_answer": "Thí sinh tự chọn 1 sản phẩm thực tế và trình bày đủ 5 bước theo barem: Nêu tên sản phẩm & giải thích lí do (0,5đ); Lập 5 bước kế hoạch kinh doanh (1,0đ).",
            "explanation": "Thang điểm: Nêu sản phẩm (0,25đ), giải thích lí do (0,25đ), ý tưởng mục tiêu (0,25đ), điều kiện thực hiện (0,25đ), chiến lược kinh doanh (0,25đ), rủi ro & giải pháp (0,25đ)."
        },
        {
            "question_number": 21,
            "section_id": "part_3",
            "question_type": "essay",
            "domain": "civics_law",
            "difficulty": "hard",
            "points": 1.5,
            "prompt": "Dựa trên các quy định của pháp luật về quyền và nghĩa vụ của công dân trong bảo vệ môi trường, hãy viết một bài tuyên truyền ngắn gửi đến cộng đồng nhằm nâng cao ý thức giữ gìn môi trường sống.",
            "correct_answer": "Trình bày: Mở đầu gắn với quyền và nghĩa vụ công dân (0,25đ); Nêu quy định quyền được sống trong môi trường trong lành và nghĩa vụ bảo vệ môi trường (0,5đ); Đưa ra ít nhất 3 luận điểm và giải pháp tuyên truyền (0,5đ); Thông điệp gắn với thiên nhiên (0,25đ).",
            "explanation": "Thang điểm 1,5đ chia theo 4 ý chính theo Bareme chính thức của ĐH Sư phạm Hà Nội."
        }
    ]
}


# --------------------------------------------------------------------------
# 7. SPT MÔN CÔNG NGHỆ (ĐỊNH HƯỚNG CÔNG NGHIỆP) (60 PHÚT - THANG 10)
# --------------------------------------------------------------------------
SPT_TECH_INDUSTRY_EXAM = {
    "id": "spt_sample_tech_industry",
    "title": "Đề Tham Khảo SPT ĐH Sư Phạm Hà Nội - Môn Công Nghệ Công Nghiệp (Mã đề 075)",
    "description": "Đề thi chính thức Kì thi ĐGNL ĐH Sư phạm Hà Nội. Cấu trúc 4 phần: Trắc nghiệm (16 câu), Đúng/Sai (2 câu 8 ý), Điền đáp số ngắn (4 câu), Tự luận (2 câu).",
    "exam_type": "spt",
    "subject": "tech_industry",
    "total_questions": 24,
    "duration_minutes": 60,
    "max_score": 10.0,
    "source": "spt_official_sample",
    "questions": [
        # Phần I: Trắc nghiệm (16 câu - 4đ, 0.25đ/câu)
        {
            "question_number": 1,
            "section_id": "part_1",
            "question_type": "multiple_choice",
            "domain": "tech_industry",
            "difficulty": "easy",
            "points": 0.25,
            "prompt": "Hình chiếu vuông góc của vật thể dưới đây tương ứng với hình nào?",
            "options": {
                "A": "Hình a.",
                "B": "Hình b.",
                "C": "Hình c.",
                "D": "Hình d."
            },
            "correct_answer": "B",
            "explanation": "Hình chiếu cạnh và hình chiếu đứng có đường nét đứt biểu diễn rãnh xuyên suốt tương ứng với Hình b."
        },
        {
            "question_number": 2,
            "section_id": "part_1",
            "question_type": "multiple_choice",
            "domain": "tech_industry",
            "difficulty": "medium",
            "points": 0.25,
            "prompt": "Xác định hình chiếu trục đo của vật thể được biểu diễn bởi các hình chiếu vuông góc đã cho.",
            "options": {
                "A": "Hình a",
                "B": "Hình b",
                "C": "Hình c",
                "D": "Hình d"
            },
            "correct_answer": "B",
            "explanation": "Đối chiếu các đường vát nghiêng và lỗ hình thoi ở giữa xác định được Hình b là hình chiếu trục đo chính xác."
        },
        {
            "question_number": 3,
            "section_id": "part_1",
            "question_type": "multiple_choice",
            "domain": "tech_industry",
            "difficulty": "easy",
            "points": 0.25,
            "prompt": "Khi thiết kế một chiếc điện thoại thông minh, yếu tố nào sau đây ít ảnh hưởng đến quá trình thiết kế kĩ thuật của sản phẩm?",
            "options": {
                "A": "Nhu cầu sử dụng của người tiêu dùng.",
                "B": "Chi phí sản xuất và vật liệu.",
                "C": "Tiến bộ công nghệ trong ngành sản xuất.",
                "D": "Màu sắc yêu thích của nhà thiết kế."
            },
            "correct_answer": "D",
            "explanation": "Màu sắc yêu thích mang tính chủ quan của cá nhân nhà thiết kế ít ảnh hưởng; thiết kế kĩ thuật phải dựa trên thị hiếu khách hàng và công nghệ sản xuất."
        },
        {
            "question_number": 4,
            "section_id": "part_1",
            "question_type": "multiple_choice",
            "domain": "tech_industry",
            "difficulty": "easy",
            "points": 0.25,
            "prompt": "Để chế tạo một trục truyền động của xe đạp có độ bền cao và khả năng chịu lực tốt, vật liệu nào sau đây là lựa chọn phù hợp nhất?",
            "options": {
                "A": "Nhôm",
                "B": "Thép hợp kim",
                "C": "Nhựa PVC",
                "D": "Đồng"
            },
            "correct_answer": "B",
            "explanation": "Thép hợp kim có độ bền kéo, giới hạn chảy và khả năng chịu va đập, chịu xoắn tốt nhất cho trục truyền động."
        },
        {
            "question_number": 5,
            "section_id": "part_1",
            "question_type": "multiple_choice",
            "domain": "tech_industry",
            "difficulty": "easy",
            "points": 0.25,
            "prompt": "Nhà máy sản xuất xe đạp lên kế hoạch chế tạo khung xe từ phôi là các ống thép. Công nghệ thường được sử dụng để ghép các ống thép tạo thành khung xe đạp là",
            "options": {
                "A": "công nghệ đúc.",
                "B": "công nghệ cắt gọt kim loại.",
                "C": "công nghệ gia công áp lực.",
                "D": "công nghệ hàn."
            },
            "correct_answer": "D",
            "explanation": "Ghép các ống kim loại thành khung kín chịu lực được thực hiện bằng phương pháp hàn (hàn TIG/MIG hoặc hàn hơi)."
        },
        {
            "question_number": 6,
            "section_id": "part_1",
            "question_type": "multiple_choice",
            "domain": "tech_industry",
            "difficulty": "easy",
            "points": 0.25,
            "prompt": "Khi động cơ đốt trong làm việc ở kì cháy giãn nở, cơ cấu trục khuỷu thanh truyền biến chuyển động tịnh tiến của pít tông thành chuyển động nào của trục khuỷu động cơ?",
            "options": {
                "A": "Tịnh tiến",
                "B": "Quay",
                "C": "Lắc",
                "D": "Thẳng"
            },
            "correct_answer": "B",
            "explanation": "Cơ cấu trục khuỷu thanh truyền biến chuyển động tịnh tiến khứ hồi của pít tông thành chuyển động quay tròn của trục khuỷu."
        },
        {
            "question_number": 7,
            "section_id": "part_1",
            "question_type": "multiple_choice",
            "domain": "tech_industry",
            "difficulty": "medium",
            "points": 0.25,
            "prompt": "Ở động cơ đốt trong 4 kì, để thực hiện 1 chu trình công tác, trục khuỷu quay bao nhiêu độ và có mấy lần sinh công?",
            "options": {
                "A": "720° và 1 lần",
                "B": "360° và 2 lần",
                "C": "180° và 1 lần",
                "D": "180° và 2 lần"
            },
            "correct_answer": "A",
            "explanation": "Động cơ 4 kì thực hiện 4 hành trình của pít tông tương ứng với 2 vòng quay trục khuỷu (720°) và chỉ có 1 kì sinh công (kì cháy giãn nở)."
        },
        {
            "question_number": 8,
            "section_id": "part_1",
            "question_type": "multiple_choice",
            "domain": "tech_industry",
            "difficulty": "medium",
            "points": 0.25,
            "prompt": "Khi ô tô chuyển hướng trên đường, bộ phận nào có nhiệm vụ phân phối mômen đến hai bán trục của các bánh xe chủ động để bánh xe quay với tốc độ khác nhau?",
            "options": {
                "A": "Hộp số",
                "B": "Truyền lực các đăng",
                "C": "Bộ vi sai",
                "D": "Bộ li hợp"
            },
            "correct_answer": "C",
            "explanation": "Bộ vi sai cho phép hai bánh xe chủ động quay với vận tốc góc khác nhau khi xe vào cua mà vẫn nhận được mômen từ động cơ."
        },
        {
            "question_number": 9,
            "section_id": "part_1",
            "question_type": "multiple_choice",
            "domain": "tech_industry",
            "difficulty": "easy",
            "points": 0.25,
            "prompt": "Dây nối đất trong hệ thống điện có vai trò gì?",
            "options": {
                "A": "Tăng cường hiệu suất hoạt động của thiết bị điện.",
                "B": "Dẫn dòng điện rò xuống đất để tránh điện giật.",
                "C": "Ổn định điện áp trong hệ thống điện.",
                "D": "Giảm lượng điện năng tiêu thụ của hệ thống điện."
            },
            "correct_answer": "B",
            "explanation": "Dây tiếp địa dẫn dòng rò từ vỏ kim loại của thiết bị xuống đất, đảm bảo an toàn tính mạng cho người sử dụng."
        },
        {
            "question_number": 10,
            "section_id": "part_1",
            "question_type": "multiple_choice",
            "domain": "tech_industry",
            "difficulty": "easy",
            "points": 0.25,
            "prompt": "Khi thiết kế sơ đồ nguyên lí cho mạch điện cầu thang, điều khiển một đèn từ hai vị trí, cần dùng",
            "options": {
                "A": "02 công tắc hai cực.",
                "B": "02 công tắc ba cực.",
                "C": "01 công tắc hai cực và 01 công tắc ba cực.",
                "D": "01 cầu dao tự động."
            },
            "correct_answer": "B",
            "explanation": "Mạch cầu thang tiêu chuẩn sử dụng 2 công tắc 3 cực (công tắc chuyển mạch 2 chiều)."
        },
        {
            "question_number": 11,
            "section_id": "part_1",
            "question_type": "multiple_choice",
            "domain": "tech_industry",
            "difficulty": "medium",
            "points": 0.25,
            "prompt": "Một điện trở trên thân có các vòng màu theo thứ tự: nâu – đen – đỏ – nhũ bạc. Trị số điện trở của linh kiện này là",
            "options": {
                "A": "100 Ω ± 5%.",
                "B": "100 KΩ ± 10%.",
                "C": "10 KΩ ± 5%.",
                "D": "1 KΩ ± 10%."
            },
            "correct_answer": "D",
            "explanation": "Nâu (1), Đen (0), Đỏ (10^2 = 100), Nhũ bạc (±10%) -> R = 10 * 100 Ω = 1000 Ω = 1 kΩ ± 10%."
        },
        {
            "question_number": 12,
            "section_id": "part_1",
            "question_type": "multiple_choice",
            "domain": "tech_industry",
            "difficulty": "easy",
            "points": 0.25,
            "prompt": "Một thiết bị gia nhiệt bằng điện trở có công suất 1000W được sử dụng liên tục trong 2 giờ mỗi ngày. Lượng điện năng tiêu thụ trong một tháng có 30 ngày của thiết bị điện đó là",
            "options": {
                "A": "30 kWh.",
                "B": "60 kWh.",
                "C": "300 kWh.",
                "D": "600 kWh."
            },
            "correct_answer": "B",
            "explanation": "A = P * t = 1 kW * (2 * 30 h) = 60 kWh."
        },
        {
            "question_number": 13,
            "section_id": "part_1",
            "question_type": "multiple_choice",
            "domain": "tech_industry",
            "difficulty": "medium",
            "points": 0.25,
            "prompt": "Mạch so sánh sử dụng khuếch đại thuật toán (Op-Amp) có điện áp UR gần bằng điện áp nguồn +E khi",
            "options": {
                "A": "U_V < U_N",
                "B": "U_V > U_N",
                "C": "U_V = +E và U_N = 0",
                "D": "U_V = 0 và U_N = -E"
            },
            "correct_answer": "B",
            "explanation": "Khi điện áp vào cửa không đảo (U_V) lớn hơn điện áp vào cửa đảo (U_N), đầu ra bão hòa dương: UR ≈ +E."
        },
        {
            "question_number": 14,
            "section_id": "part_1",
            "question_type": "multiple_choice",
            "domain": "tech_industry",
            "difficulty": "easy",
            "points": 0.25,
            "prompt": "Khi hoạt động ở điện áp định mức 220V, dòng điện đi qua thiết bị nào dưới đây có giá trị lớn nhất?",
            "options": {
                "A": "Quạt điện 50W",
                "B": "Đèn LED 20W",
                "C": "Máy nước nóng 2000W",
                "D": "Máy sấy tóc 800W"
            },
            "correct_answer": "C",
            "explanation": "Với cùng hiệu điện thế U = 220V, dòng điện tỉ lệ thuận với công suất: I = P/U. Máy nước nóng 2000W có P lớn nhất nên I lớn nhất (~9,1A)."
        },
        {
            "question_number": 15,
            "section_id": "part_1",
            "question_type": "multiple_choice",
            "domain": "tech_industry",
            "difficulty": "medium",
            "points": 0.25,
            "prompt": "Mạch logic kết hợp trong sơ đồ sử dụng các loại cổng logic cơ bản nào?",
            "options": {
                "A": "AND và OR",
                "B": "NAND và OR",
                "C": "AND và NOR",
                "D": "NAND và NOR"
            },
            "correct_answer": "B",
            "explanation": "Cổng thứ nhất có vòng tròn đảo ở đầu ra là cổng NAND, cổng thứ hai có dạng cung tròn là cổng OR."
        },
        {
            "question_number": 16,
            "section_id": "part_1",
            "question_type": "multiple_choice",
            "domain": "tech_industry",
            "difficulty": "medium",
            "points": 0.25,
            "prompt": "Theo sơ đồ mạch điện điều khiển đèn LED sử dụng vi điều khiển (chân anode của LED nối chân 10, chân cathode nối chân 2), để LED sáng thì cần lập trình xác lập mức logic đầu ra cho chân 2 và chân 10 lần lượt là:",
            "options": {
                "A": "0 và 0.",
                "B": "0 và 1.",
                "C": "1 và 0.",
                "D": "1 và 1."
            },
            "correct_answer": "B",
            "explanation": "Để LED phân cực thuận phát sáng, anode (chân 10) phải ở mức HIGH (1) và cathode (chân 2) phải ở mức LOW (0). Lần lượt chân 2 và chân 10 là 0 và 1."
        },

        # Phần II: Đúng / Sai (2 câu - 2đ, 1đ/câu theo thang 0.1 -> 0.25 -> 0.5 -> 1.0)
        {
            "question_number": 17,
            "section_id": "part_2",
            "question_type": "true_false",
            "domain": "tech_industry",
            "difficulty": "medium",
            "points": 1.0,
            "prompt": "Cho mạch điện xoay chiều 3 pha đối xứng có sơ đồ: Nguồn điện 3 pha có điện áp dây Ud = 380V. Tải 1 là một lò điện trở 3 pha, điện trở mỗi pha là 76Ω. Tải 2 là ba bóng đèn loại 100W-220V. Xét tính Đúng / Sai:",
            "tf_statements": {
                "a": "Tải 1 nối tam giác (Δ), tải 2 nối hình sao (Y) có dây trung tính.",
                "b": "Dòng điện qua mỗi bóng đèn là 2,2A.",
                "c": "Dòng điện trên một pha của lò điện trở là 15A.",
                "d": "Nếu lò điện trở làm việc trong 2 giờ sẽ tiêu thụ lượng điện năng là 11,4 kWh."
            },
            "correct_answer": {
                "a": "Đ",
                "b": "S",
                "c": "S",
                "d": "Đ"
            },
            "explanation": "a) Đúng theo sơ đồ. b) Sai vì Iđèn = P/U = 100/220 ≈ 0,45A. c) Sai vì Up = Ud = 380V -> Ip = 380/76 = 5A. d) Đúng: P = 3 * (380^2 / 76) = 5700W = 5,7 kW -> A = 5,7 * 2 = 11,4 kWh."
        },
        {
            "question_number": 18,
            "section_id": "part_2",
            "question_type": "true_false",
            "domain": "tech_industry",
            "difficulty": "medium",
            "points": 1.0,
            "prompt": "Bình dự định thiết kế một mạch điện chiếu sáng tự động cho hành lang. Mạch điện sử dụng cảm biến ánh sáng, cảm biến chuyển động và cổng logic cơ bản. Đèn chỉ bật khi trời tối và có người đi chuyển đến gần hành lang. Khi mạch hoạt động, tín hiệu đầu ra từ cảm biến ánh sáng ở mức logic '1' khi trời tối và '0' khi trời sáng. Tương tự, tín hiệu đầu ra từ cảm biến chuyển động ở mức '1' khi có người và '0' khi ngược lại. Xét tính Đúng / Sai:",
            "tf_statements": {
                "a": "Cảm biến ánh sáng sẽ gửi tín hiệu để bật đèn sáng khi phát hiện trời tối, ngay cả khi không có người đi chuyển đến gần hành lang.",
                "b": "Cổng logic được sử dụng trong mạch điện trên là cổng AND.",
                "c": "Rơ le được điều khiển bởi tín hiệu đầu ra của cổng logic, chỉ bật đèn khi tín hiệu đầu ra của cổng logic ở mức '0'.",
                "d": "Nếu sử dụng cổng OR trong mạch điện trên thì đèn chỉ tắt khi trời sáng và không có người chuyển tới."
            },
            "correct_answer": {
                "a": "S",
                "b": "Đ",
                "c": "S",
                "d": "Đ"
            },
            "explanation": "b) Đúng vì đèn chỉ bật khi CẢ HAI điều kiện cùng thỏa mãn (trời tối VÀ có người). d) Đúng vì với cổng OR, đầu ra là 0 (đèn tắt) chỉ khi cả hai đầu vào đều là 0 (trời sáng và không có người). a và c Sai."
        },

        # Phần III: Điền kết quả ngắn (4 câu - 1đ, 0.25đ/câu)
        {
            "question_number": 19,
            "section_id": "part_3",
            "question_type": "short_answer",
            "domain": "tech_industry",
            "difficulty": "easy",
            "points": 0.25,
            "prompt": "Tính dòng điện định mức của một bình đun nước nóng có công suất 2500W, điện áp định mức 220V. (Viết kết quả làm tròn đến 2 chữ số thập phân)",
            "correct_answer": "11.36",
            "accepted_answers": ["11.36", "11,36", "11.36A", "11,36 A", "11.36 A"],
            "explanation": "I = P / U = 2500 / 220 ≈ 11,36 A."
        },
        {
            "question_number": 20,
            "section_id": "part_3",
            "question_type": "short_answer",
            "domain": "tech_industry",
            "difficulty": "medium",
            "points": 0.25,
            "prompt": "Cho mạch điện xoay chiều ba pha đối xứng, tải nối hình sao. Dòng điện đo được trên pha A là 5A và coi góc pha đầu của pha A bằng 0 rad. Viết biểu thức giá trị tức thời của dòng điện trên pha C.",
            "correct_answer": "5√2 sin(ωt + 2π/3)",
            "accepted_answers": ["5√2 sin(ωt + 2π/3)", "5√2sin(ωt+2π/3)", "5*sqrt(2)*sin(wt+2pi/3)", "5sqrt(2)sin(wt+2pi/3)"],
            "explanation": "Dòng điện pha C vượt trước pha A một góc 2π/3 (hoặc trễ 4π/3), iC = 5√2 sin(ωt + 2π/3) A."
        },
        {
            "question_number": 21,
            "section_id": "part_3",
            "question_type": "short_answer",
            "domain": "tech_industry",
            "difficulty": "medium",
            "points": 0.25,
            "prompt": "Viết biểu thức logic cho mạch tổ hợp gồm cổng OR nhận đầu vào X1, X2 và cổng AND nhận đầu vào từ cổng OR và biến X3 qua cổng đảo NOT.",
            "correct_answer": "Y = (X1 + X2).X3'",
            "accepted_answers": ["Y = (X1 + X2).X3'", "(X1 + X2).X3'", "Y = (X1 + X2).~X3", "(X1+X2)*!X3", "(X1+X2).X3_bar"],
            "explanation": "Đầu ra cổng OR là (X1 + X2), đầu vào thứ hai của cổng AND là NOT(X3) = X3'. Do đó Y = (X1 + X2).X3'."
        },
        {
            "question_number": 22,
            "section_id": "part_3",
            "question_type": "short_answer",
            "domain": "tech_industry",
            "difficulty": "medium",
            "points": 0.25,
            "prompt": "Sử dụng Vôn kế để đo điện áp giữa hai chân 8 và 13 của một vi điều khiển. Chân 13 nối que đỏ được lập trình mức thấp (0V), chân 8 nối que đen được lập trình mức cao (5V). Giá trị điện áp đo được trên Vôn kế là bao nhiêu Vôn?",
            "correct_answer": "-5",
            "accepted_answers": ["-5", "-5V", "-5 V"],
            "explanation": "Vôn kế đo hiệu điện thế V_que_đỏ - V_que_đen = V_chân13 - V_chân8 = 0V - 5V = -5V."
        },

        # Phần IV: Tự luận (2 câu - 3đ, 1.5đ/câu)
        {
            "question_number": 23,
            "section_id": "part_4",
            "question_type": "essay",
            "domain": "tech_industry",
            "difficulty": "medium",
            "points": 1.5,
            "prompt": "Mạng điện gia đình 220V gồm 2 nhánh: Nhánh 1 (phòng khách & bếp): 6 đèn LED (40W), 1 quạt trần (120W), 1 ti vi (100W), 1 bếp điện (1500W), 1 tủ lạnh (180W). Nhánh 2 (phòng ngủ): 2 đèn LED (25W), 1 quạt treo tường (100W). Biết đèn LED, ti vi, bếp điện có cosφ=1; các thiết bị còn lại có cosφ=0,8.\na) Tính tổng công suất định mức mỗi nhánh.\nb) Tính dòng điện mỗi nhánh khi các thiết bị cùng làm việc.\nc) Tính tiết diện dây dẫn của mỗi nhánh nếu sử dụng dây dẫn với mật độ dòng điện cho phép J = 5 A/mm².",
            "correct_answer": "a) P_pkb = 2140W, P_pn = 150W.\nb) I_pkb ≈ 10,06 A; I_pn ≈ 0,8 A.\nc) S_pkb = 10,06 / 5 ≈ 2,012 mm²; S_pn = 0,8 / 5 = 0,16 mm².",
            "explanation": "Thang điểm 1,5đ: a) 0,5đ (mỗi nhánh 0,25đ); b) 0,5đ (mỗi nhánh 0,25đ); c) 0,5đ (mỗi nhánh 0,25đ)."
        },
        {
            "question_number": 24,
            "section_id": "part_4",
            "question_type": "essay",
            "domain": "tech_industry",
            "difficulty": "hard",
            "points": 1.5,
            "prompt": "Cho mạch khuếch đại thuật toán đảo với điện trở vào R1 và điện trở hồi tiếp R2:\na) Xác định công thức tính hệ số khuếch đại KU của mạch.\nb) Cho UV = 1V; R1 = 1 kΩ; R2 = 10 kΩ. Xác định giá trị của UR.\nc) Xác định hệ số khuếch đại của mạch khi R1 = R2. Nêu nhận xét về quan hệ giữa tín hiệu vào và tín hiệu ra trong trường hợp này.",
            "correct_answer": "a) KU = -R2 / R1.\nb) UR = -(R2/R1) * UV = -(10/1) * 1V = -10V.\nc) Khi R1 = R2 thì KU = -1. Tín hiệu ra có cùng biên độ nhưng ngược pha so với tín hiệu vào.",
            "explanation": "Thang điểm 1,5đ: ý a) 0,25đ; ý b) 0,25đ; ý c) 1,0đ (tính Ku 0,5đ, giải thích đồ thị đảo pha 0,5đ)."
        }
    ]
}


# --------------------------------------------------------------------------
# 8. SPT MÔN CÔNG NGHỆ (ĐỊNH HƯỚNG NÔNG NGHIỆP) (60 PHÚT - THANG 10)
# --------------------------------------------------------------------------
SPT_TECH_AGRICULTURE_EXAM = {
    "id": "spt_sample_tech_agriculture",
    "title": "Đề Tham Khảo SPT ĐH Sư Phạm Hà Nội - Môn Công Nghệ Nông Nghiệp (Mã đề 075)",
    "description": "Đề thi chính thức Kì thi ĐGNL ĐH Sư phạm Hà Nội. Cấu trúc 4 phần: Trắc nghiệm (16 câu), Đúng/Sai (2 câu 8 ý), Điền đáp số ngắn (4 câu), Tự luận (2 câu).",
    "exam_type": "spt",
    "subject": "tech_agriculture",
    "total_questions": 24,
    "duration_minutes": 60,
    "max_score": 10.0,
    "source": "spt_official_sample",
    "questions": [
        # Phần I: Trắc nghiệm (16 câu - 4đ, 0.25đ/câu)
        {
            "question_number": 1,
            "section_id": "part_1",
            "question_type": "multiple_choice",
            "domain": "tech_agriculture",
            "difficulty": "easy",
            "points": 0.25,
            "prompt": "Phát biểu nào sau đây không đúng khi nói về vai trò của trồng trọt?",
            "options": {
                "A": "Cung cấp thức ăn cho chăn nuôi và nguyên liệu cho công nghiệp chế biến.",
                "B": "Đảm bảo an ninh lương thực quốc gia, giúp hạn chế tình trạng thiếu lương thực.",
                "C": "Nhiều sản phẩm trồng trọt được xuất khẩu đem lại hiệu quả kinh tế cao.",
                "D": "Cung cấp nguồn thực phẩm giàu protein cho tiêu dùng và xuất khẩu."
            },
            "correct_answer": "D",
            "explanation": "Cung cấp nguồn protein chủ yếu là vai trò của ngành chăn nuôi và thủy sản; trồng trọt chủ yếu cung cấp tinh bột, vitamin, khoáng chất."
        },
        {
            "question_number": 2,
            "section_id": "part_1",
            "question_type": "multiple_choice",
            "domain": "tech_agriculture",
            "difficulty": "easy",
            "points": 0.25,
            "prompt": "Việc ứng dụng thiết bị bay không người lái trong phun thuốc bảo vệ thực vật thể hiện ưu điểm nào sau đây?",
            "options": {
                "A": "Giúp người nông dân không phải kiểm tra đồng ruộng.",
                "B": "Tăng hiệu quả tiêu diệt sâu, bệnh hại của thuốc bảo vệ thực vật.",
                "C": "Tiết kiệm lượng thuốc và giảm thiểu độc hại cho con người.",
                "D": "Tăng nồng độ thuốc hóa học để tiêu diệt sâu bệnh nhanh hơn."
            },
            "correct_answer": "B",
            "explanation": "Thiết bị bay phun sương mịn, đều trên diện rộng, bám dính tốt giúp tăng tối đa hiệu quả phòng trừ sâu bệnh hại."
        },
        {
            "question_number": 3,
            "section_id": "part_1",
            "question_type": "multiple_choice",
            "domain": "tech_agriculture",
            "difficulty": "medium",
            "points": 0.25,
            "prompt": "Một nhóm học sinh được giao nhiệm vụ trồng cây cà chua bằng kĩ thuật thủy canh. Hãy sắp xếp các bước tiến hành dưới đây sao cho đúng thứ tự:\n(1). Chuẩn bị thùng đựng dịch dinh dưỡng; rọ trồng cây; giá thể trồng cây.\n(2). Điều chỉnh pH của dịch dinh dưỡng đã pha (pH = 5,5 - 6,5).\n(3). Pha dung dịch dinh dưỡng theo tỉ lệ hướng dẫn.\n(4). Trồng cây vào rọ giá thể, đảm bảo bộ rễ ngập trong dịch dinh dưỡng.\n(5). Chọn cây giống khỏe mạnh, không bị dập nát.\n(6). Theo dõi sự sinh trưởng của cây cà chua thủy canh.",
            "options": {
                "A": "(1) – (3) – (2) – (5) – (4) – (6).",
                "B": "(1) – (2) – (3) – (5) – (4) – (6).",
                "C": "(1) – (3) – (2) – (4) – (5) – (6).",
                "D": "(1) – (5) – (2) – (4) – (3) – (6)."
            },
            "correct_answer": "A",
            "explanation": "Chuẩn bị dụng cụ (1) -> Pha dinh dưỡng (3) -> Chỉnh pH (2) -> Chọn giống (5) -> Trồng vào rọ (4) -> Theo dõi (6)."
        },
        {
            "question_number": 4,
            "section_id": "part_1",
            "question_type": "multiple_choice",
            "domain": "tech_agriculture",
            "difficulty": "medium",
            "points": 0.25,
            "prompt": "Những biện pháp nào sau đây giúp bảo vệ môi trường trong trồng trọt?\n1. Tăng cường sử dụng phân bón hóa học trong trồng trọt vì hiệu quả nhanh chóng.\n2. Tăng cường sử dụng phân bón hữu cơ, phân bón vi sinh trong trồng trọt.\n3. Súc rửa chai lọ thuốc bảo vệ thực vật ở mương, ao, hồ,...\n4. Sử dụng thuốc trừ sâu sinh học thay thế thuốc trừ sâu hóa học.\n5. Sử dụng hợp lí phân bón và thuốc bảo vệ thực vật.\n6. Đốt rơm, rạ trên đồng ruộng sau mỗi vụ thu hoạch.",
            "options": {
                "A": "1, 3, 5",
                "B": "2, 5, 6",
                "C": "2, 4, 5",
                "D": "4, 5, 6"
            },
            "correct_answer": "C",
            "explanation": "Các biện pháp thân thiện môi trường là 2 (phân hữu cơ/vi sinh), 4 (thuốc sinh học), 5 (sử dụng hợp lý)."
        },
        {
            "question_number": 5,
            "section_id": "part_1",
            "question_type": "multiple_choice",
            "domain": "tech_agriculture",
            "difficulty": "easy",
            "points": 0.25,
            "prompt": "Một cơ sở chăn nuôi gà với quy mô lớn và tập trung, hệ thống chuồng nuôi khép kín, kiểm soát dịch bệnh chặt chẽ. Sử dụng máy móc, thiết bị tự động trong cho ăn, uống nước, điều hòa nhiệt độ, chiếu sáng, và thu gom chất thải. Phương thức chăn nuôi nào phù hợp với mô tả trên?",
            "options": {
                "A": "Chăn thả tự do.",
                "B": "Chăn nuôi bán công nghiệp.",
                "C": "Chăn thả kết hợp.",
                "D": "Chăn nuôi công nghiệp."
            },
            "correct_answer": "D",
            "explanation": "Chăn nuôi chuồng kín, quy mô lớn tập trung, tự động hóa toàn diện là phương thức chăn nuôi công nghiệp."
        },
        {
            "question_number": 6,
            "section_id": "part_1",
            "question_type": "multiple_choice",
            "domain": "tech_agriculture",
            "difficulty": "easy",
            "points": 0.25,
            "prompt": "Bước thực hiện nào sau đây có trong quy trình chăn nuôi theo tiêu chuẩn VietGAP mà không có trong quy trình chăn nuôi truyền thống?",
            "options": {
                "A": "Chuẩn bị con giống tốt.",
                "B": "Lưu trữ hồ sơ – kiểm tra nội bộ.",
                "C": "Chuẩn bị chuồng nuôi và các thiết bị cần thiết.",
                "D": "Nuôi dưỡng và chăm sóc."
            },
            "correct_answer": "B",
            "explanation": "Quy trình VietGAP yêu cầu nghiêm ngặt việc ghi chép nhật ký sản xuất, lưu trữ hồ sơ và đánh giá nội bộ để truy xuất nguồn gốc."
        },
        {
            "question_number": 7,
            "section_id": "part_1",
            "question_type": "multiple_choice",
            "domain": "tech_agriculture",
            "difficulty": "easy",
            "points": 0.25,
            "prompt": "Một cơ sở chăn nuôi muốn nuôi đàn lợn thịt nội địa với mật độ 10 con/6 m². Họ chuẩn bị chuồng nuôi có diện tích 168,0 m². Số lượng lợn thích hợp để nuôi theo mật độ và diện tích như mô tả ở trên là bao nhiêu con?",
            "options": {
                "A": "280 con.",
                "B": "380 con.",
                "C": "400 con.",
                "D": "450 con."
            },
            "correct_answer": "A",
            "explanation": "Số con = (168 / 6) * 10 = 28 * 10 = 280 con."
        },
        {
            "question_number": 8,
            "section_id": "part_1",
            "question_type": "multiple_choice",
            "domain": "tech_agriculture",
            "difficulty": "easy",
            "points": 0.25,
            "prompt": "Một hộ gia đình mong muốn mở rộng quy mô chăn nuôi bò. Khi đó họ cần quản lý tốt chất thải, vì khi lượng chất thải gia tăng có thể gây ô nhiễm nghiêm trọng cho đất đai, nguồn nước và không khí xung quanh. Ngoài ra họ còn muốn tận dụng nguồn chất thải cho nhiều mục đích khác. Biện pháp nào sau đây sẽ giúp họ thực hiện được hiệu quả các mong muốn trên?",
            "options": {
                "A": "Xây dựng bể chứa để chất thải tự tách nước và lắng đọng.",
                "B": "Xây dựng hầm biogas để xử lí chất thải chăn nuôi.",
                "C": "Đào hố chứa phân sau đó bổ sung thêm phụ phẩm trồng trọt.",
                "D": "Đào hố chứa phân có lát xi măng và phủ bạt."
            },
            "correct_answer": "B",
            "explanation": "Hầm biogas vừa xử lý triệt để mầm bệnh và mùi hôi, vừa tạo khí sinh học làm chất đốt và bã thải làm phân bón hữu cơ chất lượng cao."
        },
        {
            "question_number": 9,
            "section_id": "part_1",
            "question_type": "multiple_choice",
            "domain": "tech_agriculture",
            "difficulty": "medium",
            "points": 0.25,
            "prompt": "Quế (Cinnamomum verum) là loài cây gỗ, thường được trồng thành rừng thuần loài. Gỗ màu nâu nhạt, mịn, thường dùng để xẻ ván, đóng đồ. Vỏ thân, lá chứa nhiều tinh dầu được chiết xuất dùng trong công nghệ dược liệu và thực phẩm. Tổ hợp nào sau đây đúng về vai trò của cây quế đối với tự nhiên và con người?\n1. Quế là loài dược liệu thuộc nhóm lâm sản ngoài gỗ.\n2. Quế là loài cây trồng đa mục tiêu.\n3. Cung cấp nguồn thức ăn cho gia súc chăn thả dưới tán rừng.\n4. Trồng quế có khả năng bảo vệ đất, hạn chế xói mòn.\n5. Khả năng bảo vệ đất của rừng quế cao hơn so với rừng tự nhiên do chiều cao cây lớn, đồng đều.",
            "options": {
                "A": "1, 2, 3",
                "B": "1, 2, 4",
                "C": "2, 3, 4",
                "D": "2, 4, 5"
            },
            "correct_answer": "B",
            "explanation": "Các nhận định đúng là 1, 2, 4. Nhận định 3 sai (lá/vỏ chứa tinh dầu cay gia súc không ăn); nhận định 5 sai (rừng thuần loài giữ đất kém hơn rừng tự nhiên đa tầng)."
        },
        {
            "question_number": 10,
            "section_id": "part_1",
            "question_type": "multiple_choice",
            "domain": "tech_agriculture",
            "difficulty": "easy",
            "points": 0.25,
            "prompt": "Một trong những vấn đề người trồng rừng phải đối mặt là chu kì khai thác tài nguyên gỗ rất dài, điều đó đã gây khó khăn cho đời sống của người dân. Để nâng cao hiệu quả kinh tế trên một đơn vị diện tích rừng và có thu nhập thường xuyên, người trồng rừng nên thực hiện giải pháp nào dưới đây?",
            "options": {
                "A": "Chăn thả gia súc dưới tán rừng làm tăng lượng phân bón thúc đẩy cây rừng sinh trưởng.",
                "B": "Khai thác và sử dụng bền vững các loài cây ngắn ngày dưới tán rừng như cây dược liệu.",
                "C": "Khai thác chọn các cây gỗ lớn để thu hoạch trước.",
                "D": "Trồng xen canh cây gỗ và cây lương thực như ngô hay lúa."
            },
            "correct_answer": "B",
            "explanation": "Trồng và thu hoạch cây dược liệu, cây lâm sản ngoài gỗ dưới tán rừng là giải pháp 'lấy ngắn nuôi dài' hiệu quả và bền vững."
        },
        {
            "question_number": 11,
            "section_id": "part_1",
            "question_type": "multiple_choice",
            "domain": "tech_agriculture",
            "difficulty": "easy",
            "points": 0.25,
            "prompt": "Xu hướng tăng tỉ lệ nuôi, trồng, giảm tỉ lệ khai thác thủy sản nhằm mục đích chính nào sau đây?",
            "options": {
                "A": "Tạo thêm nhiều việc làm cho người lao động.",
                "B": "Tăng cơ hội áp dụng các công nghệ cao trong nuôi, trồng thủy sản nhằm nâng cao hiệu quả kinh tế.",
                "C": "Hạn chế nguy cơ làm suy giảm nguồn lợi thủy sản để phát triển thủy sản bền vững.",
                "D": "Cung cấp nguồn nguyên liệu chất lượng cao phục vụ cho chế biến và xuất khẩu thủy sản."
            },
            "correct_answer": "C",
            "explanation": "Chuyển dịch từ khai thác tự nhiên sang nuôi trồng có kiểm soát nhằm bảo tồn và phục hồi nguồn lợi sinh vật biển."
        },
        {
            "question_number": 12,
            "section_id": "part_1",
            "question_type": "multiple_choice",
            "domain": "tech_agriculture",
            "difficulty": "easy",
            "points": 0.25,
            "prompt": "Thực vật thủy sinh trong ao nuôi thủy sản không có vai trò nào sau đây?",
            "options": {
                "A": "Cung cấp oxygen hoà tan cho nước nhờ quá trình quang hợp.",
                "B": "Cung cấp nơi trú ngụ cho động vật thuỷ sản.",
                "C": "Là nguồn thức ăn giàu protein cung cấp cho động vật thuỷ sản.",
                "D": "Hấp thụ một số kim loại nặng làm giảm ô nhiễm nguồn nước."
            },
            "correct_answer": "C",
            "explanation": "Thực vật thủy sinh chủ yếu chứa xơ và khoáng, không phải là nguồn thức ăn giàu protein cho động vật thủy sản."
        },
        {
            "question_number": 13,
            "section_id": "part_1",
            "question_type": "multiple_choice",
            "domain": "tech_agriculture",
            "difficulty": "medium",
            "points": 0.25,
            "prompt": "Phát biểu nào sau đây đúng khi nói về ứng dụng chỉ thị phân tử trong chọn giống thuỷ sản?",
            "options": {
                "A": "Xác định một đặc điểm nào đó của giống thông qua một trình tự DNA.",
                "B": "Xác định một đặc điểm nào đó của giống thông qua một trình tự protein.",
                "C": "Xác định một đặc điểm nào đó của giống thông qua số lượng nhiễm sắc thể.",
                "D": "Xác định một đặc điểm nào đó của giống thông qua tổ tiên."
            },
            "correct_answer": "A",
            "explanation": "Chỉ thị phân tử (molecular marker) liên kết với gen quy định tính trạng được xác định thông qua các đoạn trình tự DNA đặc hiệu."
        },
        {
            "question_number": 14,
            "section_id": "part_1",
            "question_type": "multiple_choice",
            "domain": "tech_agriculture",
            "difficulty": "easy",
            "points": 0.25,
            "prompt": "Một hộ nuôi cá rô phi nhận thấy cá tăng trưởng chậm dù lượng thức ăn cho ăn hằng ngày vẫn đầy đủ theo quy định. Sau khi kiểm tra, phát hiện nước ao bị ô nhiễm nhẹ và thức ăn có độ ẩm cao hơn mức cho phép. Để cải thiện tình hình, biện pháp nào sau đây là hợp lý?",
            "options": {
                "A": "Cho cá ăn nhiều hơn để bù lại lượng thức ăn bị hao hụt.",
                "B": "Cải thiện chất lượng nước ao và thay thức ăn đạt chuẩn về độ ẩm.",
                "C": "Chuyển nuôi loài cá mới có sức đề kháng tốt hơn.",
                "D": "Giảm lượng thức ăn xuống để tránh gây ô nhiễm thêm cho ao nuôi."
            },
            "correct_answer": "B",
            "explanation": "Cần khắc phục đúng nguyên nhân: xử lý nguồn nước ao và thay thế thức ăn đạt chuẩn chống nấm mốc."
        },
        {
            "question_number": 15,
            "section_id": "part_1",
            "question_type": "multiple_choice",
            "domain": "tech_agriculture",
            "difficulty": "medium",
            "points": 0.25,
            "prompt": "Một hộ nuôi tôm phát hiện tôm có dấu hiệu bỏ ăn, bơi lờ đờ và xuất hiện các đốm trắng trên vỏ. Sau khi kiểm tra, xác định tôm bị bệnh đốm trắng (WSSV). Biện pháp xử lý nào sau đây là phù hợp?",
            "options": {
                "A": "Tăng lượng thức ăn để giúp tôm khỏe hơn và chống lại bệnh.",
                "B": "Xử lí nước ao nuôi kết hợp với dùng kháng sinh để trị bệnh cho tôm.",
                "C": "Thay toàn bộ nước ao nuôi để loại bỏ mầm bệnh ra khỏi ao.",
                "D": "Cách ly và tiêu hủy tôm bệnh, xử lý nước ao nuôi, tăng cường phòng bệnh cho tôm khỏe."
            },
            "correct_answer": "D",
            "explanation": "Hội chứng đốm trắng do virus gây ra, không có thuốc kháng sinh điều trị; bắt buộc phải tiêu hủy tôm bệnh, khử trùng ao và cách ly an toàn sinh học."
        },
        {
            "question_number": 16,
            "section_id": "part_1",
            "question_type": "multiple_choice",
            "domain": "tech_agriculture",
            "difficulty": "easy",
            "points": 0.25,
            "prompt": "Việc quy định kích cỡ mắt lưới tối thiểu khi khai thác thủy sản có ý nghĩa nào sau đây?",
            "options": {
                "A": "Giúp ngư dân thu được nhiều thủy sản hơn sau mỗi chuyến ra khơi.",
                "B": "Giúp giảm chi phí mua ngư cụ đánh bắt.",
                "C": "Giúp giữ lại cá lớn, chỉ khai thác cá nhỏ để tránh cạn kiệt nguồn lợi.",
                "D": "Giúp bảo vệ thuỷ sản chưa trưởng thành, góp phần tái tạo nguồn lợi thuỷ sản."
            },
            "correct_answer": "D",
            "explanation": "Mắt lưới đủ lớn cho phép cá nhỏ chưa trưởng thành thoát ra, bảo vệ thế hệ kế tiếp và tái sinh nguồn lợi thủy sản."
        },

        # Phần II: Đúng / Sai (2 câu - 2đ, 1đ/câu theo thang 0.1 -> 0.25 -> 0.5 -> 1.0)
        {
            "question_number": 17,
            "section_id": "part_2",
            "question_type": "true_false",
            "domain": "tech_agriculture",
            "difficulty": "medium",
            "points": 1.0,
            "prompt": "Tiến hành thí nghiệm nghiên cứu ảnh hưởng của mật độ nuôi đến sinh trưởng và tỉ lệ sống của cá Nâu. Kết quả thu được:\n- Nghiệm thức 15 con/m³: Khối lượng lúc thả 30,047g; lúc thu 58,310g; tỉ lệ sống 97,78%.\n- Nghiệm thức 30 con/m³: Khối lượng lúc thả 30,223g; lúc thu 50,513g; tỉ lệ sống 98,89%.\n- Nghiệm thức 60 con/m³: Khối lượng lúc thả 30,133g; lúc thu 46,223g; tỉ lệ sống 96,11%.\nXét tính Đúng / Sai:",
            "tf_statements": {
                "a": "Mật độ nuôi có ảnh hưởng đến sinh trưởng nhưng không ảnh hưởng đến tỉ lệ sống của cá Nâu.",
                "b": "Mật độ nuôi càng cao, cá Nâu sinh trưởng càng chậm.",
                "c": "Để thu được năng suất và sản lượng cao nhất, nên nuôi cá Nâu với mật độ 15 con/m³.",
                "d": "Khi nuôi cá Nâu với mật độ 60 con/m³, sản lượng cá lúc thu hoạch sẽ là 2773,38 g/m³."
            },
            "correct_answer": {
                "a": "Đ",
                "b": "Đ",
                "c": "S",
                "d": "S"
            },
            "explanation": "a) Đúng vì tỉ lệ sống giữa 3 nghiệm thức khác biệt không có ý nghĩa thống kê (P>0,05). b) Đúng vì khối lượng lúc thu giảm dần khi mật độ tăng. c) Sai vì mật độ 30 con/m³ cho sản lượng cao hơn 15 con/m³. d) Sai vì sản lượng thực tế tính cả tỉ lệ sống: 60 * 46,223 * 0,9611 ≈ 2665,4 g/m³."
        },
        {
            "question_number": 18,
            "section_id": "part_2",
            "question_type": "true_false",
            "domain": "tech_agriculture",
            "difficulty": "medium",
            "points": 1.0,
            "prompt": "Đồ thị biểu diễn tỉ lệ cá sống sau 7 ngày thử nghiệm kết hợp nano bạc và florfenicol (Flor) trong điều trị bệnh do vi khuẩn Aeromonas veronii gây ra trên cá nheo Mỹ. Các công thức: CT1 (Flor 15 ppm), CT2 (Flor 10 ppm + nano bạc 5 ppm), CT3 (Flor 5 ppm + nano bạc 10 ppm), CT4 (nano bạc 15 ppm), ĐC (Không điều trị). Xét tính Đúng / Sai:",
            "tf_statements": {
                "a": "Sau 7 ngày điều trị, tỉ lệ cá sống ở tất cả các công thức điều trị (CT1, CT2, CT3 và CT4) đều cao hơn so với công thức ĐC (không điều trị).",
                "b": "Tỉ lệ cá sống ở phác đồ điều trị CT1 luôn cao hơn tỉ lệ cá sống ở các phác đồ điều trị còn lại.",
                "c": "Nên dừng điều trị ở ngày thứ 4 để tiết kiệm thuốc và giảm ô nhiễm môi trường.",
                "d": "Công thức sử dụng kết hợp Florfenicol 10ppm và nano bạc 5ppm cho hiệu quả điều trị cao hơn so với công thức sử dụng kết hợp Florfenicol 5ppm và nano bạc 10ppm."
            },
            "correct_answer": {
                "a": "Đ",
                "b": "S",
                "c": "S",
                "d": "S"
            },
            "explanation": "a) Đúng: Tỉ lệ sống của cả 4 CT đều cao hơn rõ rệt so với đối chứng ĐC (~50%). b, c, d Sai dựa trên số liệu và phác đồ điều trị."
        },

        # Phần III: Điền kết quả ngắn (4 câu - 1đ, 0.25đ/câu)
        {
            "question_number": 19,
            "section_id": "part_3",
            "question_type": "short_answer",
            "domain": "tech_agriculture",
            "difficulty": "easy",
            "points": 0.25,
            "prompt": "Rừng có vai trò giữ đất, giữ nước, điều hoà dòng chảy, chống xói mòn thoái hoá đất. Giữa rừng tự nhiên và rừng trồng thuần loài cùng tuổi, cùng chiều cao tầng tán rừng, kiểu rừng nào có khả năng bảo vệ đất, giữ nước tốt hơn?",
            "correct_answer": "Rừng tự nhiên",
            "accepted_answers": ["Rừng tự nhiên", "rừng tự nhiên", "Tự nhiên"],
            "explanation": "Rừng tự nhiên có cấu trúc nhiều tầng tán, thảm mục dày và hệ rễ đa tầng đan xen nên khả năng giữ đất, giữ nước vượt trội."
        },
        {
            "question_number": 20,
            "section_id": "part_3",
            "question_type": "short_answer",
            "domain": "tech_agriculture",
            "difficulty": "medium",
            "points": 0.25,
            "prompt": "Đối tượng của sản xuất lâm nghiệp chủ yếu là cây rừng có chu kì sống dài. Khi người dân được giao đất sản xuất lâm nghiệp có thời hạn sử dụng là 50 năm, người trồng rừng cần lựa chọn loại cây rừng có chu kì khai thác như thế nào để phù hợp với thực tế sử dụng đất?",
            "correct_answer": "ước số của 50",
            "accepted_answers": ["ước số của 50", "ước của 50", "<= 50 năm", "dưới 50 năm", "chu kì là ước số của 50"],
            "explanation": "Chu kì khai thác phải là ước số của 50 (ví dụ 5, 10, 25 năm) để thu hoạch trọn vẹn các luân kỳ trước khi hết thời hạn giao đất."
        },
        {
            "question_number": 21,
            "section_id": "part_3",
            "question_type": "short_answer",
            "domain": "tech_agriculture",
            "difficulty": "easy",
            "points": 0.25,
            "prompt": "Căn cứ vào nguồn gốc, rừng được chia thành rừng tự nhiên và rừng trồng. Có một số phương pháp khai thác rừng chính là khai thác trắng, khai thác dần và khai thác chọn. Khai thác trắng được áp dụng với loại rừng nào?",
            "correct_answer": "Rừng trồng",
            "accepted_answers": ["Rừng trồng", "rừng trồng"],
            "explanation": "Khai thác trắng chỉ được phép áp dụng đối với rừng trồng sản xuất, nghiêm cấm khai thác trắng rừng tự nhiên."
        },
        {
            "question_number": 22,
            "section_id": "part_3",
            "question_type": "short_answer",
            "domain": "tech_agriculture",
            "difficulty": "medium",
            "points": 0.25,
            "prompt": "Quy trình kĩ thuật trồng rừng bằng cây con được ươm trong bầu bao gồm một số bước chủ yếu sau:\n(1) Rạch, xé bỏ vỏ bầu.\n(2) Tạo hố trồng cây.\n(3) Vun gốc.\n(4) Lấp đất đảm bảo kín vỏ bầu.\nHãy sắp xếp số hiệu các bước theo trật tự đúng của quy trình.",
            "correct_answer": "(2) (1) (4) (3)",
            "accepted_answers": ["(2) (1) (4) (3)", "2, 1, 4, 3", "2 1 4 3", "2-1-4-3", "(2)-(1)-(4)-(3)"],
            "explanation": "Trình tự: Tạo hố (2) -> Rạch xé bầu (1) -> Lấp đất kín bầu (4) -> Vun gốc (3)."
        },

        # Phần IV: Tự luận (2 câu - 3đ, 1.5đ/câu)
        {
            "question_number": 23,
            "section_id": "part_4",
            "question_type": "essay",
            "domain": "tech_agriculture",
            "difficulty": "medium",
            "points": 1.5,
            "prompt": "Thực vật sống đơn lẻ hay trồng thưa thường có chiều cao thấp, phân cành sớm, thân thấp, đường kính thân lớn, tán lá rậm rạp. Ngược lại, khi trồng với mật độ cao, cạnh tranh nhiều thường có thân cao, đường kính thân nhỏ, phân cành ít, tán lá hẹp. Keo lá tràm là loài thực vật thường được trồng để lấy gỗ đóng đồ và sản xuất gỗ công nghiệp, giấy. Em hãy vận dụng những hiểu biết của mình về ảnh hưởng của ánh sáng đến thực vật và cho biết người trồng rừng nên trồng keo như thế nào để thu được các cây gỗ có đường kính lớn, thân thẳng. Giải thích.",
            "correct_answer": "Giai đoạn đầu trồng mật độ dày để cây vươn cao, thân thẳng, tự tỉa cành tự nhiên. Giai đoạn sau tỉa thưa để cây nhận đủ ánh sáng tăng trưởng đường kính thân gỗ.",
            "explanation": "Thang điểm 1,5đ: Nêu biện pháp ban đầu trồng dày (0,5đ); giải thích ảnh hưởng vươn sáng tỉa cành (0,5đ); biện pháp tỉa thưa sau đó để tăng đường kính (0,5đ)."
        },
        {
            "question_number": 24,
            "section_id": "part_4",
            "question_type": "essay",
            "domain": "tech_agriculture",
            "difficulty": "hard",
            "points": 1.5,
            "prompt": "Một hộ nuôi thủy sản muốn nuôi cá rô phi trong ao đất ở vùng đồng bằng nhưng nguồn nước đầu vào thường xuyên bị ô nhiễm bởi nước thải sinh hoạt và phân bón từ ruộng lúa xung quanh. Em hãy:\na. Phân tích các ảnh hưởng tiêu cực của nguồn nước ô nhiễm này đến quá trình nuôi cá rô phi.\nb. Đề xuất ít nhất 2 biện pháp khả thi để đảm bảo hiệu quả nuôi cá trong điều kiện đó, giải thích vì sao chọn các biện pháp đó.",
            "correct_answer": "a) Nước thải chứa hữu cơ và nitơ/phốt pho gây phú dưỡng hóa, giảm oxy hòa tan, tăng độc tố khí NH3/H2S làm cá chậm lớn, nhiễm bệnh.\nb) Đề xuất: Xây ao lắng lọc kết hợp nuôi thủy sinh (bèo lục bình, cỏ vetiver) xử lý sinh học trước khi cấp vào ao nuôi; Dùng chế phẩm sinh học vi sinh định kỳ.",
            "explanation": "Thang điểm 1,5đ: Phân tích ảnh hưởng tiêu cực (0,75đ); Đề xuất và giải thích 2 giải pháp khả thi (0,75đ)."
        }
    ]
}
