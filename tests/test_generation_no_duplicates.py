import sys, os
sys.path.insert(0, os.path.abspath("."))
import requests
import json
import re

def get_fp(prompt):
    return re.sub(r'[^a-zA-Z0-9\u00C0-\u024F\u1EA0-\u1EF9]', '', str(prompt).lower())[:90]

def test_spt_generation_direct():
    print("\n--- 1. Testing SPT Generation Across Subjects ---")
    import sqlite3
    conn = sqlite3.connect("data/dgnl_platform.db")
    conn.cursor().execute("DELETE FROM exams WHERE title LIKE 'Đề Kiểm Thử Không Trùng Lặp%'")
    conn.commit()
    conn.close()

    from backend.agent_council.full_exam_generator import full_exam_generator, GENERATION_TASKS
    
    subjects_to_test = ["math", "history", "biology", "english"]
    
    for subj in subjects_to_test:
        print(f"\nTesting generation for subject: {subj}...")
        title = f"Đề Kiểm Thử Không Trùng Lặp Môn {subj.upper()}"
        task_id = full_exam_generator.generate_full_exam_async(
            exam_title=title,
            topic_theme="Kiểm định chống trùng lặp câu hỏi",
            mode=f"spt_{subj}"
        )
        
        # Poll task until complete
        import time
        max_wait = 60
        start = time.time()
        while time.time() - start < max_wait:
            task = GENERATION_TASKS.get(task_id, {})
            if task.get("status") in ["completed", "failed"]:
                break
            time.sleep(1)
            
        task = GENERATION_TASKS.get(task_id, {})
        assert task.get("status") == "completed", f"Generation failed for {subj}: {task.get('error')}"
        
        # Read the newly generated exam from DB
        import sqlite3
        conn = sqlite3.connect("data/dgnl_platform.db")
        cursor = conn.cursor()
        cursor.execute("SELECT id, data_json, total_questions FROM exams WHERE title = ?", (title,))
        row = cursor.fetchone()
        assert row is not None, f"Exam not found in DB for {subj}"
        
        eid, data_json, total_q = row
        content = json.loads(data_json)
        qs = content.get("questions", []) if isinstance(content, dict) else content
        
        prompts = [q.get("prompt", "") for q in qs]
        fps = [get_fp(p) for p in prompts]
        unique_fps = set(fps)
        
        print(f"  -> Generated {len(qs)} questions for {subj}. Total prompts: {len(prompts)}, Unique: {len(unique_fps)}")
        assert len(prompts) == len(unique_fps), f"DUPLICATES DETECTED in {subj}: {len(prompts) - len(unique_fps)} duplicates!"
        print(f"  -> SUCCESS: 0 duplicate questions in {subj} exam!")

def test_vact_domain_batches():
    print("\n--- 2. Testing V-ACT Domain Fallback Deduplication ---")
    from backend.agent_council.domain_generators import domain_generators
    
    # Test Vietnamese
    vn_items = domain_generators.generate_vietnamese_batch("Phát triển bền vững")
    vn_prompts = [get_fp(q["prompt"]) for q in vn_items]
    assert len(vn_prompts) == 20, f"Expected 20 Vietnamese items, got {len(vn_prompts)}"
    assert len(set(vn_prompts)) == 20, f"Vietnamese has duplicates: {len(vn_prompts) - len(set(vn_prompts))}"
    print(f"  -> Vietnamese 20 items: {len(set(vn_prompts))}/20 unique (0 duplicates)")

    # Test English
    en_items = domain_generators.generate_english_batch("Global Education")
    en_prompts = [get_fp(q["prompt"]) for q in en_items]
    assert len(en_prompts) == 20, f"Expected 20 English items, got {len(en_prompts)}"
    assert len(set(en_prompts)) == 20, f"English has duplicates: {len(en_prompts) - len(set(en_prompts))}"
    print(f"  -> English 20 items: {len(set(en_prompts))}/20 unique (0 duplicates)")

    # Test Logic
    logic_items = domain_generators.generate_logic_batch("Tư duy phản biện")
    lg_prompts = [get_fp(q["prompt"]) for q in logic_items]
    assert len(lg_prompts) == 10, f"Expected 10 Logic items, got {len(lg_prompts)}"
    assert len(set(lg_prompts)) == 10, f"Logic has duplicates: {len(lg_prompts) - len(set(lg_prompts))}"
    print(f"  -> Logic 10 items: {len(set(lg_prompts))}/10 unique (0 duplicates)")

if __name__ == "__main__":
    test_vact_domain_batches()
    test_spt_generation_direct()
    print("\n=======================================================")
    print("ALL TESTS PASSED: 100% UNIQUE QUESTIONS, 0 DUPLICATES!")
    print("=======================================================")
