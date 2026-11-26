import re
from typing import List, Dict, Any, Optional
from backend.config import SCORE_DISTRIBUTION, MAX_TOTAL_SCORE

# Trọng số tương đối theo mức độ tư duy chuẩn khảo thí ĐGNL
DIFFICULTY_WEIGHTS = {
    "easy": 0.8,        # Nhận biết
    "medium": 1.0,      # Thông hiểu
    "hard": 1.25,       # Vận dụng
    "very_hard": 1.5    # Vận dụng cao
}

def propagate_passages(questions: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """
    Tự động chuẩn hóa và kế thừa đoạn văn bản đọc hiểu / ngữ liệu
    cho TẤT CẢ các câu hỏi trong cùng một chùm bài đọc hoặc cụm câu hỏi.
    """
    if not questions:
        return questions
        
    q_map = {q.get("question_number"): q for q in questions if q.get("question_number") is not None}
    range_regex = re.compile(r'(?:câu(?:\s+hỏi)?|questions?)\s*(\d+)\s*(?:[-–]|to|đến)\s*(\d+)', re.IGNORECASE)

    # Đợt 1: Quét câu gốc có passage đầy đủ (> 50 ký tự) và chứa khoảng câu hỏi
    for q in questions:
        p = q.get("passage", "") or ""
        if len(p.strip()) > 50:
            m = range_regex.search(p)
            if m:
                start_num = int(m.group(1))
                end_num = int(m.group(2))
                for target_num in range(start_num, end_num + 1):
                    target_q = q_map.get(target_num)
                    if target_q and target_num != q.get("question_number"):
                        target_p = (target_q.get("passage", "") or "").strip()
                        if len(target_p) < 50 or range_regex.search(target_p):
                            target_q["passage"] = p
                        if not target_q.get("chart_image") and q.get("chart_image"):
                            target_q["chart_image"] = q["chart_image"]

    # Đợt 2: Quét các câu có placeholder chỉ rõ khoảng câu (VD: "Đoạn trích câu 11 - 15")
    for q in questions:
        p = (q.get("passage", "") or "").strip()
        if 0 < len(p) < 50:
            m = range_regex.search(p)
            if m:
                root_num = int(m.group(1))
                root_q = q_map.get(root_num)
                if root_q and root_q.get("passage") and len(root_q["passage"].strip()) > 50:
                    q["passage"] = root_q["passage"]
                    if not q.get("chart_image") and root_q.get("chart_image"):
                        q["chart_image"] = root_q["chart_image"]

    return questions


def calculate_question_weights(questions: List[Dict[str, Any]], max_total_score: float = 1200.0) -> Dict[int, float]:
    """
    Tính toán trọng số điểm số cụ thể cho từng câu hỏi
    - Nếu max_total_score == 10.0 (Kỳ thi SPT): điểm mỗi câu được gán theo points trong câu hoặc chia đều
    - Nếu max_total_score == 1200.0 (V-ACT): Phân bổ theo 3 phân khu IRT
    """
    if max_total_score <= 20.0: # Dành cho SPT hoặc thang 10
        weights = {}
        total_q = len(questions)
        for q in questions:
            q_num = q.get("question_number", 1)
            # Nếu câu đã có trường points chỉ định sẵn
            if "points" in q and q["points"] is not None:
                weights[q_num] = float(q["points"])
            else:
                q_type = q.get("question_type", "multiple_choice")
                if q_type == "true_false":
                    weights[q_num] = 1.0
                elif q_type == "short_answer":
                    weights[q_num] = 0.25
                elif q_type == "essay":
                    weights[q_num] = 1.0
                else:
                    weights[q_num] = 0.25
        return weights

    # Phân bổ V-ACT 1200 điểm
    sections = {
        "section_1_language": [],
        "section_2_logic_data": [],
        "section_3_problem_solving": []
    }

    for q in questions:
        sec_id = q.get("section_id", "section_1_language")
        if sec_id in sections:
            sections[sec_id].append(q)
        else:
            q_num = q.get("question_number", 1)
            if q_num <= 40 or q_num <= 60:
                sections["section_1_language"].append(q)
            elif q_num <= 70 or q_num <= 90:
                sections["section_2_logic_data"].append(q)
            else:
                sections["section_3_problem_solving"].append(q)

    question_point_map = {}

    for sec_key, sec_questions in sections.items():
        if not sec_questions:
            continue
        max_sec_score = SCORE_DISTRIBUTION.get(sec_key, 400.0)
        
        total_raw_weight = 0.0
        raw_weights = {}
        for q in sec_questions:
            q_num = q["question_number"]
            diff = q.get("difficulty", "medium")
            w = DIFFICULTY_WEIGHTS.get(diff, 1.0)
            raw_weights[q_num] = w
            total_raw_weight += w

        scale_factor = max_sec_score / total_raw_weight if total_raw_weight > 0 else 1.0
        for q_num, w in raw_weights.items():
            question_point_map[q_num] = round(w * scale_factor, 2)

    for sec_key, sec_questions in sections.items():
        if not sec_questions:
            continue
        expected_score = SCORE_DISTRIBUTION.get(sec_key, 400.0)
        actual_sum = sum(question_point_map[q["question_number"]] for q in sec_questions)
        diff = round(expected_score - actual_sum, 2)
        if abs(diff) > 0 and sec_questions:
            last_q_num = sec_questions[-1]["question_number"]
            question_point_map[last_q_num] = round(question_point_map[last_q_num] + diff, 2)

    return question_point_map


def _normalize_str(val: Any) -> str:
    if val is None:
        return ""
    s = str(val).strip().lower()
    # Thay thế dấu phẩy thập phân thành dấu chấm để so khớp số
    s = re.sub(r'(\d+),(\d+)', r'\1.\2', s)
    return s


def grade_submission(
    questions: List[Dict[str, Any]], 
    user_answers: Dict[str, Any],
    exam_type: str = "vact",
    max_score: float = 1200.0
) -> Dict[str, Any]:
    """
    Chấm bài thi theo phương pháp khảo thí chuẩn hóa:
    - Hỗ trợ cả V-ACT (thang 1200) và SPT (thang 10 điểm)
    - Hỗ trợ trắc nghiệm A/B/C/D, trắc nghiệm Đúng/Sai bậc thang, và câu điền đáp số
    """
    is_spt = (exam_type == "spt" or max_score <= 20.0)
    actual_max_score = 10.0 if is_spt else 1200.0

    weights = calculate_question_weights(questions, actual_max_score)
    
    total_score = 0.0
    sec1_score = 0.0
    sec2_score = 0.0
    sec3_score = 0.0
    
    correct_count = 0
    partial_count = 0
    wrong_count = 0
    unanswered_count = 0
    
    detailed_results = []
    domain_stats = {}

    for q in questions:
        q_num = q["question_number"]
        domain = q.get("domain", "general")
        sec_id = q.get("section_id", "section_1")
        q_type = q.get("question_type", "multiple_choice")
        q_point = weights.get(q_num, 0.25 if is_spt else 10.0)
        
        user_ans = user_answers.get(str(q_num))
        if user_ans is None:
            user_ans = user_answers.get(q_num)

        earned_point = 0.0
        is_correct = False
        is_partial = False
        status = "unanswered"

        # -------------------------------------------------------------
        # DẠNG 1: TRẮC NGHIỆM ĐÚNG / SAI 4 Ý (TRUE / FALSE MATRIX)
        # -------------------------------------------------------------
        if q_type == "true_false" or isinstance(q.get("correct_answer"), dict):
            q_type = "true_false"
            correct_map = q.get("correct_answer", {})
            # correct_map e.g. {"a": "Đ", "b": "S", "c": "S", "d": "Đ"} or True/False
            user_map = user_ans if isinstance(user_ans, dict) else {}
            
            sub_matches = 0
            sub_total = len(correct_map) if correct_map else 4

            if not user_map:
                status = "unanswered"
                unanswered_count += 1
            else:
                for sub_key in ["a", "b", "c", "d"]:
                    c_val = str(correct_map.get(sub_key, "")).strip().upper()
                    u_val = str(user_map.get(sub_key, "")).strip().upper()
                    # Chuẩn hóa Đúng/Sai hoặc D/S hoặc True/False
                    c_is_true = c_val in ["Đ", "D", "TRUE", "T", "1"]
                    u_is_true = u_val in ["Đ", "D", "TRUE", "T", "1"]
                    if u_val and (c_is_true == u_is_true):
                        sub_matches += 1

                # Biểu điểm bậc thang chuẩn của ĐH Sư phạm Hà Nội:
                # 1 ý đúng = 0,1đ | 2 ý đúng = 0,25đ | 3 ý đúng = 0,5đ | 4 ý đúng = 1,0đ
                if sub_matches == 4:
                    earned_point = q_point
                    is_correct = True
                    correct_count += 1
                    status = "correct"
                elif sub_matches == 3:
                    earned_point = round(q_point * 0.5, 2)
                    is_partial = True
                    partial_count += 1
                    status = "partial"
                elif sub_matches == 2:
                    earned_point = round(q_point * 0.25, 2)
                    is_partial = True
                    partial_count += 1
                    status = "partial"
                elif sub_matches == 1:
                    earned_point = round(q_point * 0.1, 2)
                    is_partial = True
                    partial_count += 1
                    status = "partial"
                else:
                    wrong_count += 1
                    status = "wrong"

        # -------------------------------------------------------------
        # DẠNG 2: ĐIỀN ĐÁP SỐ / TRẢ LỜI NGẮN (SHORT ANSWER)
        # -------------------------------------------------------------
        elif q_type in ["short_answer", "fill_blank"]:
            q_type = "short_answer"
            correct_raw = q.get("correct_answer", "")
            accepted_answers = q.get("accepted_answers", [])
            if not accepted_answers:
                accepted_answers = [correct_raw]

            if user_ans is None or str(user_ans).strip() == "":
                status = "unanswered"
                unanswered_count += 1
            else:
                norm_u = _normalize_str(user_ans)
                match = False
                for ans_candidate in accepted_answers:
                    norm_c = _normalize_str(ans_candidate)
                    if norm_u == norm_c:
                        match = True
                        break
                    # So khớp số học nếu là số float
                    try:
                        if abs(float(norm_u) - float(norm_c)) < 1e-4:
                            match = True
                            break
                    except ValueError:
                        pass

                if match:
                    earned_point = q_point
                    is_correct = True
                    correct_count += 1
                    status = "correct"
                else:
                    wrong_count += 1
                    status = "wrong"

        # -------------------------------------------------------------
        # DẠNG 3: TỰ LUẬN (ESSAY) - CHẤM ĐIỂM BẰNG AI THEO BAREM KHẢO THÍ
        # -------------------------------------------------------------
        elif q_type == "essay":
            q_type = "essay"
            essay_text = str(user_ans).strip() if user_ans is not None else ""
            if not essay_text:
                status = "unanswered"
                unanswered_count += 1
            else:
                from backend.exam_engine.essay_grader import grade_essay_with_ai
                rubric = q.get("correct_answer") or q.get("explanation") or "Đánh giá các bước giải và lập luận tự luận theo barem chuẩn."
                eval_res = grade_essay_with_ai(
                    prompt=q.get("prompt", ""),
                    student_essay=essay_text,
                    official_rubric=str(rubric),
                    max_points=q_point,
                    subject_domain=domain
                )
                earned_point = eval_res.get("score", 0.0)
                if earned_point >= q_point * 0.8:
                    is_correct = True
                    correct_count += 1
                    status = "correct"
                elif earned_point > 0:
                    is_partial = True
                    partial_count += 1
                    status = "partial"
                else:
                    wrong_count += 1
                    status = "wrong"
                q["ai_essay_evaluation"] = eval_res

        # -------------------------------------------------------------
        # DẠNG 4: TRẮC NGHIỆM ĐƠN LỰA CHỌN (A, B, C, D)
        # -------------------------------------------------------------
        else:
            q_type = "multiple_choice"
            correct_ans = str(q.get("correct_answer", "A")).strip().upper()
            u_ans_str = str(user_ans).strip().upper() if user_ans is not None else None

            if u_ans_str is None or u_ans_str == "":
                status = "unanswered"
                unanswered_count += 1
            elif u_ans_str == correct_ans:
                earned_point = q_point
                is_correct = True
                correct_count += 1
                status = "correct"
            else:
                wrong_count += 1
                status = "wrong"

        total_score += earned_point
        if q_num <= 40 or sec_id == "section_1_language":
            sec1_score += earned_point
        elif q_num <= 70 or sec_id == "section_2_logic_data":
            sec2_score += earned_point
        else:
            sec3_score += earned_point

        if domain not in domain_stats:
            domain_stats[domain] = {"name": domain, "correct": 0, "total": 0, "score": 0.0, "max_score": 0.0}
        domain_stats[domain]["total"] += 1
        domain_stats[domain]["max_score"] += q_point
        if is_correct:
            domain_stats[domain]["correct"] += 1
        domain_stats[domain]["score"] += earned_point

        detailed_results.append({
            "question_number": q_num,
            "domain": domain,
            "section_id": sec_id,
            "question_type": q_type,
            "difficulty": q.get("difficulty", "medium"),
            "user_answer": user_ans,
            "correct_answer": q.get("correct_answer"),
            "is_correct": is_correct,
            "is_partial": is_partial,
            "status": status,
            "points": q_point,
            "earned_points": earned_point,
            "explanation": q.get("explanation", ""),
            "prompt": q.get("prompt", ""),
            "options": q.get("options", {}),
            "tf_statements": q.get("tf_statements", {}),
            "ai_essay_evaluation": q.get("ai_essay_evaluation")
        })

    radar_data = {}
    for d_key, stat in domain_stats.items():
        percentage = round((stat["score"] / stat["max_score"] * 100.0), 1) if stat["max_score"] > 0 else 0.0
        radar_data[d_key] = {
            "name": stat["name"],
            "correct": stat["correct"],
            "total": stat["total"],
            "score": round(stat["score"], 2),
            "max_score": round(stat["max_score"], 2),
            "percentage": percentage
        }

    return {
        "total_score": round(total_score, 2),
        "max_total_score": actual_max_score,
        "is_spt": is_spt,
        "sec1_score": round(sec1_score, 2),
        "sec2_score": round(sec2_score, 2),
        "sec3_score": round(sec3_score, 2),
        "correct_count": correct_count,
        "partial_count": partial_count,
        "wrong_count": wrong_count,
        "unanswered_count": unanswered_count,
        "total_questions": len(questions),
        "domain_stats": radar_data,
        "detailed_results": detailed_results
    }

