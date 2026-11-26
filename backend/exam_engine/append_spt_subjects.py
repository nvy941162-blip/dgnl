# Script to append the 3 remaining SPT subjects to spt_sample_subjects.py
import os

code_to_append = '''

# --------------------------------------------------------------------------
# 6. SPT MÔN GIÁO DỤC KINH TẾ VÀ PHÁP LUẬT (60 PHÚT - THANG 10)
# --------------------------------------------------------------------------
SPT_CIVICS_LAW_EXAM = {
    "id": "spt_sample_civics_law",
    "title": "Đề Tham Khảo SPT ĐH Sư Phạm Hà Nội - Môn GDKT&PL",
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
            "passage": "Bộ Lao động - Thương binh và Xã hội ước tính năm 2023, khoảng 155.000 lao động Việt Nam đi làm việc ở nước ngoài, tăng 8,55% so với năm 2022, mức cao nhất từ trước đến nay. Mỗi năm, bình quân từ 120.000 đến 143.000 lao động ra nước ngoài làm việc; lượng kiều hối từ lực lượng lao động này gửi về đạt 3,5 - 4 tỉ USD, góp phần thúc đẩy phát triển kinh tế - xã hội của đất nước.\\n(Theo Báo Điện tử Chính phủ số ra ngày 30/12/2023)",
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
            "passage": "Bộ Lao động - Thương binh và Xã hội ước tính năm 2023, khoảng 155.000 lao động Việt Nam đi làm việc ở nước ngoài, tăng 8,55% so với năm 2022, mức cao nhất từ trước đến nay. Mỗi năm, bình quân từ 120.000 đến 143.000 lao động ra nước ngoài làm việc; lượng kiều hối từ lực lượng lao động này gửi về đạt 3,5 - 4 tỉ USD, góp phần thúc đẩy phát triển kinh tế - xã hội của đất nước.\\n(Theo Báo Điện tử Chính phủ số ra ngày 30/12/2023)",
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
    "title": "Đề Tham Khảo SPT ĐH Sư Phạm Hà Nội - Môn Công Nghệ Công Nghiệp",
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
            "prompt": "Mạng điện gia đình 220V gồm 2 nhánh: Nhánh 1 (phòng khách & bếp): 6 đèn LED (40W), 1 quạt trần (120W), 1 ti vi (100W), 1 bếp điện (1500W), 1 tủ lạnh (180W). Nhánh 2 (phòng ngủ): 2 đèn LED (25W), 1 quạt treo tường (100W). Biết đèn LED, ti vi, bếp điện có cosφ=1; các thiết bị còn lại có cosφ=0,8.\\na) Tính tổng công suất định mức mỗi nhánh.\\nb) Tính dòng điện mỗi nhánh khi các thiết bị cùng làm việc.\\nc) Tính tiết diện dây dẫn của mỗi nhánh nếu sử dụng dây dẫn với mật độ dòng điện cho phép J = 5 A/mm².",
            "correct_answer": "a) P_pkb = 2140W, P_pn = 150W.\\nb) I_pkb ≈ 10,06 A; I_pn ≈ 0,8 A.\\nc) S_pkb = 10,06 / 5 ≈ 2,012 mm²; S_pn = 0,8 / 5 = 0,16 mm².",
            "explanation": "Thang điểm 1,5đ: a) 0,5đ (mỗi nhánh 0,25đ); b) 0,5đ (mỗi nhánh 0,25đ); c) 0,5đ (mỗi nhánh 0,25đ)."
        },
        {
            "question_number": 24,
            "section_id": "part_4",
            "question_type": "essay",
            "domain": "tech_industry",
            "difficulty": "hard",
            "points": 1.5,
            "prompt": "Cho mạch khuếch đại thuật toán đảo với điện trở vào R1 và điện trở hồi tiếp R2:\\na) Xác định công thức tính hệ số khuếch đại KU của mạch.\\nb) Cho UV = 1V; R1 = 1 kΩ; R2 = 10 kΩ. Xác định giá trị của UR.\\nc) Xác định hệ số khuếch đại của mạch khi R1 = R2. Nêu nhận xét về quan hệ giữa tín hiệu vào và tín hiệu ra trong trường hợp này.",
            "correct_answer": "a) KU = -R2 / R1.\\nb) UR = -(R2/R1) * UV = -(10/1) * 1V = -10V.\\nc) Khi R1 = R2 thì KU = -1. Tín hiệu ra có cùng biên độ nhưng ngược pha so với tín hiệu vào.",
            "explanation": "Thang điểm 1,5đ: ý a) 0,25đ; ý b) 0,25đ; ý c) 1,0đ (tính Ku 0,5đ, giải thích đồ thị đảo pha 0,5đ)."
        }
    ]
}


# --------------------------------------------------------------------------
# 8. SPT MÔN CÔNG NGHỆ (ĐỊNH HƯỚNG NÔNG NGHIỆP) (60 PHÚT - THANG 10)
# --------------------------------------------------------------------------
SPT_TECH_AGRICULTURE_EXAM = {
    "id": "spt_sample_tech_agriculture",
    "title": "Đề Tham Khảo SPT ĐH Sư Phạm Hà Nội - Môn Công Nghệ Nông Nghiệp",
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
            "prompt": "Một nhóm học sinh được giao nhiệm vụ trồng cây cà chua bằng kĩ thuật thủy canh. Hãy sắp xếp các bước tiến hành dưới đây sao cho đúng thứ tự:\\n(1). Chuẩn bị thùng đựng dịch dinh dưỡng; rọ trồng cây; giá thể trồng cây.\\n(2). Điều chỉnh pH của dịch dinh dưỡng đã pha (pH = 5,5 - 6,5).\\n(3). Pha dung dịch dinh dưỡng theo tỉ lệ hướng dẫn.\\n(4). Trồng cây vào rọ giá thể, đảm bảo bộ rễ ngập trong dịch dinh dưỡng.\\n(5). Chọn cây giống khỏe mạnh, không bị dập nát.\\n(6). Theo dõi sự sinh trưởng của cây cà chua thủy canh.",
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
            "prompt": "Những biện pháp nào sau đây giúp bảo vệ môi trường trong trồng trọt?\\n1. Tăng cường sử dụng phân bón hóa học trong trồng trọt vì hiệu quả nhanh chóng.\\n2. Tăng cường sử dụng phân bón hữu cơ, phân bón vi sinh trong trồng trọt.\\n3. Súc rửa chai lọ thuốc bảo vệ thực vật ở mương, ao, hồ,...\\n4. Sử dụng thuốc trừ sâu sinh học thay thế thuốc trừ sâu hóa học.\\n5. Sử dụng hợp lí phân bón và thuốc bảo vệ thực vật.\\n6. Đốt rơm, rạ trên đồng ruộng sau mỗi vụ thu hoạch.",
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
            "prompt": "Quế (Cinnamomum verum) là loài cây gỗ, thường được trồng thành rừng thuần loài. Gỗ màu nâu nhạt, mịn, thường dùng để xẻ ván, đóng đồ. Vỏ thân, lá chứa nhiều tinh dầu được chiết xuất dùng trong công nghệ dược liệu và thực phẩm. Tổ hợp nào sau đây đúng về vai trò của cây quế đối với tự nhiên và con người?\\n1. Quế là loài dược liệu thuộc nhóm lâm sản ngoài gỗ.\\n2. Quế là loài cây trồng đa mục tiêu.\\n3. Cung cấp nguồn thức ăn cho gia súc chăn thả dưới tán rừng.\\n4. Trồng quế có khả năng bảo vệ đất, hạn chế xói mòn.\\n5. Khả năng bảo vệ đất của rừng quế cao hơn so với rừng tự nhiên do chiều cao cây lớn, đồng đều.",
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
            "prompt": "Tiến hành thí nghiệm nghiên cứu ảnh hưởng của mật độ nuôi đến sinh trưởng và tỉ lệ sống của cá Nâu. Kết quả thu được:\\n- Nghiệm thức 15 con/m³: Khối lượng lúc thả 30,047g; lúc thu 58,310g; tỉ lệ sống 97,78%.\\n- Nghiệm thức 30 con/m³: Khối lượng lúc thả 30,223g; lúc thu 50,513g; tỉ lệ sống 98,89%.\\n- Nghiệm thức 60 con/m³: Khối lượng lúc thả 30,133g; lúc thu 46,223g; tỉ lệ sống 96,11%.\\nXét tính Đúng / Sai:",
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
            "prompt": "Quy trình kĩ thuật trồng rừng bằng cây con được ươm trong bầu bao gồm một số bước chủ yếu sau:\\n(1) Rạch, xé bỏ vỏ bầu.\\n(2) Tạo hố trồng cây.\\n(3) Vun gốc.\\n(4) Lấp đất đảm bảo kín vỏ bầu.\\nHãy sắp xếp số hiệu các bước theo trật tự đúng của quy trình.",
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
            "prompt": "Một hộ nuôi thủy sản muốn nuôi cá rô phi trong ao đất ở vùng đồng bằng nhưng nguồn nước đầu vào thường xuyên bị ô nhiễm bởi nước thải sinh hoạt và phân bón từ ruộng lúa xung quanh. Em hãy:\\na. Phân tích các ảnh hưởng tiêu cực của nguồn nước ô nhiễm này đến quá trình nuôi cá rô phi.\\nb. Đề xuất ít nhất 2 biện pháp khả thi để đảm bảo hiệu quả nuôi cá trong điều kiện đó, giải thích vì sao chọn các biện pháp đó.",
            "correct_answer": "a) Nước thải chứa hữu cơ và nitơ/phốt pho gây phú dưỡng hóa, giảm oxy hòa tan, tăng độc tố khí NH3/H2S làm cá chậm lớn, nhiễm bệnh.\\nb) Đề xuất: Xây ao lắng lọc kết hợp nuôi thủy sinh (bèo lục bình, cỏ vetiver) xử lý sinh học trước khi cấp vào ao nuôi; Dùng chế phẩm sinh học vi sinh định kỳ.",
            "explanation": "Thang điểm 1,5đ: Phân tích ảnh hưởng tiêu cực (0,75đ); Đề xuất và giải thích 2 giải pháp khả thi (0,75đ)."
        }
    ]
}
'''

target_file = r'e:\tin hoc\Dang gia nang luc\backend\exam_engine\spt_sample_subjects.py'
with open(target_file, 'a', encoding='utf-8') as f:
    f.write(code_to_append)

print('Successfully appended 3 subjects to spt_sample_subjects.py!')
