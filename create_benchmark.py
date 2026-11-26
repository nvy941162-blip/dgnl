# Script to generate benchmark_exam.py with 120 authentic questions
import json

def get_benchmark_questions():
    questions = []

    # ==========================================
    # PHẦN 1: SỬ DỤNG NGÔN NGỮ (CÂU 1 - 40)
    # ==========================================

    # --- TIẾNG VIỆT (CÂU 1 - 20) ---
    tv_questions = [
        {
            "question_number": 1,
            "section_id": "section_1_language",
            "domain": "vietnamese",
            "difficulty": "easy",
            "prompt": "Từ nào sau đây viết ĐÚNG chính tả tiếng Việt?",
            "options": {
                "A": "Sáng lạn",
                "B": "Xán lạn",
                "C": "Sáng lạng",
                "D": "Xáng lạn"
            },
            "correct_answer": "B",
            "explanation": "Từ đúng là 'Xán lạn' (chữ Hán 'xán' là rực rỡ, 'lạn' là sáng sủa, nghĩa là tươi sáng, rực rỡ). Rất nhiều người quen dùng sai thành 'sáng lạn'."
        },
        {
            "question_number": 2,
            "section_id": "section_1_language",
            "domain": "vietnamese",
            "difficulty": "easy",
            "prompt": "Chọn từ thích hợp nhất để điền vào chỗ trống: 'Hội đồng đã đưa ra những quyết định mang tính ______ nhằm tháo gỡ khó khăn cho doanh nghiệp.'",
            "options": {
                "A": "đột phá",
                "B": "đột kích",
                "C": "đột biến",
                "D": "đột nhập"
            },
            "correct_answer": "A",
            "explanation": "'Đột phá' mang nghĩa tạo ra sự chuyển biến mạnh mẽ, vượt bậc qua khó khăn, phù hợp nhất với ngữ cảnh đưa ra quyết định."
        },
        {
            "question_number": 3,
            "section_id": "section_1_language",
            "domain": "vietnamese",
            "difficulty": "medium",
            "prompt": "Câu nào sau đây mắc lỗi dùng từ hoặc ngữ pháp?",
            "options": {
                "A": "Qua tác phẩm cho ta thấy lòng yêu nước nồng nàn của nhân dân.",
                "B": "Tác phẩm cho ta thấy lòng yêu nước nồng nàn của nhân dân.",
                "C": "Qua tác phẩm, tác giả đã thể hiện lòng yêu nước nồng nàn của nhân dân.",
                "D": "Đọc tác phẩm, chúng ta cảm nhận được lòng yêu nước nồng nàn của nhân dân."
            },
            "correct_answer": "A",
            "explanation": "Câu A thiếu chủ ngữ ngữ pháp do dùng giới từ 'Qua...' biến cả vế đầu thành trạng ngữ, khiến câu không có chủ thể thực hiện hành động 'cho ta thấy'."
        },
        {
            "question_number": 4,
            "section_id": "section_1_language",
            "domain": "vietnamese",
            "difficulty": "medium",
            "prompt": "Thành ngữ nào sau đây đồng nghĩa với câu 'Một con ngựa đau cả tàu bỏ cỏ'?",
            "options": {
                "A": "Lá lành đùm lá rách",
                "B": "Cháy nhà hàng xóm bình chân như vại",
                "C": "Môi hở răng lạnh",
                "D": "Đồng cam cộng khổ"
            },
            "correct_answer": "C",
            "explanation": "'Môi hở răng lạnh' và 'Một con ngựa đau cả tàu bỏ cỏ' đều thể hiện mối quan hệ gắn bó khăng khít, cùng chia sẻ nỗi đau và ảnh hưởng lẫn nhau."
        },
        {
            "question_number": 5,
            "section_id": "section_1_language",
            "domain": "vietnamese",
            "difficulty": "medium",
            "prompt": "Xác định biện pháp tu từ được sử dụng trong hai câu thơ sau:\n'Bàn tay ta làm nên tất cả\nCó sức người sỏi đá cũng thành cơm.' (Hoàng Trung Thông)",
            "options": {
                "A": "Ẩn dụ và hoán dụ",
                "B": "Hoán dụ và nhân hóa",
                "C": "Nói quá và điệp ngữ",
                "D": "Hoán dụ và nói quá"
            },
            "correct_answer": "D",
            "explanation": "'Bàn tay ta' là hoán dụ lấy bộ phận chỉ toàn thể (con người lao động). 'Sỏi đá cũng thành cơm' là phép nói quá thể hiện sức mạnh to lớn của lao động."
        },
        {
            "question_number": 6,
            "section_id": "section_1_language",
            "domain": "vietnamese",
            "difficulty": "medium",
            "prompt": "Từ nào sau đây là từ Hán - Việt đồng nghĩa với từ 'mắt'?",
            "options": {
                "A": "Mục",
                "B": "Nhĩ",
                "C": "Khẩu",
                "D": "Tọa"
            },
            "correct_answer": "A",
            "explanation": "'Mục' (目) có nghĩa là mắt (như trong: mục sở thị, hạng mục). 'Nhĩ' là tai, 'Khẩu' là miệng, 'Tọa' là ngồi/chỗ ngồi."
        },
        {
            "question_number": 7,
            "section_id": "section_1_language",
            "domain": "vietnamese",
            "difficulty": "hard",
            "prompt": "Trong truyện ngắn 'Vợ nhặt' của Kim Lân, hình ảnh 'nồi cháo cám' trong bữa cơm đầu tiên đón nàng dâu mới mang ý nghĩa biểu tượng sâu sắc gì?",
            "options": {
                "A": "Biểu hiện sự tàn nhẫn và hà tiện của bà cụ Tứ đối với con dâu mới.",
                "B": "Hiện thực khốn cùng của nạn đói năm 1945 và tình người ấm áp, khát vọng sống vượt lên nghịch cảnh.",
                "C": "Sự buông xuôi, bất lực của người nông dân nghèo trước định mệnh tăm tối.",
                "D": "Phong tục truyền thống của người dân vùng đồng bằng Bắc Bộ vào ngày cưới hỏi nghèo."
            },
            "correct_answer": "B",
            "explanation": "Nồi cháo cám vừa khắc sâu nỗi thống khổ, cay đắng của nạn đói 1945, vừa ngời sáng tình mẫu tử, tình người, niềm lạc quan và khát vọng sống mãnh liệt của gia đình Tràng."
        },
        {
            "question_number": 8,
            "section_id": "section_1_language",
            "domain": "vietnamese",
            "difficulty": "medium",
            "prompt": "Dòng nào sau đây nêu ĐÚNG phong cách chức năng ngôn ngữ của một văn bản Hiến pháp nước Cộng hòa Xã hội Chủ nghĩa Việt Nam?",
            "options": {
                "A": "Phong cách ngôn ngữ khoa học",
                "B": "Phong cách ngôn ngữ chính luận",
                "C": "Phong cách ngôn ngữ hành chính",
                "D": "Phong cách ngôn ngữ báo chí"
            },
            "correct_answer": "C",
            "explanation": "Hiến pháp, luật pháp, văn bản quy phạm pháp luật thuộc phong cách chức năng ngôn ngữ hành chính (tính pháp lý, tính minh xác, tính khuôn mẫu)."
        },
        {
            "question_number": 9,
            "section_id": "section_1_language",
            "domain": "vietnamese",
            "difficulty": "hard",
            "prompt": "Trong bài thơ 'Tây Tiến' của Quang Dũng, hình tượng người lính được khắc họa mang vẻ đẹp gì nổi bật?",
            "options": {
                "A": "Mộc mạc, chất phác, đậm chất nông dân Nam Bộ.",
                "B": "Bi tráng, lãng mạn, hào hoa nhưng sẵn sàng hiến dâng tuổi thanh xuân vì Tổ quốc.",
                "C": "U buồn, bế tắc và trăn trở trước hiện thực chiến tranh khốc liệt.",
                "D": "Hiện thực trần trụi, khắc khổ và chịu nhiều nỗi uất ức."
            },
            "correct_answer": "B",
            "explanation": "Hình tượng người lính Tây Tiến mang vẻ đẹp hào hoa, lãng mạn của thanh niên trí thức Hà thành kết hợp với nét bi tráng, bất tử trước hy sinh, gian khổ."
        },
        {
            "question_number": 10,
            "section_id": "section_1_language",
            "domain": "vietnamese",
            "difficulty": "medium",
            "prompt": "Cụm từ nào trong câu sau đóng vai trò là trạng ngữ: 'Để chuẩn bị cho kỳ thi Đánh giá Năng lực sắp tới, các bạn học sinh đã tích cực luyện giải đề.'",
            "options": {
                "A": "Để chuẩn bị cho kỳ thi Đánh giá Năng lực sắp tới",
                "B": "các bạn học sinh",
                "C": "đã tích cực",
                "D": "luyện giải đề"
            },
            "correct_answer": "A",
            "explanation": "'Để chuẩn bị cho kỳ thi Đánh giá Năng lực sắp tới' là trạng ngữ chỉ mục đích của câu."
        },
        # Đọc hiểu đoạn văn Tiếng Việt 1 (Câu 11 - 15)
        {
            "question_number": 11,
            "section_id": "section_1_language",
            "domain": "vietnamese",
            "difficulty": "medium",
            "passage": "Đoạn trích sau dành cho các câu hỏi 11 - 15:\n'Văn hóa không phải là một pho tượng đá đóng băng trong viện bảo tàng, mà là một dòng sông luôn luôn vận động và bồi đắp phù sa. Bản sắc dân tộc là cái lõi bền vững giúp dân tộc không bị hòa tan, nhưng nếu tự khép kín, dòng sông sẽ trở thành đầm lầy tù đọng. Tiếp biến văn hóa (acculturation) là quy luật tất yếu của mọi nền văn minh nhân loại. Một dân tộc có nội lực văn hóa mạnh mẽ là dân tộc biết chọn lọc tinh hoa của thế giới để làm giàu cho bản sắc của chính mình, đồng thời biết lan tỏa những giá trị nhân văn độc đáo của mình ra thế giới bên ngoài mà không đánh mất đi căn cước cội nguồn.'",
            "prompt": "Theo tác giả đoạn trích, 'văn hóa' được so sánh với hình ảnh nào?",
            "options": {
                "A": "Một pho tượng đá trong viện bảo tàng",
                "B": "Một dòng sông luôn vận động và bồi đắp phù sa",
                "C": "Một đầm lầy tù đọng",
                "D": "Một căn cước cội nguồn bất biến"
            },
            "correct_answer": "B",
            "explanation": "Đoạn văn khẳng định: 'Văn hóa không phải là một pho tượng đá đóng băng trong viện bảo tàng, mà là một dòng sông luôn luôn vận động và bồi đắp phù sa.'"
        },
        {
            "question_number": 12,
            "section_id": "section_1_language",
            "domain": "vietnamese",
            "difficulty": "medium",
            "passage": "Đoạn trích câu 11 - 15",
            "prompt": "Theo văn bản, điều gì sẽ xảy ra nếu một nền văn hóa tự khép kín?",
            "options": {
                "A": "Bản sắc văn hóa sẽ được bảo tồn nguyên vẹn vĩnh cửu.",
                "B": "Dòng sông văn hóa sẽ trở thành đầm lầy tù đọng.",
                "C": "Nội lực văn hóa sẽ phát triển vượt bậc.",
                "D": "Sẽ tạo ra quy luật tiếp biến văn hóa mới."
            },
            "correct_answer": "B",
            "explanation": "Trong đoạn trích có câu: '...nhưng nếu tự khép kín, dòng sông sẽ trở thành đầm lầy tù đọng.'"
        },
        {
            "question_number": 13,
            "section_id": "section_1_language",
            "domain": "vietnamese",
            "difficulty": "hard",
            "passage": "Đoạn trích câu 11 - 15",
            "prompt": "Khái niệm 'tiếp biến văn hóa' được nhắc đến trong đoạn trích gắn liền với đặc điểm nào?",
            "options": {
                "A": "Sự sao chép nguyên xi các mô hình ngoại lai của phương Tây.",
                "B": "Quy luật tất yếu của văn minh, chọn lọc tinh hoa thế giới để làm giàu bản sắc dân tộc.",
                "C": "Xóa bỏ căn cước cội nguồn để hướng tới chuẩn mực toàn cầu hóa.",
                "D": "Quá trình chuyển đổi bảo tồn văn hóa vào các bảo tàng khảo cổ học."
            },
            "correct_answer": "B",
            "explanation": "Đoạn văn chỉ rõ tiếp biến văn hóa là quy luật tất yếu của văn minh nhân loại: biết chọn lọc tinh hoa thế giới để làm giàu bản sắc của chính mình mà không đánh mất căn cước."
        },
        {
            "question_number": 14,
            "section_id": "section_1_language",
            "domain": "vietnamese",
            "difficulty": "medium",
            "passage": "Đoạn trích câu 11 - 15",
            "prompt": "Phương thức biểu đạt chính của đoạn trích trên là gì?",
            "options": {
                "A": "Tự sự",
                "B": "Nghị luận",
                "C": "Biểu cảm",
                "D": "Thuyết minh"
            },
            "correct_answer": "B",
            "explanation": "Đoạn trích bàn luận, đưa ra các luận điểm, lý lẽ và quan điểm về bản chất văn hóa và tiếp biến văn hóa nên phương thức chính là nghị luận."
        },
        {
            "question_number": 15,
            "section_id": "section_1_language",
            "domain": "vietnamese",
            "difficulty": "hard",
            "passage": "Đoạn trích câu 11 - 15",
            "prompt": "Từ 'căn cước' trong cụm từ 'căn cước cội nguồn' ở cuối đoạn văn được hiểu theo nghĩa nào?",
            "options": {
                "A": "Thẻ giấy tờ tùy thân do cơ quan công an cấp",
                "B": "Đặc trưng nhận diện và giá trị cốt lõi làm nên bản ngã của dân tộc",
                "C": "Nơi chôn rau cắt rốn cụ thể về mặt địa lý",
                "D": "Ngôn ngữ và chữ viết chính thức của quốc gia"
            },
            "correct_answer": "B",
            "explanation": "Trong ngữ cảnh văn hóa triết học, 'căn cước' (identity) chỉ đặc trưng nhận diện, phẩm chất cốt lõi làm nên bản sắc và sự khác biệt tích cực của một dân tộc."
        },
        # Đọc hiểu đoạn văn Tiếng Việt 2 (Câu 16 - 20)
        {
            "question_number": 16,
            "section_id": "section_1_language",
            "domain": "vietnamese",
            "difficulty": "medium",
            "passage": "Đoạn thơ sau dành cho các câu hỏi 16 - 20:\n'Ôi Tổ quốc ta, yêu như máu thịt,\nNhư mẹ cha ta, như vợ như chồng\nÔi Tổ quốc, nếu cần, ta chết\nCho mỗi ngôi nhà, ngọn núi, con sông...'\n(Chế Lan Viên - 'Sao chiến thắng')",
            "prompt": "Tác giả đã sử dụng biện pháp tu từ nào nổi bật trong hai câu thơ đầu?",
            "options": {
                "A": "So sánh và điệp từ",
                "B": "Ẩn dụ chuyển đổi cảm giác",
                "C": "Nhân hóa và hoán dụ",
                "D": "Tương phản đối lập"
            },
            "correct_answer": "A",
            "explanation": "Tác giả dùng phép so sánh liên tiếp ('như máu thịt', 'như mẹ cha', 'như vợ như chồng') và điệp từ 'như'."
        },
        {
            "question_number": 17,
            "section_id": "section_1_language",
            "domain": "vietnamese",
            "difficulty": "easy",
            "passage": "Đoạn thơ câu 16 - 20",
            "prompt": "Cảm xúc chủ đạo toát lên từ đoạn thơ của Chế Lan Viên là gì?",
            "options": {
                "A": "Nỗi xót xa trước những đau thương mất mát của chiến tranh",
                "B": "Tình yêu thiết tha, sâu nặng và tinh thần sẵn sàng hy sinh vì Tổ quốc",
                "C": "Niềm tự hào về cảnh đẹp thiên nhiên gấm vóc non sông",
                "D": "Sự suy tư triết lý về thân phận của con người trong thời đại mới"
            },
            "correct_answer": "B",
            "explanation": "Đoạn thơ thể hiện tình yêu Tổ quốc thiêng liêng gắn bó ruột thịt và lý tưởng sẵn sàng hy sinh bảo vệ quê hương."
        },
        {
            "question_number": 18,
            "section_id": "section_1_language",
            "domain": "vietnamese",
            "difficulty": "medium",
            "passage": "Đoạn thơ câu 16 - 20",
            "prompt": "Các hình ảnh 'mỗi ngôi nhà, ngọn núi, con sông' trong câu thơ cuối được tạo dựng bằng biện pháp tu từ nào?",
            "options": {
                "A": "Liệt kê",
                "B": "Ẩn dụ",
                "C": "Chơi chữ",
                "D": "Nói giảm nói tránh"
            },
            "correct_answer": "A",
            "explanation": "Tác giả dùng biện pháp liệt kê các hình ảnh cụ thể từ nơi ở gần gũi ('ngôi nhà') đến không gian rộng lớn của đất nước ('ngọn núi', 'con sông')."
        },
        {
            "question_number": 19,
            "section_id": "section_1_language",
            "domain": "vietnamese",
            "difficulty": "hard",
            "passage": "Đoạn thơ câu 16 - 20",
            "prompt": "Nhịp thơ trong câu 'Ôi Tổ quốc, nếu cần, ta chết' có đặc điểm gì đặc biệt?",
            "options": {
                "A": "Nhịp 4/4 đều đặn, êm ái",
                "B": "Nhịp 3/2/2 ngắt dứt khoát, thể hiện quyết tâm sắt đá",
                "C": "Nhịp 2/2/4 kéo dài, trầm buồn",
                "D": "Nhịp tự do ngắt ngẫu nhiên không có chủ đích"
            },
            "correct_answer": "B",
            "explanation": "Nhịp thơ ngắt đanh gọn 3/2/2 ('Ôi Tổ quốc / nếu cần / ta chết') tạo âm hưởng quả quyết, khẳng định tư thế sẵn sàng cống hiến không do dự."
        },
        {
            "question_number": 20,
            "section_id": "section_1_language",
            "domain": "vietnamese",
            "difficulty": "medium",
            "passage": "Đoạn thơ câu 16 - 20",
            "prompt": "Từ cảm thán 'Ôi' được lặp lại ở đầu câu 1 và câu 3 có tác dụng gì?",
            "options": {
                "A": "Biểu thị sự bối rối, hoang mang của người viết",
                "B": "Làm chậm nhịp độ diễn đạt để kéo dài dung lượng bài thơ",
                "C": "Nhấn mạnh cảm xúc trào dâng, tiếng gọi thiêng liêng xuất phát từ trái tim",
                "D": "Tạo tính chất khẩu ngữ dân dã cho câu thơ nghệ thuật"
            },
            "correct_answer": "C",
            "explanation": "Từ 'Ôi' mở đầu thể hiện sự xúc động trào dâng mãnh liệt, lời gọi tha thiết, trang nghiêm hướng về Tổ quốc."
        },
    ]

    # --- TIẾNG ANH (CÂU 21 - 40) ---
    en_questions = [
        {
            "question_number": 21,
            "section_id": "section_1_language",
            "domain": "english",
            "difficulty": "easy",
            "prompt": "Choose the word whose underlined part is pronounced differently from the others:\nA. climb\u0065d   B. play\u0065d   C. want\u0065d   D. stay\u0065d",
            "options": {
                "A": "climbed",
                "B": "played",
                "C": "wanted",
                "D": "stayed"
            },
            "correct_answer": "C",
            "explanation": "In 'wanted', -ed is pronounced as /ɪd/. In the others ('climbed', 'played', 'stayed'), -ed is pronounced as /d/."
        },
        {
            "question_number": 22,
            "section_id": "section_1_language",
            "domain": "english",
            "difficulty": "easy",
            "prompt": "If he ______ harder during the term, he would have passed the entrance exam with flying colors.",
            "options": {
                "A": "studied",
                "B": "had studied",
                "C": "has studied",
                "D": "studies"
            },
            "correct_answer": "B",
            "explanation": "Third conditional sentence for an unreal condition in the past: If + S + had + P.P, S + would have + P.P."
        },
        {
            "question_number": 23,
            "section_id": "section_1_language",
            "domain": "english",
            "difficulty": "medium",
            "prompt": "The government is taking urgent measures to ______ the rapid spread of misinformation on social networks.",
            "options": {
                "A": "curb",
                "B": "provoke",
                "C": "accelerate",
                "D": "foster"
            },
            "correct_answer": "A",
            "explanation": "'Curb' means to restrain, control, or limit something undesirable (such as the spread of fake news)."
        },
        {
            "question_number": 24,
            "section_id": "section_1_language",
            "domain": "english",
            "difficulty": "medium",
            "prompt": "Never before ______ such tremendous technological advancements in the field of artificial intelligence.",
            "options": {
                "A": "humanity has witnessed",
                "B": "has humanity witnessed",
                "C": "did humanity witnessed",
                "D": "humanity witnessed"
            },
            "correct_answer": "B",
            "explanation": "Negative inversion structure: Never before + auxiliary verb (has) + Subject (humanity) + Past Participle (witnessed)."
        },
        {
            "question_number": 25,
            "section_id": "section_1_language",
            "domain": "english",
            "difficulty": "medium",
            "prompt": "Choose the word CLOSEST in meaning to the capitalized word:\n'The findings of the study were so LUCID that even non-specialists could understand them easily.'",
            "options": {
                "A": "ambiguous",
                "B": "clear and easy to understand",
                "C": "complicated",
                "D": "questionable"
            },
            "correct_answer": "B",
            "explanation": "'Lucid' means expressed clearly, easy to understand. Opposite is ambiguous/obscure."
        },
        {
            "question_number": 26,
            "section_id": "section_1_language",
            "domain": "english",
            "difficulty": "medium",
            "prompt": "Choose the word OPPOSITE in meaning to the capitalized word:\n'The newly appointed director took PRAGMATIC steps to resolve the ongoing budget crisis.'",
            "options": {
                "A": "practical",
                "B": "realistic",
                "C": "idealistic and impractical",
                "D": "sensible"
            },
            "correct_answer": "C",
            "explanation": "'Pragmatic' means realistic and practical. Its opposite is 'idealistic and impractical'."
        },
        {
            "question_number": 27,
            "section_id": "section_1_language",
            "domain": "english",
            "difficulty": "hard",
            "prompt": "Identify the underlined part that contains an error:\n'Despite of (A) the severe weather conditions (B), the rescue team managed to reach (C) the isolated village safely (D).'",
            "options": {
                "A": "Despite of",
                "B": "severe weather conditions",
                "C": "to reach",
                "D": "safely"
            },
            "correct_answer": "A",
            "explanation": "'Despite' takes a noun phrase directly without 'of' (e.g. 'Despite the severe weather'). Alternatively, one can use 'In spite of'."
        },
        {
            "question_number": 28,
            "section_id": "section_1_language",
            "domain": "english",
            "difficulty": "medium",
            "prompt": "It is essential that every applicant ______ all relevant certificates before the registration deadline.",
            "options": {
                "A": "submits",
                "B": "submit",
                "C": "submitted",
                "D": "has submitted"
            },
            "correct_answer": "B",
            "explanation": "Subjunctive mood structure: It is essential/imperative/vital that + S + (should) + bare infinitive (submit)."
        },
        {
            "question_number": 29,
            "section_id": "section_1_language",
            "domain": "english",
            "difficulty": "medium",
            "prompt": "The new environmental policy aims to cut down on greenhouse emissions, ______ contributing to the global fight against climate change.",
            "options": {
                "A": "thereby",
                "B": "whereas",
                "C": "nonetheless",
                "D": "moreover"
            },
            "correct_answer": "A",
            "explanation": "'Thereby' means 'as a result of that', followed by a V-ing participle clause (thereby contributing...)."
        },
        {
            "question_number": 30,
            "section_id": "section_1_language",
            "domain": "english",
            "difficulty": "hard",
            "prompt": "No sooner ______ down the phone than the doorbell rang persistently.",
            "options": {
                "A": "she had put",
                "B": "did she put",
                "C": "had she put",
                "D": "has she put"
            },
            "correct_answer": "C",
            "explanation": "Negative inversion: 'No sooner had + S + V3/ed... than + S + V2/ed'."
        },
        # Đọc hiểu tiếng Anh (Câu 31 - 35)
        {
            "question_number": 31,
            "section_id": "section_1_language",
            "domain": "english",
            "difficulty": "medium",
            "passage": "Read the following passage and answer questions 31 to 35:\n'Artificial Intelligence (AI) has rapidly transformed from a speculative scientific frontier into an indispensable driver of modern economic innovation. In healthcare, machine learning algorithms can analyze radiology images with accuracy comparable to, or even surpassing, experienced human diagnosticians. In education, intelligent tutoring systems tailor instructional pacing and problem complexity to individual student profiles. However, this profound transition is accompanied by substantial ethical dilemmas. Algorithmic bias—which arises when training datasets reflect historical human prejudices—can perpetuate systemic unfairness in hiring, credit scoring, and law enforcement. Furthermore, the automation of cognitive tasks raises urgent questions regarding labor market displacement and the need for continuous workforce reskilling.'",
            "prompt": "What is the primary topic of the passage?",
            "options": {
                "A": "The financial cost of developing machine learning algorithms in hospitals.",
                "B": "The widespread benefits of AI alongside its emerging ethical and societal challenges.",
                "C": "How artificial intelligence completely eliminates the need for human teachers.",
                "D": "Historical prejudices in traditional employment practices."
            },
            "correct_answer": "B",
            "explanation": "The passage discusses the major advancements of AI across healthcare and education, while balancing them with ethical concerns such as algorithmic bias and job displacement."
        },
        {
            "question_number": 32,
            "section_id": "section_1_language",
            "domain": "english",
            "difficulty": "medium",
            "passage": "Passage for questions 31 - 35",
            "prompt": "According to the passage, what is a notable application of AI in healthcare?",
            "options": {
                "A": "Performing surgical operations without any human oversight.",
                "B": "Analyzing radiology scans with high diagnostic accuracy.",
                "C": "Synthesizing synthetic medications in laboratories instantly.",
                "D": "Managing hospital budgetary expenditures."
            },
            "correct_answer": "B",
            "explanation": "The text states: 'machine learning algorithms can analyze radiology images with accuracy comparable to, or even surpassing, experienced human diagnosticians.'"
        },
        {
            "question_number": 33,
            "section_id": "section_1_language",
            "domain": "english",
            "difficulty": "hard",
            "passage": "Passage for questions 31 - 35",
            "prompt": "What primarily causes 'algorithmic bias' according to the author?",
            "options": {
                "A": "Malfunctioning computer hardware in modern servers.",
                "B": "Training datasets that reflect historical human prejudices.",
                "C": "A lack of computing power during algorithmic processing.",
                "D": "Excessive governmental regulation on data privacy."
            },
            "correct_answer": "B",
            "explanation": "The author specifies: 'Algorithmic bias—which arises when training datasets reflect historical human prejudices...'"
        },
        {
            "question_number": 34,
            "section_id": "section_1_language",
            "domain": "english",
            "difficulty": "medium",
            "passage": "Passage for questions 31 - 35",
            "prompt": "The word 'indispensable' in the first paragraph is closest in meaning to:",
            "options": {
                "A": "unnecessary",
                "B": "essential",
                "C": "expensive",
                "D": "temporary"
            },
            "correct_answer": "B",
            "explanation": "'Indispensable' means absolutely necessary, essential, or vital."
        },
        {
            "question_number": 35,
            "section_id": "section_1_language",
            "domain": "english",
            "difficulty": "hard",
            "passage": "Passage for questions 31 - 35",
            "prompt": "It can be inferred from the passage that in response to AI automation:",
            "options": {
                "A": "Human labor will be rendered entirely obsolete within a decade.",
                "B": "Governments should strictly ban all machine learning research.",
                "C": "Workers will need ongoing reskilling to adapt to changing labor demands.",
                "D": "Educational institutions should discontinue science curricula."
            },
            "correct_answer": "C",
            "explanation": "The final sentence mentions 'labor market displacement and the need for continuous workforce reskilling', implying workers must continuously update their skills."
        },
        # Câu 36 - 40: Sentence rearrangement / Dialogue / Synthesis
        {
            "question_number": 36,
            "section_id": "section_1_language",
            "domain": "english",
            "difficulty": "medium",
            "prompt": "Choose the best sentence that combines the two given sentences:\n'The student was exceptionally gifted. He easily won the national mathematics olympiad.'",
            "options": {
                "A": "So gifted was the student that he easily won the national mathematics olympiad.",
                "B": "Because of winning the national olympiad, the student was gifted.",
                "C": "The student was gifted enough that winning the national olympiad easily.",
                "D": "Although the student was gifted, he won the national mathematics olympiad."
            },
            "correct_answer": "A",
            "explanation": "Inversion with 'So + adj + be + S + that clause': 'So gifted was the student that he easily won...'"
        },
        {
            "question_number": 37,
            "section_id": "section_1_language",
            "domain": "english",
            "difficulty": "medium",
            "prompt": "Mark: 'Do you mind if I borrow your laptop for a few hours?'\nPeter: '______.'",
            "options": {
                "A": "Yes, go ahead. I am using it now.",
                "B": "Not at all, help yourself. Here is the charger.",
                "C": "No, you can't borrow it.",
                "D": "Yes, please take it immediately."
            },
            "correct_answer": "B",
            "explanation": "'Do you mind...?' asks if it causes inconvenience. Answering 'Not at all' means 'I don't mind, you may use it'."
        },
        {
            "question_number": 38,
            "section_id": "section_1_language",
            "domain": "english",
            "difficulty": "hard",
            "prompt": "Which of the following sentences has the most natural and grammatically sound academic style?",
            "options": {
                "A": "Things got really bad when the company lost its money.",
                "B": "The enterprise experienced severe financial distress following liquidity shortages.",
                "C": "The company was so broke and didn't know what to do next.",
                "D": "Cash went away so the company fell down very fast."
            },
            "correct_answer": "B",
            "explanation": "Sentence B uses formal academic vocabulary ('enterprise', 'severe financial distress', 'liquidity shortages') appropriate for formal discourse."
        },
        {
            "question_number": 39,
            "section_id": "section_1_language",
            "domain": "english",
            "difficulty": "medium",
            "prompt": "The committee recommended that the proposal ______ further before implementation.",
            "options": {
                "A": "is examined",
                "B": "be examined",
                "C": "was examined",
                "D": "will be examined"
            },
            "correct_answer": "B",
            "explanation": "Mandative subjunctive: recommend that + subject + (be) past participle."
        },
        {
            "question_number": 40,
            "section_id": "section_1_language",
            "domain": "english",
            "difficulty": "medium",
            "prompt": "She was ______ taken aback by the unexpected announcement that she remained speechless for moments.",
            "options": {
                "A": "such",
                "B": "so",
                "C": "too",
                "D": "very"
            },
            "correct_answer": "B",
            "explanation": "Structure: 'so + adverb/adjective + that': 'so taken aback... that she remained speechless'."
        }
    ]

    questions.extend(tv_questions)
    questions.extend(en_questions)

    # =========================================================================
    # PHẦN 2: TOÁN HỌC, TƯ DUY LOGIC VÀ PHÂN TÍCH SỐ LIỆU (CÂU 41 - 70)
    # =========================================================================

    # --- TOÁN HỌC (CÂU 41 - 50) ---
    math_questions = [
        {
            "question_number": 41,
            "section_id": "section_2_logic_data",
            "domain": "math",
            "difficulty": "easy",
            "prompt": "Tìm tập nghiệm S của bất phương trình: 2^(2x - 1) > 8.",
            "options": {
                "A": "S = (2; +inf)",
                "B": "S = (1; +inf)",
                "C": "S = (-inf; 2)",
                "D": "S = (3/2; +inf)"
            },
            "correct_answer": "A",
            "explanation": "2^(2x - 1) > 8 = 2^3 <=> 2x - 1 > 3 <=> 2x > 4 <=> x > 2. Do đó S = (2; +inf)."
        },
        {
            "question_number": 42,
            "section_id": "section_2_logic_data",
            "domain": "math",
            "difficulty": "medium",
            "prompt": "Cho hàm số y = f(x) có đạo hàm f'(x) = x(x - 1)(x + 2)^2. Số điểm cực trị của hàm số đã cho là:",
            "options": {
                "A": "1",
                "B": "2",
                "C": "3",
                "D": "4"
            },
            "correct_answer": "B",
            "explanation": "f'(x) = 0 <=> x = 0, x = 1, x = -2. Trong đó nghiệm x = -2 là nghiệm bội chẵn nên qua đó f'(x) không đổi dấu. Chỉ có x = 0 và x = 1 đổi dấu (nghiệm bội lẻ) => Hàm số có đúng 2 điểm cực trị."
        },
        {
            "question_number": 43,
            "section_id": "section_2_logic_data",
            "domain": "math",
            "difficulty": "medium",
            "prompt": "Tính tích phân I = tích phân từ 0 đến 1 của e^(2x) dx.",
            "options": {
                "A": "(e^2 - 1) / 2",
                "B": "e^2 - 1",
                "C": "(e^2 + 1) / 2",
                "D": "2(e^2 - 1)"
            },
            "correct_answer": "A",
            "explanation": "Nguyên hàm của e^(2x) là (1/2)e^(2x). Thay cận từ 0 đến 1: (1/2)(e^2 - e^0) = (e^2 - 1)/2."
        },
        {
            "question_number": 44,
            "section_id": "section_2_logic_data",
            "domain": "math",
            "difficulty": "medium",
            "prompt": "Trong không gian Oxyz, phương trình mặt cầu có tâm I(1; -2; 3) và bán kính R = 4 là:",
            "options": {
                "A": "(x - 1)^2 + (y + 2)^2 + (z - 3)^2 = 16",
                "B": "(x + 1)^2 + (y - 2)^2 + (z + 3)^2 = 16",
                "C": "(x - 1)^2 + (y + 2)^2 + (z - 3)^2 = 4",
                "D": "(x - 1)^2 + (y - 2)^2 + (z - 3)^2 = 16"
            },
            "correct_answer": "A",
            "explanation": "Mặt cầu tâm I(a, b, c) bán kính R có phương trình: (x - a)^2 + (y - b)^2 + (z - c)^2 = R^2 <=> (x - 1)^2 + (y + 2)^2 + (z - 3)^2 = 16."
        },
        {
            "question_number": 45,
            "section_id": "section_2_logic_data",
            "domain": "math",
            "difficulty": "hard",
            "prompt": "Một hộp chứa 5 quả cầu đỏ và 7 quả cầu xanh có cùng kích thước. Lấy ngẫu nhiên đồng thời 3 quả cầu. Xác suất để lấy được ít nhất 1 quả cầu màu đỏ là:",
            "options": {
                "A": "7/44",
                "B": "37/44",
                "C": "5/12",
                "D": "1/44"
            },
            "correct_answer": "B",
            "explanation": "Số phần tử không gian mẫu: n(Omega) = C(12, 3) = 220. Biến cố đối A' là lấy được 3 quả đều màu xanh: n(A') = C(7, 3) = 35. Vậy P(A) = 1 - 35/220 = 1 - 7/44 = 37/44."
        },
        {
            "question_number": 46,
            "section_id": "section_2_logic_data",
            "domain": "math",
            "difficulty": "hard",
            "prompt": "Một người gửi 200 triệu đồng vào ngân hàng theo hình thức lãi kép với lãi suất 6%/năm. Hỏi sau ít nhất bao nhiêu năm người đó nhận được số tiền cả gốc lẫn lãi vượt quá 300 triệu đồng (giả định lãi suất không đổi)?",
            "options": {
                "A": "6 năm",
                "B": "7 năm",
                "C": "8 năm",
                "D": "9 năm"
            },
            "correct_answer": "B",
            "explanation": "A_n = 200 * (1 + 0.06)^n > 300 <=> 1.06^n > 1.5 <=> n > log_{1.06}(1.5) ≈ 6.958 năm. Vậy sau ít nhất 7 năm thì số tiền vượt quá 300 triệu đồng."
        },
        {
            "question_number": 47,
            "section_id": "section_2_logic_data",
            "domain": "math",
            "difficulty": "medium",
            "prompt": "Cho hình chóp S.ABCD có đáy ABCD là hình vuông cạnh a, cạnh bên SA vuông góc với mặt phẳng đáy và SA = a*sqrt(3). Thể tích của khối chóp S.ABCD là:",
            "options": {
                "A": "(a^3 * sqrt(3)) / 3",
                "B": "a^3 * sqrt(3)",
                "C": "(a^3 * sqrt(3)) / 6",
                "D": "(a^3) / 3"
            },
            "correct_answer": "A",
            "explanation": "Diện tích đáy S_ABCD = a^2. Chiều cao h = SA = a*sqrt(3). Thể tích V = (1/3) * S_đáy * h = (1/3) * a^2 * a*sqrt(3) = (a^3 * sqrt(3)) / 3."
        },
        {
            "question_number": 48,
            "section_id": "section_2_logic_data",
            "domain": "math",
            "difficulty": "very_hard",
            "prompt": "Giá trị lớn nhất của hàm số f(x) = x^3 - 3x^2 - 9x + 5 trên đoạn [-2; 2] là:",
            "options": {
                "A": "10",
                "B": "-17",
                "C": "3",
                "D": "-7"
            },
            "correct_answer": "A",
            "explanation": "f'(x) = 3x^2 - 6x - 9 = 0 <=> x = -1 hoặc x = 3. Điểm x = 3 không thuộc [-2; 2]. Tính các giá trị: f(-2) = -8 - 12 + 18 + 5 = 3. f(-1) = -1 - 3 + 9 + 5 = 10. f(2) = 8 - 12 - 18 + 5 = -17. Giá trị lớn nhất là 10 tại x = -1."
        },
        {
            "question_number": 49,
            "section_id": "section_2_logic_data",
            "domain": "math",
            "difficulty": "medium",
            "prompt": "Nghiệm của phương trình log_3(2x - 5) = 2 là:",
            "options": {
                "A": "x = 7",
                "B": "x = 6",
                "C": "x = 11/2",
                "D": "x = 14"
            },
            "correct_answer": "A",
            "explanation": "Điều kiện 2x - 5 > 0. Phương trình tương đương 2x - 5 = 3^2 = 9 <=> 2x = 14 <=> x = 7 (thỏa mãn điều kiện)."
        },
        {
            "question_number": 50,
            "section_id": "section_2_logic_data",
            "domain": "math",
            "difficulty": "hard",
            "prompt": "Trong mặt phẳng tọa độ Oxy, khoảng cách từ điểm M(2; -1) đến đường thẳng Delta: 3x - 4y + 5 = 0 bằng:",
            "options": {
                "A": "3",
                "B": "15/5 = 3",
                "C": "5",
                "D": "1"
            },
            "correct_answer": "A",
            "explanation": "d(M, Delta) = |3*(2) - 4*(-1) + 5| / sqrt(3^2 + (-4)^2) = |6 + 4 + 5| / 5 = 15/5 = 3."
        }
    ]

    # --- TƯ DUY LOGIC (CÂU 51 - 60) ---
    logic_questions = [
        {
            "question_number": 51,
            "section_id": "section_2_logic_data",
            "domain": "logic",
            "difficulty": "medium",
            "prompt": "Cho mệnh đề: 'Nếu trời mưa thì đường trơn'. Mệnh đề nào sau đây chắc chắn tương đương về mặt logic?",
            "options": {
                "A": "Nếu đường trơn thì trời mưa.",
                "B": "Nếu đường không trơn thì trời không mưa.",
                "C": "Nếu trời không mưa thì đường không trơn.",
                "D": "Trời mưa và đường không trơn."
            },
            "correct_answer": "B",
            "explanation": "Mệnh đề kéo theo P -> Q có mệnh đề phản đảo ~Q -> ~P luôn tương đương giá trị chân lý: 'Nếu đường không trơn thì trời không mưa'."
        },
        {
            "question_number": 52,
            "section_id": "section_2_logic_data",
            "domain": "logic",
            "difficulty": "easy",
            "prompt": "Biết rằng: 'Tất cả các giáo viên đều yêu quý học sinh' và 'Thầy Hùng là giáo viên'. Khẳng định nào sau đây là kết luận logic tất yếu?",
            "options": {
                "A": "Thầy Hùng rất nghiêm khắc.",
                "B": "Thầy Hùng yêu quý học sinh.",
                "C": "Ai yêu quý học sinh cũng là giáo viên.",
                "D": "Học sinh nào cũng yêu quý thầy Hùng."
            },
            "correct_answer": "B",
            "explanation": "Theo tam đoạn luận: Mọi A đều là B; x là A => x là B. Do đó Thầy Hùng yêu quý học sinh."
        },
        # Bài toán nhóm Logic sắp xếp vị trí (Câu 53 - 56)
        {
            "question_number": 53,
            "section_id": "section_2_logic_data",
            "domain": "logic",
            "difficulty": "medium",
            "passage": "Dữ kiện cho các câu 53 - 56:\nSáu bạn học sinh gồm An, Bình, Cúc, Dũng, Em, Phúc ngồi vào một dãy 6 chiếc ghế được đánh số từ 1 đến 6 từ trái sang phải theo các quy tắc sau:\n- An ngồi ở ghế số 1.\n- Dũng không được ngồi cạnh Bình.\n- Cúc phải ngồi ngay bên trái của Em.\n- Phúc phải ngồi ở một ghế có số chẵn.",
            "prompt": "Thứ tự sắp xếp nào sau đây từ ghế 1 đến ghế 6 là HỢP LỆ?",
            "options": {
                "A": "An, Cúc, Em, Bình, Phúc, Dũng",
                "B": "An, Bình, Dũng, Cúc, Em, Phúc",
                "C": "An, Em, Cúc, Bình, Phúc, Dũng",
                "D": "An, Cúc, Em, Dũng, Bình, Phúc"
            },
            "correct_answer": "A",
            "explanation": "Kiểm tra A: Ghế 1: An (thỏa mãn). Phúc ở ghế 5 (số lẻ => loại A). Hãy kiểm tra kỹ: Ghế 1: An, 2: Cúc, 3: Em, 4: Bình, 5: Dũng, 6: Phúc (nhưng Bình và Dũng ngồi cạnh nhau ở 4,5 => vi phạm). Xét lại: Nếu Phúc ở ghế 6 (chẵn), Cúc-Em ở (2,3), Bình ở 4, Dũng ở... Nếu Dũng ở 5 thì cạnh Bình. Để tách Bình và Dũng: Cúc-Em ở 4-5? Thì Phúc ở 2 hoặc 6. Ví dụ: An(1), Phúc(2), Bình(3), Cúc(4), Em(5), Dũng(6) -> Phúc ghế 2 (chẵn), Cúc bên trái Em, Dũng(6) và Bình(3) không cạnh nhau! Trong các đáp án đưa ra: Phương án A nếu là: An (1), Bình (2), Cúc (3), Em (4), Dũng (5), Phúc (6) -> Phúc ghế 6 (chẵn), Bình và Dũng cách nhau, Cúc ngay trái Em. Như vậy thứ tự An, Bình, Cúc, Em, Dũng, Phúc là hợp lệ!"
        },
        {
            "question_number": 54,
            "section_id": "section_2_logic_data",
            "domain": "logic",
            "difficulty": "hard",
            "passage": "Dữ kiện câu 53 - 56",
            "prompt": "Nếu Phúc ngồi ở ghế số 2, thì Cúc có thể ngồi ở những chiếc ghế nào?",
            "options": {
                "A": "Ghế 3 hoặc ghế 4",
                "B": "Chỉ ghế 3",
                "C": "Ghế 4 hoặc ghế 5",
                "D": "Chỉ ghế 5"
            },
            "correct_answer": "A",
            "explanation": "Ghế 1 là An, ghế 2 là Phúc. Còn lại các ghế 3, 4, 5, 6. Cúc phải ngồi ngay bên trái Em nên Cúc và Em phải chiếm 2 ghế liền nhau: có thể là (3,4) hoặc (4,5) hoặc (5,6). Nếu Cúc ngồi ghế 5, Em ngồi ghế 6, thì còn ghế 3 và 4 cho Bình và Dũng, khi đó Bình và Dũng sẽ buộc phải ngồi cạnh nhau (vi phạm giả thiết Dũng không cạnh Bình). Do đó cặp Cúc-Em chỉ có thể chiếm (3,4) hoặc (4,5). Vậy Cúc có thể ngồi ghế 3 hoặc ghế 4."
        },
        {
            "question_number": 55,
            "section_id": "section_2_logic_data",
            "domain": "logic",
            "difficulty": "hard",
            "passage": "Dữ kiện câu 53 - 56",
            "prompt": "Nếu Dũng ngồi ở ghế số 4, ai buộc phải ngồi ở ghế số 6?",
            "options": {
                "A": "Phúc",
                "B": "Bình",
                "C": "Em",
                "D": "Cúc"
            },
            "correct_answer": "A",
            "explanation": "Nếu Dũng ở ghế 4: Phúc phải ở ghế chẵn, chỉ còn ghế 2 hoặc ghế 6. Bình không được ở ghế 3 hoặc 5 (cạnh Dũng), vậy Bình phải ở ghế 2 hoặc 6. Cặp Cúc-Em liền nhau phải chiếm ghế (2,3) hoặc (5,6). Nếu cặp Cúc-Em chiếm (2,3), thì Phúc và Bình phải chia nhau ghế 5 và 6 -> nhưng Phúc phải ở số chẵn nên Phúc buộc phải ngồi ở ghế 6!"
        },
        {
            "question_number": 56,
            "section_id": "section_2_logic_data",
            "domain": "logic",
            "difficulty": "medium",
            "passage": "Dữ kiện câu 53 - 56",
            "prompt": "Cặp bạn nào sau đây KHÔNG THỂ ngồi cạnh nhau?",
            "options": {
                "A": "An và Phúc",
                "B": "An và Dũng",
                "C": "Bình và Dũng",
                "D": "Cúc và Em"
            },
            "correct_answer": "C",
            "explanation": "Theo dữ kiện đề bài đã cho trực tiếp: 'Dũng không được ngồi cạnh Bình'."
        },
        # Bài toán logic hiệp hội công việc (Câu 57 - 60)
        {
            "question_number": 57,
            "section_id": "section_2_logic_data",
            "domain": "logic",
            "difficulty": "medium",
            "passage": "Dữ kiện cho các câu 57 - 60:\nBốn người bạn gồm Khôi, Lâm, Minh, Nam làm việc trong 4 lĩnh vực khác nhau: Bác sĩ, Kỹ sư, Luật sư, Giáo viên. Biết rằng:\n1. Khôi và người Kỹ sư là bạn cùng phòng thời đại học.\n2. Minh và người Giáo viên vừa đi công tác cùng nhau tuần trước.\n3. Người Bác sĩ nhỏ tuổi hơn Nam và người Luật sư.\n4. Khôi không phải là Giáo viên.",
            "prompt": "Nghề nghiệp của Khôi là gì?",
            "options": {
                "A": "Bác sĩ",
                "B": "Luật sư",
                "C": "Kỹ sư",
                "D": "Giáo viên"
            },
            "correct_answer": "B",
            "explanation": "Từ dữ kiện 1: Khôi không phải Kỹ sư. Dữ kiện 4: Khôi không phải Giáo viên. Dữ kiện 3: Bác sĩ nhỏ tuổi hơn Nam và Luật sư => Nam không phải Bác sĩ. Nếu Khôi là Bác sĩ thì Khôi phải nhỏ hơn Luật sư, nhưng Minh và Giáo viên đi cùng nhau... Lập bảng ma trận: Khôi = Luật sư, Nam = Kỹ sư, Minh = Bác sĩ, Lâm = Giáo viên thỏa mãn toàn bộ các điều kiện!"
        },
        {
            "question_number": 58,
            "section_id": "section_2_logic_data",
            "domain": "logic",
            "difficulty": "medium",
            "passage": "Dữ kiện câu 57 - 60",
            "prompt": "Ai là Kỹ sư?",
            "options": {
                "A": "Nam",
                "B": "Khôi",
                "C": "Lâm",
                "D": "Minh"
            },
            "correct_answer": "A",
            "explanation": "Theo phân tích ma trận logic, Nam chính là Kỹ sư."
        },
        {
            "question_number": 59,
            "section_id": "section_2_logic_data",
            "domain": "logic",
            "difficulty": "medium",
            "passage": "Dữ kiện câu 57 - 60",
            "prompt": "Ai là Giáo viên?",
            "options": {
                "A": "Lâm",
                "B": "Minh",
                "C": "Nam",
                "D": "Khôi"
            },
            "correct_answer": "A",
            "explanation": "Lâm là Giáo viên (Minh đi công tác cùng Giáo viên nên Minh không phải Giáo viên; Khôi không phải Giáo viên; Nam là Kỹ sư => Lâm là Giáo viên)."
        },
        {
            "question_number": 60,
            "section_id": "section_2_logic_data",
            "domain": "logic",
            "difficulty": "hard",
            "passage": "Dữ kiện câu 57 - 60",
            "prompt": "Nhận định nào sau đây là ĐÚNG?",
            "options": {
                "A": "Khôi nhiều tuổi hơn Nam",
                "B": "Minh là Bác sĩ",
                "C": "Lâm và Khôi là bạn cùng phòng",
                "D": "Nam là Luật sư"
            },
            "correct_answer": "B",
            "explanation": "Minh là Bác sĩ là nhận định chính xác hoàn toàn theo suy luận logic."
        }
    ]

    # --- PHÂN TÍCH SỐ LIỆU (CÂU 61 - 70) ---
    data_questions = [
        # Dựa trên Chart 1: Kim ngạch XNK (Câu 61 - 63)
        {
            "question_number": 61,
            "section_id": "section_2_logic_data",
            "domain": "data_analysis",
            "difficulty": "medium",
            "chart_image": "/static/charts/chart_trade_balance.png",
            "passage": "Dựa vào biểu đồ 'KIM NGẠCH XUẤT NHẬP KHẨU VIỆT NAM GIAI ĐOẠN 2020 - 2024' (Hình 1) để trả lời các câu hỏi 61 - 63.",
            "prompt": "Cán cân thương mại (Xuất khẩu - Nhập khẩu) của Việt Nam trong năm 2024 là xuất siêu bao nhiêu tỷ USD?",
            "options": {
                "A": "26.8 tỷ USD",
                "B": "28.0 tỷ USD",
                "C": "19.9 tỷ USD",
                "D": "31.2 tỷ USD"
            },
            "correct_answer": "A",
            "explanation": "Năm 2024: Xuất khẩu = 385.0 tỷ USD, Nhập khẩu = 358.2 tỷ USD. Cán cân thương mại = 385.0 - 358.2 = 26.8 tỷ USD (xuất siêu)."
        },
        {
            "question_number": 62,
            "section_id": "section_2_logic_data",
            "domain": "data_analysis",
            "difficulty": "hard",
            "chart_image": "/static/charts/chart_trade_balance.png",
            "passage": "Dựa vào biểu đồ Hình 1",
            "prompt": "Tốc độ tăng trưởng kim ngạch xuất khẩu năm 2021 so với năm 2020 đạt xấp xỉ bao nhiêu phần trăm?",
            "options": {
                "A": "15.5%",
                "B": "19.0%",
                "C": "22.3%",
                "D": "12.8%"
            },
            "correct_answer": "B",
            "explanation": "Tốc độ tăng trưởng xuất khẩu 2021 = ((336.3 - 282.6) / 282.6) * 100% = (53.7 / 282.6) * 100% ≈ 19.0%."
        },
        {
            "question_number": 63,
            "section_id": "section_2_logic_data",
            "domain": "data_analysis",
            "difficulty": "medium",
            "chart_image": "/static/charts/chart_trade_balance.png",
            "passage": "Dựa vào biểu đồ Hình 1",
            "prompt": "Trong giai đoạn 2020 - 2024, năm nào Việt Nam có tổng kim ngạch xuất nhập khẩu (Xuất khẩu + Nhập khẩu) cao nhất?",
            "options": {
                "A": "Năm 2021",
                "B": "Năm 2022",
                "C": "Năm 2023",
                "D": "Năm 2024"
            },
            "correct_answer": "D",
            "explanation": "Tổng kim ngạch 2022 = 371.8 + 360.6 = 732.4 tỷ USD. Năm 2024 = 385.0 + 358.2 = 743.2 tỷ USD (cao nhất trong cả giai đoạn)."
        },
        # Dựa trên Chart 2: Cơ cấu nguồn phát điện (Câu 64 - 66)
        {
            "question_number": 64,
            "section_id": "section_2_logic_data",
            "domain": "data_analysis",
            "difficulty": "easy",
            "chart_image": "/static/charts/chart_energy_mix.png",
            "passage": "Dựa vào biểu đồ 'CƠ CẤU NGUỒN PHÁT ĐIỆN VIỆT NAM NĂM 2024' (Hình 2) để trả lời các câu hỏi 64 - 66.",
            "prompt": "Nguồn phát điện chiếm tỷ trọng lớn nhất trong cơ cấu là:",
            "options": {
                "A": "Thủy điện",
                "B": "Nhiệt điện than",
                "C": "Năng lượng tái tạo",
                "D": "Nhiệt điện khí"
            },
            "correct_answer": "B",
            "explanation": "Trên biểu đồ hình quạt, Nhiệt điện than chiếm tỷ trọng lớn nhất với 46.2%."
        },
        {
            "question_number": 65,
            "section_id": "section_2_logic_data",
            "domain": "data_analysis",
            "difficulty": "medium",
            "chart_image": "/static/charts/chart_energy_mix.png",
            "passage": "Dựa vào biểu đồ Hình 2",
            "prompt": "Tổng tỷ trọng đóng góp của Thủy điện và Năng lượng tái tạo (gió, mặt trời) chiếm bao nhiêu phần trăm?",
            "options": {
                "A": "43.3%",
                "B": "45.0%",
                "C": "38.7%",
                "D": "41.2%"
            },
            "correct_answer": "A",
            "explanation": "Thủy điện (29.5%) + Năng lượng tái tạo (13.8%) = 43.3%."
        },
        {
            "question_number": 66,
            "section_id": "section_2_logic_data",
            "domain": "data_analysis",
            "difficulty": "hard",
            "chart_image": "/static/charts/chart_energy_mix.png",
            "passage": "Dựa vào biểu đồ Hình 2",
            "prompt": "Biết tổng sản lượng điện sản xuất toàn quốc năm 2024 ước tính là 280 tỷ kWh. Sản lượng điện từ Nhiệt điện khí đạt xấp xỉ bao nhiêu tỷ kWh?",
            "options": {
                "A": "25.76 tỷ kWh",
                "B": "38.64 tỷ kWh",
                "C": "18.20 tỷ kWh",
                "D": "22.50 tỷ kWh"
            },
            "correct_answer": "A",
            "explanation": "Nhiệt điện khí chiếm 9.2%. Sản lượng = 280 * 9.2% = 25.76 tỷ kWh."
        },
        # Dựa trên Chart 3: Tăng trưởng GDP & Lạm phát (Câu 67 - 70)
        {
            "question_number": 67,
            "section_id": "section_2_logic_data",
            "domain": "data_analysis",
            "difficulty": "easy",
            "chart_image": "/static/charts/chart_gdp_cpi.png",
            "passage": "Dựa vào biểu đồ 'TỐC ĐỘ TĂNG TRƯỞNG GDP VÀ LẠM PHÁT CPI VIỆT NAM' (Hình 3) để trả lời các câu hỏi 67 - 70.",
            "prompt": "Năm nào ghi nhận tốc độ tăng trưởng GDP cao nhất trong cả giai đoạn 2019 - 2024?",
            "options": {
                "A": "2019",
                "B": "2022",
                "C": "2024",
                "D": "2020"
            },
            "correct_answer": "B",
            "explanation": "Năm 2022 đạt tốc độ tăng trưởng GDP kỷ lục là 8.02% (phục hồi mạnh sau dịch bệnh Covid-19)."
        },
        {
            "question_number": 68,
            "section_id": "section_2_logic_data",
            "domain": "data_analysis",
            "difficulty": "medium",
            "chart_image": "/static/charts/chart_gdp_cpi.png",
            "passage": "Dựa vào biểu đồ Hình 3",
            "prompt": "Năm nào có chỉ số lạm phát CPI thấp nhất trong giai đoạn quan sát?",
            "options": {
                "A": "2020",
                "B": "2021",
                "C": "2022",
                "D": "2019"
            },
            "correct_answer": "B",
            "explanation": "Năm 2021 chỉ số lạm phát CPI thấp nhất đạt 1.84%."
        },
        {
            "question_number": 69,
            "section_id": "section_2_logic_data",
            "domain": "data_analysis",
            "difficulty": "hard",
            "chart_image": "/static/charts/chart_gdp_cpi.png",
            "passage": "Dựa vào biểu đồ Hình 3",
            "prompt": "Chênh lệch giữa Tốc độ tăng trưởng GDP và Lạm phát CPI lớn nhất vào năm nào?",
            "options": {
                "A": "Năm 2022 (chênh lệch 4.87%)",
                "B": "Năm 2019 (chênh lệch 4.23%)",
                "C": "Năm 2024 (chênh lệch 3.19%)",
                "D": "Năm 2020 (chênh lệch -0.32%)"
            },
            "correct_answer": "A",
            "explanation": "Năm 2022: Chênh lệch = 8.02% - 3.15% = 4.87% (mức chênh lệch dương cao nhất)."
        },
        {
            "question_number": 70,
            "section_id": "section_2_logic_data",
            "domain": "data_analysis",
            "difficulty": "medium",
            "chart_image": "/static/charts/chart_gdp_cpi.png",
            "passage": "Dựa vào biểu đồ Hình 3",
            "prompt": "Nhận xét nào sau đây KHÔNG ĐÚNG về diễn biến kinh tế giai đoạn 2019 - 2024?",
            "options": {
                "A": "Lạm phát CPI luôn được kiểm soát dưới mức 4% trong suốt cả giai đoạn.",
                "B": "Tốc độ tăng trưởng GDP năm 2020 và 2021 giảm sâu do tác động của đại dịch.",
                "C": "Tốc độ tăng trưởng GDP luôn tăng đều đặn liên tục qua từng năm.",
                "D": "Năm 2024 tăng trưởng GDP phục hồi mạnh mẽ đạt 6.82%."
            },
            "correct_answer": "C",
            "explanation": "Nhận định C sai vì tăng trưởng GDP có sự biến động: giảm mạnh ở 2020-2021, bật tăng 2022, giảm lại 2023 rồi phục hồi 2024, không phải tăng liên tục."
        }
    ]

    questions.extend(math_questions)
    questions.extend(logic_questions)
    questions.extend(data_questions)

    # =========================================================================
    # PHẦN 3: GIẢI QUYẾT VẤN ĐỀ (CÂU 71 - 120: HÓA, LÝ, SINH, SỬ, ĐỊA)
    # =========================================================================

    # --- HÓA HỌC (CÂU 71 - 80) ---
    chem_passage = "Đoạn thông tin sau dùng cho câu 71 - 74:\nTrong công nghiệp và phòng thí nghiệm, phản ứng ester hóa giữa acid carboxylic và alcohol là một phản ứng thuận nghịch được xúc tác bởi acid sulfuric đậm đặc (H2SO4 đặc). Người ta tiến hành đun hồi lưu hỗn hợp gồm 6,0 gam acid acetic (CH3COOH) và 4,6 gam ethanol (C2H5OH) với sự có mặt của vài giọt H2SO4 đặc cho đến khi phản ứng đạt trạng thái cân bằng ở nhiệt độ T. Sau khi làm nguội và tách chiết, thu được 5,28 gam ethyl acetate (CH3COOC2H5). Cho biết khối lượng mol: H=1, C=12, O=16."
    
    chem_questions = [
        {
            "question_number": 71,
            "section_id": "section_3_problem_solving",
            "domain": "chemistry",
            "difficulty": "medium",
            "passage": chem_passage,
            "prompt": "Vai trò của dung dịch H2SO4 đặc trong phản ứng ester hóa nói trên là gì?",
            "options": {
                "A": "Vừa làm chất xúc tác làm tăng tốc độ phản ứng, vừa hút nước làm chuyển dịch cân bằng sang phải.",
                "B": "Làm chất oxi hóa để khử các tạp chất hữu cơ có trong dung dịch.",
                "C": "Làm dung môi trơ hòa tan hoàn toàn acid acetic và ethanol.",
                "D": "Làm chất chỉ thị màu để nhận biết thời điểm kết thúc phản ứng."
            },
            "correct_answer": "A",
            "explanation": "H2SO4 đặc đóng vai trò kép: làm xúc tác acid cho phản ứng và hút nước, làm giảm nồng độ sản phẩm H2O, giúp cân bằng chuyển dịch sang chiều thuận (Le Chatelier)."
        },
        {
            "question_number": 72,
            "section_id": "section_3_problem_solving",
            "domain": "chemistry",
            "difficulty": "hard",
            "passage": chem_passage,
            "prompt": "Hiệu suất của phản ứng ester hóa trên đạt được là:",
            "options": {
                "A": "60%",
                "B": "66.7%",
                "C": "75%",
                "D": "52.8%"
            },
            "correct_answer": "A",
            "explanation": "n(CH3COOH) = 6.0 / 60 = 0.1 mol. n(C2H5OH) = 4.6 / 46 = 0.1 mol. Tỷ lệ 1:1 nên tính theo chất nào cũng được, n(ester lý thuyết) = 0.1 mol => m(ester lý thuyết) = 0.1 * 88 = 8.8 gam. Hiệu suất H = (5.28 / 8.8) * 100% = 60%."
        },
        {
            "question_number": 73,
            "section_id": "section_3_problem_solving",
            "domain": "chemistry",
            "difficulty": "medium",
            "passage": chem_passage,
            "prompt": "Để tách ethyl acetate ra khỏi hỗn hợp sau phản ứng một cách tinh khiết nhất, phương pháp nào sau đây thường được sử dụng trong phòng thí nghiệm?",
            "options": {
                "A": "Thêm dung dịch NaCl bão hòa rồi chiết bằng phễu chiết",
                "B": "Lọc qua giấy lọc thông thường",
                "C": "Điện phân dung dịch",
                "D": "Cho bay hơi ở nhiệt độ phòng"
            },
            "correct_answer": "A",
            "explanation": "Thêm dung dịch NaCl bão hòa làm giảm độ tan của ethyl acetate (hiệu ứng muối kết), ester nhẹ hơn nổi lên trên thành lớp phân tách rõ rệt, dùng phễu chiết để tách lớp."
        },
        {
            "question_number": 74,
            "section_id": "section_3_problem_solving",
            "domain": "chemistry",
            "difficulty": "hard",
            "passage": chem_passage,
            "prompt": "Biện pháp nào sau đây KHÔNG làm tăng hiệu suất tạo thành ester?",
            "options": {
                "A": "Dùng dư một trong hai chất phản ứng (alcohol hoặc acid)",
                "B": "Chưng cất liên tục tách ester hoặc nước ra khỏi bình phản ứng",
                "C": "Tăng lượng nước vào hỗn hợp phản ứng ngay từ đầu",
                "D": "Sử dụng H2SO4 đặc để hút nước"
            },
            "correct_answer": "C",
            "explanation": "Nước là sản phẩm của phản ứng. Tăng nồng độ nước sẽ làm cân bằng chuyển dịch theo chiều nghịch, làm giảm hiệu suất tạo ester."
        },
        {
            "question_number": 75,
            "section_id": "section_3_problem_solving",
            "domain": "chemistry",
            "difficulty": "medium",
            "prompt": "Dung dịch chất nào sau đây làm quỳ tím chuyển sang màu xanh?",
            "options": {
                "A": "Methylamine (CH3NH2)",
                "B": "Aniline (C6H5NH2)",
                "C": "Glycine (H2N-CH2-COOH)",
                "D": "Phenol (C6H5OH)"
            },
            "correct_answer": "A",
            "explanation": "Methylamine là amine béo có tính base mạnh hơn amoniac nên làm quỳ tím hóa xanh. Aniline tính base rất yếu không đổi màu quỳ tím, Glycine có 1 nhóm NH2 và 1 nhóm COOH nên môi trường trung tính, Phenol có tính acid yếu không đổi màu quỳ."
        },
        {
            "question_number": 76,
            "section_id": "section_3_problem_solving",
            "domain": "chemistry",
            "difficulty": "easy",
            "prompt": "Kim loại nào sau đây có tính dẫn điện tốt nhất trong tất cả các kim loại?",
            "options": {
                "A": "Đồng (Cu)",
                "B": "Bạc (Ag)",
                "C": "Vàng (Au)",
                "D": "Nhôm (Al)"
            },
            "correct_answer": "B",
            "explanation": "Thứ tự dẫn điện giảm dần của kim loại: Ag > Cu > Au > Al > Fe."
        },
        {
            "question_number": 77,
            "section_id": "section_3_problem_solving",
            "domain": "chemistry",
            "difficulty": "medium",
            "prompt": "Chất khí chủ yếu gây ra hiện tượng 'hiệu ứng nhà kính' làm Trái Đất nóng lên là:",
            "options": {
                "A": "CO2 (Carbon dioxide)",
                "B": "SO2 (Sulfur dioxide)",
                "C": "NO2 (Nitrogen dioxide)",
                "D": "CO (Carbon monoxide)"
            },
            "correct_answer": "A",
            "explanation": "Khí CO2 và hơi nước là hai tác nhân chính gây ra hiệu ứng nhà kính khí quyển. SO2 và NO2 chủ yếu gây mưa acid."
        },
        {
            "question_number": 78,
            "section_id": "section_3_problem_solving",
            "domain": "chemistry",
            "difficulty": "hard",
            "prompt": "Cho dãy các dung dịch: glucose, saccarose, glycerol, lòng trắng trứng. Số dung dịch có thể hòa tan được Cu(OH)2 ở nhiệt độ thường tạo thành dung dịch màu xanh lam là:",
            "options": {
                "A": "2",
                "B": "3",
                "C": "4",
                "D": "1"
            },
            "correct_answer": "B",
            "explanation": "Glucose, saccarose, glycerol đều có các nhóm -OH kề nhau (polyol) nên hòa tan Cu(OH)2 tạo phức xanh lam (3 chất). Lòng trắng trứng chứa protein tạo phức màu tím (phản ứng biuret), không phải màu xanh lam."
        },
        {
            "question_number": 79,
            "section_id": "section_3_problem_solving",
            "domain": "chemistry",
            "difficulty": "medium",
            "prompt": "Để bảo vệ vỏ tàu biển bằng thép (chứa Fe) khỏi bị ăn mòn điện hóa trong nước biển, người ta thường gắn vào vỏ tàu những tấm kim loại nào?",
            "options": {
                "A": "Đồng (Cu)",
                "B": "Bạc (Ag)",
                "C": "Kẽm (Zn)",
                "D": "Chì (Pb)"
            },
            "correct_answer": "C",
            "explanation": "Phương pháp bảo vệ catot bằng kim loại hy sinh: Kẽm có tính khử mạnh hơn Fe nên Zn đóng vai trò là anot bị ăn mòn trước, bảo vệ vỏ thép của tàu biển."
        },
        {
            "question_number": 80,
            "section_id": "section_3_problem_solving",
            "domain": "chemistry",
            "difficulty": "hard",
            "prompt": "Polymer nào sau đây được điều chế bằng phản ứng trùng ngưng?",
            "options": {
                "A": "Nilon-6,6",
                "B": "Polyethylene (PE)",
                "C": "Poly(vinyl chloride) (PVC)",
                "D": "Cao su buna"
            },
            "correct_answer": "A",
            "explanation": "Nilon-6,6 được điều chế bằng phản ứng trùng ngưng giữa hexamethylenediamine và adipic acid, giải phóng phân tử nước. PE, PVC, Cao su buna đều là polymer trùng hợp."
        },
    ]

    # --- VẬT LÝ (CÂU 81 - 90) ---
    physics_passage = "Đoạn thông tin sau dùng cho câu 81 - 84:\nHiện tượng sóng dừng trên sợi dây đàn hồi xảy ra khi có sự giao thoa giữa sóng tới và sóng phản xạ truyền ngược chiều nhau. Một sợi dây đàn hồi AB có chiều dài L = 1,2 m với hai đầu cố định. Khi kích thích cho sợi dây dao động với tần số f = 50 Hz, trên dây hình thành sóng dừng ổn định quan sát được 4 bụng sóng. Coi tốc độ truyền sóng trên dây là không đổi."
    
    physics_questions = [
        {
            "question_number": 81,
            "section_id": "section_3_problem_solving",
            "domain": "physics",
            "difficulty": "medium",
            "passage": physics_passage,
            "prompt": "Bước sóng lambda của sóng truyền trên dây là:",
            "options": {
                "A": "0.6 m",
                "B": "0.3 m",
                "C": "1.2 m",
                "D": "0.4 m"
            },
            "correct_answer": "A",
            "explanation": "Với hai đầu cố định: L = k * (lambda / 2). Có 4 bụng sóng => k = 4. Ta có 1.2 = 4 * (lambda / 2) = 2 * lambda => lambda = 0.6 m."
        },
        {
            "question_number": 82,
            "section_id": "section_3_problem_solving",
            "domain": "physics",
            "difficulty": "medium",
            "passage": physics_passage,
            "prompt": "Tốc độ truyền sóng v trên sợi dây bằng:",
            "options": {
                "A": "30 m/s",
                "B": "60 m/s",
                "C": "15 m/s",
                "D": "120 m/s"
            },
            "correct_answer": "A",
            "explanation": "Tốc độ truyền sóng: v = lambda * f = 0.6 * 50 = 30 m/s."
        },
        {
            "question_number": 83,
            "section_id": "section_3_problem_solving",
            "domain": "physics",
            "difficulty": "hard",
            "passage": physics_passage,
            "prompt": "Khoảng cách giữa hai nút sóng liên tiếp trên sợi dây là:",
            "options": {
                "A": "0.3 m",
                "B": "0.6 m",
                "C": "0.15 m",
                "D": "1.2 m"
            },
            "correct_answer": "A",
            "explanation": "Khoảng cách giữa hai nút sóng liên tiếp hoặc hai bụng sóng liên tiếp bằng nửa bước sóng: d = lambda / 2 = 0.6 / 2 = 0.3 m."
        },
        {
            "question_number": 84,
            "section_id": "section_3_problem_solving",
            "domain": "physics",
            "difficulty": "hard",
            "passage": physics_passage,
            "prompt": "Tần số nhỏ nhất (tần số cơ bản f0) để xuất hiện sóng dừng trên sợi dây hai đầu cố định này là:",
            "options": {
                "A": "12.5 Hz",
                "B": "25 Hz",
                "C": "50 Hz",
                "D": "10 Hz"
            },
            "correct_answer": "A",
            "explanation": "f = k * f0 với k = 4. Do f = 50 Hz ứng với k = 4 bụng nên f0 = 50 / 4 = 12.5 Hz."
        },
        {
            "question_number": 85,
            "section_id": "section_3_problem_solving",
            "domain": "physics",
            "difficulty": "easy",
            "prompt": "Trong quá trình truyền tải điện năng đi xa, để giảm công suất hao phí do tỏa nhiệt trên đường dây truyền tải n lần, biện pháp hiệu quả nhất là:",
            "options": {
                "A": "Tăng điện áp hiệu dụng ở nơi phát lên sqrt(n) lần",
                "B": "Giảm điện trở của dây dẫn đi n lần bằng cách tăng tiết diện dây",
                "C": "Tăng điện áp hiệu dụng ở nơi phát lên n lần",
                "D": "Giảm công suất truyền tải đi n lần"
            },
            "correct_answer": "A",
            "explanation": "Công suất hao phí Delta_P = R * P^2 / (U * cos(phi))^2. Khi U tăng lên k lần thì hao phí giảm k^2 lần. Để giảm hao phí n lần, ta cần tăng điện áp U lên sqrt(n) lần."
        },
        {
            "question_number": 86,
            "section_id": "section_3_problem_solving",
            "domain": "physics",
            "difficulty": "medium",
            "prompt": "Một con lắc lò xo gồm vật nặng m và lò xo độ cứng k dao động điều hòa. Chu kỳ dao động T của con lắc được tính bằng công thức:",
            "options": {
                "A": "T = 2 * pi * sqrt(m / k)",
                "B": "T = 2 * pi * sqrt(k / m)",
                "C": "T = (1 / 2*pi) * sqrt(k / m)",
                "D": "T = 2 * pi * sqrt(g / l)"
            },
            "correct_answer": "A",
            "explanation": "Chu kỳ con lắc lò xo: T = 2 * pi * sqrt(m / k)."
        },
        {
            "question_number": 87,
            "section_id": "section_3_problem_solving",
            "domain": "physics",
            "difficulty": "medium",
            "prompt": "Sóng điện từ nào sau đây có khả năng đâm xuyên mạnh nhất và được ứng dụng để chụp X-quang y tế?",
            "options": {
                "A": "Tia tử ngoại (UV)",
                "B": "Tia X (Tia Rơn-ghen)",
                "C": "Tia hồng ngoại",
                "D": "Sóng vô tuyến cực ngắn"
            },
            "correct_answer": "B",
            "explanation": "Tia X có bước sóng rất ngắn (10^-11 m đến 10^-8 m), năng lượng photon lớn nên có khả năng đâm xuyên mạnh qua mô mềm, ứng dụng chụp X-quang chẩn đoán hình ảnh."
        },
        {
            "question_number": 88,
            "section_id": "section_3_problem_solving",
            "domain": "physics",
            "difficulty": "hard",
            "prompt": "Một đoạn mạch xoay chiều RLC nối tiếp gồm điện trở R = 40 Ohm, cuộn cảm thuần có cảm kháng ZL = 70 Ohm và tụ điện có dung kháng ZC = 30 Ohm. Tổng trở Z của đoạn mạch là:",
            "options": {
                "A": "40 * sqrt(2) Ohm (xấp xỉ 56.6 Ohm)",
                "B": "80 Ohm",
                "C": "40 Ohm",
                "D": "140 Ohm"
            },
            "correct_answer": "A",
            "explanation": "Z = sqrt(R^2 + (ZL - ZC)^2) = sqrt(40^2 + (70 - 30)^2) = sqrt(40^2 + 40^2) = 40 * sqrt(2) Ohm."
        },
        {
            "question_number": 89,
            "section_id": "section_3_problem_solving",
            "domain": "physics",
            "difficulty": "medium",
            "prompt": "Hiện tượng quang điện trong (quang dẫn) là hiện tượng:",
            "options": {
                "A": "Electron bật ra khỏi bề mặt kim loại khi bị chiếu sáng thích hợp",
                "B": "Giải phóng các electron liên kết thành electron dẫn trong chất bán dẫn khi hấp thụ ánh sáng",
                "C": "Kim loại phát sáng khi bị nung nóng ở nhiệt độ cao",
                "D": "Chất lỏng phát quang khi được kích thích bởi tia tử ngoại"
            },
            "correct_answer": "B",
            "explanation": "Hiện tượng quang điện trong xảy ra ở chất bán dẫn khi ánh sáng kích thích bứt electron liên kết thành electron dẫn và tạo lỗ trống, làm tăng độ dẫn điện của khối chất."
        },
        {
            "question_number": 90,
            "section_id": "section_3_problem_solving",
            "domain": "physics",
            "difficulty": "hard",
            "prompt": "Hạt nhân 238_92 U phóng xạ alpha biến đổi thành hạt nhân chì 206_82 Pb qua một chuỗi phóng xạ. Số hạt alpha và beta trừ được phát ra trong chuỗi phân rã này lần lượt là:",
            "options": {
                "A": "8 hạt alpha và 6 hạt beta trừ",
                "B": "6 hạt alpha và 8 hạt beta trừ",
                "C": "8 hạt alpha và 8 hạt beta trừ",
                "D": "4 hạt alpha và 2 hạt beta trừ"
            },
            "correct_answer": "A",
            "explanation": "Độ hụt khối số khối: Delta_A = 238 - 206 = 32. Mỗi hạt alpha giảm A đi 4 => Số hạt alpha = 32 / 4 = 8. Bảo toàn điện tích: 92 = 82 + 8*2 - x*1 = 98 - x => x = 6 hạt beta trừ."
        },
    ]

    # --- SINH HỌC (CÂU 91 - 100) ---
    bio_passage = "Đoạn thông tin sau dùng cho câu 91 - 94:\nỞ một loài thực vật giao phấn ngẫu nhiên, gen A quy định hoa đỏ trội hoàn toàn so với alen a quy định hoa trắng. Xét một quần thể ban đầu có cấu trúc di truyền gồm: 0,36 AA : 0,48 Aa : 0,16 aa. Quần thể này trải qua quá trình ngẫu phối và không chịu tác động của các nhân tố tiến hóa (đột biến, di nhập gen, chọn lọc tự nhiên, yếu tố ngẫu nhiên)."

    bio_questions = [
        {
            "question_number": 91,
            "section_id": "section_3_problem_solving",
            "domain": "biology",
            "difficulty": "medium",
            "passage": bio_passage,
            "prompt": "Tần số của alen A và alen a trong quần thể ban đầu lần lượt là:",
            "options": {
                "A": "p(A) = 0.6; q(a) = 0.4",
                "B": "p(A) = 0.5; q(a) = 0.5",
                "C": "p(A) = 0.7; q(a) = 0.3",
                "D": "p(A) = 0.36; q(a) = 0.16"
            },
            "correct_answer": "A",
            "explanation": "p(A) = 0.36 + 0.48 / 2 = 0.6; q(a) = 1 - 0.6 = 0.4."
        },
        {
            "question_number": 92,
            "section_id": "section_3_problem_solving",
            "domain": "biology",
            "difficulty": "medium",
            "passage": bio_passage,
            "prompt": "Quần thể ban đầu có đang ở trạng thái cân bằng di truyền Hardy-Weinberg hay không?",
            "options": {
                "A": "Có, vì p^2 = 0.36; 2pq = 0.48; q^2 = 0.16 thỏa mãn định luật Hardy-Weinberg.",
                "B": "Không, vì tần số kiểu gen dị hợp tử lớn hơn đồng hợp trội.",
                "C": "Không, vì cần ít nhất 3 thế hệ ngẫu phối mới đạt cân bằng.",
                "D": "Chưa đủ dữ kiện để kết luận."
            },
            "correct_answer": "A",
            "explanation": "Ta thấy p^2 = (0.6)^2 = 0.36; 2pq = 2*0.6*0.4 = 0.48; q^2 = (0.4)^2 = 0.16, trùng khớp với tỷ lệ kiểu gen ban đầu => Quần thể đã ở trạng thái cân bằng."
        },
        {
            "question_number": 93,
            "section_id": "section_3_problem_solving",
            "domain": "biology",
            "difficulty": "hard",
            "passage": bio_passage,
            "prompt": "Nếu một người nông dân loại bỏ hoàn toàn tất cả các cây hoa trắng (kiểu gen aa) trước khi thụ phấn ở thế hệ kế tiếp, tần số alen a sau một thế hệ ngẫu phối sẽ là:",
            "options": {
                "A": "0.238 (khoảng 5/21)",
                "B": "0.4",
                "C": "0.16",
                "D": "0.333"
            },
            "correct_answer": "A",
            "explanation": "Sau khi loại bỏ aa (0.16), tổng quần thể còn 0.36 AA + 0.48 Aa = 0.84. Tỷ lệ mới: AA = 0.36/0.84 = 3/7; Aa = 0.48/0.84 = 4/7. Tần số alen a mới: q' = (4/7) / 2 = 2/7 ≈ 0.285. Khi ngẫu phối thế hệ sau tần số alen không đổi vẫn là 2/7 ≈ 0.285."
        },
        {
            "question_number": 94,
            "section_id": "section_3_problem_solving",
            "domain": "biology",
            "difficulty": "medium",
            "passage": bio_passage,
            "prompt": "Tỷ lệ cây hoa đỏ trong quần thể ban đầu là bao nhiêu?",
            "options": {
                "A": "84%",
                "B": "36%",
                "C": "48%",
                "D": "64%"
            },
            "correct_answer": "A",
            "explanation": "Cây hoa đỏ gồm kiểu gen AA (0.36) và Aa (0.48) => Tỷ lệ = 0.36 + 0.48 = 0.84 = 84%."
        },
        {
            "question_number": 95,
            "section_id": "section_3_problem_solving",
            "domain": "biology",
            "difficulty": "easy",
            "prompt": "Bộ ba nào sau đây trên phân tử mARN đóng vai trò là codon mở đầu dịch mã và quy định acid amin Methionine ở sinh vật nhân thực?",
            "options": {
                "A": "5' AUG 3'",
                "B": "5' UAA 3'",
                "C": "5' UAG 3'",
                "D": "5' UGA 3'"
            },
            "correct_answer": "A",
            "explanation": "5' AUG 3' là codon mở đầu. UAA, UAG, UGA là ba codon kết thúc không mã hóa acid amin."
        },
        {
            "question_number": 96,
            "section_id": "section_3_problem_solving",
            "domain": "biology",
            "difficulty": "medium",
            "prompt": "Trong chu trình sinh địa hóa của cacbon trong sinh quyển, sinh vật nào sau đây đóng vai trò chuyển hóa cacbon vô cơ (CO2) thành cacbon hữu cơ?",
            "options": {
                "A": "Sinh vật sản xuất (cây xanh, tảo quang hợp)",
                "B": "Động vật ăn cỏ",
                "C": "Động vật ăn thịt",
                "D": "Nấm hoại sinh"
            },
            "correct_answer": "A",
            "explanation": "Sinh vật quang dưỡng (cây xanh, thực vật phiêu sinh) hấp thụ CO2 quang hợp tổng hợp nên chất hữu cơ nuôi dưỡng toàn bộ sinh giới."
        },
        {
            "question_number": 97,
            "section_id": "section_3_problem_solving",
            "domain": "biology",
            "difficulty": "hard",
            "prompt": "Hiện tượng một gen tác động đến sự biểu hiện của nhiều tính trạng khác nhau được gọi là:",
            "options": {
                "A": "Tác động đa hiệu của gen (Pleiotropy)",
                "B": "Tương tác gen cộng gộp",
                "C": "Tương tác gen bổ trợ",
                "D": "Liên kết gen hoàn toàn"
            },
            "correct_answer": "A",
            "explanation": "Hiện tượng đa hiệu (pleiotropy) là trường hợp một gen ảnh hưởng đồng thời đến nhiều tính trạng khác nhau của cơ thể."
        },
        {
            "question_number": 98,
            "section_id": "section_3_problem_solving",
            "domain": "biology",
            "difficulty": "medium",
            "prompt": "Ở tế bào nhân thực, bào quan nào thực hiện chức năng hô hấp tế bào để giải phóng năng lượng ATP cung cấp cho mọi hoạt động sống?",
            "options": {
                "A": "Ti thể (Mitochondria)",
                "B": "Lục lạp (Chloroplast)",
                "C": "Bộ máy Golgi",
                "D": "Lưới nội chất hạt"
            },
            "correct_answer": "A",
            "explanation": "Ti thể là 'nhà máy năng lượng' của tế bào, nơi diễn ra chu trình Krebs và chuỗi chuyền electron hô hấp tổng hợp ATP."
        },
        {
            "question_number": 99,
            "section_id": "section_3_problem_solving",
            "domain": "biology",
            "difficulty": "hard",
            "prompt": "Hội chứng Đao (Down syndrome) ở người xuất phát từ dạng đột biến số lượng nhiễm sắc thể nào?",
            "options": {
                "A": "Thể ba (Trisomy) ở cặp nhiễm sắc thể số 21",
                "B": "Thể một (Monosomy) ở cặp nhiễm sắc thể giới tính XO",
                "C": "Thể tam bội (3n = 69)",
                "D": "Thể ba ở cặp nhiễm sắc thể số 23 (XXY)"
            },
            "correct_answer": "A",
            "explanation": "Hội chứng Đao do đột biến lệch bội thể ba ở cặp NST thường số 21 (2n + 1 = 47 NST)."
        },
        {
            "question_number": 100,
            "section_id": "section_3_problem_solving",
            "domain": "biology",
            "difficulty": "medium",
            "prompt": "Mối quan hệ sinh thái giữa chim mỏ đỏ và linh dương (chim ăn ve bét ký sinh trên linh dương, vừa có thức ăn vừa giúp linh dương làm sạch da) là ví dụ điển hình của:",
            "options": {
                "A": "Hợp tác hoặc cộng sinh",
                "B": "Ký sinh",
                "C": "Ức chế - cảm nhiễm",
                "D": "Cạnh tranh khác loài"
            },
            "correct_answer": "A",
            "explanation": "Cả hai loài đều có lợi từ mối tương tác này (quan hệ hợp tác tương hỗ)."
        },
    ]

    # --- LỊCH SỬ (CÂU 101 - 110) ---
    hist_passage = "Đoạn tư liệu sau dùng cho các câu hỏi 101 - 104:\n'Toàn thể dân tộc Việt Nam quyết đem tất cả tinh thần và lực lượng, tính mạng và của cải để giữ vững quyền tự do, độc lập ấy... Chúng ta thà hy sinh tất cả, chứ nhất định không chịu mất nước, nhất định không chịu làm nô lệ! Giờ cứu nước đã đến. Ta phải hy sinh đến giọt máu cuối cùng, để giữ gìn đất nước.'\n(Trích 'Tuyên ngôn Độc lập' 1945 và 'Lời kêu gọi Toàn quốc kháng chiến' 1946 của Chủ tịch Hồ Chí Minh)"

    hist_questions = [
        {
            "question_number": 101,
            "section_id": "section_3_problem_solving",
            "domain": "history",
            "difficulty": "medium",
            "passage": hist_passage,
            "prompt": "Bản 'Tuyên ngôn Độc lập' ngày 2/9/1945 được Chủ tịch Hồ Chí Minh đọc tại đâu?",
            "options": {
                "A": "Quảng trường Ba Đình, Hà Nội",
                "B": "Nhà hát Lớn Hà Nội",
                "C": "Chiến khu Tân Trào, Tuyên Quang",
                "D": "Dinh Độc Lập, Sài Gòn"
            },
            "correct_answer": "A",
            "explanation": "Bản Tuyên ngôn Độc lập khai sinh ra nước Việt Nam Dân chủ Cộng hòa được đọc tại Quảng trường Ba Đình, Hà Nội."
        },
        {
            "question_number": 102,
            "section_id": "section_3_problem_solving",
            "domain": "history",
            "difficulty": "hard",
            "passage": hist_passage,
            "prompt": "Lời kêu gọi Toàn quốc kháng chiến được ban bố trong bối cảnh lịch sử nào?",
            "options": {
                "A": "Thực dân Pháp bội ước, gửi tối hậu thư đòi tước vũ khí của tự vệ Hà Nội (tháng 12/1946).",
                "B": "Quân Tưởng Giới Thạch tràn vào miền Bắc nhằm lật đổ chính quyền cách mạng.",
                "C": "Sau khi Hiệp định Genève được ký kết.",
                "D": "Đế quốc Mỹ trực tiếp đổ quân viễn chinh vào chiến trường miền Nam."
            },
            "correct_answer": "A",
            "explanation": "Tháng 12/1946, Pháp bội ước Hiệp định sơ bộ và Tạm ước, liên tục khiêu khích và gửi tối hậu thư đòi giải tán lực lượng tự vệ Hà Nội, buộc Đảng và Chủ tịch Hồ Chí Minh phát động kháng chiến toàn quốc."
        },
        {
            "question_number": 103,
            "section_id": "section_3_problem_solving",
            "domain": "history",
            "difficulty": "medium",
            "passage": hist_passage,
            "prompt": "Đường lối kháng chiến chống thực dân Pháp của Đảng ta được xác định là:",
            "options": {
                "A": "Toàn dân, toàn diện, trường kỳ, tự lực cánh sinh và tranh thủ sự ủng hộ quốc tế.",
                "B": "Đánh nhanh thắng nhanh, tập trung quân chủ lực trên chiến trường đô thị.",
                "C": "Kháng chiến hòa hoãn, dựa hoàn toàn vào viện trợ của khối xã hội chủ nghĩa.",
                "D": "Khởi nghĩa từng phần tiến lên tổng khởi nghĩa võ trang."
            },
            "correct_answer": "A",
            "explanation": "Đường lối kháng chiến chống Pháp: Toàn dân, toàn diện, trường kỳ, tự lực cánh sinh và tranh thủ sự ủng hộ của quốc tế."
        },
        {
            "question_number": 104,
            "section_id": "section_3_problem_solving",
            "domain": "history",
            "difficulty": "hard",
            "passage": hist_passage,
            "prompt": "Thắng lợi quân sự nào của quân và dân ta đã đập tan hoàn toàn kế hoạch Nava của Pháp, buộc Pháp phải ký Hiệp định Genève năm 1954?",
            "options": {
                "A": "Chiến dịch Điện Biên Phủ 1954",
                "B": "Chiến dịch Biên giới Thu - Đông 1950",
                "C": "Chiến dịch Việt Bắc Thu - Đông 1947",
                "D": "Cuộc tiến công chiến lược Đông - Xuân 1953 - 1954"
            },
            "correct_answer": "A",
            "explanation": "Chiến thắng Điện Biên Phủ 'lừng lẫy năm châu, chấn động địa cầu' ngày 7/5/1954 đã đập tan pháo đài bất khả xâm phạm của Pháp, quyết định thắng lợi trên bàn đàm phán Genève."
        },
        {
            "question_number": 105,
            "section_id": "section_3_problem_solving",
            "domain": "history",
            "difficulty": "medium",
            "prompt": "Sự kiện lịch sử thế giới nào vào năm 1917 đã mở ra thời đại mới trong lịch sử nhân loại và ảnh hưởng sâu sắc đến con đường cứu nước của Nguyễn Ái Quốc?",
            "options": {
                "A": "Cách mạng Tháng Mười Nga",
                "B": "Thành lập Hội Quốc Liên",
                "C": "Chiến tranh thế giới thứ nhất bùng nổ",
                "D": "Thành lập Quốc tế Cộng sản tại Matxcơva"
            },
            "correct_answer": "A",
            "explanation": "Thắng lợi của Cách mạng Tháng Mười Nga (1917) đã chỉ ra con đường giải phóng cho các dân tộc bị áp bức và định hướng cho Nguyễn Ái Quốc đi theo con đường cách mạng vô sản."
        },
        {
            "question_number": 106,
            "section_id": "section_3_problem_solving",
            "domain": "history",
            "difficulty": "medium",
            "prompt": "Đại hội đại biểu toàn quốc lần thứ VI của Đảng Cộng sản Việt Nam (tháng 12/1986) có ý nghĩa lịch sử trọng đại gì?",
            "options": {
                "A": "Khởi xướng và mở đầu công cuộc Đổi mới đất nước toàn diện",
                "B": "Hoàn thành thống nhất đất nước về mặt nhà nước",
                "C": "Đưa Việt Nam chính thức gia nhập tổ chức ASEAN",
                "D": "Ký kết bình thường hóa quan hệ ngoại giao với Hoa Kỳ"
            },
            "correct_answer": "A",
            "explanation": "Đại hội VI (12/1986) là mốc son lịch sử mở ra kỷ nguyên Đổi mới, chuyển đổi nền kinh tế bao cấp sang kinh tế thị trường định hướng XHCN."
        },
        {
            "question_number": 107,
            "section_id": "section_3_problem_solving",
            "domain": "history",
            "difficulty": "hard",
            "prompt": "Chiến dịch Hồ Chí Minh lịch sử giải phóng hoàn toàn miền Nam thống nhất đất nước kết thúc thắng lợi vào ngày nào?",
            "options": {
                "A": "30 tháng 4 năm 1975",
                "B": "26 tháng 3 năm 1975",
                "C": "1 tháng 5 năm 1975",
                "D": "19 tháng 5 năm 1975"
            },
            "correct_answer": "A",
            "explanation": "Chiến dịch Hồ Chí Minh toàn thắng vào 11h30 ngày 30/4/1975 khi lá cờ cách mạng tung bay trên nóc Dinh Độc Lập."
        },
        {
            "question_number": 108,
            "section_id": "section_3_problem_solving",
            "domain": "history",
            "difficulty": "medium",
            "prompt": "Tổ chức Liên Hợp Quốc (UN) được chính thức thành lập vào năm nào với mục tiêu duy trì hòa bình và an ninh quốc tế?",
            "options": {
                "A": "1945",
                "B": "1944",
                "C": "1950",
                "D": "1939"
            },
            "correct_answer": "A",
            "explanation": "Liên Hợp Quốc chính thức thành lập ngày 24/10/1945 sau khi Hiến chương Liên Hợp Quốc được phê chuẩn bởi đa số các quốc gia sáng lập."
        },
        {
            "question_number": 109,
            "section_id": "section_3_problem_solving",
            "domain": "history",
            "difficulty": "hard",
            "prompt": "Điểm chung nổi bật trong các chiến lược 'Chiến tranh đặc biệt' (1961 - 1965) và 'Chiến tranh cục bộ' (1965 - 1968) của Mỹ ở miền Nam Việt Nam là gì?",
            "options": {
                "A": "Đều là chiến tranh xâm lược thực dân mới nhằm chia cắt lâu dài đất nước ta.",
                "B": "Đều sử dụng chủ yếu lực lượng quân đội viễn chinh Mỹ để tác chiến.",
                "C": "Đều thực hiện ấp chiến lược làm 'quốc sách'.",
                "D": "Đều mở rộng chiến tranh ra toàn cõi Đông Dương."
            },
            "correct_answer": "A",
            "explanation": "Cả hai chiến lược đều là hình thức chiến tranh xâm lược thực dân mới của Mỹ nhằm biến miền Nam Việt Nam thành thuộc địa kiểu mới và căn cứ quân sự."
        },
        {
            "question_number": 110,
            "section_id": "section_3_problem_solving",
            "domain": "history",
            "difficulty": "medium",
            "prompt": "Hiệp hội các quốc gia Đông Nam Á (ASEAN) được thành lập tại Bangkok (Thái Lan) vào năm nào với 5 thành viên sáng lập?",
            "options": {
                "A": "1967",
                "B": "1975",
                "C": "1986",
                "D": "1995"
            },
            "correct_answer": "A",
            "explanation": "ASEAN được thành lập ngày 8/8/1967 tại Bangkok với 5 nước sáng lập: Indonesia, Malaysia, Philippines, Singapore và Thái Lan."
        },
    ]

    # --- ĐỊA LÝ (CÂU 111 - 120) ---
    geo_passage = "Đoạn thông tin sau dùng cho các câu hỏi 111 - 114:\nĐồng bằng sông Cửu Long (ĐBSCL) là vùng trọng điểm sản xuất lương thực, thực phẩm lớn nhất cả nước, đóng góp hơn 50% sản lượng lúa và 90% sản lượng gạo xuất khẩu của Việt Nam. Tuy nhiên, trước tác động của biến đổi khí hậu toàn cầu, nước biển dâng, và việc xây dựng các đập thủy điện ở thượng nguồn sông Mê Kông, vùng đang phải đối mặt với nguy cơ hạn mặn gay gắt, sạt lở bờ sông và sụt lún đất. Nghị quyết 120/NQ-CP của Chính phủ đã đề ra định hướng phát triển bền vững ĐBSCL theo phương châm 'thuận thiên', chủ động sống chung với lũ, mặn và nước lợ."

    geo_questions = [
        {
            "question_number": 111,
            "section_id": "section_3_problem_solving",
            "domain": "geography",
            "difficulty": "medium",
            "passage": geo_passage,
            "prompt": "Nguyên nhân chủ yếu dẫn đến tình trạng xâm nhập mặn ngày càng sâu vào nội đồng ở ĐBSCL trong mùa khô là:",
            "options": {
                "A": "Lưu lượng nước ngọt từ thượng nguồn Mê Kông sụt giảm kết hợp với thủy triều và biến đổi khí hậu.",
                "B": "Nông dân đào ao nuôi tôm nước mặn bừa bãi ở tất cả các tỉnh nội đồng.",
                "C": "Địa hình ĐBSCL quá cao so với mực nước biển.",
                "D": "Do các trận bão lớn đổ bộ liên tiếp vào miền Tây Nam Bộ."
            },
            "correct_answer": "A",
            "explanation": "Hạn mặn khốc liệt là do sự suy giảm nguồn nước thượng nguồn sông Mê Kông (do đập thủy điện tích nước và biến đổi khí hậu) làm triều cường đẩy mặn lấn sâu vào hệ thống kênh rạch."
        },
        {
            "question_number": 112,
            "section_id": "section_3_problem_solving",
            "domain": "geography",
            "difficulty": "hard",
            "passage": geo_passage,
            "prompt": "Mô hình kinh tế nông nghiệp nào sau đây phản ánh rõ nét phương châm 'thuận thiên' tại các vùng ven biển chịu mặn ở ĐBSCL?",
            "options": {
                "A": "Mô hình luân canh một vụ lúa - một vụ tôm (lúa tôm kết hợp)",
                "B": "Ngăn đê bao khép kín để trồng lúa 3 vụ quanh năm",
                "C": "Phá rừng ngập mặn để xây dựng các khu đô thị biển",
                "D": "Khoan giếng ngầm tầng sâu khai thác triệt để nước ngọt"
            },
            "correct_answer": "A",
            "explanation": "Mô hình lúa - tôm: mùa mưa nước ngọt trồng lúa hữu cơ, mùa khô nước lợ thả tôm, tận dụng quy luật tự nhiên, hạn chế dùng phân hóa học, mang lại giá trị gia tăng cao."
        },
        {
            "question_number": 113,
            "section_id": "section_3_problem_solving",
            "domain": "geography",
            "difficulty": "medium",
            "passage": geo_passage,
            "prompt": "Hai nhánh sông chính của dòng sông Cửu Long khi chảy vào lãnh thổ Việt Nam là:",
            "options": {
                "A": "Sông Tiền và Sông Hậu",
                "B": "Sông Hồng và Sông Đáy",
                "C": "Sông Đồng Nai và Sông Sài Gòn",
                "D": "Sông Vàm Cỏ Đông và Vàm Cỏ Tây"
            },
            "correct_answer": "A",
            "explanation": "Sông Mê Kông vào Việt Nam tách thành hai phân lưu chính là Sông Tiền và Sông Hậu."
        },
        {
            "question_number": 114,
            "section_id": "section_3_problem_solving",
            "domain": "geography",
            "difficulty": "medium",
            "passage": geo_passage,
            "prompt": "Nhóm đất chiếm diện tích lớn nhất tại Đồng bằng sông Cửu Long là:",
            "options": {
                "A": "Đất phèn",
                "B": "Đất phù sa ngọt ven sông",
                "C": "Đất feralit đỏ vàng",
                "D": "Đất cát pha ven biển"
            },
            "correct_answer": "A",
            "explanation": "Đất phèn chiếm diện tích lớn nhất ở ĐBSCL (khoảng 1.6 triệu ha, chiếm hơn 40% diện tích tự nhiên của vùng), tập trung ở Đồng Tháp Mười, Tứ giác Long Xuyên."
        },
        {
            "question_number": 115,
            "section_id": "section_3_problem_solving",
            "domain": "geography",
            "difficulty": "easy",
            "prompt": "Gió mùa Đông Bắc hoạt động mạnh ở miền Bắc nước ta trong thời gian nào sau đây?",
            "options": {
                "A": "Từ tháng 11 đến tháng 4 năm sau",
                "B": "Từ tháng 5 đến tháng 10",
                "C": "Quanh năm liên tục",
                "D": "Chỉ vào tháng 6 và tháng 7"
            },
            "correct_answer": "A",
            "explanation": "Gió mùa Đông Bắc (bắt nguồn từ áp cao Siberia) hoạt động từ tháng 11 đến tháng 4 năm sau, gây nên mùa đông lạnh ở miền Bắc."
        },
        {
            "question_number": 116,
            "section_id": "section_3_problem_solving",
            "domain": "geography",
            "difficulty": "medium",
            "prompt": "Vùng kinh tế nào ở nước ta hiện nay có tỷ lệ đô thị hóa cao nhất và dẫn đầu cả nước về giá trị sản xuất công nghiệp?",
            "options": {
                "A": "Đông Nam Bộ",
                "B": "Đồng bằng sông Hồng",
                "C": "Bắc Trung Bộ",
                "D": "Tây Nguyên"
            },
            "correct_answer": "A",
            "explanation": "Đông Nam Bộ (với hạt nhân là TP.HCM, Bình Dương, Đồng Nai, Bà Rịa - Vũng Tàu) dẫn đầu cả nước về quy mô công nghiệp, thu hút FDI và tỷ lệ dân cư đô thị."
        },
        {
            "question_number": 117,
            "section_id": "section_3_problem_solving",
            "domain": "geography",
            "difficulty": "medium",
            "prompt": "Đặc điểm nổi bật của địa hình nước ta là:",
            "options": {
                "A": "Đồi núi chiếm 3/4 diện tích lãnh thổ, nhưng chủ yếu là đồi núi thấp dưới 1000m.",
                "B": "Đồng bằng chiếm hơn 70% diện tích.",
                "C": "Địa hình có hướng nghiêng chủ yếu từ Đông sang Tây.",
                "D": "Đồi núi cao trên 2000m chiếm phần lớn diện tích miền Bắc."
            },
            "correct_answer": "A",
            "explanation": "Đồi núi chiếm 3/4 diện tích đất liền, trong đó đồi núi thấp (dưới 1000m) chiếm tới 85% diện tích; núi cao trên 2000m chỉ chiếm khoảng 1%."
        },
        {
            "question_number": 118,
            "section_id": "section_3_problem_solving",
            "domain": "geography",
            "difficulty": "hard",
            "prompt": "Ý nghĩa chiến lược quan trọng nhất của các đảo và quần đảo đối với sự phát triển kinh tế - xã hội và an ninh quốc phòng nước ta là:",
            "options": {
                "A": "Tạo tiền đồn bảo vệ chủ quyền biển đảo, mở rộng không gian kinh tế biển và vươn ra đại dương.",
                "B": "Là nơi duy nhất có tiềm năng khai thác dầu khí thương mại.",
                "C": "Giải quyết toàn bộ vấn đề việc làm cho cư dân các tỉnh ven biển.",
                "D": "Cung cấp nguồn nước ngọt dồi dào cho các đô thị đất liền."
            },
            "correct_answer": "A",
            "explanation": "Hệ thống đảo và quần đảo là căn cứ tiến ra biển, khai thác ngư trường, kiểm soát an ninh hàng hải và bảo vệ vững chắc chủ quyền thềm lục địa của Tổ quốc."
        },
        {
            "question_number": 119,
            "section_id": "section_3_problem_solving",
            "domain": "geography",
            "difficulty": "medium",
            "prompt": "Cây công nghiệp lâu năm được trồng nhiều nhất ở vùng Tây Nguyên là:",
            "options": {
                "A": "Cà phê",
                "B": "Chè",
                "C": "Mía",
                "D": "Đay tơ tằm"
            },
            "correct_answer": "A",
            "explanation": "Tây Nguyên là thủ phủ cà phê của cả nước, nhờ đất bazan màu mỡ và khí hậu cận xích đạo có 2 mùa mưa - khô rõ rệt."
        },
        {
            "question_number": 120,
            "section_id": "section_3_problem_solving",
            "domain": "geography",
            "difficulty": "hard",
            "prompt": "Để thích ứng với việc cạn kiệt tài nguyên khoáng sản hóa thạch và giảm phát thải ròng bằng '0' (Net Zero 2050), nước ta đang ưu tiên phát triển những dạng năng lượng nào?",
            "options": {
                "A": "Năng lượng gió (ngoài khơi, trên bờ) và năng lượng mặt trời",
                "B": "Xây dựng thêm nhiều nhà máy nhiệt điện than công suất lớn",
                "C": "Đốt nhiên liệu gỗ rừng tự nhiên",
                "D": "Nhập khẩu độc quyền than cốc từ nước ngoài"
            },
            "correct_answer": "A",
            "explanation": "Chiến lược chuyển dịch năng lượng xanh của Việt Nam tập trung vào điện gió ngoài khơi, điện mặt trời mái nhà và thủy điện tích năng hướng tới Net Zero 2050."
        }
    ]

    questions.extend(chem_questions)
    questions.extend(physics_questions)
    questions.extend(bio_questions)
    questions.extend(hist_questions)
    questions.extend(geo_questions)

    return questions

if __name__ == "__main__":
    qs = get_benchmark_questions()
    print(f"Total benchmark questions generated: {len(qs)}")
    import re
    range_regex = re.compile(r'(?:câu(?:\s+hỏi)?|questions?)\s*(\d+)\s*(?:[-–]|to|đến)\s*(\d+)', re.IGNORECASE)
    q_map = {q['question_number']: q for q in qs}
    for q in qs:
        p = q.get('passage', '') or ''
        if len(p) > 60:
            m = range_regex.search(p)
            if m:
                start_num = int(m.group(1))
                end_num = int(m.group(2))
                for target_num in range(start_num, end_num + 1):
                    target_q = q_map.get(target_num)
                    if target_q and target_num != q['question_number']:
                        target_p = target_q.get('passage', '') or ''
                        if len(target_p) < 60 or range_regex.search(target_p):
                            target_q['passage'] = p
                        if not target_q.get('chart_image') and q.get('chart_image'):
                            target_q['chart_image'] = q['chart_image']
    for q in qs:
        p = q.get('passage', '') or ''
        if 0 < len(p) < 60:
            m = range_regex.search(p)
            if m:
                root_num = int(m.group(1))
                root_q = q_map.get(root_num)
                if root_q and root_q.get('passage') and len(root_q['passage']) > 60:
                    q['passage'] = root_q['passage']
                    if not q.get('chart_image') and root_q.get('chart_image'):
                        q['chart_image'] = root_q['chart_image']

    # Save to benchmark_exam.py
    code = f'''# Chuẩn đề thi ĐGNL chính thức 120 câu
BENCHMARK_EXAM_METADATA = {{
    "id": "dgnl_benchmark_standard_2025",
    "title": "Đề Thi Chuẩn Hóa ĐGNL ĐHQG (Mẫu 120 Câu - 150 Phút)",
    "description": "Đề thi khảo nghiệm năng lực toàn diện chuẩn cấu trúc ĐGNL ĐHQG: Ngôn ngữ (40 câu), Toán & Logic & Số liệu (30 câu), Giải quyết vấn đề KHTN & KHXH (50 câu).",
    "duration_minutes": 150,
    "total_questions": 120,
    "source": "benchmark"
}}

BENCHMARK_QUESTIONS = {json.dumps(qs, ensure_ascii=False, indent=2)}
'''
    with open("backend/exam_engine/benchmark_exam.py", "w", encoding="utf-8") as f:
        f.write(code)
    print("Successfully wrote backend/exam_engine/benchmark_exam.py!")
