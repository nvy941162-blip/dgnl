// Competency Analytics & Reporting Module
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

    // 2. Subscores (400 - 300 - 500 for V-ACT)
    const subscoresBar = document.getElementById('report-subscores-bar');
    if (subscoresBar) {
      if (grade.is_spt) {
        subscoresBar.style.display = 'none';
      } else {
        subscoresBar.style.display = 'flex';
        document.getElementById('report-sec1-score').innerText = `${grade.sec1_score} / ${grade.sec1_max || 400}`;
        document.getElementById('report-sec2-score').innerText = `${grade.sec2_score} / ${grade.sec2_max || 300}`;
        document.getElementById('report-sec3-score').innerText = `${grade.sec3_score} / ${grade.sec3_max || 500}`;
      }
    }

    // 3. Radar Chart Image
    const radarImg = document.getElementById('report-radar-img');
    if (data.radar_image) {
      radarImg.src = data.radar_image;
      radarImg.style.cursor = 'zoom-in';
      radarImg.title = 'Nhấp để phóng to biểu đồ';
      radarImg.onclick = () => imageZoomViewer.open(data.radar_image, 'Biểu đồ Radar Phân Tích 10 Năng Lực');
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

    // 5. AI Study Advice
    const adviceBox = document.getElementById('report-ai-advice');
    adviceBox.innerText = data.ai_advice || 'Không có lời khuyên bổ sung.';

    // 6. Detailed 120-question review
    this.renderDetailedQuestionsTable('all');
  },

  renderDetailedQuestionsTable(filter = 'all') {
    this.currentFilter = filter;
    const container = document.getElementById('report-detailed-table-container');
    if (!this.submissionData) return;

    const results = this.submissionData.grade_report.detailed_results || [];
    let filtered = results;

    if (filter === 'correct') {
      filtered = results.filter(r => r.is_correct);
    } else if (filter === 'wrong') {
      filtered = results.filter(r => !r.is_correct && r.user_answer !== null);
    } else if (filter === 'unanswered') {
      filtered = results.filter(r => r.user_answer === null);
    }

    container.innerHTML = `
      <div style="display: flex; gap: 0.5rem; margin-bottom: 1rem;">
        <button class="btn ${filter === 'all' ? 'btn-primary' : 'btn-outline'}" onclick="analyticsView.renderDetailedQuestionsTable('all')">
          Tất Cả (${results.length})
        </button>
        <button class="btn ${filter === 'correct' ? 'btn-success' : 'btn-outline'}" onclick="analyticsView.renderDetailedQuestionsTable('correct')">
          Đúng (${results.filter(r => r.is_correct).length})
        </button>
        <button class="btn ${filter === 'wrong' ? 'btn-warning' : 'btn-outline'}" onclick="analyticsView.renderDetailedQuestionsTable('wrong')">
          Sai (${results.filter(r => !r.is_correct && r.user_answer !== null).length})
        </button>
        <button class="btn ${filter === 'unanswered' ? 'btn-primary' : 'btn-outline'}" onclick="analyticsView.renderDetailedQuestionsTable('unanswered')">
          Chưa làm (${results.filter(r => r.user_answer === null).length})
        </button>
      </div>

      <div style="display: flex; flex-direction: column; gap: 1rem;">
        ${filtered.map(r => {
          let statusBadge = '';
          if (r.is_correct) {
            statusBadge = '<span class="badge badge-success">✔️ Đúng (+ ' + r.earned_points + 'đ)</span>';
          } else if (r.user_answer === null) {
            statusBadge = '<span class="badge badge-secondary">⚪ Bỏ qua (0đ)</span>';
          } else {
            statusBadge = '<span class="badge" style="background:#fee2e2; color:#dc2626;">❌ Sai (0đ / ' + r.points + 'đ)</span>';
          }

          return `
            <div style="border: 1px solid var(--border); border-radius: 0.6rem; padding: 1.1rem; background: #ffffff;">
              <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.5rem;">
                <span style="font-weight: 700; color: var(--primary);">Câu ${r.question_number} [${r.domain}]</span>
                ${statusBadge}
              </div>
              <div style="font-size: 0.98rem; margin-bottom: 0.5rem; font-weight: 600;">${app.formatMathText(r.prompt)}</div>
              <div style="display: flex; gap: 1.5rem; font-size: 0.9rem; margin-bottom: 0.5rem;">
                <span>Bạn chọn: <strong>${r.user_answer ? app.formatMathText(r.user_answer) : 'Không chọn'}</strong></span>
                <span>Đáp án đúng: <strong style="color: var(--success);">${app.formatMathText(r.correct_answer)}</strong></span>
              </div>
              <div style="background: #f8fafc; border-left: 3px solid var(--primary); padding: 0.6rem 0.9rem; border-radius: 0 0.4rem 0.4rem 0; font-size: 0.88rem; color: #475569;">
                <strong>Giải thích:</strong> ${app.formatMathText(r.explanation || 'Không có giải thích chi tiết.')}
              </div>
            </div>
          `;
        }).join('')}
      </div>
    `;

    // Render KaTeX for review table formulas
    app.renderMath(container);
  }
};
