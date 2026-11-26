// Exam Runner Module
const examRunner = {
  examData: null,
  currentQuestionIndex: 0,
  userAnswers: {}, // { "1": "A", "2": "C", ... }
  flaggedQuestions: new Set(),
  remainingSeconds: 150 * 60,
  timerInterval: null,
  examStartTime: null,

  async startBenchmarkExam() {
    await this.loadAndStartExam("dgnl_benchmark_standard_2025");
  },

  async loadAndStartExam(examId) {
    try {
      const res = await fetch(`/api/exams/${examId}?mode=test`);
      if (!res.ok) throw new Error("Không thể tải đề thi");
      const exam = await res.json();
      
      this.examData = exam;
      this.currentQuestionIndex = 0;
      this.userAnswers = {};
      this.flaggedQuestions = new Set();
      this.remainingSeconds = (exam.duration_minutes || 150) * 60;
      this.examStartTime = Date.now();

      document.getElementById('exam-title-display').innerText = exam.title;
      
      const printBtn = document.getElementById('exam-print-btn');
      if (printBtn) {
        printBtn.href = `/api/exams/${examId}/print`;
        printBtn.style.display = 'inline-block';
      }

      this.renderPalette();
      this.renderCurrentQuestion();
      this.startTimer();

      app.showTab('exam');
      this.saveSession();
    } catch (err) {
      alert("Lỗi tải đề thi: " + err.message);
    }
  },

  startCustomMistakePractice(mistakes) {
    if (!mistakes || mistakes.length === 0) {
      alert("Sổ tay chưa có câu sai nào!");
      return;
    }
    const questions = mistakes.map((m, idx) => ({
      id: m.id || ('q_mis_' + idx),
      question_number: idx + 1,
      section_id: 'part_1',
      domain: m.domain || 'Luyện tập câu sai',
      prompt: m.prompt,
      passage: m.passage || null,
      chart_image: null,
      question_type: m.question_type || 'multiple_choice',
      options: m.options || [],
      tf_statements: m.tf_statements || [],
      points: 10.0,
      difficulty: 'Vận dụng'
    }));

    this.examData = {
      id: 'mistake_practice_' + Date.now(),
      title: `Luyện Tập Bứt Phá: ${questions.length} Câu Từng Sai`,
      duration_minutes: Math.max(15, questions.length * 2),
      exam_type: 'spt',
      max_score: questions.length * 10,
      questions: questions
    };

    this.currentQuestionIndex = 0;
    this.userAnswers = {};
    this.flaggedQuestions = new Set();
    this.remainingSeconds = this.examData.duration_minutes * 60;
    this.examStartTime = Date.now();

    document.getElementById('exam-title-display').innerText = this.examData.title;
    const printBtn = document.getElementById('exam-print-btn');
    if (printBtn) printBtn.style.display = 'none';

    this.renderPalette();
    this.renderCurrentQuestion();
    this.startTimer();

    app.showTab('exam');
    this.saveSession();
  },

  startTimer() {
    if (this.timerInterval) clearInterval(this.timerInterval);
    
    this.updateTimerDisplay();
    this.timerInterval = setInterval(() => {
      this.remainingSeconds--;
      this.updateTimerDisplay();

      // Cảnh báo khi còn 10 phút
      if (this.remainingSeconds === 600) {
        alert("⚠️ CHÚ Ý: Còn 10 phút nữa là hết thời gian làm bài! Hãy rà soát lại các câu đã gắn cờ xem lại.");
      }

      // Hết giờ tự động nộp bài
      if (this.remainingSeconds <= 0) {
        clearInterval(this.timerInterval);
        alert("⏰ ĐÃ HẾT THỜI GIAN LÀM BÀI! Hệ thống sẽ tự động nộp bài thi của bạn.");
        this.submitExam();
      }
    }, 1000);
  },

  updateTimerDisplay() {
    const mins = Math.floor(Math.max(0, this.remainingSeconds) / 60);
    const secs = Math.max(0, this.remainingSeconds) % 60;
    const mStr = mins < 10 ? `0${mins}` : `${mins}`;
    const sStr = secs < 10 ? `0${secs}` : `${secs}`;
    
    const minEl = document.getElementById('timer-minutes');
    const secEl = document.getElementById('timer-seconds');
    if (minEl) minEl.innerText = mStr;
    if (secEl) secEl.innerText = sStr;

    // Tiến độ làm bài
    const answeredCount = Object.keys(this.userAnswers).length;
    const totalCount = this.examData?.questions?.length || 120;
    const progEl = document.getElementById('exam-progress-display');
    if (progEl) progEl.innerText = `Tiến độ: ${answeredCount}/${totalCount} câu đã làm`;
  },

  renderPalette() {
    const container = document.getElementById('palette-sections-container');
    if (!container || !this.examData) return;

    container.innerHTML = '';
    const questions = this.examData.questions || [];
    const isSpt = (this.examData.exam_type === 'spt');

    // Nhóm câu hỏi theo phần
    const groups = [];

    if (isSpt) {
      // SPT có 4 phần: Trắc nghiệm, Đúng/Sai, Điền đáp số, Tự luận
      const p1 = questions.filter(q => q.section_id === 'part_1' || q.question_type === 'multiple_choice');
      const p2 = questions.filter(q => q.section_id === 'part_2' || q.question_type === 'true_false');
      const p3 = questions.filter(q => q.section_id === 'part_3' || q.question_type === 'short_answer');
      const p4 = questions.filter(q => q.section_id === 'part_4' || q.question_type === 'essay');

      if (p1.length > 0) groups.push({ title: `Phần I: Trắc nghiệm (${p1.length} câu)`, questions: p1 });
      if (p2.length > 0) groups.push({ title: `Phần II: Đúng / Sai (${p2.length} câu)`, questions: p2 });
      if (p3.length > 0) groups.push({ title: `Phần III: Điền đáp số (${p3.length} câu)`, questions: p3 });
      if (p4.length > 0) groups.push({ title: `Phần IV: Tự luận (${p4.length} câu)`, questions: p4 });
    } else {
      // V-ACT 120 câu
      const p1 = questions.filter(q => q.question_number <= 60);
      const p2 = questions.filter(q => q.question_number > 60 && q.question_number <= 90);
      const p3 = questions.filter(q => q.question_number > 90);

      if (p1.length > 0) groups.push({ title: `Phần 1: Sử dụng ngôn ngữ (1 - ${p1.length})`, questions: p1 });
      if (p2.length > 0) groups.push({ title: `Phần 2: Toán học (${p2[0]?.question_number} - ${p2[p2.length - 1]?.question_number})`, questions: p2 });
      if (p3.length > 0) groups.push({ title: `Phần 3: Tư duy khoa học (${p3[0]?.question_number} - ${p3[p3.length - 1]?.question_number})`, questions: p3 });
    }

    // Nếu không khớp phân nhóm trên, hiển thị toàn bộ
    if (groups.length === 0) {
      groups.push({ title: `Danh sách câu hỏi (${questions.length} câu)`, questions: questions });
    }

    groups.forEach(group => {
      const groupEl = document.createElement('div');
      groupEl.className = 'palette-group';

      const titleEl = document.createElement('div');
      titleEl.className = 'palette-group-title';
      titleEl.innerText = group.title;
      groupEl.appendChild(titleEl);

      const gridEl = document.createElement('div');
      gridEl.className = 'palette-grid';

      group.questions.forEach(q => {
        const qNum = q.question_number;
        const qIndex = questions.findIndex(item => item.question_number === qNum);
        
        const btn = document.createElement('button');
        btn.className = 'palette-btn';
        btn.id = `palette-btn-${qIndex}`;
        btn.innerText = qNum;
        btn.onclick = () => this.jumpToQuestion(qIndex);
        gridEl.appendChild(btn);
      });

      groupEl.appendChild(gridEl);
      container.appendChild(groupEl);
    });

    this.updatePaletteClasses();
  },

  updatePaletteClasses() {
    if (!this.examData) return;
    this.examData.questions.forEach((q, idx) => {
      const qNum = q.question_number || (idx + 1);
      const btn = document.getElementById(`palette-btn-${idx}`);
      if (!btn) return;

      btn.className = 'palette-btn';
      if (idx === this.currentQuestionIndex) {
        btn.classList.add('active');
      }

      // Kiểm tra câu đã làm
      const ans = this.userAnswers[qNum];
      let isAnswered = false;
      if (q.question_type === 'true_false') {
        isAnswered = Boolean(ans && typeof ans === 'object' && Object.keys(ans).length > 0);
      } else if (typeof ans === 'string') {
        isAnswered = ans.trim().length > 0;
      } else {
        isAnswered = Boolean(ans);
      }

      if (isAnswered) {
        btn.classList.add('answered');
      }
      if (this.flaggedQuestions.has(qNum)) {
        btn.classList.add('flagged');
      }
    });
  },

  renderCurrentQuestion() {
    if (!this.examData || !this.examData.questions) return;
    const q = this.examData.questions[this.currentQuestionIndex];
    if (!q) return;

    // Luôn cuộn khung câu hỏi về đầu trang khi chuyển câu
    const panels = document.querySelectorAll('.exam-panel .panel-content');
    panels.forEach(p => p.scrollTop = 0);

    const qNum = q.question_number || (this.currentQuestionIndex + 1);
    const qType = q.question_type || 'multiple_choice';

    // Header info
    document.getElementById('question-header-num').innerText = `Câu hỏi số ${qNum}`;
    document.getElementById('question-domain-badge').innerText = this.getDomainLabel(q.domain);
    
    const maxScore = this.examData.max_score || (this.examData.exam_type === 'spt' ? 10.0 : 1200.0);
    const pointsText = q.points ? `${q.points} điểm` : (maxScore <= 10.0 ? '0.25 điểm' : '10.0 điểm');
    document.getElementById('question-points-badge').innerText = `Trọng số: ${pointsText}`;
    
    const diffBadge = document.getElementById('question-difficulty-badge');
    diffBadge.innerText = this.getDifficultyLabel(q.difficulty);

    // Flag button status
    const flagBtn = document.getElementById('btn-flag-toggle');
    if (this.flaggedQuestions.has(qNum)) {
      flagBtn.innerHTML = '🚩 Bỏ đánh dấu';
      flagBtn.classList.add('btn-warning');
      flagBtn.classList.remove('btn-outline');
    } else {
      flagBtn.innerHTML = '🏳️ Đánh dấu xem lại';
      flagBtn.classList.remove('btn-warning');
      flagBtn.classList.add('btn-outline');
    }

    // Passage or Chart (Left Panel)
    const passageText = document.getElementById('passage-text');
    const chartContainer = document.getElementById('chart-image-container');
    const chartImg = document.getElementById('chart-image-display');
    const contextTag = document.getElementById('context-tag');

    const imageSource = q.chart_image || q.image;

    if (imageSource) {
      chartContainer.style.display = 'block';
      chartImg.src = imageSource;
      if (q.domain === 'geography') {
        contextTag.innerText = "Bản đồ / Sơ đồ Địa lý";
      } else if (q.domain === 'data_analysis') {
        contextTag.innerText = "Biểu đồ phân tích số liệu";
      } else {
        contextTag.innerText = "Hình ảnh / Sơ đồ minh họa";
      }
    } else {
      chartContainer.style.display = 'none';
      contextTag.innerText = "Ngữ liệu đọc hiểu";
    }

    if (q.passage) {
      passageText.innerHTML = app.formatMathText(q.passage);
    } else {
      passageText.innerHTML = "Câu hỏi trắc nghiệm kiến thức tổng hợp. Thí sinh đọc kỹ yêu cầu bên phải và hoàn thành câu trả lời.";
    }

    // Prompt
    const promptEl = document.getElementById('question-prompt-text');
    promptEl.innerHTML = app.formatMathText(q.prompt);

    // Options Container - Hỗ trợ cả 4 dạng câu hỏi:
    const optionsContainer = document.getElementById('question-options-list');
    optionsContainer.innerHTML = '';

    if (qType === 'multiple_choice') {
      // DẠNG 1: TRẮC NGHIỆM 4 PHƯƠNG ÁN (A, B, C, D)
      const selectedOption = this.userAnswers[qNum];
      ['A', 'B', 'C', 'D'].forEach(optKey => {
        const optText = q.options ? q.options[optKey] : '';
        if (!optText) return;

        const optItem = document.createElement('div');
        optItem.className = 'option-item';
        if (selectedOption === optKey) {
          optItem.classList.add('selected');
        }

        optItem.onclick = () => this.selectOption(qNum, optKey);

        optItem.innerHTML = `
          <div class="option-letter">${optKey}</div>
          <div class="option-content-text" style="font-size: 1rem; line-height: 1.5; color: #1e293b;">${app.formatMathText(optText)}</div>
        `;
        optionsContainer.appendChild(optItem);
      });
    } else if (qType === 'true_false') {
      // DẠNG 2: TRẮC NGHIỆM ĐÚNG / SAI 4 MỆNH ĐỀ (a, b, c, d)
      const stmts = q.tf_statements || {};
      const currentAns = (this.userAnswers[qNum] && typeof this.userAnswers[qNum] === 'object') ? this.userAnswers[qNum] : {};

      const tableWrapper = document.createElement('div');
      tableWrapper.innerHTML = `
        <table class="tf-matrix-table">
          <thead>
            <tr>
              <th>Mệnh đề phát biểu</th>
              <th style="width: 170px; text-align: center;">Khẳng định của thí sinh</th>
            </tr>
          </thead>
          <tbody>
            ${['a', 'b', 'c', 'd'].map(key => {
              if (!stmts[key]) return '';
              const val = currentAns[key];
              return `
                <tr>
                  <td class="tf-statement-cell">
                    <span class="tf-statement-letter">${key})</span>
                    ${app.formatMathText(stmts[key])}
                  </td>
                  <td class="tf-actions-cell">
                    <div class="tf-btn-group">
                      <button type="button" class="tf-btn ${val === 'Đ' ? 'selected-true' : ''}" onclick="examRunner.selectTrueFalse(${qNum}, '${key}', 'Đ')">
                        ✓ Đúng
                      </button>
                      <button type="button" class="tf-btn ${val === 'S' ? 'selected-false' : ''}" onclick="examRunner.selectTrueFalse(${qNum}, '${key}', 'S')">
                        ✗ Sai
                      </button>
                    </div>
                  </td>
                </tr>
              `;
            }).join('')}
          </tbody>
        </table>
        <div style="font-size: 0.8rem; color: #64748b; margin-top: 0.5rem;">
          ⚖️ Điểm bậc thang SPT: Đúng 1 ý = 0,1đ | Đúng 2 ý = 0,25đ | Đúng 3 ý = 0,5đ | Đúng cả 4 ý = 1,0đ.
        </div>
      `;
      optionsContainer.appendChild(tableWrapper);
    } else if (qType === 'short_answer') {
      // DẠNG 3: ĐIỀN ĐÁP SỐ / TRẢ LỜI NGẮN
      const currentVal = this.userAnswers[qNum] || '';
      const inputWrapper = document.createElement('div');
      inputWrapper.className = 'short-answer-wrapper';
      inputWrapper.innerHTML = `
        <label class="short-answer-label">✏️ Nhập đáp số / câu trả lời ngắn:</label>
        <input type="text" class="short-answer-input" id="short-answer-input-${qNum}"
          placeholder="Nhập kết quả theo yêu cầu của đề bài..."
          value="${currentVal}"
          oninput="examRunner.selectShortAnswer(${qNum}, this.value)" />
        <div class="short-answer-hint">
          💡 Lưu ý: Hệ thống chấp nhận dấu phẩy hoặc chấm cho số thập phân (Ví dụ: 11.36 hoặc 11,36).
        </div>
      `;
      optionsContainer.appendChild(inputWrapper);
    } else if (qType === 'essay') {
      // DẠNG 4: TỰ LUẬN / PHÂN TÍCH
      const currentNotes = this.userAnswers[qNum] || '';
      const essayWrapper = document.createElement('div');
      essayWrapper.className = 'essay-wrapper';
      essayWrapper.innerHTML = `
        <label class="short-answer-label">📝 Dàn ý bài làm / Ghi chú của thí sinh:</label>
        <textarea class="essay-textarea"
          placeholder="Ghi chú các luận điểm, công thức giải hoặc tóm tắt bài làm của bạn..."
          oninput="examRunner.selectEssay(${qNum}, this.value)">${currentNotes}</textarea>
        <div class="essay-notice">
          ℹ️ Câu hỏi tự luận sẽ có đáp án và barem chấm điểm chi tiết của trường ĐH Sư phạm Hà Nội sau khi nộp bài.
        </div>
      `;
      optionsContainer.appendChild(essayWrapper);
    }

    // Biên dịch KaTeX cho các công thức Toán học & Khoa học
    app.renderMath(passageText);
    app.renderMath(promptEl);
    app.renderMath(optionsContainer);

    // Prev / Next button state
    document.getElementById('btn-prev-q').disabled = (this.currentQuestionIndex === 0);
    document.getElementById('btn-next-q').innerText = (this.currentQuestionIndex === this.examData.questions.length - 1) ? 'Về câu đầu ↩️' : 'Câu Tiếp Theo ➡️';

    this.updatePaletteClasses();
  },

  selectOption(qNum, optKey) {
    this.userAnswers[qNum] = optKey;
    this.renderCurrentQuestion();
    this.updateTimerDisplay();
    this.saveSession();
  },

  selectTrueFalse(qNum, stmtKey, value) {
    if (!this.userAnswers[qNum] || typeof this.userAnswers[qNum] !== 'object') {
      this.userAnswers[qNum] = {};
    }
    // Toggle: nếu bấm lại cùng giá trị thì bỏ chọn
    if (this.userAnswers[qNum][stmtKey] === value) {
      delete this.userAnswers[qNum][stmtKey];
    } else {
      this.userAnswers[qNum][stmtKey] = value;
    }
    this.renderCurrentQuestion();
    this.updateTimerDisplay();
    this.saveSession();
  },

  selectShortAnswer(qNum, value) {
    this.userAnswers[qNum] = value;
    this.updateTimerDisplay();
    this.updatePaletteClasses();
    this.saveSession();
  },

  selectEssay(qNum, value) {
    this.userAnswers[qNum] = value;
    this.updateTimerDisplay();
    this.updatePaletteClasses();
    this.saveSession();
  },

  toggleFlagCurrent() {
    if (!this.examData) return;
    const qNum = this.examData.questions[this.currentQuestionIndex].question_number;
    if (this.flaggedQuestions.has(qNum)) {
      this.flaggedQuestions.delete(qNum);
    } else {
      this.flaggedQuestions.add(qNum);
    }
    this.renderCurrentQuestion();
  },

  jumpToQuestion(index) {
    if (index >= 0 && index < this.examData.questions.length) {
      this.currentQuestionIndex = index;
      this.renderCurrentQuestion();
    }
  },

  nextQuestion() {
    if (this.currentQuestionIndex < this.examData.questions.length - 1) {
      this.currentQuestionIndex++;
    } else {
      this.currentQuestionIndex = 0;
    }
    this.renderCurrentQuestion();
  },

  prevQuestion() {
    if (this.currentQuestionIndex > 0) {
      this.currentQuestionIndex--;
      this.renderCurrentQuestion();
    }
  },

  confirmSubmitExam() {
    const totalQ = this.examData?.questions?.length || 120;
    const answeredCount = Object.keys(this.userAnswers).length;
    const unansweredCount = totalQ - answeredCount;
    const flaggedCount = this.flaggedQuestions.size;
    const isSpt = (this.examData?.exam_type === 'spt');
    const scaleText = isSpt ? 'thang điểm 10.0 chuẩn ĐH Sư Phạm Hà Nội' : 'trọng số IRT (thang 1200 điểm)';

    let msg = `Bạn có chắc chắn muốn nộp bài thi không?\n\n`;
    msg += `• Số câu đã làm: ${answeredCount}/${totalQ}\n`;
    if (unansweredCount > 0) {
      msg += `• CẢNH BÁO: Còn ${unansweredCount} câu CHƯA TRẢ LỜI!\n`;
    }
    if (flaggedCount > 0) {
      msg += `• Còn ${flaggedCount} câu đang gắn cờ xem lại.\n`;
    }
    msg += `\nHệ thống sẽ tiến hành chấm điểm theo ${scaleText} và lập báo cáo phân tích năng lực.`;

    if (confirm(msg)) {
      this.submitExam();
    }
  },

  async submitExam() {
    if (this.timerInterval) clearInterval(this.timerInterval);
    const timeSpentSeconds = Math.round((Date.now() - this.examStartTime) / 1000);

    try {
      const res = await fetch(`/api/exams/${this.examData.id}/submit`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          candidate_name: "Thí sinh ĐGNL 2025",
          answers: this.userAnswers,
          time_spent_seconds: timeSpentSeconds
        })
      });

      if (!res.ok) throw new Error("Gặp sự cố khi nộp bài");
      const submissionResult = await res.json();
      
      this.clearSession();
      app.latestSubmission = submissionResult;
      
      // Chuyển sang màn hình Báo cáo Phân tích Năng lực
      analyticsView.renderReport(submissionResult);
      app.showTab('analytics');
    } catch (err) {
      alert("Lỗi nộp bài thi: " + err.message);
    }
  },

  saveSession() {
    if (!this.examData) return;
    const session = {
      examId: this.examData.id,
      userAnswers: this.userAnswers,
      flaggedQuestions: Array.from(this.flaggedQuestions),
      remainingSeconds: this.remainingSeconds,
      currentQuestionIndex: this.currentQuestionIndex,
      examStartTime: this.examStartTime
    };
    localStorage.setItem("dgnl_active_session", JSON.stringify(session));
  },

  clearSession() {
    localStorage.removeItem("dgnl_active_session");
  },

  async checkRestoreSession() {
    const raw = localStorage.getItem("dgnl_active_session");
    if (!raw) return;
    try {
      const s = JSON.parse(raw);
      if (!s || !s.examId) {
        this.clearSession();
        return;
      }

      // Kiểm tra đề bài còn tồn tại trong cơ sở dữ liệu không
      const checkRes = await fetch(`/api/exams/${s.examId}?mode=test`);
      if (!checkRes.ok) {
        // Đề bài đã bị xóa -> tự động xóa phiên và thoát giao diện làm bài về trang chủ
        this.clearSession();
        app.showTab('dashboard');
        return;
      }

      // Đề bài vẫn còn -> tự động tiếp tục phòng thi, bắt buộc học sinh làm bài và nộp bài
      const exam = await checkRes.json();
      this.examData = exam;
      this.userAnswers = s.userAnswers || {};
      this.flaggedQuestions = new Set(s.flaggedQuestions || []);
      this.remainingSeconds = (typeof s.remainingSeconds === 'number' && s.remainingSeconds > 0) ? s.remainingSeconds : (exam.duration_minutes || 150) * 60;
      this.currentQuestionIndex = (typeof s.currentQuestionIndex === 'number' && s.currentQuestionIndex < (exam.questions?.length || 0)) ? s.currentQuestionIndex : 0;
      this.examStartTime = s.examStartTime || Date.now();

      document.getElementById('exam-title-display').innerText = exam.title;
      this.renderPalette();
      this.renderCurrentQuestion();
      this.startTimer();
      app.showTab('exam');
    } catch (e) {
      console.warn("Session restore note:", e);
      this.clearSession();
      app.showTab('dashboard');
    }
  },

  getDomainLabel(d) {
    const map = {
      vietnamese: "Tiếng Việt",
      english: "Tiếng Anh",
      math: "Toán học",
      logic: "Tư duy logic",
      data_analysis: "Phân tích số liệu",
      chemistry: "Hóa học",
      physics: "Vật lý",
      biology: "Sinh học",
      history: "Lịch sử",
      geography: "Địa lý",
      civics_law: "GD Kinh tế & Pháp luật",
      tech_industry: "Công nghệ Công nghiệp",
      tech_agriculture: "Công nghệ Nông nghiệp"
    };
    return map[d] || d;
  },

  getDifficultyLabel(diff) {
    const map = {
      easy: "Nhận biết",
      medium: "Thông hiểu",
      hard: "Vận dụng",
      very_hard: "Vận dụng cao"
    };
    return map[diff] || diff;
  }
};
