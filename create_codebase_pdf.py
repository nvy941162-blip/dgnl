import sys
import subprocess
from pathlib import Path

# Đường dẫn thư mục dự án
PROJECT_DIR = Path("D:/Antigravity/Dang gia nang luc")
HTML_PATH = PROJECT_DIR / "tailieu_giaithich_code_multiagent.html"
PDF_PATH = PROJECT_DIR / "TAI_LIEU_GIAI_THICH_MA_NGUON_MULTIAGENT_KHKT.pdf"

html_content = """<!DOCTYPE html>
<html lang="vi">
<head>
  <meta charset="UTF-8">
  <title>BÁO CÁO KHOA HỌC: GIẢI THÍCH CHI TIẾT MÃ NGUỒN & MULTI-AGENT LANGGRAPH</title>
  <style>
    @page { size: A4; margin: 18mm 15mm 18mm 15mm; }
    body { font-family: "Times New Roman", Times, serif; font-size: 11pt; line-height: 1.4; color: #111; margin: 0; padding: 10px; }
    .doc-header { text-align: center; border-bottom: 2px solid #1e3a8a; padding-bottom: 10px; margin-bottom: 18px; }
    .doc-header h2 { margin: 0; font-size: 13pt; text-transform: uppercase; color: #1e3a8a; }
    .doc-header h1 { margin: 5px 0; font-size: 15pt; text-transform: uppercase; color: #b91c1c; }
    .doc-header p { margin: 3px 0; font-style: italic; font-size: 10pt; color: #475569; }
    h2 { font-size: 12pt; color: #1e3a8a; border-left: 4px solid #1e3a8a; padding-left: 8px; margin-top: 18px; margin-bottom: 6px; text-transform: uppercase; }
    p, li { text-align: justify; }
    table { width: 100%; border-collapse: collapse; margin: 10px 0; font-size: 9.5pt; }
    th, td { border: 1px solid #334155; padding: 5px 8px; text-align: left; }
    th { background: #f1f5f9; font-weight: bold; }
    .box-highlight { background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 5px; padding: 10px 12px; margin: 10px 0; }
    .agent-card { border-left: 3px solid #2563eb; background: #eff6ff; padding: 7px 10px; margin: 6px 0; border-radius: 0 4px 4px 0; }
    .page-break { page-break-before: always; }
  </style>
</head>
<body>
  <div class="doc-header">
    <h2>CUỘC THI KHOA HỌC KỸ THUẬT CẤP TỈNH NĂM HỌC 2026</h2>
    <h1>BÁO CÁO GIẢI THÍCH CHI TIẾT CẤU TRÚC MÃ NGUỒN<br>& HỘI ĐỒNG TÁC TỬ MULTI-AGENT LANGGRAPH</h1>
    <p>Đề tài: Nền tảng Khảo thí & Tạo đề ĐGNL Chuẩn hóa Tự động ứng dụng AI và Lý thuyết IRT</p>
    <p>Đối tượng thẩm định: Hội đồng Giám khảo chuyên môn Lĩnh vực Phần mềm Hệ thống & AI</p>
  </div>

  <h2>1. TỔNG QUAN KIẾN TRÚC MÃ NGUỒN HỆ THỐNG</h2>
  <p>Toàn bộ mã nguồn dự án được tổ chức theo kiến trúc <strong>Modular Service-Oriented Architecture</strong> chặt chẽ:</p>
  <table>
    <tr><th style="width: 28%;">Thư mục / Tệp tin</th><th style="width: 22%;">Công nghệ / Thư viện</th><th>Chức năng cốt lõi trong hệ thống</th></tr>
    <tr><td><strong>backend/app.py</strong></td><td>FastAPI, Starlette</td><td>Bộ điều khiển API trung tâm, phân quyền RBAC (Admin vs Student), chấm điểm và lưu trữ.</td></tr>
    <tr><td><strong>backend/database.py</strong></td><td>SQLAlchemy, SQLite</td><td>Mô hình CSDL quan hệ ORM (UserModel, ExamModel, SubmissionModel) kèm Auto-Migration.</td></tr>
    <tr><td><strong>backend/agent_council/</strong></td><td>LangGraph, Google GenAI</td><td><strong>Hội đồng Tác tử Thông minh</strong>: Đồ thị trạng thái LangGraph, HyDE RAG, Critic Agent, Ragas.</td></tr>
    <tr><td><strong>backend/exam_engine/</strong></td><td>Pandas, Scipy, Matplotlib</td><td>Động cơ khảo thí: Chấm điểm IRT, Rubric tự luận, vẽ biểu đồ Radar phân tích năng lực.</td></tr>
    <tr><td><strong>frontend/js/app.js</strong></td><td>Vanilla JS ES6+</td><td>Điều phối giao diện SPA, Màn chắn đăng nhập (Login Wall), Sổ tay câu sai và Bảng xếp hạng.</td></tr>
    <tr><td><strong>frontend/js/generator.js</strong></td><td>Polling / REST API</td><td>Giao diện điều khiển Studio tạo đề thông minh thời gian thực (Bảo mật chỉ dành cho Admin).</td></tr>
    <tr><td><strong>frontend/js/analytics.js</strong></td><td>Vanilla JS, KaTeX</td><td>Xuất điểm thi, sao chép văn bản clipboard dán Word/Excel, xuất CSV và kết nối Gia Sư AI.</td></tr>
  </table>

  <h2>2. ĐẶC BIỆT: HỘI ĐỒNG TÁC TỬ THÔNG MINH MULTI-AGENT LANGGRAPH</h2>
  <div class="box-highlight">
    <strong>Sự khác biệt mang tính đột phá so với Single-Prompt truyền thống:</strong><br>
    Việc sử dụng 1 câu prompt dài gọi AI sinh đề thường gây ra ảo giác (Hallucination), trùng lặp và phương án gây nhiễu yếu. Dự án đã chuyển đổi thành <strong>Đồ thị tác tử đa luồng (LangGraph StateGraph)</strong> gồm 4 nút chuyên biệt:
  </div>

  <div class="agent-card">
    <strong>1. Nút hyde_retriever_node (HyDE RAG Agent):</strong><br>
    Ứng dụng thuật toán <em>Hypothetical Document Embeddings</em>. Khi nhận một chủ đề khảo thí, tác tử tự động sinh ra văn bản học thuật giả định, sau đó dùng làm vector truy xuất chính xác vào kho sách giáo khoa GDPT 2018.
  </div>

  <div class="agent-card">
    <strong>2. Nút generation_node (Generation Council):</strong><br>
    Phân hóa theo năng lực chuyên môn: <em>Language Agent</em> biên soạn đọc hiểu tiếng Việt & tiếng Anh B1-B2; <em>LogicDataAgent</em> tự động lập trình mã Python vẽ biểu đồ cột/tròn lưu ảnh minh họa thực tế; <em>DomainGenerators</em> sinh các môn chuyên biệt SPT.
  </div>

  <div class="agent-card">
    <strong>3. Nút critic_node (Critic Agent - Thẩm định viên phản biện khó tính):</strong><br>
    Đóng vai trò "gác cổng" khảo thí. Thẩm định 2 tiêu chí sống còn: (1) <em>single_truth_verified</em> - Bảo đảm câu hỏi chỉ có DUY NHẤT 1 đáp án đúng; (2) <em>distractor_score</em> - Đo lường độ bẫy học thuật của 3 phương án nhiễu (yêu cầu >= 0.75). Tự động hiệu chỉnh câu hỏi trước khi cấp phép.
  </div>

  <div class="agent-card">
    <strong>4. Nút ragas_node (Ragas Quantitative Evaluator):</strong><br>
    Đo lường định lượng câu hỏi trước khi nạp vào CSDL: Chỉ số <em>Faithfulness</em> >= 85% (Độ trung thực, không ảo giác tri thức) và <em>Answer Relevance</em> >= 90% (Mức độ bám sát chuẩn ma trận khảo thí).
  </div>

  <div class="page-break"></div>

  <h2>3. CƠ CHẾ ĐIỀU PHỐI API XOAY TUA GEMINI ROTATOR</h2>
  <p>Để Hội đồng Tác tử có thể sinh các đề thi lớn 120 câu hỏi mà không bao giờ bị nghẽn (HTTP 429 Rate-Limit), dự án xây dựng <strong>GeminiRotator</strong> với thuật toán xoay vòng thông minh:</p>
  <ul>
    <li><strong>Quản lý 9 API Keys song song</strong> độc lập từ tệp bảo mật <code>.env</code>.</li>
    <li><strong>Thuật toán Round-Robin với Auto-Cooldown</strong>: Tự động phân bổ tải trọng. Khi một key chạm giới hạn tần suất, hệ thống tự động đưa vào trạng thái đóng băng tạm thời và chuyển sang key tiếp theo trong <strong>0.01 giây</strong>.</li>
    <li><strong>Khóa cứng mô hình thế hệ mới</strong>: Tự động lọc bỏ các mô hình cũ đã ngừng hỗ trợ, khóa cố định vào <code>gemini-flash-lite-latest</code> với độ trễ phản hồi cực thấp (~1.28 giây).</li>
  </ul>

  <h2>4. MA TRẬN BẢO MẬT PHÂN QUYỀN VÀ CÔ LẬP BÀI THI (RBAC)</h2>
  <table>
    <tr><th>Nghiệp vụ khảo thí</th><th>Học sinh (Student)</th><th>Quản trị viên (Admin)</th><th>Giải pháp công nghệ kiểm soát</th></tr>
    <tr><td>Màn chắn đăng nhập (Login Wall)</td><td>Bắt buộc đăng nhập</td><td>Bắt buộc đăng nhập</td><td>Khóa UI toàn trang khi chưa có session</td></tr>
    <tr><td>Xem đề thi & Vào phòng thi</td><td>Toàn quyền xem mọi đề</td><td>Toàn quyền xem mọi đề</td><td>Ẩn đáp án đúng khi mode == 'test'</td></tr>
    <tr><td>Xem kết quả bài làm</td><td><strong>Chỉ xem bài của mình</strong></td><td>Xem được tất cả</td><td>Bảo vệ API: So khớp user_id, chặn 403 Forbidden</td></tr>
    <tr><td>Tạo đề thi mới (LangGraph)</td><td>❌ <strong>Bị chặn tuyệt đối</strong></td><td>✅ <strong>Toàn quyền tạo đề</strong></td><td>Chặn cả trên UI và Backend API (403 Forbidden)</td></tr>
    <tr><td>Bảng vàng xếp hạng (Leaderboard)</td><td>❌ Không hiển thị</td><td>✅ <strong>Xem từ cao xuống thấp</strong></td><td>Sắp xếp điểm % chuẩn hóa tự động</td></tr>
    <tr><td>Xóa bài thi thí sinh</td><td>❌ Không có quyền</td><td>✅ <strong>Xóa 1 bài hoặc tất cả</strong></td><td>Endpoint DELETE /api/admin/submissions</td></tr>
  </table>

  <h2>5. THUẬT TOÁN ĐỘT BIẾN CHỐNG TRÙNG LẶP (MUTATION)</h2>
  <p>Hệ thống tích hợp hàm <code>_mutate_question_template</code>:</p>
  <ul>
    <li><strong>Đột biến số học</strong>: Thay đổi ngẫu nhiên các tham số toán học, số liệu biểu đồ.</li>
    <li><strong>Xáo trộn phương án</strong>: Hoán vị vị trí các đáp án đúng/sai A, B, C, D.</li>
    <li><strong>Đảm bảo không trùng lặp 100%</strong>: Đề thi sinh ra hoàn toàn mới, không sao chép nguyên bản từ ngân hàng đề mẫu.</li>
  </ul>

  <div style="margin-top: 35px; border-top: 1px solid #334155; padding-top: 10px; font-style: italic; text-align: center; color: #475569;">
    Báo cáo kỹ thuật được khởi tạo tự động từ hệ thống mã nguồn phục vụ Hội đồng Giám khảo Cuộc thi KHKT năm học 2026.
  </div>
</body>
</html>
"""

with open(HTML_PATH, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"Created HTML documentation at: {HTML_PATH}")

# Dùng headless Edge để in ra PDF chuẩn A4
edge_exe = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
cmd = [
    edge_exe,
    "--headless",
    "--disable-gpu",
    f"--print-to-pdf={PDF_PATH}",
    "--no-pdf-header-footer",
    str(HTML_PATH.resolve())
]

res = subprocess.run(cmd, capture_output=True, text=True)
if res.returncode == 0 and PDF_PATH.exists():
    print(f"SUCCESS: Generated PDF at {PDF_PATH} (Size: {PDF_PATH.stat().st_size} bytes)")
else:
    print(f"Edge print output: {res.stderr}")
