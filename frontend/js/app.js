// Image Zoom Lightbox Viewer Module
const imageZoomViewer = {
  currentSrc: '',
  currentTitle: '',
  zoomLevel: 1.0,
  minZoom: 0.5,
  maxZoom: 4.0,
  zoomStep: 0.25,
  isDragging: false,
  startX: 0,
  startY: 0,
  translateX: 0,
  translateY: 0,

  init() {
    const viewport = document.getElementById('img-zoom-viewport');
    if (!viewport) return;

    // Con cuộn chuột (Wheel) phóng to / thu nhỏ
    viewport.addEventListener('wheel', (e) => {
      e.preventDefault();
      if (e.deltaY < 0) {
        this.zoomIn();
      } else {
        this.zoomOut();
      }
    }, { passive: false });

    // Kéo chuột di chuyển ảnh (Drag / Pan)
    viewport.addEventListener('mousedown', (e) => {
      if (e.button !== 0) return;
      this.isDragging = true;
      this.startX = e.clientX - this.translateX;
      this.startY = e.clientY - this.translateY;
      viewport.classList.add('is-dragging');
    });

    window.addEventListener('mousemove', (e) => {
      if (!this.isDragging) return;
      this.translateX = e.clientX - this.startX;
      this.translateY = e.clientY - this.startY;
      this.updateTransform();
    });

    window.addEventListener('mouseup', () => {
      if (this.isDragging) {
        this.isDragging = false;
        viewport.classList.remove('is-dragging');
      }
    });

    // Nhấp đúp chuột chuyển đổi phóng to 180% / 100%
    viewport.addEventListener('dblclick', () => {
      if (this.zoomLevel === 1.0) {
        this.zoomLevel = 1.8;
      } else {
        this.zoomLevel = 1.0;
        this.translateX = 0;
        this.translateY = 0;
      }
      this.updateTransform();
      this.updateBadge();
    });

    // Phím tắt Esc, +, -, 0
    window.addEventListener('keydown', (e) => {
      const modal = document.getElementById('image-zoom-modal');
      if (modal && modal.style.display !== 'none') {
        if (e.key === 'Escape') {
          this.close();
        } else if (e.key === '+' || e.key === '=') {
          this.zoomIn();
        } else if (e.key === '-' || e.key === '_') {
          this.zoomOut();
        } else if (e.key === '0') {
          this.resetZoom();
        }
      }
    });
  },

  open(src, caption = 'Biểu đồ minh họa câu hỏi') {
    if (!src) return;
    this.currentSrc = src;
    this.currentTitle = caption;
    this.zoomLevel = 1.0;
    this.translateX = 0;
    this.translateY = 0;

    const modal = document.getElementById('image-zoom-modal');
    const target = document.getElementById('img-zoom-target');
    const captionEl = document.getElementById('img-zoom-caption');

    if (target) target.src = src;
    if (captionEl) captionEl.innerText = caption;

    this.updateTransform();
    this.updateBadge();

    if (modal) {
      modal.style.display = 'flex';
      document.body.style.overflow = 'hidden';
    }
  },

  openCurrentChart() {
    const chartImg = document.getElementById('chart-image-display');
    if (chartImg && chartImg.src) {
      const q = examRunner?.examData?.questions?.[examRunner.currentQuestionIndex];
      const qNum = q?.question_number || (examRunner.currentQuestionIndex + 1);
      const domain = q?.domain || '';
      const domainLabel = examRunner?.getDomainLabel ? examRunner.getDomainLabel(domain) : domain;
      const caption = `Hình ảnh minh họa Câu ${qNum} [${domainLabel}]`;
      this.open(chartImg.src, caption);
    }
  },

  close() {
    const modal = document.getElementById('image-zoom-modal');
    if (modal) {
      modal.style.display = 'none';
      document.body.style.overflow = '';
    }
  },

  handleBackdropClick(e) {
    if (e.target.id === 'image-zoom-modal' || e.target.id === 'img-zoom-viewport') {
      this.close();
    }
  },

  zoomIn() {
    this.zoomLevel = Math.min(this.maxZoom, Math.round((this.zoomLevel + this.zoomStep) * 100) / 100);
    this.updateTransform();
    this.updateBadge();
  },

  zoomOut() {
    this.zoomLevel = Math.max(this.minZoom, Math.round((this.zoomLevel - this.zoomStep) * 100) / 100);
    if (this.zoomLevel <= 1.0) {
      this.translateX = 0;
      this.translateY = 0;
    }
    this.updateTransform();
    this.updateBadge();
  },

  resetZoom() {
    this.zoomLevel = 1.0;
    this.translateX = 0;
    this.translateY = 0;
    this.updateTransform();
    this.updateBadge();
  },

  updateTransform() {
    const canvas = document.getElementById('img-zoom-canvas');
    if (canvas) {
      canvas.style.transform = `translate(${this.translateX}px, ${this.translateY}px) scale(${this.zoomLevel})`;
    }
  },

  updateBadge() {
    const badge = document.getElementById('img-zoom-level-badge');
    if (badge) {
      badge.innerText = `${Math.round(this.zoomLevel * 100)}%`;
    }
  }
};

// Main Application Controller
const app = {
  currentTab: 'dashboard',
  latestSubmission: null,
  currentExamFilter: 'all',
  cachedExams: [],

  init() {
    this.setupEventListeners();
    imageZoomViewer.init();
    this.loadExams();
    if (typeof generatorStudio !== 'undefined' && generatorStudio.loadNextExamTitle) {
      generatorStudio.loadNextExamTitle();
    }
  },

  setupEventListeners() {
    // Check if there is an active exam saved in localStorage
    examRunner.checkRestoreSession();

    // Click outside to close exam dropdown
    document.addEventListener('click', (e) => {
      const dd = document.getElementById('nav-exam-dropdown');
      if (dd && !dd.contains(e.target)) {
        dd.classList.remove('open');
      }
    });
  },

  toggleExamDropdown(e) {
    if (e) {
      e.preventDefault();
      e.stopPropagation();
    }
    const dd = document.getElementById('nav-exam-dropdown');
    if (dd) {
      dd.classList.toggle('open');
    }
  },

  closeExamDropdown() {
    const dd = document.getElementById('nav-exam-dropdown');
    if (dd) {
      dd.classList.remove('open');
    }
  },

  renderMath(targetElement) {
    if (!targetElement) return;

    const doRender = () => {
      if (typeof renderMathInElement === 'function') {
        try {
          renderMathInElement(targetElement, {
            delimiters: [
              { left: '$$', right: '$$', display: true },
              { left: '$', right: '$', display: false },
              { left: '\\[', right: '\\]', display: true },
              { left: '\\(', right: '\\)', display: false }
            ],
            ignoredTags: ['script', 'noscript', 'style', 'textarea', 'pre', 'code'],
            throwOnError: false,
            errorColor: '#dc2626'
          });
        } catch (err) {
          console.warn('KaTeX render warning:', err);
        }
      } else {
        setTimeout(doRender, 150);
      }
    };

    doRender();
  },

  formatMathText(text) {
    if (!text) return '';
    let str = String(text);

    // Tách chuỗi theo các khối đã có dấu $ (ví dụ ... hoặc $...$)
    // để không can thiệp làm hỏng các công thức đã bọc chuẩn
    const tokens = str.split(/(\$\$[\s\S]*?\$\$|\$[^\$\n]+?\$)/g);
    
    // Pattern tìm các công thức LaTeX trần chưa được bọc dấu $
    const nakedPattern = /(\b[a-zA-Z]\s*=\s*\\(?:frac|sqrt|int|log|vec|lim|sum)\b[^\$\n]+|\\(?:frac\{[^{}]+\}\{[^{}]+\}|sqrt\{[^{}]+\}|int_\{?[^{}\s]+\}?^\{?[^{}\s]+\}?|log_\{?[^{}\s]+\}?\([^{}]+\)))/g;

    const parts = tokens.map(token => {
      if (!token) return '';
      // Nếu đã nằm trong $...$ hoặc ..., giữ nguyên 100%
      if (token.startsWith('$') && token.endsWith('$')) {
        return token;
      }
      // Chỉ bọc $ cho các biểu thức LaTeX trần nằm bên ngoài
      return token.replace(nakedPattern, '');
    });

    return parts.join('').replace(/\n/g, '<br>');
  },

  showTab(tabName) {
    const tabs = ['dashboard', 'exam', 'generator', 'analytics', 'settings'];
    tabs.forEach(t => {
      const el = document.getElementById(`tab-${t}`);
      const btn = document.getElementById(`btn-tab-${t}`);
      if (el) el.style.display = (t === tabName) ? 'block' : 'none';
      if (btn) {
        if (t === tabName) btn.classList.add('active');
        else btn.classList.remove('active');
      }
    });
    this.currentTab = tabName;
    window.scrollTo({ top: 0, behavior: 'smooth' });

    if (tabName === 'dashboard') {
      this.loadExams();
    } else if (tabName === 'generator') {
      if (typeof generatorStudio !== 'undefined' && generatorStudio.loadNextExamTitle) {
        generatorStudio.loadNextExamTitle();
      }
    } else if (tabName === 'settings') {
      this.loadSettingsStatus();
    }
  },

  async loadSettingsStatus() {
    const badge = document.getElementById('settings-keys-badge');
    const desc = document.getElementById('settings-keys-desc');
    const modelSelect = document.getElementById('select-gemini-model');
    try {
      const res = await fetch('/api/settings');
      const data = await res.json();
      if (badge) {
        if (data.gemini_keys_count > 0) {
          badge.innerHTML = `✅ Đang kích hoạt <strong>${data.gemini_keys_count} Gemini API Keys</strong> xoay vòng tự động!`;
          badge.style.color = 'var(--success)';
          if (desc) desc.innerText = `Mô hình: ${data.gemini_model} • Tự động round-robin & chuyển key khi gặp lỗi rate limit 429.`;
        } else {
          badge.innerText = '⚠️ Chưa nạp được Gemini API Key nào.';
          badge.style.color = 'var(--warning)';
        }
      }
      if (modelSelect && data.gemini_model) {
        modelSelect.value = data.gemini_model;
      }
    } catch (e) {
      console.error('Failed to load settings status:', e);
    }
  },

  setExamFilter(filter) {
    this.currentExamFilter = filter;
    const tabs = ['all', 'vact', 'spt', 'ai'];
    tabs.forEach(t => {
      const btn = document.getElementById(`filter-${t}`);
      if (btn) {
        if (t === filter) btn.classList.add('active');
        else btn.classList.remove('active');
      }
    });
    this.renderFilteredExams();
  },

  async loadExams() {
    const container = document.getElementById('exams-list-container');
    try {
      const res = await fetch('/api/exams');
      const exams = await res.json();
      this.cachedExams = exams || [];
      this.renderFilteredExams();
    } catch (err) {
      console.error('Failed to load exams:', err);
      if (container) {
        container.innerHTML = '<p style="color: var(--danger);">Không thể kết nối đến máy chủ để tải danh sách đề thi.</p>';
      }
    }
  },

  renderFilteredExams() {
    const container = document.getElementById('exams-list-container');
    if (!container) return;

    if (!this.cachedExams || this.cachedExams.length === 0) {
      container.innerHTML = '<p style="color: var(--text-muted); padding: 1.5rem; text-align: center;">Chưa có đề thi nào trong hệ thống.</p>';
      return;
    }

    const filter = this.currentExamFilter || 'all';
    let filtered = this.cachedExams;

    if (filter === 'vact') {
      filtered = this.cachedExams.filter(e => e.exam_type === 'vact' || (!e.exam_type && !e.id.startsWith('spt_')));
    } else if (filter === 'spt') {
      filtered = this.cachedExams.filter(e => e.exam_type === 'spt' || e.id.startsWith('spt_'));
    } else if (filter === 'ai') {
      filtered = this.cachedExams.filter(e => e.source === 'langgraph_generated');
    }

    if (filtered.length === 0) {
      container.innerHTML = '<p style="color: var(--text-muted); padding: 2rem; text-align: center;">Không có đề thi nào trong danh mục này.</p>';
      return;
    }

    const generatedExams = this.cachedExams.filter(e => e.source === 'langgraph_generated');
    let html = '';
    if (filter === 'ai' || (filter === 'all' && generatedExams.length > 0)) {
      if (generatedExams.length > 0) {
        html += `
          <div style="display: flex; justify-content: flex-end; margin-bottom: 0.75rem;">
            <button class="btn btn-outline" style="color: #dc2626; border-color: #fca5a5; font-size: 0.85rem; padding: 0.35rem 0.8rem;" onclick="app.deleteAllGeneratedExams()">
              🗑️ Xóa Tất Cả Đề AI Tạo (${generatedExams.length} đề)
            </button>
          </div>
        `;
      }
    }

    html += filtered.map(e => {
      const isGenerated = (e.source === 'langgraph_generated');
      const isSpt = (e.exam_type === 'spt' || e.id.startsWith('spt_'));
      const maxScore = e.max_score || (isSpt ? 10.0 : 1200);

      let badgeHtml = '';
      if (isSpt) {
        badgeHtml = `<span class="badge" style="background: #eef2ff; color: #4338ca; border: 1px solid #c7d2fe; font-size: 0.75rem;">🎓 SPT ĐH Sư Phạm (${maxScore}đ)</span>`;
      } else if (isGenerated) {
        badgeHtml = `<span class="badge badge-secondary" style="font-size: 0.75rem;">🤖 AI Tạo Mới (${maxScore}đ)</span>`;
      } else if (e.id === 'vact_sample_2026') {
        badgeHtml = `<span class="badge badge-primary" style="font-size: 0.75rem;">🎯 V-ACT 2026 Mới (${maxScore}đ)</span>`;
      } else {
        badgeHtml = `<span class="badge badge-primary" style="font-size: 0.75rem;">🎯 V-ACT Chuẩn Hóa (${maxScore}đ)</span>`;
      }

      const deleteBtn = isGenerated ? `
        <button class="btn btn-outline" style="color: #dc2626; border-color: #fecaca; padding: 0.55rem 0.9rem;" title="Xóa đề này" onclick="app.deleteExam('${e.id}', '${e.title.replace(/'/g, "\\'")}')">
          🗑️ Xóa
        </button>
      ` : '';

      return `
        <div style="border: 1px solid var(--border); border-radius: 0.6rem; padding: 1.25rem; margin-bottom: 1rem; display: flex; justify-content: space-between; align-items: center; background: #ffffff; transition: box-shadow 0.2s;" onmouseover="this.style.boxShadow='0 4px 12px rgba(0,0,0,0.06)'" onmouseout="this.style.boxShadow='none'">
          <div>
            <div style="display: flex; align-items: center; gap: 0.5rem; margin-bottom: 0.3rem; flex-wrap: wrap;">
              <h4 style="font-size: 1.1rem; color: var(--primary);">${e.title}</h4>
              ${badgeHtml}
            </div>
            <p style="font-size: 0.9rem; color: var(--text-muted); max-width: 700px; margin-bottom: 0.5rem;">${e.description || 'Đề thi chuẩn hóa ĐGNL.'}</p>
            <div style="display: flex; gap: 0.85rem; font-size: 0.85rem; color: #475569; flex-wrap: wrap;">
              <span>📝 <strong>${e.total_questions}</strong> câu hỏi</span>
              <span>⏱️ <strong>${e.duration_minutes}</strong> phút</span>
              <span>🎯 Thang điểm: <strong>${maxScore}</strong></span>
              ${e.subject ? `<span>📚 Môn: <strong>${e.subject}</strong></span>` : ''}
            </div>
          </div>
          <div style="display: flex; gap: 0.5rem; align-items: center;">
            <button class="btn btn-primary" onclick="examRunner.loadAndStartExam('${e.id}')">
              Vào Thi Thử
            </button>
            ${deleteBtn}
          </div>
        </div>
      `;
    }).join('');

    container.innerHTML = html;
  },

  async deleteExam(examId, title) {
    if (!confirm(`Bạn có chắc chắn muốn xóa đề thi:\n"${title}"\nkhỏi hệ thống không?`)) {
      return;
    }

    try {
      const res = await fetch(`/api/exams/${examId}`, { method: 'DELETE' });
      const data = await res.json();
      if (!res.ok) throw new Error(data.detail || 'Lỗi khi xóa đề');
      alert(data.message || 'Đã xóa đề thi thành công!');
      this.loadExams();
    } catch (e) {
      alert('Không thể xóa đề: ' + e.message);
    }
  },

  async deleteAllGeneratedExams() {
    if (!confirm('Bạn có chắc chắn muốn xóa TẤT CẢ các đề thi do AI tạo không?\n(Đề gốc chuẩn của hệ thống vẫn sẽ được giữ nguyên)')) {
      return;
    }

    try {
      const res = await fetch('/api/exams-generated', { method: 'DELETE' });
      const data = await res.json();
      if (!res.ok) throw new Error(data.detail || 'Lỗi khi xóa đề');
      alert(data.message || 'Đã xóa tất cả đề thi AI thành công!');
      this.loadExams();
    } catch (e) {
      alert('Không thể xóa đề: ' + e.message);
    }
  },

  async saveSettings() {
    const openaiKey = document.getElementById('input-openai-key')?.value.trim() || '';
    const geminiKeys = document.getElementById('input-gemini-keys')?.value.trim() || '';
    const geminiModel = document.getElementById('select-gemini-model')?.value || 'gemini-flash-lite-latest';
    const openaiModel = document.getElementById('input-openai-model')?.value.trim() || 'gpt-4o-mini';

    try {
      const res = await fetch('/api/settings', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          openai_api_key: openaiKey,
          gemini_api_keys: geminiKeys,
          gemini_model: geminiModel,
          openai_model: openaiModel
        })
      });
      const data = await res.json();
      alert(data.message || 'Đã lưu cài đặt thành công!');
      this.showTab('dashboard');
    } catch (err) {
      alert('Lỗi lưu cài đặt: ' + err.message);
    }
  }
};

document.addEventListener('DOMContentLoaded', () => {
  app.init();
});
