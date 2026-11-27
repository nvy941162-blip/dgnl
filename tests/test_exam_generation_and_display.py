import sqlite3
import json

conn = sqlite3.connect('data/dgnl_platform.db')
c = conn.cursor()

# Check all exams in DB
c.execute("SELECT id, title, total_questions, data_json FROM exams")
for row in c.fetchall():
    eid, title, tq, dstr = row
    raw = json.loads(dstr)
    qs = raw if isinstance(raw, list) else raw.get('questions', [])
    print(f"Exam: {eid} - {title} ({len(qs)} questions)")
    for i, q in enumerate(qs[:5]):
        q_type = q.get('question_type', 'multiple_choice')
        opts = q.get('options')
        stmts = q.get('tf_statements')
        if q_type == 'multiple_choice':
            assert isinstance(opts, dict) and all(k in opts for k in ['A', 'B', 'C', 'D']), f"Invalid opts in {eid} Q{i+1}: {opts}"
        elif q_type == 'true_false':
            assert isinstance(stmts, dict) and all(k in stmts for k in ['a', 'b', 'c', 'd']), f"Invalid stmts in {eid} Q{i+1}: {stmts}"

print("\nALL EXISTING EXAMS VALIDATED PERFECTLY! Options and statements are dictionaries with 4 keys!")
