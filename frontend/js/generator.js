// LangGraph AI Generator Studio & Full 120-Exam Automation
const generatorStudio = {
  isGenerating: false,
  isGenerating120: false,
  newExamId: null,
  pollTimer: null,
  currentMode: 'vact_full',
  recentExamsByMode: {},

  // -------------------------------------------------------------
  // TẠO ĐỀ THI HOÀN CHỈNH (V-ACT 120 CÂU HOẶC SPT TỪNG MÔN) & CHO PHÉP VÀO THI NGAY
  // -------------------------------------------------------------
  async startFull120Generation() {
    if (this.isGenerating120) return;

    // KIỂM TRA PHÂN QUYỀN: CHỈ ADMIN MỚI ĐƯỢC TẠO ĐỀ MỚI
    let currentUser = (window.authManager && window.authManager.currentUser) ? window.authManager.currentUser : (typeof authManager !== 'undefined' ? authManager.currentUser : null);
    if (!currentUser) {
      try {
        const raw = sessionStorage.getItem('dgnl_current_session_user') || localStorage.getItem('dgnl_current_student');
        if (raw) currentUser = JSON.parse(raw);
      } catch (e) {}
    }

    const navLabel = (document.getElementById('nav-user-label')?.innerText || '').toLowerCase();
    const isAdmin = Boolean(
      (typeof authManager !== 'undefined' && authManager.isAdmin && authManager.isAdmin()) ||
      (window.authManager && window.authManager.isAdmin && window.authManager.isAdmin()) ||
      (currentUser && (
        currentUser.role === 'admin' ||
        currentUser.username === 'admin' ||
        (currentUser.full_name && currentUser.full_name.toLowerCase().includes('admin')) ||
        (currentUser.student_class && currentUser.student_class.toLowerCase().includes('quản trị'))
      )) ||
      navLabel.includes('admin') ||
      navLabel.includes('quản trị')
    );

    if (!isAdmin) {
      alert("⚠️ THÔNG BÁO QUYỀN TRUY CẬP:\n\nChỉ Quản trị viên (Admin) mới có quyền tạo đề thi mới.\nHọc sinh chỉ có quyền xem đề và làm bài thi!");
      return;
    }

    const title = document.getElementById('full-exam-title-input').value.trim();
    const theme = document.getElementById('full-exam-theme-input').value.trim();
    const modeInput = document.getElementById('full-exam-mode-input');
    let mode = (modeInput && modeInput.value) ? modeInput.value : (this.currentMode || 'vact_full');

    // Khóa an toàn 2 lớp: Nếu tiêu đề hoặc giao diện đang ở môn SPT cụ thể, bắt buộc truyền mode SPT tương ứng
    const heroTitle = document.getElementById('generator-hero-title')?.innerText || '';
    const startBtnEl = document.getElementById('btn-start-full-120')?.innerText || '';
    const uiText = (heroTitle + " " + startBtnEl + " " + title + " " + theme).toLowerCase();

    if (uiText.includes("toán") || uiText.includes("đại số") || uiText.includes("giải tích")) mode = "spt_math";
    else if (uiText.includes("tiếng anh") || uiText.includes("english")) mode = "spt_english";
    else if (uiText.includes("hóa")) mode = "spt_chemistry";
    else if (uiText.includes("địa lí") || uiText.includes("địa lý") || uiText.includes("vùng kinh tế")) mode = "spt_geography";
    else if (uiText.includes("lịch sử") || uiText.includes("sử")) mode = "spt_history";
    else if (uiText.includes("gdkt") || uiText.includes("pháp luật")) mode = "spt_civics";
    else if (uiText.includes("công nghệ công nghiệp") || uiText.includes("công nghệ cn") || uiText.includes("cơ khí")) mode = "spt_tech_ind";
    else if (uiText.includes("công nghệ nông nghiệp") || uiText.includes("công nghệ nn") || uiText.includes("nông nghiệp")) mode = "spt_tech_agr";

    this.currentMode = mode;
    if (modeInput) modeInput.value = mode;

    const startBtn = document.getElementById('btn-start-full-120');
    const statusText = document.getElementById('full-exam-status-text');
    const progressBox = document.getElementById('full-exam-progress-box');
    const readyBanner = document.getElementById('full-exam-ready-banner');
    const progressBar = document.getElementById('full-progress-bar');
    const progressPercent = document.getElementById('full-progress-percent');
    const progressStep = document.getElementById('full-progress-step');
    const progressCounter = document.getElementById('full-progress-counter');

    this.isGenerating120 = true;
    startBtn.disabled = true;
    startBtn.innerHTML = "⏳ Đang tạo đề thi...";
    statusText.innerText = "Hội đồng tác tử LangGraph đang làm việc...";
    progressBox.style.display = 'block';
    readyBanner.style.display = 'none';

    progressBar.style.width = '5%';
    progressPercent.innerText = '5%';
    progressStep.innerText = 'Đang khởi động Hội đồng Tác tử...';
    progressCounter.innerText = 'Đang khởi tạo câu hỏi...';

    try {
      const res = await fetch('/api/exams/generate-120', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          title,
          theme,
          mode,
          user_id: currentUser ? currentUser.id : "user_admin_root",
          role: "admin"
        })
      });

      if (!res.ok) throw new Error("Không thể khởi động tác vụ sinh đề");
      const data = await res.json();
      const taskId = data.task_id;

      // Bắt đầu chu kỳ thăm dò tiến độ (Polling)
      this.pollProgress(taskId);

    } catch (err) {
      alert("Lỗi: " + err.message);
      this.resetFull120UI();
    }
  },

  pollProgress(taskId) {
    if (this.pollTimer) clearInterval(this.pollTimer);

    this.pollTimer = setInterval(async () => {
      try {
        const res = await fetch(`/api/exams/generate-120/status/${taskId}`);
        if (!res.ok) return;
        const task = await res.json();

        const progressBar = document.getElementById('full-progress-bar');
        const progressPercent = document.getElementById('full-progress-percent');
        const progressStep = document.getElementById('full-progress-step');
        const progressCounter = document.getElementById('full-progress-counter');

        const total = task.total_count || 120;
        if (progressBar) progressBar.style.width = `${task.percent}%`;
        if (progressPercent) progressPercent.innerText = `${task.percent}%`;
        if (progressStep) progressStep.innerText = task.current_step;
        if (progressCounter) progressCounter.innerText = `${task.generated_count || 0} / ${total} câu hỏi đã xử lý`;

        // Render live agent council logs
        const liveLogs = document.getElementById('full-exam-live-logs');
        if (liveLogs && task.agent_logs && task.agent_logs.length > 0) {
          liveLogs.innerHTML = task.agent_logs.map(l => `
            <div style="margin-bottom: 0.35rem; padding-bottom: 0.3rem; border-bottom: 1px solid #f1f5f9;">
              <strong style="color: var(--primary);">[${l.agent}]</strong>: ${l.action}
            </div>
          `).join('');
          liveLogs.scrollTop = liveLogs.scrollHeight;
        }

        if (task.status === 'completed') {
          clearInterval(this.pollTimer);
          this.newExamId = task.exam_id;
          this.onFull120Completed(task);
        } else if (task.status === 'failed') {
          clearInterval(this.pollTimer);
          alert("Quá trình sinh đề gặp lỗi: " + task.error);
          this.resetFull120UI();
        }
      } catch (e) {
        console.error("Polling error:", e);
      }
    }, 600);
  },

  onFull120Completed(task) {
    this.isGenerating120 = false;
    const startBtn = document.getElementById('btn-start-full-120');
    const statusText = document.getElementById('full-exam-status-text');
    const readyBanner = document.getElementById('full-exam-ready-banner');
    const readyDesc = document.getElementById('full-exam-ready-desc');

    startBtn.disabled = false;
    startBtn.innerHTML = "⚡ Tạo Thêm Đề Thi Mới";
    const total = task.total_count || 120;
    statusText.innerText = `✅ Hoàn tất đề thi (${total} câu)!`;
    
    // Lưu thông tin đề vừa tạo theo mode
    this.newExamId = task.exam_id;
    if (!this.recentExamsByMode) this.recentExamsByMode = {};
    this.recentExamsByMode[this.currentMode] = {
      id: task.exam_id,
      title: task.exam_title,
      total: total
    };
    this.updateRecentUI();

    if (readyDesc) {
      if (total < 120) {
        readyDesc.innerHTML = `
          Đề thi <strong>"${task.exam_title}"</strong> (Mã: <code>${task.exam_id}</code>) đã được hoàn thành với <strong>${total} câu hỏi chuẩn hóa</strong>:
          <br>• Thời gian làm bài: <strong>${task.duration_minutes || 60} phút</strong> - Thang điểm <strong>10.0 điểm</strong>.
          <br>• Đã được <strong>Critic Agent</strong> thẩm định và phân bổ cấu trúc câu hỏi chuẩn hóa môn thi SPT.
        `;
      } else {
        readyDesc.innerHTML = `
          Đề thi <strong>"${task.exam_title}"</strong> (Mã: <code>${task.exam_id}</code>) đã được hoàn thành với trọn vẹn 120 câu hỏi chuẩn hóa:
          <br>• <strong>Phần 1: Ngôn ngữ (40 câu)</strong>: 20 Tiếng Việt + 20 Tiếng Anh
          <br>• <strong>Phần 2: Toán, Logic & Số liệu (30 câu)</strong>: 10 Toán + 10 Logic + 10 Số liệu kèm biểu đồ mới
          <br>• <strong>Phần 3: Giải quyết vấn đề (50 câu)</strong>: Hóa, Lý, Sinh, Sử, Địa
          <br>Đã được <strong>Critic Agent</strong> phê duyệt và chuẩn hóa thang điểm <strong>1200 điểm theo trọng số IRT</strong>.
        `;
      }
    }
    readyBanner.style.display = 'block';

    // Cập nhật lại danh sách kho đề
    if (typeof app !== 'undefined' && app.loadExams) {
      app.loadExams();
    }

    // Tự động nạp số thứ tự đề kế tiếp cho ô nhập liệu nếu là vact_full
    if (!this.currentMode || this.currentMode === 'vact_full') {
      this.loadNextExamTitle();
    }
  },

  updateRecentUI() {
    const recent = this.recentExamsByMode && this.recentExamsByMode[this.currentMode];
    const delRecentBtn = document.getElementById('btn-delete-recent');
    const recentBox = document.getElementById('generator-recent-box');
    const recentTitle = document.getElementById('generator-recent-title');

    if (recent && recent.id) {
      this.newExamId = recent.id;
      if (delRecentBtn) delRecentBtn.style.display = 'inline-flex';
      if (recentBox && recentTitle) {
        recentTitle.innerText = `"${recent.title}" (${recent.total} câu)`;
        recentBox.style.display = 'flex';
      }
    } else {
      if (delRecentBtn) delRecentBtn.style.display = 'none';
      if (recentBox) recentBox.style.display = 'none';
    }
  },

  async deleteGeneratedExam() {
    const examId = this.newExamId || (this.recentExamsByMode && this.recentExamsByMode[this.currentMode]?.id);
    const examTitle = (this.recentExamsByMode && this.recentExamsByMode[this.currentMode]?.title) || "đề thi vừa tạo";

    if (!examId) {
      alert("Chưa có đề thi mới nào được tạo trong mục này!");
      return;
    }

    if (!confirm(`Bạn có chắc chắn muốn xóa đề thi vừa tạo:\n"${examTitle}"\nkhỏi hệ thống không?`)) {
      return;
    }

    try {
      const res = await fetch(`/api/exams/${examId}`, { method: 'DELETE' });
      const data = await res.json();
      if (!res.ok) throw new Error(data.detail || 'Lỗi khi xóa đề');
      
      alert(data.message || 'Đã xóa đề thi vừa tạo thành công!');

      // Xóa tham chiếu
      this.newExamId = null;
      if (this.recentExamsByMode) {
        delete this.recentExamsByMode[this.currentMode];
      }

      // Ẩn banners và reset UI
      const readyBanner = document.getElementById('full-exam-ready-banner');
      if (readyBanner) readyBanner.style.display = 'none';

      const progressBox = document.getElementById('full-exam-progress-box');
      if (progressBox) progressBox.style.display = 'none';

      this.updateRecentUI();
      this.resetFull120UI();

      // Cập nhật danh sách đề thi ở Dashboard
      if (typeof app !== 'undefined' && app.loadExams) {
        app.loadExams();
      }
    } catch (err) {
      alert("Lỗi khi xóa đề: " + err.message);
    }
  },

  resetFormToDefault() {
    // Đặt lại các trường nhập về mặc định cho môn/mục hiện tại
    if (typeof app !== 'undefined' && app.openGeneratorWithMode) {
      app.openGeneratorWithMode(this.currentMode || 'vact_full');
    }
    const progressBox = document.getElementById('full-exam-progress-box');
    if (progressBox) progressBox.style.display = 'none';
    const readyBanner = document.getElementById('full-exam-ready-banner');
    if (readyBanner) readyBanner.style.display = 'none';
    this.resetFull120UI();
  },

  redoGeneration() {
    // Làm lại: Ẩn thông báo cũ và bắt đầu tạo lại đề mới
    const readyBanner = document.getElementById('full-exam-ready-banner');
    if (readyBanner) readyBanner.style.display = 'none';
    this.startFull120Generation();
  },

  async loadNextExamTitle() {
    // Không ghi đè nếu người dùng đang ở chế độ môn thi SPT
    if (this.currentMode && this.currentMode !== 'vact_full') return;
    const modeInput = document.getElementById('full-exam-mode-input');
    if (modeInput && modeInput.value && modeInput.value !== 'vact_full') return;

    try {
      const res = await fetch('/api/exams/next-info');
      if (res.ok) {
        const data = await res.json();
        const input = document.getElementById('full-exam-title-input');
        if (input && data.suggested_title) {
          if (!this.currentMode || this.currentMode === 'vact_full') {
            input.value = data.suggested_title;
          }
        }
      }
    } catch (e) {
      console.error("Failed to fetch next exam title:", e);
    }
  },

  takeGeneratedExamNow() {
    const examId = this.newExamId || (this.recentExamsByMode && this.recentExamsByMode[this.currentMode]?.id);
    if (!examId) {
      alert("Chưa có đề thi mới nào được tạo trong mục này!");
      return;
    }
    // Trực tiếp nạp đề mới vào phòng thi và chuyển tab ngay lập tức
    examRunner.loadAndStartExam(examId);
  },

  resetFull120UI() {
    this.isGenerating120 = false;
    const startBtn = document.getElementById('btn-start-full-120');
    const statusText = document.getElementById('full-exam-status-text');
    if (startBtn) {
      startBtn.disabled = false;
      const isSPT = this.currentMode && this.currentMode !== 'vact_full';
      startBtn.innerHTML = isSPT ? "⚡ Bắt Đầu Tạo Đề Thi Bằng AI" : "⚡ Bắt Đầu Tạo Đề 120 Câu Bằng AI";
    }
    if (statusText) statusText.innerText = "Sẵn sàng tạo đề thi.";
  }
};
