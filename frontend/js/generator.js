// LangGraph AI Generator Studio & Full 120-Exam Automation
const generatorStudio = {
  isGenerating: false,
  isGenerating120: false,
  newExamId: null,
  pollTimer: null,

  // -------------------------------------------------------------
  // TẠO ĐỀ THI HOÀN CHỈNH 120 CÂU & CHO PHÉP VÀO THI NGAY
  // -------------------------------------------------------------
  async startFull120Generation() {
    if (this.isGenerating120) return;

    const title = document.getElementById('full-exam-title-input').value.trim();
    const theme = document.getElementById('full-exam-theme-input').value.trim();

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
    startBtn.innerHTML = "⏳ Đang tạo đề 120 câu...";
    statusText.innerText = "Hội đồng tác tử LangGraph đang làm việc...";
    progressBox.style.display = 'block';
    readyBanner.style.display = 'none';

    progressBar.style.width = '5%';
    progressPercent.innerText = '5%';
    progressStep.innerText = 'Đang khởi động Hội đồng Tác tử & chuẩn bị 3 phân khu...';
    progressCounter.innerText = '0 / 120 câu hỏi';

    try {
      const res = await fetch('/api/exams/generate-120', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ title, theme })
      });

      if (!res.ok) throw new Error("Không thể khởi động tác vụ sinh đề 120 câu");
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

        if (progressBar) progressBar.style.width = `${task.percent}%`;
        if (progressPercent) progressPercent.innerText = `${task.percent}%`;
        if (progressStep) progressStep.innerText = task.current_step;
        if (progressCounter) progressCounter.innerText = `${task.generated_count || 0} / 120 câu hỏi đã xử lý`;

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
    statusText.innerText = "✅ Hoàn tất đề thi 120 câu!";
    
    if (readyDesc) {
      readyDesc.innerHTML = `
        Đề thi <strong>"${task.exam_title}"</strong> (Mã: <code>${task.exam_id}</code>) đã được hoàn thành với trọn vẹn 120 câu hỏi chuẩn hóa:
        <br>• <strong>Phần 1: Ngôn ngữ (40 câu)</strong>: 20 Tiếng Việt + 20 Tiếng Anh
        <br>• <strong>Phần 2: Toán, Logic & Số liệu (30 câu)</strong>: 10 Toán + 10 Logic + 10 Số liệu kèm biểu đồ mới
        <br>• <strong>Phần 3: Giải quyết vấn đề (50 câu)</strong>: Hóa, Lý, Sinh, Sử, Địa
        <br>Đã được <strong>Critic Agent</strong> phê duyệt và chuẩn hóa thang điểm <strong>1200 điểm theo trọng số IRT</strong>.
      `;
    }
    readyBanner.style.display = 'block';

    // Tự động nạp số thứ tự đề kế tiếp (03 -> 04...) cho ô nhập liệu
    this.loadNextExamTitle();
  },

  async loadNextExamTitle() {
    try {
      const res = await fetch('/api/exams/next-info');
      if (res.ok) {
        const data = await res.json();
        const input = document.getElementById('full-exam-title-input');
        if (input && data.suggested_title) {
          input.value = data.suggested_title;
        }
      }
    } catch (e) {
      console.error("Failed to fetch next exam title:", e);
    }
  },

  takeGeneratedExamNow() {
    if (!this.newExamId) {
      alert("Chưa có đề thi mới nào được tạo!");
      return;
    }
    // Trực tiếp nạp đề mới vào phòng thi 150 phút và chuyển tab ngay lập tức
    examRunner.loadAndStartExam(this.newExamId);
  },

  resetFull120UI() {
    this.isGenerating120 = false;
    const startBtn = document.getElementById('btn-start-full-120');
    const statusText = document.getElementById('full-exam-status-text');
    if (startBtn) {
      startBtn.disabled = false;
      startBtn.innerHTML = "⚡ Bắt Đầu Tạo Đề 120 Câu Bằng AI";
    }
    if (statusText) statusText.innerText = "Sẵn sàng tạo đề thi hoàn chỉnh.";
  }
};
