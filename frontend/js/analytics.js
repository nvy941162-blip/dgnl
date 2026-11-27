// Competency Analytics & Reporting Module with Pedagogical AI Tutor & Mistake Tracking
const analyticsView = {
  currentFilter: 'all',
  submissionData: null,

  renderReport(data) {
    this.submissionData = data;

    document.getElementById('analytics-empty-notice').style.display = 'none';
    document.getElementById('analytics-report-content').style.display = 'block';

    const grade = data.grade_report;
    const comp = data.competency_analysis;

    // 1. Total score & Tier
    document.getElementById('report-total-score').innerText = grade.total_score;
    const maxScoreEl = document.getElementById('report-max-score-display');
    if (maxScoreEl) {
      maxScoreEl.innerText = `/ ${grade.max_total_score || 1200} điểm`;
    }
    
    const tierBadge = document.getElementById('report-tier-badge');
    tierBadge.innerText = `${comp.tier_rating} • Top ${100 - comp.estimated_percentile}% toàn quốc (Phân vị: ${comp.estimated_percentile}%)`;
    tierBadge.style.background = comp.tier_color;
    tierBadge.style.color = '#ffffff';

    // 2. Subscores (V-ACT or SPT Sections)
    const subscoresBar = document.getElementById('report-subscores-bar');
    if (subscoresBar) {
      subscoresBar.style.display = 'flex';
      if (grade.is_spt) {
        subscoresBar.innerHTML = `
          <div class="subscore-item">
            <div style="font-size: 0.85rem; color: var(--text-muted);">Phần I: Trắc nghiệm</div>
            <div class="num" style="color: #4f46e5;">${grade.sec1_score} đ</div>
          </div>
          <div class="subscore-item">
            <div style="font-size: 0.85rem; color: var(--text-muted);">Phần II: Đúng / Sai</div>
            <div class="num" style="color: #0ea5e9;">${grade.sec2_score} đ</div>
          </div>
          <div class="subscore-item">
            <div style="font-size: 0.85rem; color: var(--text-muted);">Phần III: Điền số / Trả lời ngắn</div>
            <div class="num" style="color: #10b981;">${grade.sec3_score} đ</div>
          </div>
          ${(grade.sec4_score && grade.sec4_score > 0) ? `
          <div class="subscore-item">
            <div style="font-size: 0.85rem; color: var(--text-muted);">Phần IV: Tự luận</div>
            <div class="num" style="color: #f59e0b;">${grade.sec4_score} đ</div>
          </div>` : ''}
        `;
      } else {
        subscoresBar.innerHTML = `
          <div class="subscore-item">
            <div style="font-size: 0.85rem; color: var(--text-muted);">Phần 1: Ngôn ngữ</div>
            <div class="num" style="color: #4f46e5;" id="report-sec1-score">${grade.sec1_score} / ${grade.sec1_max || 400}</div>
          </div>
          <div class="subscore-item">
            <div style="font-size: 0.85rem; color: var(--text-muted);">Phần 2: Toán, Logic & Số liệu</div>
            <div class="num" style="color: #0ea5e9;" id="report-sec2-score">${grade.sec2_score} / ${grade.sec2_max || 300}</div>
          </div>
          <div class="subscore-item">
            <div style="font-size: 0.85rem; color: var(--text-muted);">Phần 3: Giải quyết vấn đề</div>
            <div class="num" style="color: #10b981;" id="report-sec3-score">${grade.sec3_score} / ${grade.sec3_max || 500}</div>
          </div>
        `;
      }
    }

    // 3. Radar Chart Image
    const radarImg = document.getElementById('report-radar-img');
    if (data.radar_image) {
      radarImg.src = data.radar_image;
      radarImg.style.cursor = 'zoom-in';
      radarImg.title = 'Nhấp để phóng to biểu đồ';
      radarImg.onclick = () => imageZoomViewer.open(data.radar_image, 'Biểu đồ Radar Phân Tích Năng Lực Khảo Thí');
    }

    // 4. Strengths & Weaknesses
    const strongList = document.getElementById('strong-areas-list');
    const weakList = document.getElementById('weak-areas-list');

    if (comp.strong_areas && comp.strong_areas.length > 0) {
      strongList.innerHTML = comp.strong_areas.map(a => `
        <li><strong>${a.name}:</strong> Đạt <strong>${a.percentage}%</strong> (${a.correct}/${a.total} câu) - Điểm: ${a.score}/${a.max_score}đ</li>
      `).join('');
    } else {
      strongList.innerHTML = '<li>Chưa có chuyên đề nào đạt trên 70%. Cần tăng tốc độ giải đề và mở rộng kiến thức.</li>';
    }

    if (comp.weak_areas && comp.weak_areas.length > 0) {
      weakList.innerHTML = comp.weak_areas.map(a => `
        <li><strong>${a.name}:</strong> Đạt <strong>${a.percentage}%</strong> (${a.correct}/${a.total} câu) - Điểm: ${a.score}/${a.max_score}đ</li>
      `).join('');
    } else {
      weakList.innerHTML = '<li>Rất xuất sắc! Bạn không có chuyên đề nào bị dưới 50%.</li>';
    }

    // 5. AI Study Advice (Render Markdown sạch đẹp)
    const adviceBox = document.getElementById('report-ai-advice');
    if (adviceBox) {
      const rawText = data.ai_advice || 'Không có lời khuyên bổ sung.';
      let formatted = rawText
        .replace(/^### (.*$)/gim, '<h4 style="color:var(--primary); margin:0.8rem 0 0.3rem 0; font-size:1.05rem;">$1</h4>')
        .replace(/^## (.*$)/gim, '<h3 style="color:var(--primary); margin:1rem 0 0.4rem 0; font-size:1.15rem;">$1</h3>')
        .replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>')
        .replace(/^\* (.*$)/gim, '• $1<br>')
        .replace(/---/g, '<hr style="border:0; border-top:1px solid #e2e8f0; margin:0.75rem 0;">');
      adviceBox.innerHTML = formatted;
    }

    // Tự động lưu các câu sai vào Sổ Tay Bẫy Điểm (Mistake Notebook)
    this.autoSaveMistakes(data);

    // 6. Detailed question review table
    this.renderDetailedQuestionsTable('all');

    // 7. Load tiến trình lịch sử học tập
    this.loadHistoryChart();
  },

  autoSaveMistakes(data) {
    try {
      const results = data.grade_report?.detailed_results || [];
      const examTitle = data.grade_report?.is_spt ? "Bài thi SPT ĐHSPHN" : "Bài thi ĐGNL V-ACT";
      let notebook = JSON.parse(localStorage.getItem('dgnl_mistakes_notebook') || '[]');
      
      let addedCount = 0;
      results.forEach(r => {
        if (!r.is_correct && r.user_answer !== null && r.user_answer !== "") {
          const exists = notebook.some(m => m.prompt === r.prompt);
          if (!exists) {
            notebook.unshift({
              id: 'mis_' + Date.now() + '_' + Math.random().toString(36).substr(2, 4),
              exam_title: examTitle,
              question_number: r.question_number,
              domain: r.domain,
              prompt: r.prompt,
              user_answer: r.user_answer,
              correct_answer: r.correct_answer,
              explanation: r.explanation,
              question_type: r.question_type,
              options: r.options,
              tf_statements: r.tf_statements,
              saved_at: new Date().toLocaleDateString('vi-VN')
            });
            addedCount++;
          }
        }
      });
      // Giới hạn 100 câu sai gần nhất
      notebook = notebook.slice(0, 100);
      localStorage.setItem('dgnl_mistakes_notebook', JSON.stringify(notebook));
      if (typeof app !== 'undefined' && app.updateMistakeBadge) {
        app.updateMistakeBadge(notebook.length);
      }
    } catch (e) {
      console.warn("Could not auto-save mistakes:", e);
    }
  },

  renderDetailedQuestionsTable(filter = 'all') {
    this.currentFilter = filter;
    const container = document.getElementById('report-detailed-table-container');
    if (!this.submissionData || !container) return;

    const results = this.submissionData.grade_report.detailed_results || [];
    let filtered = results;

    if (filter === 'correct') {
      filtered = results.filter(r => r.is_correct);
    } else if (filter === 'wrong') {
      filtered = results.filter(r => !r.is_correct && r.user_answer !== null && r.user_answer !== "");
    } else if (filter === 'unanswered') {
      filtered = results.filter(r => r.user_answer === null || r.user_answer === "");
    }

    container.innerHTML = `
      <div style="display: flex; gap: 0.5rem; margin-bottom: 1rem; flex-wrap: wrap;">
        <button class="btn ${filter === 'all' ? 'btn-primary' : 'btn-outline'}" onclick="analyticsView.renderDetailedQuestionsTable('all')">
          Tất Cả (${results.length})
        </button>
        <button class="btn ${filter === 'correct' ? 'btn-success' : 'btn-outline'}" onclick="analyticsView.renderDetailedQuestionsTable('correct')">
          Đúng (${results.filter(r => r.is_correct).length})
        </button>
        <button class="btn ${filter === 'wrong' ? 'btn-warning' : 'btn-outline'}" onclick="analyticsView.renderDetailedQuestionsTable('wrong')">
          Sai (${results.filter(r => !r.is_correct && r.user_answer !== null && r.user_answer !== "").length})
        </button>
        <button class="btn ${filter === 'unanswered' ? 'btn-outline' : 'btn-outline'}" onclick="analyticsView.renderDetailedQuestionsTable('unanswered')">
          Chưa làm (${results.filter(r => r.user_answer === null || r.user_answer === "").length})
        </button>
      </div>

      <div style="display: flex; flex-direction: column; gap: 1rem;">
        ${filtered.map(r => {
          let statusBadge = '';
          if (r.is_correct) {
            statusBadge = `<span class="badge badge-success">✔️ Đúng (+${r.earned_points}đ)</span>`;
          } else if (r.is_partial) {
            statusBadge = `<span class="badge badge-warning">⚡ Đúng một phần (+${r.earned_points}đ / ${r.points}đ)</span>`;
          } else if (r.user_answer === null || r.user_answer === "") {
            statusBadge = `<span class="badge badge-secondary">⚪ Bỏ qua (0đ / ${r.points}đ)</span>`;
          } else {
            statusBadge = `<span class="badge" style="background:#fee2e2; color:#dc2626;">❌ Sai (0đ / ${r.points}đ)</span>`;
          }

          // Xử lý hiển thị đáp án học sinh và đáp án đúng tùy theo dạng câu hỏi
          let answerComparisonHtml = '';
          if (r.question_type === 'true_false') {
            const uMap = (typeof r.user_answer === 'object' && r.user_answer) ? r.user_answer : {};
            const cMap = (typeof r.correct_answer === 'object' && r.correct_answer) ? r.correct_answer : {};
            const tfRows = ['a', 'b', 'c', 'd'].map(k => {
              const uVal = uMap[k] ? 'Đúng' : (uMap[k] === false ? 'Sai' : 'Chưa chọn');
              const cVal = (cMap[k] === true || cMap[k] === 'Đ' || cMap[k] === 'D') ? 'Đúng' : 'Sai';
              const match = uMap[k] !== undefined && ((uVal === 'Đúng') === (cVal === 'Đúng'));
              return `<span>Ý (${k}): Bạn chọn <strong>${uVal}</strong> • Đáp án: <strong style="color:var(--success)">${cVal}</strong> ${match ? '✅' : '❌'}</span>`;
            }).join(' | ');
            answerComparisonHtml = `<div style="font-size: 0.88rem; line-height: 1.5; margin-bottom: 0.5rem; color: #334155;">${tfRows}</div>`;
          } else if (r.question_type === 'essay') {
            const evalObj = r.ai_essay_evaluation || {};
            answerComparisonHtml = `
              <div style="margin-bottom: 0.5rem; background: #f1f5f9; padding: 0.65rem 0.85rem; border-radius: 0.4rem; font-size: 0.9rem;">
                <div><strong>Bài làm của bạn:</strong> <em>"${r.user_answer || 'Không có bài làm'}"</em></div>
                <div style="margin-top: 0.35rem; color: #1e293b;">
                  🤖 <strong>AI Chấm Barem Khảo Thí (${r.earned_points}/${r.points}đ):</strong> ${evalObj.feedback || 'Đã đánh giá theo barem điểm sư phạm.'}
                </div>
              </div>
            `;
          } else {
            const uStr = (typeof r.user_answer === 'object') ? JSON.stringify(r.user_answer) : (r.user_answer ? app.formatMathText(String(r.user_answer)) : 'Không chọn');
            const cStr = (typeof r.correct_answer === 'object') ? JSON.stringify(r.correct_answer) : app.formatMathText(String(r.correct_answer || ''));
            answerComparisonHtml = `
              <div style="display: flex; gap: 1.5rem; font-size: 0.9rem; margin-bottom: 0.5rem; flex-wrap: wrap;">
                <span>Bạn chọn: <strong>${uStr}</strong></span>
                <span>Đáp án đúng: <strong style="color: var(--success);">${cStr}</strong></span>
              </div>
            `;
          }

          const qPayload = encodeURIComponent(JSON.stringify({
            prompt: r.prompt,
            user_answer: r.user_answer,
            correct_answer: r.correct_answer,
            explanation: r.explanation,
            question_type: r.question_type
          }));

          return `
            <div style="border: 1px solid var(--border); border-radius: 0.6rem; padding: 1.1rem; background: #ffffff;">
              <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.5rem; flex-wrap: wrap; gap: 0.4rem;">
                <span style="font-weight: 700; color: var(--primary);">Câu ${r.question_number} [${r.domain}] • Dạng: ${r.question_type}</span>
                ${statusBadge}
              </div>
              <div style="font-size: 0.98rem; margin-bottom: 0.5rem; font-weight: 600;">${app.formatMathText(r.prompt)}</div>
              ${answerComparisonHtml}
              <div style="background: #f8fafc; border-left: 3px solid var(--primary); padding: 0.65rem 0.9rem; border-radius: 0 0.4rem 0.4rem 0; font-size: 0.88rem; color: #475569; margin-bottom: 0.75rem;">
                <strong>💡 Lời giải chi tiết:</strong> ${app.formatMathText(r.explanation || 'Không có giải thích chi tiết.')}
              </div>
              <div style="display: flex; gap: 0.5rem; align-items: center;">
                <button class="btn btn-sm btn-outline" style="font-size: 0.82rem; padding: 0.35rem 0.75rem; border-color: #c7d2fe; color: #4338ca;" onclick="analyticsView.askAITutor('${qPayload}')">
                  🤖 Hỏi Gia Sư AI Về Câu Này
                </button>
              </div>
            </div>
          `;
        }).join('')}
      </div>
    `;

    // Render KaTeX for review table formulas
    app.renderMath(container);
  },

  async askAITutor(encodedPayload) {
    const qData = JSON.parse(decodeURIComponent(encodedPayload));
    const studentQuestion = prompt(
      "Nhập thắc mắc của bạn về câu hỏi này cho Gia Sư AI (hoặc để trống để AI tự phân tích lỗi sai):",
      "Thầy/Cô hãy giải thích tại sao câu này lại chọn đáp án như vậy và con bị sai ở bước tư duy nào ạ?"
    );
    if (studentQuestion === null) return; // Người dùng ấn Hủy

    const loadingMsg = "⏳ Gia Sư AI Sư phạm đang đọc bài và suy nghĩ lời giải thích...";
    alert(loadingMsg);

    try {
      const res = await fetch('/api/exams/ask-tutor', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          prompt: qData.prompt,
          user_answer: qData.user_answer,
          correct_answer: qData.correct_answer,
          explanation: qData.explanation,
          question_type: qData.question_type,
          student_query: studentQuestion
        })
      });
      const data = await res.json();
      if (data.tutor_reply) {
        alert(data.tutor_reply);
      } else {
        alert("Không nhận được phản hồi từ Gia Sư AI.");
      }
    } catch (e) {
      alert("Lỗi kết nối Gia Sư AI: " + e.message);
    }
  },

  async loadHistoryChart() {
    try {
      const user = (window.authManager && window.authManager.currentUser) ? window.authManager.currentUser : null;
      let url = '/api/history';
      if (user) {
        url += `?user_id=${encodeURIComponent(user.id)}&candidate_name=${encodeURIComponent(user.full_name)}`;
      }

      const res = await fetch(url);
      if (!res.ok) return;
      const data = await res.json();
      const history = data.history || [];
      const historyContainer = document.getElementById('analytics-history-section');
      if (!historyContainer) return;

      const historyList = document.getElementById('analytics-history-list');
      if (history.length === 0) {
        if (historyList) {
          historyList.innerHTML = `<div style="text-align: center; color: #94a3b8; padding: 1.5rem;">Học sinh <strong>${user ? user.full_name : ''}</strong> chưa có lịch sử làm bài nào. Hãy bắt đầu làm bài thi để tích lũy điểm nhé!</div>`;
        }
        return;
      }

      historyContainer.style.display = 'block';
      if (historyList) {
        historyList.innerHTML = history.slice(0, 10).map(h => `
          <div style="display: flex; justify-content: space-between; align-items: center; padding: 0.65rem 0.85rem; border-bottom: 1px solid #f1f5f9; font-size: 0.9rem;">
            <div>
              <strong style="color: var(--primary);">${h.exam_title}</strong>
              <div style="font-size: 0.8rem; color: #64748b;">${h.submitted_at} • Thời gian: ${Math.round(h.time_spent_seconds / 60)} phút • Thí sinh: ${h.candidate_name || 'Học sinh'}</div>
            </div>
            <div style="text-align: right;">
              <span style="font-weight: 700; font-size: 1.05rem; color: var(--success);">${h.total_score} / ${h.max_score}đ</span>
              <div style="font-size: 0.8rem; color: #475569;">Đạt ${h.percentage}%</div>
            </div>
          </div>
        `).join('');
      }
    } catch (e) {
      console.warn("Could not load history", e);
    }
  },
          </div>
        `).join('');
      }
    } catch (e) {
      console.warn("Could not load history chart:", e);
    }
  },

  // -------------------------------------------------------------
  // SAO CHÉP BÁO CÁO ĐIỂM (CHO PHÉP COPY VÀO PHẦN MỀM KHÁC / ZALO / EXCEL)
  // -------------------------------------------------------------
  copyReportText() {
    if (!this.submissionData) {
      alert("Chưa có dữ liệu bài thi để sao chép!");
      return;
    }

    const grade = this.submissionData.grade_report;
    const comp = this.submissionData.competency_analysis;
    const isSpt = grade.is_spt;
    const examTitle = isSpt ? "BÀI THI SPT ĐH SƯ PHẠM HÀ NỘI" : "BÀI THI ĐÁNH GIÁ NĂNG LỰC (V-ACT ĐHQG-HCM)";
    const maxScore = grade.max_total_score || (isSpt ? 10.0 : 1200);

    let reportLines = [
      "==================================================",
      `     PHIẾU KẾT QUẢ KHẢO THÍ ĐÁNH GIÁ NĂNG LỰC     `,
      "==================================================",
      `Họ và tên thí sinh : ${this.submissionData.candidate_name || "Thí sinh khảo thí"}`,
      `Kỳ thi / Đề thi    : ${examTitle}`,
      `Thời gian nộp bài  : ${new Date().toLocaleString("vi-VN")}`,
      `--------------------------------------------------`,
      `TỔNG ĐIỂM ĐẠT ĐƯỢC : ${grade.total_score} / ${maxScore} điểm`,
      `Xếp loại năng lực  : ${comp.tier_rating}`,
      `Thứ hạng phân vị   : Top ${100 - comp.estimated_percentile}% toàn quốc (Phân vị: ${comp.estimated_percentile}%)`
    ];

    if (!isSpt) {
      reportLines.push(
        `--------------------------------------------------`,
        `ĐIỂM CÁC PHẦN THI (CHUẨN ĐHQG-HCM 1200Đ):`,
        `• Phần 1 (Ngôn ngữ)           : ${grade.sec1_score} / 400đ`,
        `• Phần 2 (Toán & Số liệu)     : ${grade.sec2_score} / 300đ`,
        `• Phần 3 (Giải quyết vấn đề)  : ${grade.sec3_score} / 500đ`
      );
    }

    if (comp.strong_areas && comp.strong_areas.length > 0) {
      reportLines.push(
        `--------------------------------------------------`,
        `NĂNG LỰC VƯỢT TRỘI (>= 70%):`,
        ...comp.strong_areas.map(a => `• ${a.name}: ${a.percentage}% (${a.correct}/${a.total} câu) - Điểm: ${a.score}/${a.max_score}đ`)
      );
    }

    if (comp.weak_areas && comp.weak_areas.length > 0) {
      reportLines.push(
        `--------------------------------------------------`,
        `LỖ HỔNG CẦN KHẮC PHỤC (< 50%):`,
        ...comp.weak_areas.map(a => `• ${a.name}: ${a.percentage}% (${a.correct}/${a.total} câu) - Điểm: ${a.score}/${a.max_score}đ`)
      );
    }

    if (this.submissionData.ai_advice) {
      reportLines.push(
        `--------------------------------------------------`,
        `LỜI KHUYÊN ÔN TẬP TỪ AI CHUYÊN GIA:`,
        this.submissionData.ai_advice.replace(/[#*]/g, "")
      );
    }

    reportLines.push(
      "==================================================",
      "Được chứng nhận bởi Hệ Thống Khảo Thí ĐGNL Chuẩn Hóa GDPT 2018."
    );

    const fullText = reportLines.join("\n");

    // Copy to clipboard
    if (navigator.clipboard && navigator.clipboard.writeText) {
      navigator.clipboard.writeText(fullText).then(() => {
        alert("✅ ĐÃ SAO CHÉP THÀNH CÔNG BẢNG ĐIỂM!\n\nBạn có thể dán (Ctrl + V) vào Zalo, Word, Excel, Google Docs hoặc gửi cho Thầy/Cô và phụ huynh xem ngay.");
      }).catch(err => {
        this.fallbackCopyText(fullText);
      });
    } else {
      this.fallbackCopyText(fullText);
    }
  },

  fallbackCopyText(text) {
    const ta = document.createElement("textarea");
    ta.value = text;
    document.body.appendChild(ta);
    ta.select();
    try {
      document.execCommand("copy");
      alert("✅ ĐÃ SAO CHÉP BẢNG ĐIỂM VÀO BỘ NHỚ TẠM!\n\nBạn có thể dán (Ctrl + V) vào phần mềm khác.");
    } catch (e) {
      prompt("Sao chép thủ công báo cáo dưới đây (Ctrl + C):", text);
    }
    document.body.removeChild(ta);
  },

  // -------------------------------------------------------------
  // XUẤT FILE BẢNG ĐIỂM EXCEL / CSV
  // -------------------------------------------------------------
  exportCSV() {
    if (!this.submissionData) {
      alert("Chưa có dữ liệu bài thi để xuất file!");
      return;
    }

    const results = this.submissionData.grade_report?.detailed_results || [];
    if (results.length === 0) {
      alert("Chưa có danh sách chi tiết các câu hỏi.");
      return;
    }

    // Header UTF-8 BOM để Excel hiển thị đúng tiếng Việt có dấu
    let csvContent = "\uFEFF";
    csvContent += "Câu số,Miền năng lực,Dạng câu hỏi,Đáp án bạn chọn,Đáp án chính xác,Kết quả,Điểm đạt được,Điểm tối đa,Lời giải chi tiết\n";

    results.forEach(r => {
      const qNum = r.question_number || "";
      const domain = `"${(r.domain || "").replace(/"/g, '""')}"`;
      const qType = `"${(r.question_type || "").replace(/"/g, '""')}"`;
      
      let uAns = r.user_answer;
      if (typeof uAns === "object" && uAns !== null) {
        uAns = JSON.stringify(uAns);
      }
      uAns = `"${String(uAns || "").replace(/"/g, '""')}"`;

      let cAns = r.correct_answer;
      if (typeof cAns === "object" && cAns !== null) {
        cAns = JSON.stringify(cAns);
      }
      cAns = `"${String(cAns || "").replace(/"/g, '""')}"`;

      const resultText = r.is_correct ? "Đúng" : (r.is_partial ? "Đúng một phần" : "Sai");
      const earned = r.earned_points || 0;
      const pts = r.points || 0;
      const expl = `"${(r.explanation || "").replace(/"/g, '""').replace(/\n/g, ' ')}"`;

      csvContent += `${qNum},${domain},${qType},${uAns},${cAns},${resultText},${earned},${pts},${expl}\n`;
    });

    const blob = new Blob([csvContent], { type: "text/csv;charset=utf-8;" });
    const url = URL.createObjectURL(blob);
    const link = document.createElement("a");
    const dateStr = new Date().toISOString().slice(0, 10);
    link.setAttribute("href", url);
    link.setAttribute("download", `Bang_Diem_Chi_Tiet_DGNL_${dateStr}.csv`);
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
  }
};

window.analyticsView = analyticsView;
