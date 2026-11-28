// Competency Analytics & Reporting Module with Pedagogical AI Tutor & Mistake Tracking
const analyticsView = {
  currentFilter: 'all',
  submissionData: null,

  async loadLatest() {
    try {
      const user = (typeof authManager !== 'undefined') ? authManager.currentUser : null;
      const userId = user?.id || '';
      const candName = user?.full_name || '';

      let url = '/api/submissions/latest';
      const params = new URLSearchParams();
      if (userId) params.append('user_id', userId);
      else if (candName) params.append('candidate_name', candName);

      if (params.toString()) url += '?' + params.toString();

      const res = await fetch(url);
      if (!res.ok) return;
      const json = await res.json();
      if (json.has_submission && json.data) {
        this.renderReport(json.data);
      } else {
        const emptyNotice = document.getElementById('analytics-empty-notice');
        const reportContent = document.getElementById('analytics-report-content');
        if (emptyNotice) emptyNotice.style.display = 'block';
        if (reportContent) reportContent.style.display = 'none';
      }
    } catch (err) {
      console.error('Failed to load latest submission:', err);
    }
  },

  async loadSubmission(submissionId) {
    if (!submissionId) return;
    try {
      const res = await fetch(`/api/submissions/${submissionId}/analytics`);
      if (!res.ok) {
        alert('Không thể tải bài thi này.');
        return;
      }
      const data = await res.json();
      this.renderReport(data);
      window.scrollTo({ top: 0, behavior: 'smooth' });
    } catch (err) {
      alert('Lỗi tải bài làm: ' + err.message);
    }
  },

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

    // 2.5. Báo cáo & Nhận xét Khảo thí IRT (Item Response Theory)
    const irtData = comp.irt || {};
    const thetaVal = (irtData.theta !== undefined && irtData.theta !== null) ? ((irtData.theta > 0 ? '+' : '') + Number(irtData.theta).toFixed(2)) : '+0.00';
    const semVal = (irtData.sem !== undefined && irtData.sem !== null) ? `±${Number(irtData.sem).toFixed(2)}` : '±0.25';
    const ciLower = (irtData.ci_lower !== undefined && irtData.ci_lower !== null) ? ((irtData.ci_lower > 0 ? '+' : '') + Number(irtData.ci_lower).toFixed(2)) : '-0.50';
    const ciUpper = (irtData.ci_upper !== undefined && irtData.ci_upper !== null) ? ((irtData.ci_upper > 0 ? '+' : '') + Number(irtData.ci_upper).toFixed(2)) : '+0.50';

    const thetaEl = document.getElementById('irt-theta-value');
    if (thetaEl) thetaEl.innerText = thetaVal;
    const semEl = document.getElementById('irt-sem-value');
    if (semEl) semEl.innerText = semVal;
    const ciEl = document.getElementById('irt-ci-display');
    if (ciEl) ciEl.innerText = `Khoảng tin cậy 95%: [${ciLower}; ${ciUpper}]`;

    // Bậc nhận thức
    const cog = irtData.cognitive_stats || {};
    const pEasy = cog.nhan_biet?.percentage ?? Math.round((grade.total_score / (grade.max_total_score || 1200)) * 100);
    const pMed = cog.thong_hieu?.percentage ?? Math.round(pEasy * 0.9);
    const pHard = cog.van_dung?.percentage ?? Math.round(pEasy * 0.75);
    const pVHard = cog.van_dung_cao?.percentage ?? Math.round(pEasy * 0.6);

    const easyEl = document.getElementById('cog-p-easy');
    if (easyEl) easyEl.innerText = `${pEasy}%`;
    const medEl = document.getElementById('cog-p-med');
    if (medEl) medEl.innerText = `${pMed}%`;
    const hardEl = document.getElementById('cog-p-hard');
    if (hardEl) hardEl.innerText = `${pHard}%`;
    const vhardEl = document.getElementById('cog-p-vhard');
    if (vhardEl) vhardEl.innerText = `${pVHard}%`;

    const domEl = document.getElementById('irt-cognitive-dominant');
    if (domEl) {
      if (pVHard >= 60 || (irtData.theta && irtData.theta >= 1.5)) {
        domEl.innerText = "Vận Dụng Cao (Tư Duy Đột Phá)";
      } else if (pHard >= 60 || (irtData.theta && irtData.theta >= 0.5)) {
        domEl.innerText = "Vận Dụng (Tư Duy Độc Lập)";
      } else if (pMed >= 60) {
        domEl.innerText = "Thông Hiểu (Vững Khái Niệm)";
      } else {
        domEl.innerText = "Nhận Biết (Cần Củng Cố Nền)";
      }
    }

    const commEl = document.getElementById('report-irt-commentary');
    if (commEl) {
      if (irtData.remarks && irtData.remarks.length > 0) {
        commEl.innerHTML = irtData.remarks.map(r => `<div style="margin-bottom: 0.35rem;">${r}</div>`).join('');
      } else {
        commEl.innerHTML = `
          <div>• <strong>Chỉ số Năng lực Tiềm ẩn (θ):</strong> ${thetaVal} (SEM: ${semVal}) phản ánh khả năng giải quyết các câu hỏi khảo thí.</div>
          <div>• Thí sinh kiểm soát tốt các câu hỏi thông hiểu, cần tiếp tục rèn luyện kỹ năng phân tích đề thi phân hóa cao.</div>
        `;
      }
      if (typeof app !== 'undefined' && app.renderMath) {
        app.renderMath(commEl);
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
          <div style="display: flex; justify-content: space-between; align-items: center; padding: 0.65rem 0.85rem; border-bottom: 1px solid #f1f5f9; font-size: 0.9rem; cursor: pointer; transition: background 0.2s;" onmouseover="this.style.background='#f8fafc'" onmouseout="this.style.background='transparent'" onclick="analyticsView.loadSubmission('${h.id}')" title="Nhấp để xem lại bài làm chi tiết">
            <div>
              <strong style="color: var(--primary);">${h.exam_title}</strong> <span style="font-size:0.75rem; color:#6366f1; background:#eef2ff; padding:2px 6px; border-radius:4px;">Xem lại 🔍</span>
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

  // -------------------------------------------------------------
  // SAO CHÉP BÁO CÁO ĐIỂM (CHO PHÉP COPY VÀO PHẦN MỀM KHÁC / ZALO / EXCEL)
  // -------------------------------------------------------------
  copyReportText() {
    if (!this.submissionData) {
      alert("Chưa có dữ liệu bài thi để sao chép!");
      return;
    }

    const grade = this.submissionData.grade_report || {};
    const comp = this.submissionData.competency_analysis || {};
    const irt = comp.irt || {};
    const isSpt = grade.is_spt;
    const examTitle = this.submissionData.exam_title || (isSpt ? "BÀI THI SPT ĐH SƯ PHẠM HÀ NỘI" : "BÀI THI ĐÁNH GIÁ NĂNG LỰC (V-ACT ĐHQG-HCM)");
    const maxScore = grade.max_total_score || (isSpt ? 10.0 : 1200);

    const thetaVal = (irt.theta !== undefined && irt.theta !== null) ? ((irt.theta > 0 ? '+' : '') + Number(irt.theta).toFixed(2)) : 'N/A';
    const semVal = (irt.sem !== undefined && irt.sem !== null) ? `±${Number(irt.sem).toFixed(2)}` : 'N/A';

    let reportLines = [
      "==================================================",
      `     PHIẾU KẾT QUẢ KHẢO THÍ ĐÁNH GIÁ NĂNG LỰC     `,
      "==================================================",
      `Họ và tên thí sinh : ${this.submissionData.candidate_name || "Thí sinh khảo thí"}`,
      `Kỳ thi / Đề thi    : ${examTitle}`,
      `Thời gian nộp bài  : ${this.submissionData.submitted_at || new Date().toLocaleString("vi-VN")}`,
      `--------------------------------------------------`,
      `TỔNG ĐIỂM ĐẠT ĐƯỢC : ${grade.total_score} / ${maxScore} điểm`,
      `Xếp loại năng lực  : ${comp.tier_rating || "Đạt chuẩn"}`,
      `Thứ hạng phân vị   : Top ${100 - (comp.estimated_percentile || 50)}% toàn quốc (Phân vị: ${comp.estimated_percentile || 50}%)`,
      `Chỉ số IRT Theta   : ${thetaVal} (Sai số chuẩn SEM: ${semVal})`
    ];

    if (!isSpt) {
      reportLines.push(
        `--------------------------------------------------`,
        `ĐIỂM CÁC PHẦN THI (CHUẨN ĐHQG-HCM 1200Đ):`,
        `• Phần 1 (Ngôn ngữ)           : ${grade.sec1_score} / 400đ`,
        `• Phần 2 (Toán & Số liệu)     : ${grade.sec2_score} / 300đ`,
        `• Phần 3 (Giải quyết vấn đề)  : ${grade.sec3_score} / 500đ`
      );
    } else {
      reportLines.push(
        `--------------------------------------------------`,
        `ĐIỂM CÁC PHẦN THI (CHUẨN ĐH SƯ PHẠM HÀ NỘI 10.0Đ):`,
        `• Phần 1 (Trắc nghiệm khách quan) : ${grade.sec1_score} đ`,
        `• Phần 2 (Đúng / Sai đa mệnh đề) : ${grade.sec2_score} đ`,
        `• Phần 3 (Điền đáp số ngắn)       : ${grade.sec3_score} đ`,
        (grade.sec4_score && grade.sec4_score > 0) ? `• Phần 4 (Tự luận & Luận điểm)    : ${grade.sec4_score} đ` : ''
      );
    }

    if (irt.cognitive_stats) {
      const cog = irt.cognitive_stats;
      reportLines.push(
        `--------------------------------------------------`,
        `HIỆU SUẤT THEO 4 BẬC NHẬN THỨC GDPT 2018:`,
        `• Nhận biết     : ${cog.nhan_biet?.percentage ?? 0}%`,
        `• Thông hiểu    : ${cog.thong_hieu?.percentage ?? 0}%`,
        `• Vận dụng      : ${cog.van_dung?.percentage ?? 0}%`,
        `• Vận dụng cao  : ${cog.van_dung_cao?.percentage ?? 0}%`
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

    const fullText = reportLines.filter(Boolean).join("\n");

    if (navigator.clipboard && navigator.clipboard.writeText) {
      navigator.clipboard.writeText(fullText).then(() => {
        alert("✅ ĐÃ SAO CHÉP THÀNH CÔNG BẢNG ĐIỂM!\n\nBạn có thể dán (Ctrl + V) vào Zalo, Word, Excel, Google Docs hoặc gửi cho Thầy/Cô xem ngay.");
      }).catch(() => {
        this.fallbackCopyText(fullText, "bảng điểm");
      });
    } else {
      this.fallbackCopyText(fullText, "bảng điểm");
    }
  },

  // -------------------------------------------------------------
  // SAO CHÉP DỮ LIỆU ĐIỂM NĂNG LỰC DẠNG JSON ĐỂ DÁN VÀO PHẦN MỀM KHÁC
  // -------------------------------------------------------------
  copyJSON() {
    if (!this.submissionData) {
      alert("Chưa có dữ liệu bài thi để sao chép!");
      return;
    }

    const payload = this.buildExportPayload();
    const jsonStr = JSON.stringify(payload, null, 2);

    if (navigator.clipboard && navigator.clipboard.writeText) {
      navigator.clipboard.writeText(jsonStr).then(() => {
        alert("✅ ĐÃ SAO CHÉP DỮ LIỆU NĂNG LỰC (JSON) VÀO CLIPBOARD!\n\nBạn có thể dán (Ctrl + V) trực tiếp vào Python, R, SPSS, Google Colab hoặc hệ thống phân tích khác.");
      }).catch(() => {
        this.fallbackCopyText(jsonStr, "dữ liệu JSON năng lực");
      });
    } else {
      this.fallbackCopyText(jsonStr, "dữ liệu JSON năng lực");
    }
  },

  // -------------------------------------------------------------
  // XUẤT FILE JSON CHỨA TRỌN VẸN CHỈ SỐ IRT & NĂNG LỰC
  // -------------------------------------------------------------
  exportJSON() {
    if (!this.submissionData) {
      alert("Chưa có dữ liệu bài thi để xuất file!");
      return;
    }

    const payload = this.buildExportPayload();
    const jsonStr = JSON.stringify(payload, null, 2);
    const blob = new Blob([jsonStr], { type: "application/json;charset=utf-8;" });
    const url = URL.createObjectURL(blob);
    const link = document.createElement("a");
    const candClean = (this.submissionData.candidate_name || "ThiSinh").replace(/[^a-zA-Z0-9_\u00C0-\u024F\u1EA0-\u1EF9]/g, "_");
    const dateStr = new Date().toISOString().slice(0, 10);
    link.setAttribute("href", url);
    link.setAttribute("download", `Ho_So_Nang_Luc_IRT_${candClean}_${dateStr}.json`);
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
  },

  buildExportPayload() {
    const s = this.submissionData || {};
    const grade = s.grade_report || {};
    const comp = s.competency_analysis || {};
    const irt = comp.irt || {};

    return {
      version: "DGNL_IRT_v2.0",
      export_timestamp: new Date().toISOString(),
      candidate_info: {
        candidate_name: s.candidate_name || "Thí sinh khảo thí",
        submission_id: s.submission_id || "",
        exam_id: s.exam_id || "",
        exam_title: s.exam_title || "",
        submitted_at: s.submitted_at || "",
        time_spent_seconds: s.time_spent_seconds || 0
      },
      assessment_scores: {
        total_score: grade.total_score || 0,
        max_total_score: grade.max_total_score || (grade.is_spt ? 10.0 : 1200.0),
        is_spt: Boolean(grade.is_spt),
        sec1_score: grade.sec1_score || 0,
        sec2_score: grade.sec2_score || 0,
        sec3_score: grade.sec3_score || 0,
        sec4_score: grade.sec4_score || 0,
        correct_count: grade.correct_count || 0,
        total_questions: grade.total_questions || 0,
        tier_rating: comp.tier_rating || "Đạt chuẩn",
        estimated_percentile: comp.estimated_percentile || 50.0
      },
      irt_parameters: {
        theta: irt.theta ?? 0.0,
        sem: irt.sem ?? 0.25,
        ci_lower_95: irt.ci_lower ?? -0.5,
        ci_upper_95: irt.ci_upper ?? 0.5,
        model: irt.model || "2PL / 3PL Item Response Theory",
        cognitive_levels: irt.cognitive_stats || {},
        pedagogical_remarks: irt.remarks || []
      },
      domain_competencies: grade.domain_stats || {},
      item_responses: (grade.detailed_results || []).map(r => ({
        question_number: r.question_number,
        domain: r.domain,
        section_id: r.section_id,
        question_type: r.question_type,
        difficulty: r.difficulty,
        user_answer: r.user_answer,
        correct_answer: r.correct_answer,
        is_correct: r.is_correct,
        is_partial: r.is_partial,
        points: r.points,
        earned_points: r.earned_points
      })),
      ai_advice: s.ai_advice || ""
    };
  },

  fallbackCopyText(text, label = "dữ liệu") {
    const ta = document.createElement("textarea");
    ta.value = text;
    document.body.appendChild(ta);
    ta.select();
    try {
      document.execCommand("copy");
      alert(`✅ ĐÃ SAO CHÉP ${label.toUpperCase()} VÀO BỘ NHỚ TẠM!\n\nBạn có thể dán (Ctrl + V) vào phần mềm khác.`);
    } catch (e) {
      prompt(`Sao chép thủ công ${label} dưới đây (Ctrl + C):`, text);
    }
    document.body.removeChild(ta);
  },

  cleanLatexForExport(raw) {
    if (!raw) return '';
    let str = String(raw);

    // Xóa sạch các thẻ tag mã đề thừa
    str = str.replace(/\s*\((?:Mã đề|Đề số)\s*#?\d+\)/gi, '')
             .replace(/\s*\[(?:Biến thể|Đề số|Mã đề)\s*#?\d+\]/gi, '');

    // 1. Phân số: \frac{a}{b} -> a/b
    str = str.replace(/\\frac\s*\{([^{}]+)\}\s*\{([^{}]+)\}/g, '$1/$2');

    // 2. Căn bậc hai / bậc n
    str = str.replace(/\\sqrt\s*\{([^{}]+)\}/g, '√($1)');
    str = str.replace(/\\sqrt\s*\[([^\]]+)\]\s*\{([^{}]+)\}/g, '$1√($2)');

    // 3. Vectơ, góc, ký hiệu hình học
    str = str.replace(/\\vec\s*\{([^{}]+)\}/g, 'vectơ $1');
    str = str.replace(/\\overrightarrow\s*\{([^{}]+)\}/g, 'vectơ $1');
    str = str.replace(/\\angle\s*([a-zA-Z0-9]+)/g, 'góc $1');
    str = str.replace(/\\hat\s*\{([^{}]+)\}/g, 'góc $1');

    // 4. Các thẻ text trong math: \text{...}, \mathrm{...}
    str = str.replace(/\\(?:text|mathrm|mathbf|mathit|textsf)\s*\{([^{}]+)\}/g, '$1');

    // 5. Thay thế ký tự Hy Lạp và ký hiệu toán học phổ biến sang Unicode chuẩn
    const symbolMap = {
      '\\approx': '≈',
      '\\le': '≤',
      '\\leq': '≤',
      '\\ge': '≥',
      '\\geq': '≥',
      '\\ne': '≠',
      '\\neq': '≠',
      '\\pm': '±',
      '\\times': '×',
      '\\cdot': '·',
      '\\div': '÷',
      '\\infty': '∞',
      '\\in': '∈',
      '\\notin': '∉',
      '\\subset': '⊂',
      '\\supset': '⊃',
      '\\cup': '∪',
      '\\cap': '∩',
      '\\emptyset': '∅',
      '\\forall': '∀',
      '\\exists': '∃',
      '\\perp': '⊥',
      '\\parallel': '∥',
      '\\Delta': 'Δ',
      '\\delta': 'δ',
      '\\alpha': 'α',
      '\\beta': 'β',
      '\\gamma': 'γ',
      '\\pi': 'π',
      '\\theta': 'θ',
      '\\sigma': 'σ',
      '\\lambda': 'λ',
      '\\omega': 'ω',
      '\\Omega': 'Ω',
      '\\mu': 'μ',
      '\\phi': 'φ',
      '\\Phi': 'Φ',
      '\\rightarrow': '→',
      '\\leftarrow': '←',
      '\\Rightarrow': '⇒',
      '\\Leftrightarrow': '⇔',
      '\\degree': '°',
      '^{\\circ}': '°',
      '^\\circ': '°'
    };

    for (const [tex, uni] of Object.entries(symbolMap)) {
      str = str.split(tex).join(uni);
    }

    // 6. Số mũ và chỉ số dưới Unicode
    str = str.replace(/\^2\b|\^\{2\}/g, '²')
             .replace(/\^3\b|\^\{3\}/g, '³')
             .replace(/\^4\b|\^\{4\}/g, '⁴')
             .replace(/\^0\b|\^\{0\}/g, '⁰')
             .replace(/\^1\b|\^\{1\}/g, '¹')
             .replace(/\^(-?\d+)/g, '^($1)')
             .replace(/\^\{([^}]+)\}/g, '^($1)')
             .replace(/_\{([^}]+)\}/g, '($1)');

    // 7. Xóa các dấu bọc math $ và $$
    str = str.replace(/\$\$|\$/g, '');

    // 8. Dọn dẹp lệnh thừa LaTeX
    str = str.replace(/\\left|\\right|\\,|\\;|\\!/g, ' ');

    return str.replace(/\s+/g, ' ').trim();
  },

  // -------------------------------------------------------------
  // XUẤT FILE BẢNG ĐIỂM EXCEL / CSV (KHỬ SẠCH MÃ LATEX SANG UNICODE)
  // -------------------------------------------------------------
  exportCSV() {
    if (!this.submissionData) {
      alert("Chưa có dữ liệu bài thi để xuất file!");
      return;
    }

    const s = this.submissionData;
    const grade = s.grade_report || {};
    const comp = s.competency_analysis || {};
    const irt = comp.irt || {};
    const results = grade.detailed_results || [];

    // Header UTF-8 BOM để Excel hiển thị đúng tiếng Việt có dấu
    let csvContent = "\uFEFF";

    // PHẦN 1: TÓM TẮT HỒ SƠ NĂNG LỰC (METADATA & IRT PARAMETERS)
    csvContent += "=== BÁO CÁO ĐÁNH GIÁ NĂNG LỰC VÀ KHẢO THÍ IRT ===\n";
    csvContent += `Thí sinh,${JSON.stringify(s.candidate_name || "Thí sinh")}\n`;
    csvContent += `Đề thi,${JSON.stringify(s.exam_title || "Bài thi ĐGNL")}\n`;
    csvContent += `Thời gian nộp bài,${JSON.stringify(s.submitted_at || new Date().toLocaleString("vi-VN"))}\n`;
    csvContent += `Thời gian làm bài,${Math.round((s.time_spent_seconds || 0) / 60)} phút\n`;
    csvContent += `Tổng điểm đạt được,${grade.total_score || 0} / ${grade.max_total_score || (grade.is_spt ? 10.0 : 1200.0)}\n`;
    csvContent += `Xếp loại năng lực,${JSON.stringify(comp.tier_rating || "Đạt chuẩn")}\n`;
    csvContent += `Phân vị toàn quốc (Percentile),${comp.estimated_percentile || 50.0}%\n`;
    csvContent += `Chỉ số năng lực tiềm ẩn IRT Theta (θ),${irt.theta ?? 0.0}\n`;
    csvContent += `Sai số đo lường chuẩn SEM,${irt.sem ?? 0.25}\n`;
    csvContent += `Khoảng tin cậy 95% IRT,"[${irt.ci_lower ?? -0.5}; ${irt.ci_upper ?? 0.5}]"\n`;
    if (irt.cognitive_stats) {
      const cog = irt.cognitive_stats;
      csvContent += `Nhận biết (%),${cog.nhan_biet?.percentage ?? 0}%\n`;
      csvContent += `Thông hiểu (%),${cog.thong_hieu?.percentage ?? 0}%\n`;
      csvContent += `Vận dụng (%),${cog.van_dung?.percentage ?? 0}%\n`;
      csvContent += `Vận dụng cao (%),${cog.van_dung_cao?.percentage ?? 0}%\n`;
    }
    csvContent += "\n";

    // PHẦN 2: CHI TIẾT TỪNG CÂU HỎI
    csvContent += "=== BẢNG CHI TIẾT PHẢN HỒI TỪNG CÂU HỎI (ITEM RESPONSES) ===\n";
    csvContent += "Câu số,Miền năng lực,Dạng câu hỏi,Độ khó,Đáp án bạn chọn,Đáp án chính xác,Kết quả,Điểm đạt được,Điểm tối đa,Lời giải chi tiết\n";

    results.forEach(r => {
      const qNum = r.question_number || "";
      const domain = `"${(r.domain || "").replace(/"/g, '""')}"`;
      const qType = `"${(r.question_type || "").replace(/"/g, '""')}"`;
      const diff = `"${(r.difficulty || "medium").replace(/"/g, '""')}"`;
      
      let uAns = r.user_answer;
      if (typeof uAns === "object" && uAns !== null) {
        uAns = JSON.stringify(uAns);
      }
      uAns = this.cleanLatexForExport(String(uAns || ""));
      uAns = `"${uAns.replace(/"/g, '""')}"`;

      let cAns = r.correct_answer;
      if (typeof cAns === "object" && cAns !== null) {
        cAns = JSON.stringify(cAns);
      }
      cAns = this.cleanLatexForExport(String(cAns || ""));
      cAns = `"${cAns.replace(/"/g, '""')}"`;

      const resultText = r.is_correct ? "Đúng" : (r.is_partial ? "Đúng một phần" : "Sai");
      const earned = r.earned_points || 0;
      const pts = r.points || 0;
      
      let explClean = this.cleanLatexForExport(r.explanation || "");
      const expl = `"${explClean.replace(/"/g, '""')}"`;

      csvContent += `${qNum},${domain},${qType},${diff},${uAns},${cAns},${resultText},${earned},${pts},${expl}\n`;
    });

    const blob = new Blob([csvContent], { type: "text/csv;charset=utf-8;" });
    const url = URL.createObjectURL(blob);
    const link = document.createElement("a");
    const candClean = (s.candidate_name || "ThiSinh").replace(/[^a-zA-Z0-9_\u00C0-\u024F\u1EA0-\u1EF9]/g, "_");
    const dateStr = new Date().toISOString().slice(0, 10);
    link.setAttribute("href", url);
    link.setAttribute("download", `Bang_Diem_Nang_Luc_DGNL_${candClean}_${dateStr}.csv`);
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
  },

  // -------------------------------------------------------------
  // XUẤT FILE BÁO CÁO KẾT QUẢ WORD (.DOC) CHUẨN ĐỒ HỌA KHÔNG MÃ LATEX
  // -------------------------------------------------------------
  exportWord() {
    if (!this.submissionData) {
      alert("Chưa có dữ liệu bài thi để xuất file Word!");
      return;
    }

    const s = this.submissionData;
    const grade = s.grade_report || {};
    const comp = s.competency_analysis || {};
    const irt = comp.irt || {};
    const results = grade.detailed_results || [];
    const isSpt = Boolean(grade.is_spt);

    const candName = s.candidate_name || "Thí sinh";
    const examTitle = s.exam_title || "Bài thi Đánh giá Năng lực";
    const submittedAt = s.submitted_at || new Date().toLocaleString("vi-VN");
    const timeMins = Math.round((s.time_spent_seconds || 0) / 60);
    const totalScore = grade.total_score || 0;
    const maxScore = grade.max_total_score || (isSpt ? 10.0 : 1200.0);
    const percentage = Math.round((totalScore / maxScore) * 100);
    const tier = comp.tier_rating || "Đạt chuẩn khảo thí";
    const percentile = comp.estimated_percentile || 50.0;
    const theta = (irt.theta ?? 0.0).toFixed(2);
    const sem = (irt.sem ?? 0.25).toFixed(2);
    const advice = this.cleanLatexForExport(s.ai_advice || comp.ai_advice || "Tiếp tục phát huy các phần thế mạnh và rà soát các câu hỏi lý thuyết chuyên sâu.");

    // Xây dựng các hàng bảng chi tiết câu hỏi
    const tableRows = results.map(r => {
      const qNum = r.question_number || "";
      const domain = this.cleanLatexForExport(r.domain || "");
      const diff = r.difficulty || "Thông hiểu";
      
      let uAns = r.user_answer;
      if (typeof uAns === 'object' && uAns !== null) uAns = JSON.stringify(uAns);
      uAns = this.cleanLatexForExport(String(uAns || 'Chưa trả lời'));

      let cAns = r.correct_answer;
      if (typeof cAns === 'object' && cAns !== null) cAns = JSON.stringify(cAns);
      cAns = this.cleanLatexForExport(String(cAns || ''));

      const status = r.is_correct ? '<span style="color:#16a34a; font-weight:bold;">Đúng</span>' : (r.is_partial ? '<span style="color:#d97706; font-weight:bold;">Đúng 1 phần</span>' : '<span style="color:#dc2626; font-weight:bold;">Sai</span>');
      const earned = r.earned_points || 0;
      const pts = r.points || 0;
      const expl = this.cleanLatexForExport(r.explanation || 'Không có giải thích.');

      return `
        <tr>
          <td style="text-align:center; font-weight:bold; padding:6px; border:1px solid #cbd5e1;">${qNum}</td>
          <td style="padding:6px; border:1px solid #cbd5e1;">${domain}</td>
          <td style="text-align:center; padding:6px; border:1px solid #cbd5e1;">${diff}</td>
          <td style="padding:6px; border:1px solid #cbd5e1; word-break:break-word;">${uAns}</td>
          <td style="padding:6px; border:1px solid #cbd5e1; word-break:break-word; font-weight:600;">${cAns}</td>
          <td style="text-align:center; padding:6px; border:1px solid #cbd5e1;">${status}<br><small>${earned}/${pts}đ</small></td>
          <td style="padding:6px; border:1px solid #cbd5e1; font-size:11pt; color:#334155;">${expl}</td>
        </tr>
      `;
    }).join('');

    const wordHtml = `
      <html xmlns:o='urn:schemas-microsoft-com:office:office' xmlns:w='urn:schemas-microsoft-com:office:word' xmlns='http://www.w3.org/TR/REC-html40'>
      <head>
        <meta charset='utf-8'>
        <title>${examTitle} - Báo Cáo Kết Quả</title>
        <style>
          body {
            font-family: 'Times New Roman', Times, serif;
            font-size: 12pt;
            line-height: 1.4;
            color: #0f172a;
            margin: 20mm;
          }
          h1, h2, h3, h4 { color: #1e3a8a; }
          .header-table { width: 100%; border-collapse: collapse; margin-bottom: 20px; }
          .header-table td { vertical-align: top; border: none; }
          .box-summary {
            background-color: #f8fafc;
            border: 1.5pt solid #2563eb;
            padding: 12pt;
            margin-bottom: 18pt;
          }
          .detail-table {
            width: 100%;
            border-collapse: collapse;
            margin-top: 10pt;
          }
          .detail-table th {
            background-color: #1e40af;
            color: #ffffff;
            font-weight: bold;
            padding: 8px;
            border: 1px solid #1e3a8a;
            text-align: center;
          }
          .advice-box {
            background-color: #eff6ff;
            border-left: 4pt solid #3b82f6;
            padding: 10pt;
            margin-top: 15pt;
          }
        </style>
      </head>
      <body>
        <table class="header-table">
          <tr>
            <td style="text-align: center; width: 45%;">
              <strong>${isSpt ? 'TRƯỜNG ĐẠI HỌC SƯ PHẠM HÀ NỘI' : 'ĐẠI HỌC QUỐC GIA TP. HỒ CHÍ MINH'}</strong><br>
              <strong>HỆ THỐNG KHẢO THÍ ĐÁNH GIÁ NĂNG LỰC</strong><br>
              -----------------------
            </td>
            <td style="text-align: center; width: 55%;">
              <strong>CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM</strong><br>
              <strong>Độc lập - Tự do - Hạnh phúc</strong><br>
              -----------------------
            </td>
          </tr>
        </table>

        <div style="text-align: center; margin: 15pt 0;">
          <h2 style="margin: 0; color: #1e3a8a; font-size: 16pt;">PHIẾU BÁO ĐIỂM & HỒ SƠ ĐÁNH GIÁ NĂNG LỰC</h2>
          <p style="margin: 4pt 0; font-style: italic; color: #475569;">Áp dụng Mô hình Trắc lượng học Khảo thí IRT (Item Response Theory)</p>
        </div>

        <div class="box-summary">
          <table style="width: 100%; border-collapse: collapse; border: none;">
            <tr>
              <td style="width: 50%; padding: 4px; border:none;"><strong>Họ và tên thí sinh:</strong> ${candName}</td>
              <td style="width: 50%; padding: 4px; border:none;"><strong>Tổng điểm đạt được:</strong> <span style="font-size: 14pt; color: #dc2626; font-weight: bold;">${totalScore} / ${maxScore}</span> (${percentage}%)</td>
            </tr>
            <tr>
              <td style="padding: 4px; border:none;"><strong>Tên đề thi:</strong> ${examTitle}</td>
              <td style="padding: 4px; border:none;"><strong>Xếp loại năng lực:</strong> <strong style="color: #2563eb;">${tier}</strong></td>
            </tr>
            <tr>
              <td style="padding: 4px; border:none;"><strong>Thời gian nộp bài:</strong> ${submittedAt}</td>
              <td style="padding: 4px; border:none;"><strong>Phân vị ước lượng (Percentile):</strong> Top ${percentile}% toàn quốc</td>
            </tr>
            <tr>
              <td style="padding: 4px; border:none;"><strong>Thời gian làm bài:</strong> ${timeMins} phút</td>
              <td style="padding: 4px; border:none;"><strong>Năng lực tiềm ẩn IRT (&theta;):</strong> ${theta} (Sai số đo SEM: &plusmn;${sem})</td>
            </tr>
          </table>
        </div>

        <div class="advice-box">
          <strong style="color: #1d4ed8; font-size: 13pt;">💡 Đánh giá chuyên môn & Lời khuyên từ Cố vấn AI:</strong>
          <p style="margin: 6pt 0 0 0; line-height: 1.45; text-align: justify;">${advice}</p>
        </div>

        <h3 style="margin-top: 20pt; border-bottom: 1.5pt solid #cbd5e1; padding-bottom: 4pt;">BẢNG ĐIỂM CHI TIẾT TỪNG CÂU HỎI (ĐÃ CHUYỂN ĐỔI CHUẨN KHOA HỌC)</h3>
        <table class="detail-table">
          <thead>
            <tr>
              <th style="width: 5%;">Câu</th>
              <th style="width: 14%;">Phần / Môn</th>
              <th style="width: 11%;">Cấp độ</th>
              <th style="width: 15%;">Bài làm thí sinh</th>
              <th style="width: 15%;">Đáp án chuẩn</th>
              <th style="width: 10%;">Kết quả</th>
              <th style="width: 30%;">Lời giải chi tiết</th>
            </tr>
          </thead>
          <tbody>
            ${tableRows}
          </tbody>
        </table>

        <div style="margin-top: 25pt; display: flex; justify-content: space-between; text-align: center;">
          <table style="width: 100%; border: none; margin-top: 20pt;">
            <tr>
              <td style="width: 50%; text-align: center; border: none;">
                <strong>THÍ SINH XÁC NHẬN</strong><br>
                <em>(Ký và ghi rõ họ tên)</em><br><br><br><br>
                <strong>${candName}</strong>
              </td>
              <td style="width: 50%; text-align: center; border: none;">
                <em>Ngày ..... tháng ..... năm 202...</em><br>
                <strong>CHỦ TỊCH HỘI ĐỒNG KHẢO THÍ</strong><br>
                <em>(Ký, đóng dấu xác nhận)</em><br><br><br><br>
                <strong>HỘI ĐỒNG AI & IRT PLATFORM</strong>
              </td>
            </tr>
          </table>
        </div>
      </body>
      </html>
    `;

    const blob = new Blob(['\ufeff', wordHtml], { type: 'application/msword;charset=utf-8' });
    const url = URL.createObjectURL(blob);
    const link = document.createElement("a");
    const candClean = (s.candidate_name || "ThiSinh").replace(/[^a-zA-Z0-9_\u00C0-\u024F\u1EA0-\u1EF9]/g, "_");
    const dateStr = new Date().toISOString().slice(0, 10);
    link.setAttribute("href", url);
    link.setAttribute("download", `Bao_Cao_Nang_Luc_DGNL_${candClean}_${dateStr}.doc`);
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
  }
};

window.analyticsView = analyticsView;
