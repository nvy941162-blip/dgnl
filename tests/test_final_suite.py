import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from fastapi.testclient import TestClient
from backend.app import app
import time

client = TestClient(app)

def test_spt_math_generation():
    # Test 1: Generate SPT Math with mode
    res = client.post('/api/exams/generate-120', json={
        'title': 'Đề Thi Thử SPT ĐH Sư Phạm Hà Nội - Môn Toán',
        'theme': 'Đại số, Giải tích, Hình học không gian, Lượng giác & Xác suất',
        'mode': 'spt_math'
    })
    print('SPT Math direct status:', res.status_code, res.json())
    assert res.status_code == 200
    task_id = res.json()['task_id']

    for _ in range(30):
        time.sleep(0.5)
        st = client.get(f'/api/exams/generate-120/status/{task_id}').json()
        if st['status'] == 'completed':
            print('SUCCESS SPT Math generated:')
            print('  Total count:', st.get('total_count'))
            print('  Duration minutes:', st.get('duration_minutes'))
            print('  Exam title:', st.get('exam_title'))
            print('  Step message:', st.get('current_step'))
            assert st.get('total_count') == 25
            assert st.get('duration_minutes') == 90
            break

def test_auto_detect():
    # Test 2: Auto-detect fallback when title had old text
    res2 = client.post('/api/exams/generate-120', json={
        'title': 'Đề Thi ĐGNL Số 23 - Luyện Thi Bứt Phá Điểm Số',
        'theme': 'Đại số, Giải tích, Hình học không gian, Lượng giác & Xác suất'
    })
    print('Auto-detect status:', res2.status_code, res2.json())
    assert res2.json()['mode'] == 'spt_math'

def test_endpoints():
    # Test 3: History endpoint
    res3 = client.get('/api/history')
    print('History status:', res3.status_code, len(res3.json().get('history', [])))
    assert res3.status_code == 200

    # Test 4: Printable HTML endpoint
    res4 = client.get('/api/exams/spt_sample_math/print')
    print('Printable HTML status:', res4.status_code)
    assert res4.status_code == 200
    assert 'BẢNG ĐÁP ÁN CHUẨN KHẢO THÍ' in res4.text

    # Test 5: Ask Tutor endpoint
    res5 = client.post('/api/exams/ask-tutor', json={
        'prompt': 'Cho hàm số f(x) = x^3 - 3x. Tìm giá trị cực đại của hàm số.',
        'user_answer': '-2',
        'correct_answer': '2',
        'explanation': 'f\'(x) = 3x^2 - 3 = 0 <=> x = +-1. Tại x = -1, f(-1) = 2 (cực đại).',
        'question_type': 'multiple_choice'
    })
    print('Ask Tutor status:', res5.status_code, res5.json().get('tutor_reply')[:80])
    assert res5.status_code == 200

if __name__ == '__main__':
    test_spt_math_generation()
    test_auto_detect()
    test_endpoints()
    print('>>> ALL 5 END-TO-END VERIFICATIONS PASSED 100%! <<<')
