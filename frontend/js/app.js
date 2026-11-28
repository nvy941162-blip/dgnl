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
    if (typeof mistakesNotebook !== 'undefined' && mistakesNotebook.updateBadge) {
      mistakesNotebook.updateBadge();
    }
  },

  setupEventListeners() {
    // Check if there is an active exam saved in localStorage
    examRunner.checkRestoreSession();

    // Click outside to close any open dropdowns
    document.addEventListener('click', (e) => {
      const examDd = document.getElementById('nav-exam-dropdown');
      if (examDd && !examDd.contains(e.target)) {
        examDd.classList.remove('open');
      }
      const genDd = document.getElementById('nav-generator-dropdown');
      if (genDd && !genDd.contains(e.target)) {
        genDd.classList.remove('open');
      }
    });
  },

  toggleExamDropdown(e) {
    if (e) {
      e.preventDefault();
      e.stopPropagation();
    }
    const genDd = document.getElementById('nav-generator-dropdown');
    if (genDd) genDd.classList.remove('open');

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

  toggleGeneratorDropdown(e) {
    if (e) {
      e.preventDefault();
      e.stopPropagation();
    }
    const examDd = document.getElementById('nav-exam-dropdown');
    if (examDd) examDd.classList.remove('open');

    const dd = document.getElementById('nav-generator-dropdown');
    if (dd) {
      dd.classList.toggle('open');
    }
  },

  closeGeneratorDropdown() {
    const dd = document.getElementById('nav-generator-dropdown');
    if (dd) {
      dd.classList.remove('open');
    }
  },

  closeAllDropdowns() {
    this.closeExamDropdown();
    this.closeGeneratorDropdown();
  },

  openGeneratorWithMode(mode) {
    this.closeAllDropdowns();
    this.showTab('generator');

    const modeKey = mode || 'vact_full';
    const modeInput = document.getElementById('full-exam-mode-input');
    if (modeInput) modeInput.value = modeKey;

    // Reset sạch sẽ trạng thái & Cache của Studio tạo đề
    const readyBanner = document.getElementById('full-exam-ready-banner');
    if (readyBanner) readyBanner.style.display = 'none';

    const progressBox = document.getElementById('full-exam-progress-box');
    if (progressBox) progressBox.style.display = 'none';

    if (typeof generatorStudio !== 'undefined') {
      generatorStudio.currentMode = modeKey;
      generatorStudio.isGenerating120 = false;
      if (generatorStudio.pollTimer) {
        clearInterval(generatorStudio.pollTimer);
        generatorStudio.pollTimer = null;
      }
      if (typeof generatorStudio.updateRecentUI === 'function') {
        generatorStudio.updateRecentUI();
      }
      if (modeKey === 'vact_full' && typeof generatorStudio.loadNextExamTitle === 'function') {
        generatorStudio.loadNextExamTitle();
      }
    }

    const titleInput = document.getElementById('full-exam-title-input');
    const themeInput = document.getElementById('full-exam-theme-input');
    const statusText = document.getElementById('full-exam-status-text');
    const startBtn = document.getElementById('btn-start-full-120');
    const badge = document.getElementById('generator-exam-badge');
    const heroTitle = document.getElementById('generator-hero-title');
    const heroDesc = document.getElementById('generator-hero-desc');

    const modeConfigs = {
      vact_full: {
        badge: "120 Câu - 150 Phút - 1200đ",
        btnText: "⚡ Bắt Đầu Tạo Đề 120 Câu Bằng AI",
        heroTitle: "🚀 TẠO ĐỀ THI ĐGNL HOÀN CHỈNH 120 CÂU (V-ACT)",
        heroDesc: "Tự động sinh trọn vẹn 120 câu hỏi (Ngôn ngữ 40c, Logic/Số liệu 30c, Giải quyết vấn đề 50c), tính trọng số IRT 1200 điểm.",
        title: "Đề Thi ĐGNL Số 02 - Luyện Thi Bứt Phá Điểm Số",
        theme: "Khoa học, Xã hội, Biến đổi khí hậu & Đổi mới kinh tế",
        desc: "🎯 Đã chọn: Tạo Đề ĐGNL Hoàn Chỉnh 120 Câu (Chuẩn ĐHQG-HCM 1200 điểm IRT)"
      },
      spt_math: {
        badge: "25 Câu - 90 Phút - Thang 10.0đ",
        btnText: "⚡ Bắt Đầu Tạo Đề Toán Học (25 Câu)",
        heroTitle: "📐 TẠO ĐỀ THI THỬ SPT - MÔN TOÁN HỌC",
        heroDesc: "Sinh trọn vẹn 25 câu hỏi môn Toán học theo 4 phần: Trắc nghiệm (16c), Đúng/Sai (2c 8 ý), Điền đáp số (4c), Tự luận (3c) - Thang điểm 10.0.",
        title: "Đề Thi Thử SPT ĐH Sư Phạm Hà Nội - Môn Toán",
        theme: "Đại số, Giải tích, Hình học không gian, Lượng giác & Xác suất",
        desc: "📐 Đã chọn: Sinh đề thi thử SPT Môn Toán học (25 câu - 90 phút - Thang 10.0)"
      },
      spt_english: {
        badge: "33 Câu - 60 Phút - Thang 10.0đ",
        btnText: "⚡ Bắt Đầu Tạo Đề Tiếng Anh (33 Câu)",
        heroTitle: "🇬🇧 TẠO ĐỀ THI THỬ SPT - MÔN TIẾNG ANH",
        heroDesc: "Sinh trọn vẹn 33 câu hỏi môn Tiếng Anh: Use of English (18c), Reading (10c), Word Formation (4c), Writing (1c) - Thang điểm 10.0.",
        title: "Đề Thi Thử SPT ĐH Sư Phạm Hà Nội - Môn Tiếng Anh",
        theme: "English Lexico-Grammar, Reading Comprehension & Writing",
        desc: "🇬🇧 Đã chọn: Sinh đề thi thử SPT Môn Tiếng Anh (33 câu - 60 phút - Thang 10.0)"
      },
      spt_chemistry: {
        badge: "27 Câu - 60 Phút - Thang 10.0đ",
        btnText: "⚡ Bắt Đầu Tạo Đề Hóa Học (27 Câu)",
        heroTitle: "🧪 TẠO ĐỀ THI THỬ SPT - MÔN HÓA HỌC",
        heroDesc: "Sinh trọn vẹn 27 câu hỏi môn Hóa học: Trắc nghiệm (20c), Đúng/Sai (2c 8 ý), Điền kết quả (4c), Tự luận (1c) - Thang điểm 10.0.",
        title: "Đề Thi Thử SPT ĐH Sư Phạm Hà Nội - Môn Hóa Học",
        theme: "Hóa học hữu cơ, Vô cơ, Tốc độ phản ứng, Cân bằng hóa học & Thực nghiệm",
        desc: "🧪 Đã chọn: Sinh đề thi thử SPT Môn Hóa học (27 câu - 60 phút - Thang 10.0)"
      },
      spt_geography: {
        badge: "20 Câu - 60 Phút - Thang 10.0đ",
        btnText: "⚡ Bắt Đầu Tạo Đề Địa Lí (20 Câu)",
        heroTitle: "🌍 TẠO ĐỀ THI THỬ SPT - MÔN ĐỊA LÍ",
        heroDesc: "Sinh trọn vẹn 20 câu hỏi môn Địa lí: Trắc nghiệm (12c), Đúng/Sai (3c 12 ý), Điền đáp số (4c), Tự luận (1c) - Thang điểm 10.0.",
        title: "Đề Thi Thử SPT ĐH Sư Phạm Hà Nội - Môn Địa Lí",
        theme: "Địa lí tự nhiên, Dân cư, Các vùng kinh tế trọng điểm & Biến đổi khí hậu",
        desc: "🌍 Đã chọn: Sinh đề thi thử SPT Môn Địa lí (20 câu - 60 phút - Thang 10.0)"
      },
      spt_history: {
        badge: "25 Câu - 60 Phút - Thang 10.0đ",
        btnText: "⚡ Bắt Đầu Tạo Đề Lịch Sử (25 Câu)",
        heroTitle: "📜 TẠO ĐỀ THI THỬ SPT - MÔN LỊCH SỬ",
        heroDesc: "Sinh trọn vẹn 25 câu hỏi môn Lịch sử: Trắc nghiệm (20c), Đúng/Sai (2c 8 ý), Tự luận (3c) - Thang điểm 10.0.",
        title: "Đề Thi Thử SPT ĐH Sư Phạm Hà Nội - Môn Lịch Sử",
        theme: "Lịch sử Việt Nam hiện đại, Cách mạng giải phóng dân tộc & Hội nhập quốc tế",
        desc: "📜 Đã chọn: Sinh đề thi thử SPT Môn Lịch sử (25 câu - 60 phút - Thang 10.0)"
      },
      spt_civics: {
        badge: "21 Câu - 60 Phút - Thang 10.0đ",
        btnText: "⚡ Bắt Đầu Tạo Đề GDKT&PL (21 Câu)",
        heroTitle: "⚖️ TẠO ĐỀ THI THỬ SPT - MÔN GDKT & PHÁP LUẬT",
        heroDesc: "Sinh trọn vẹn 21 câu hỏi môn GDKT&PL: Trắc nghiệm (16c), Đúng/Sai (3c 12 ý), Tự luận (2c) - Thang điểm 10.0.",
        title: "Đề Thi Thử SPT ĐH Sư Phạm Hà Nội - Môn GDKT&PL",
        theme: "Kinh tế thị trường, Pháp luật dân sự, Quyền bình đẳng & Trách nhiệm công dân",
        desc: "⚖️ Đã chọn: Sinh đề thi thử SPT Môn GDKT & Pháp luật (21 câu - 60 phút - Thang 10.0)"
      },
      spt_tech_ind: {
        badge: "24 Câu - 60 Phút - Thang 10.0đ",
        btnText: "⚡ Bắt Đầu Tạo Đề Công Nghệ CN (24 Câu)",
        heroTitle: "⚙️ TẠO ĐỀ THI THỬ SPT - CÔNG NGHỆ CÔNG NGHIỆP",
        heroDesc: "Sinh trọn vẹn 24 câu hỏi môn Công nghệ CN: Trắc nghiệm (16c), Đúng/Sai (2c 8 ý), Điền kết quả (4c), Tự luận (2c) - Thang điểm 10.0.",
        title: "Đề Thi Thử SPT ĐH Sư Phạm Hà Nội - Môn Công Nghệ Công Nghiệp",
        theme: "Cơ khí chế tạo, Bản vẽ kỹ thuật, Mạch điện tử & Công nghệ tự động hóa",
        desc: "⚙️ Đã chọn: Sinh đề thi thử SPT Môn Công nghệ Công nghiệp (24 câu - 60 phút - Thang 10.0)"
      },
      spt_tech_agr: {
        badge: "24 Câu - 60 Phút - Thang 10.0đ",
        btnText: "⚡ Bắt Đầu Tạo Đề Công Nghệ NN (24 Câu)",
        heroTitle: "🌾 TẠO ĐỀ THI THỬ SPT - CÔNG NGHỆ NÔNG NGHIỆP",
        heroDesc: "Sinh trọn vẹn 24 câu hỏi môn Công nghệ NN: Trắc nghiệm (16c), Đúng/Sai (2c 8 ý), Điền kết quả (4c), Tự luận (2c) - Thang điểm 10.0.",
        title: "Đề Thi Thử SPT ĐH Sư Phạm Hà Nội - Môn Công Nghệ Nông Nghiệp",
        theme: "Nông nghiệp công nghệ cao, Lâm nghiệp sinh thái & Thủy sản bền vững",
        desc: "🌾 Đã chọn: Sinh đề thi thử SPT Môn Công nghệ Nông nghiệp (24 câu - 60 phút - Thang 10.0)"
      }
    };

    const cfg = modeConfigs[mode] || modeConfigs.vact_full;
    if (cfg.title && titleInput) titleInput.value = cfg.title;
    if (cfg.theme && themeInput) themeInput.value = cfg.theme;
    if (statusText) statusText.innerText = cfg.desc;
    if (startBtn) {
      startBtn.disabled = false;
      if (cfg.btnText) startBtn.innerHTML = cfg.btnText;
    }
    if (badge && cfg.badge) badge.innerText = cfg.badge;
    if (heroTitle && cfg.heroTitle) heroTitle.innerText = cfg.heroTitle;
    if (heroDesc && cfg.heroDesc) heroDesc.innerText = cfg.heroDesc;

    const notif = document.getElementById('generator-mode-notification');
    if (notif) {
      notif.style.display = 'block';
      notif.innerHTML = `${cfg.desc} • Sẵn sàng tạo đề!`;
      notif.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
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

    // Tách chuỗi theo các khối đã có dấu $ (ví dụ $$...$$ hoặc $...$)
    // để không can thiệp làm hỏng các công thức đã bọc chuẩn
    const tokens = str.split(/(\$\$[\s\S]*?\$\$|\$[^\$\n]+?\$)/g);
    
    // Pattern tìm các công thức LaTeX trần chưa được bọc dấu $
    // Bao gồm: số + \text{...}, \frac, \sqrt, \int, \log, \vec, \lim, \sum, \text{...}, ký hiệu hy lạp, quan hệ toán học
    const nakedPattern = /(\b\d+(?:[.,]\d+)?\s*\\text\{[^{}]+\}(?:\^[^{}\s]+)?|\b[a-zA-Z]\s*=\s*\\(?:frac|sqrt|int|log|vec|lim|sum)\b[^\$\n]+|\\(?:frac\{[^{}]+\}\{[^{}]+\}|sqrt\{[^{}]+\}|int_\{?[^{}\s]+\}?^\{?[^{}\s]+\}?|log_\{?[^{}\s]+\}?\([^{}]+\)|text\{[^{}]+\}(?:\^[^{}\s]+)?|(?:alpha|beta|gamma|delta|Delta|lambda|Lambda|mu|pi|rho|sigma|omega|Omega|infty|approx|ne|le|ge|pm|times|cdot|perp|parallel|angle)\b))/g;

    const parts = tokens.map(token => {
      if (!token) return '';
      // Nếu đã nằm trong $...$ hoặc $$...$$, giữ nguyên 100%
      if (token.startsWith('$') && token.endsWith('$')) {
        return token;
      }
      // Chỉ bọc $ cho các biểu thức LaTeX trần nằm bên ngoài
      return token.replace(nakedPattern, (match) => `$${match}$`);
    });

    return parts.join('').replace(/\n/g, '<br>');
  },

  showTab(tabName) {
    const tabs = ['dashboard', 'exam', 'generator', 'analytics', 'settings', 'admin'];
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
    } else if (tabName === 'admin') {
      if (typeof adminManager !== 'undefined') {
        if (adminManager.loadUsers) adminManager.loadUsers();
        if (adminManager.loadLeaderboard) adminManager.loadLeaderboard();
      }
    } else if (tabName === 'generator') {
      if (typeof generatorStudio !== 'undefined' && generatorStudio.loadNextExamTitle) {
        generatorStudio.loadNextExamTitle();
      }
    } else if (tabName === 'analytics') {
      if (typeof analyticsView !== 'undefined' && analyticsView.loadLatest) {
        analyticsView.loadLatest();
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
          <div style="display: flex; gap: 0.5rem; align-items: center; flex-wrap: wrap;">
            <a href="/api/exams/${e.id}/print" target="_blank" class="btn btn-outline" style="text-decoration: none; padding: 0.55rem 0.85rem; font-size: 0.85rem; font-weight: 600;" title="Mở bản in A4 và đáp án chuẩn khảo thí">
              🖨️ In Đề
            </a>
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

// Mistake Notebook Controller (Sổ Tay Bẫy Điểm & Luyện Tập Câu Sai)
const mistakesNotebook = {
  openModal() {
    const modal = document.getElementById('mistakes-modal');
    if (modal) {
      modal.style.display = 'flex';
      this.render();
    }
  },
  closeModal() {
    const modal = document.getElementById('mistakes-modal');
    if (modal) modal.style.display = 'none';
  },
  getStorageKey() {
    const user = (window.authManager && window.authManager.currentUser) ? window.authManager.currentUser.username : 'default';
    return `dgnl_mistakes_notebook_${user}`;
  },
  getItems() {
    try {
      return JSON.parse(localStorage.getItem(this.getStorageKey()) || '[]');
    } catch {
      return [];
    }
  },
  render() {
    const items = this.getItems();
    const container = document.getElementById('mistakes-list-container');
    const label = document.getElementById('mistakes-total-label');
    if (label) label.innerText = `Đang có ${items.length} câu hỏi cần khắc phục bẫy điểm`;
    this.updateBadge();

    if (!container) return;
    if (items.length === 0) {
      container.innerHTML = '<p style="color: var(--text-muted); text-align: center; padding: 2rem;">Chưa có câu sai nào trong sổ tay. Hãy làm bài thi thử để hệ thống tự động ghi nhận nhé!</p>';
      return;
    }

    container.innerHTML = items.map((m, idx) => {
      const qPayload = encodeURIComponent(JSON.stringify({
        prompt: m.prompt,
        user_answer: m.user_answer,
        correct_answer: m.correct_answer,
        explanation: m.explanation,
        question_type: m.question_type || 'multiple_choice'
      }));

      return `
        <div style="background: #ffffff; border: 1px solid #e2e8f0; border-radius: 0.6rem; padding: 1rem; margin-bottom: 1rem; box-shadow: 0 1px 3px rgba(0,0,0,0.05);">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.5rem; flex-wrap: wrap; gap: 0.5rem;">
            <div>
              <span class="badge badge-primary" style="font-size: 0.75rem;">${m.domain || 'Tổng hợp'}</span>
              <strong style="margin-left: 0.5rem; color: #1e293b;">Câu ${idx + 1} (${m.exam_title || 'Đề thi'})</strong>
            </div>
            <div style="display: flex; gap: 0.4rem; align-items: center;">
              <button class="btn btn-primary btn-sm" onclick="analyticsView.askAITutor('${qPayload}')" style="font-size: 0.8rem; padding: 0.3rem 0.6rem;">
                🤖 Hỏi Gia Sư AI
              </button>
              <button class="btn btn-outline btn-sm" onclick="mistakesNotebook.deleteItem('${m.id}')" style="font-size: 0.8rem; padding: 0.3rem 0.6rem; color: #dc2626; border-color: #fecaca;">
                🗑️ Xóa
              </button>
            </div>
          </div>
          <div style="font-size: 0.95rem; line-height: 1.5; margin-bottom: 0.75rem; color: #334155;">
            ${m.prompt}
          </div>
          <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 0.75rem; background: #f8fafc; padding: 0.65rem 0.85rem; border-radius: 0.4rem; font-size: 0.85rem; margin-bottom: 0.5rem;">
            <div><span style="color: #dc2626; font-weight: 700;">❌ Bạn đã chọn:</span> ${typeof m.user_answer === 'object' ? JSON.stringify(m.user_answer) : m.user_answer}</div>
            <div><span style="color: #16a34a; font-weight: 700;">✅ Đáp án đúng:</span> ${typeof m.correct_answer === 'object' ? JSON.stringify(m.correct_answer) : m.correct_answer}</div>
          </div>
          ${m.explanation ? `
            <div style="font-size: 0.85rem; color: #475569; background: #fffbeb; border-left: 3px solid #f59e0b; padding: 0.5rem 0.75rem; border-radius: 0.2rem;">
              <strong>💡 Phân tích & Lời giải:</strong> ${m.explanation}
            </div>
          ` : ''}
        </div>
      `;
    }).join('');

    app.renderMath(container);
  },
  deleteItem(id) {
    let items = this.getItems().filter(m => m.id !== id);
    localStorage.setItem(this.getStorageKey(), JSON.stringify(items));
    this.render();
  },
  clearAll() {
    if (!confirm("Bạn có chắc chắn muốn xóa toàn bộ câu hỏi trong Sổ tay câu sai không?")) return;
    localStorage.removeItem(this.getStorageKey());
    this.render();
  },
  startDrill() {
    const items = this.getItems();
    if (items.length === 0) {
      alert("Sổ tay chưa có câu sai nào để luyện tập!");
      return;
    }
    this.closeModal();
    // Lấy tối đa 10 câu
    const drillSet = items.slice(0, 10);
    examRunner.startCustomMistakePractice(drillSet);
  },
  updateBadge() {
    const items = this.getItems();
    const badge = document.getElementById('mistakes-count-badge');
    if (badge) {
      if (items.length > 0) {
        badge.innerText = items.length;
        badge.style.display = 'inline-block';
      } else {
        badge.style.display = 'none';
      }
    }
  }
};

// Authentication & Student Profile Manager Module
const authManager = {
  currentUser: null,

  init() {
    // KHÔNG TỰ ĐỘNG ĐĂNG NHẬP: Bắt buộc người dùng phải chọn tài khoản hoặc đăng nhập mỗi phiên
    sessionStorage.removeItem('dgnl_current_student');
    this.currentUser = null;

    // Kiểm tra xem trong phiên làm việc hiện tại (sessionStorage) có đăng nhập chưa
    const sessionSaved = sessionStorage.getItem('dgnl_current_session_user');
    if (sessionSaved) {
      try {
        this.currentUser = JSON.parse(sessionSaved);
      } catch (e) {
        this.currentUser = null;
      }
    }

    this.updateUI();

    // MỖI KHI MỞ TRANG WEB: BẮT BUỘC BẬT FORM ĐĂNG NHẬP NGAY LẬP TỨC
    if (!this.currentUser) {
      this.openModal(true);
    }
  },

  getCurrentUser() {
    return this.currentUser;
  },

  isAdmin() {
    if (!this.currentUser) {
      try {
        const raw = sessionStorage.getItem('dgnl_current_session_user') || localStorage.getItem('dgnl_current_student');
        if (raw) this.currentUser = JSON.parse(raw);
      } catch (e) {}
    }
    return Boolean(this.currentUser && (
      this.currentUser.role === 'admin' ||
      this.currentUser.username === 'admin' ||
      (this.currentUser.full_name && this.currentUser.full_name.toLowerCase().includes('admin')) ||
      (this.currentUser.student_class && this.currentUser.student_class.toLowerCase().includes('quản trị'))
    ));
  },

  updateUI() {
    const label = document.getElementById('nav-user-label');
    const logoutBtn = document.getElementById('btn-logout-user');
    const authBtn = document.getElementById('btn-open-auth-modal');
    const adminNavBtn = document.getElementById('btn-tab-admin');
    const closeBtn = document.getElementById('auth-modal-close-btn');

    if (this.currentUser) {
      if (closeBtn) closeBtn.style.display = 'inline-block';
      const roleBadge = this.isAdmin() ? '🛡️ Admin' : (this.currentUser.student_class || 'HS');
      if (label) label.innerText = `${this.currentUser.full_name} (${roleBadge})`;
      if (logoutBtn) logoutBtn.style.display = 'inline-block';
      if (authBtn) {
        if (this.isAdmin()) {
          authBtn.style.background = '#fef3c7';
          authBtn.style.borderColor = '#f59e0b';
          authBtn.style.color = '#b45309';
          authBtn.title = `Tài khoản Quản trị: ${this.currentUser.username}`;
        } else {
          authBtn.style.background = '#e0f2fe';
          authBtn.style.borderColor = '#0284c7';
          authBtn.style.color = '#0369a1';
          authBtn.title = `Học sinh: ${this.currentUser.username} - Nhấn để đổi hoặc xem hồ sơ`;
        }
      }

      // Hiển thị nút Tab Quản trị nếu là Admin
      if (adminNavBtn) {
        adminNavBtn.style.display = this.isAdmin() ? 'inline-block' : 'none';
      }

      // Ẩn Menu "Sinh Đề Mới" đối với Học Sinh, CHỈ ADMIN MỚI ĐƯỢC TẠO ĐỀ MỚI
      const genDropdown = document.getElementById('nav-generator-dropdown');
      if (genDropdown) {
        genDropdown.style.display = this.isAdmin() ? 'inline-block' : 'none';
      }
    } else {
      if (closeBtn) closeBtn.style.display = 'none'; // Bắt buộc phải đăng nhập
      if (label) label.innerText = 'Đăng Nhập Khảo Thí';
      if (logoutBtn) logoutBtn.style.display = 'none';
      if (adminNavBtn) adminNavBtn.style.display = 'none';
      const genDropdown = document.getElementById('nav-generator-dropdown');
      if (genDropdown) genDropdown.style.display = 'none';
      if (authBtn) {
        authBtn.style.background = '#ffffff';
        authBtn.style.borderColor = 'var(--primary)';
        authBtn.style.color = 'var(--primary)';
        authBtn.title = 'Đăng nhập vào hệ thống';
      }
    }

    // Tự động làm mới lịch sử và sổ tay câu sai theo học sinh hiện tại
    if (window.analyticsApp && typeof window.analyticsApp.loadHistory === 'function') {
      window.analyticsApp.loadHistory();
    }
    if (window.mistakesNotebook && typeof window.mistakesNotebook.updateBadge === 'function') {
      window.mistakesNotebook.updateBadge();
    }
  },

  openModal(forceLogin = false) {
    const modal = document.getElementById('auth-modal');
    if (modal) {
      modal.style.display = 'flex';
      const closeBtn = document.getElementById('auth-modal-close-btn');
      if (closeBtn) {
        closeBtn.style.display = (forceLogin || !this.currentUser) ? 'none' : 'inline-block';
      }
      this.clearAlert();
      this.fetchDemoStudents();
    }
  },

  closeModal() {
    if (!this.currentUser) {
      this.showAlert("Vui lòng đăng nhập hoặc chọn 1 tài khoản để tiếp tục vào ứng dụng!", "danger");
      return;
    }
    const modal = document.getElementById('auth-modal');
    if (modal) modal.style.display = 'none';
  },

  switchAuthTab(tab) {
    const loginForm = document.getElementById('form-login');
    const regForm = document.getElementById('form-register');
    const btnLogin = document.getElementById('auth-tab-btn-login');
    const btnReg = document.getElementById('auth-tab-btn-register');
    this.clearAlert();

    if (tab === 'login') {
      if (loginForm) loginForm.style.display = 'block';
      if (regForm) regForm.style.display = 'none';
      if (btnLogin) {
        btnLogin.style.borderBottomColor = 'var(--primary)';
        btnLogin.style.color = 'var(--primary)';
        btnLogin.style.background = '#ffffff';
      }
      if (btnReg) {
        btnReg.style.borderBottomColor = 'transparent';
        btnReg.style.color = '#64748b';
        btnReg.style.background = '#f8fafc';
      }
    } else {
      if (loginForm) loginForm.style.display = 'none';
      if (regForm) regForm.style.display = 'block';
      if (btnReg) {
        btnReg.style.borderBottomColor = 'var(--primary)';
        btnReg.style.color = 'var(--primary)';
        btnReg.style.background = '#ffffff';
      }
      if (btnLogin) {
        btnLogin.style.borderBottomColor = 'transparent';
        btnLogin.style.color = '#64748b';
        btnLogin.style.background = '#f8fafc';
      }
    }
  },

  async handleLogin(event) {
    event.preventDefault();
    const uname = document.getElementById('login-username').value.trim();
    const pass = document.getElementById('login-password').value.trim();

    try {
      const res = await fetch('/api/auth/login', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ username: uname, password: pass })
      });
      const data = await res.json();
      if (!res.ok) {
        this.showAlert(data.detail || "Đăng nhập thất bại!", "danger");
        return;
      }

      this.currentUser = data.user;
      sessionStorage.setItem('dgnl_current_session_user', JSON.stringify(this.currentUser));
      this.showAlert(`Xin chào ${this.currentUser.full_name}! Đăng nhập thành công.`, "success");
      this.updateUI();

      if (this.isAdmin()) {
        setTimeout(() => {
          this.closeModal();
          app.showTab('admin');
          adminManager.loadUsers();
        }, 600);
      } else {
        setTimeout(() => {
          this.closeModal();
        }, 600);
      }
    } catch (err) {
      this.showAlert(`Lỗi kết nối máy chủ: ${err.message}`, "danger");
    }
  },

  async handleRegister(event) {
    event.preventDefault();
    const fullname = document.getElementById('reg-fullname').value.trim();
    const sclass = document.getElementById('reg-class').value.trim();
    const school = document.getElementById('reg-school').value.trim();
    const uname = document.getElementById('reg-username').value.trim();
    const pass = document.getElementById('reg-password').value.trim();

    try {
      const res = await fetch('/api/auth/register', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          full_name: fullname,
          student_class: sclass,
          school: school,
          username: uname,
          password: pass
        })
      });
      const data = await res.json();
      if (!res.ok) {
        this.showAlert(data.detail || "Đăng ký thất bại!", "danger");
        return;
      }

      this.currentUser = data.user;
      sessionStorage.setItem('dgnl_current_session_user', JSON.stringify(this.currentUser));
      this.showAlert(`Đã tạo tài khoản cho ${this.currentUser.full_name}!`, "success");
      this.updateUI();
      setTimeout(() => {
        this.closeModal();
      }, 700);
    } catch (err) {
      this.showAlert(`Lỗi kết nối máy chủ: ${err.message}`, "danger");
    }
  },

  async fetchDemoStudents() {
    try {
      const res = await fetch('/api/auth/students');
      const data = await res.json();
      const container = document.getElementById('quick-demo-students');
      if (!container || !data.students) return;

      let html = '';
      // Nút Admin 1-Click Demo
      const isAdminSelected = this.currentUser && this.currentUser.username === 'admin';
      html += `
        <button type="button" class="btn btn-sm" style="font-size: 0.75rem; padding: 0.2rem 0.55rem; border-radius: 4px; font-weight: bold; ${isAdminSelected ? 'background: #b45309; color: white;' : 'background: #fef3c7; color: #b45309; border: 1px solid #fde68a;'}" onclick="authManager.quickSwitch('admin', 'Quản Trị Viên (Admin)', 'user_admin_root', 'Ban Giám Khảo', 'admin')">
          🛡️ Admin (Quản trị)
        </button>
      `;

      // Nút Học sinh Demo
      html += data.students.map(s => {
        const isSelected = this.currentUser && this.currentUser.username === s.username;
        return `
          <button type="button" class="btn btn-sm" style="font-size: 0.75rem; padding: 0.2rem 0.5rem; border-radius: 4px; ${isSelected ? 'background: #2563eb; color: white;' : 'background: #e2e8f0; color: #1e293b;'}" onclick="authManager.quickSwitch('${s.username}', '${s.full_name.replace(/'/g, "\\'")}', '${s.id}', '${s.student_class}', 'student')">
            ${s.full_name.split(' ').pop()} (${s.student_class})
          </button>
        `;
      }).join('');

      container.innerHTML = html;
    } catch (e) {
      console.warn("Could not load demo students", e);
    }
  },

  quickSwitch(username, fullName, id, studentClass, role = 'student') {
    this.currentUser = {
      id: id,
      username: username,
      full_name: fullName,
      student_class: studentClass || "12",
      role: role
    };
    sessionStorage.setItem('dgnl_current_session_user', JSON.stringify(this.currentUser));
    this.showAlert(`Đã chọn tài khoản: ${fullName} (${role === 'admin' ? 'Quyền Admin' : 'Học sinh'})`, "success");
    this.updateUI();

    if (this.isAdmin()) {
      setTimeout(() => {
        this.closeModal();
        app.showTab('admin');
        adminManager.loadUsers();
      }, 500);
    } else {
      setTimeout(() => {
        this.closeModal();
      }, 500);
    }
  },

  logout() {
    if (confirm(`Bạn có chắc chắn muốn đăng xuất khỏi tài khoản ${this.currentUser?.full_name || ''}?`)) {
      this.currentUser = null;
      sessionStorage.removeItem('dgnl_current_session_user');
      localStorage.removeItem('dgnl_current_student');
      this.updateUI();
      app.showTab('dashboard');
      this.openModal(true); // Mở lại form đăng nhập bắt buộc
    }
  },

  showAlert(msg, type) {
    const box = document.getElementById('auth-alert-box');
    if (!box) return;
    box.style.display = 'block';
    box.innerText = msg;
    if (type === 'success') {
      box.style.background = '#ecfdf5';
      box.style.color = '#065f46';
      box.style.border = '1px solid #a7f3d0';
    } else {
      box.style.background = '#fef2f2';
      box.style.color = '#991b1b';
      box.style.border = '1px solid #fecaca';
    }
  },

  clearAlert() {
    const box = document.getElementById('auth-alert-box');
    if (box) {
      box.style.display = 'none';
      box.innerText = '';
    }
  }
};

// Admin Management Module
const adminManager = {
  async loadUsers() {
    try {
      const res = await fetch('/api/admin/users');
      if (!res.ok) throw new Error("Không thể tải danh sách tài khoản.");
      const data = await res.json();
      const users = data.users || [];

      const countBadge = document.getElementById('admin-user-count');
      if (countBadge) countBadge.innerText = `${users.length} tài khoản`;

      const tbody = document.getElementById('admin-users-table-body');
      if (!tbody) return;

      if (users.length === 0) {
        tbody.innerHTML = '<tr><td colspan="7" style="text-align: center; padding: 2rem; color: #94a3b8;">Chưa có tài khoản học sinh nào.</td></tr>';
        return;
      }

      tbody.innerHTML = users.map(u => {
        const isAdmin = (u.role === 'admin' || u.username === 'admin');
        const roleTag = isAdmin ? '<span class="badge" style="background: #fef3c7; color: #b45309; border: 1px solid #fde68a;">Quản trị viên</span>' : '<span class="badge" style="background: #e0f2fe; color: #0369a1;">Học sinh</span>';
        
        const actionBtns = isAdmin ? '<span style="color: #94a3b8; font-style: italic;">Mặc định</span>' : `
          <div style="display: flex; gap: 0.35rem; justify-content: center;">
            <button class="btn btn-outline btn-sm" onclick="adminManager.resetPassword('${u.id}', '${u.full_name}')" style="font-size: 0.75rem; padding: 0.2rem 0.5rem;" title="Đặt lại mật khẩu">
              🔑 Đổi Pass
            </button>
            <button class="btn btn-outline btn-sm" onclick="adminManager.deleteUser('${u.id}', '${u.full_name}')" style="font-size: 0.75rem; padding: 0.2rem 0.5rem; color: #dc2626; border-color: #fca5a5;" title="Xóa tài khoản này">
              🗑️ Xóa
            </button>
          </div>
        `;

        return `
          <tr style="border-bottom: 1px solid #f1f5f9;">
            <td style="padding: 0.75rem 0.5rem;">
              <strong>${u.username}</strong>
              <div style="margin-top: 2px;">${roleTag}</div>
            </td>
            <td style="padding: 0.75rem 0.5rem; font-weight: 600; color: #1e293b;">${u.full_name}</td>
            <td style="padding: 0.75rem 0.5rem; color: #64748b;">${u.student_class} - ${u.school}</td>
            <td style="padding: 0.75rem 0.5rem; text-align: center; font-weight: bold; color: var(--primary);">${u.exam_count || 0}</td>
            <td style="padding: 0.75rem 0.5rem; text-align: center; font-weight: bold; color: ${u.avg_percentage >= 50 ? '#16a34a' : '#d97706'};">${u.avg_percentage || 0}%</td>
            <td style="padding: 0.75rem 0.5rem; font-size: 0.8rem; color: #64748b;">${u.latest_submission || 'Chưa thi'}</td>
            <td style="padding: 0.75rem 0.5rem; text-align: center;">${actionBtns}</td>
          </tr>
        `;
      }).join('');

    } catch (err) {
      alert("Lỗi tải bảng Admin: " + err.message);
    }
  },

  async deleteUser(userId, fullName) {
    if (!confirm(`Bạn có chắc chắn muốn XÓA học sinh '${fullName}' và toàn bộ lịch sử thi cử liên quan không?`)) return;
    try {
      const res = await fetch(`/api/admin/users/${userId}`, { method: 'DELETE' });
      const data = await res.json();
      if (!res.ok) throw new Error(data.detail || "Không thể xóa học sinh.");
      alert(data.message);
      this.loadUsers();
      authManager.fetchDemoStudents();
    } catch (err) {
      alert("Lỗi xóa học sinh: " + err.message);
    }
  },

  async resetPassword(userId, fullName) {
    const newPass = prompt(`Nhập mật khẩu mới cho học sinh '${fullName}':`, "123456");
    if (!newPass) return;
    try {
      const res = await fetch(`/api/admin/users/${userId}/reset-password`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ new_pass: newPass })
      });
      const data = await res.json();
      if (!res.ok) throw new Error(data.detail || "Không thể đổi mật khẩu.");
      alert(data.message);
    } catch (err) {
      alert("Lỗi đổi mật khẩu: " + err.message);
    }
  },

  async loadLeaderboard() {
    try {
      const res = await fetch('/api/admin/leaderboard');
      if (!res.ok) throw new Error("Không thể tải bảng xếp hạng.");
      const data = await res.json();
      const list = data.leaderboard || [];

      const tbody = document.getElementById('admin-leaderboard-table-body');
      if (!tbody) return;

      if (list.length === 0) {
        tbody.innerHTML = '<tr><td colspan="8" style="text-align: center; padding: 2rem; color: #94a3b8;">Chưa có bài thi nào được nộp trong hệ thống.</td></tr>';
        return;
      }

      this.cachedLeaderboard = list;

      tbody.innerHTML = list.map((r, idx) => {
        let rankBadge = `<span style="font-weight: 700; color: #64748b;">#${idx + 1}</span>`;
        if (idx === 0) rankBadge = `<span class="badge" style="background: #fef08a; color: #854d0e; font-size: 0.85rem;">🥇 Top 1</span>`;
        else if (idx === 1) rankBadge = `<span class="badge" style="background: #e2e8f0; color: #334155; font-size: 0.85rem;">🥈 Top 2</span>`;
        else if (idx === 2) rankBadge = `<span class="badge" style="background: #fed7aa; color: #9a3412; font-size: 0.85rem;">🥉 Top 3</span>`;

        return `
          <tr style="border-bottom: 1px solid #f1f5f9;">
            <td style="padding: 0.75rem 0.5rem; text-align: center;">${rankBadge}</td>
            <td style="padding: 0.75rem 0.5rem;">
              <strong style="color: #1e293b;">${r.candidate_name}</strong>
              <div style="font-size: 0.8rem; color: #64748b;">@${r.username}</div>
            </td>
            <td style="padding: 0.75rem 0.5rem; color: #475569;">${r.student_class} - ${r.school}</td>
            <td style="padding: 0.75rem 0.5rem; color: var(--primary); font-weight: 600;">${r.exam_title}</td>
            <td style="padding: 0.75rem 0.5rem; text-align: center; font-weight: bold; color: var(--success); font-size: 1rem;">
              ${r.total_score} / ${r.max_score}đ
            </td>
            <td style="padding: 0.75rem 0.5rem; text-align: center;">
              <span class="badge ${r.percentage >= 80 ? 'badge-success' : (r.percentage >= 50 ? 'badge-primary' : 'badge-warning')}">
                ${r.percentage}%
              </span>
            </td>
            <td style="padding: 0.75rem 0.5rem; text-align: center; color: #64748b;">${Math.round(r.time_spent_seconds / 60)} phút</td>
            <td style="padding: 0.75rem 0.5rem; font-size: 0.8rem; color: #64748b;">${r.submitted_at}</td>
            <td style="padding: 0.75rem 0.5rem; text-align: center;">
              <button class="btn btn-outline btn-sm" onclick="adminManager.deleteSubmission('${r.id}', '${r.candidate_name}')" style="font-size: 0.75rem; padding: 0.2rem 0.5rem; color: #dc2626; border-color: #fca5a5;" title="Xóa kết quả bài thi này">
                🗑️ Xóa Bài
              </button>
            </td>
          </tr>
        `;
      }).join('');

    } catch (err) {
      console.warn("Lỗi tải Leaderboard: " + err.message);
    }
  },

  async deleteSubmission(subId, candidateName) {
    if (!confirm(`Bạn có chắc chắn muốn XÓA bài thi của thí sinh '${candidateName}' không?`)) return;
    try {
      const res = await fetch(`/api/admin/submissions/${subId}`, { method: 'DELETE' });
      const data = await res.json();
      if (!res.ok) throw new Error(data.detail || "Không thể xóa bài làm.");
      alert(data.message);
      this.loadLeaderboard();
      this.loadUsers();
    } catch (err) {
      alert("Lỗi xóa bài làm: " + err.message);
    }
  },

  async deleteAllSubmissions() {
    if (!confirm("⚠️ CẢNH BÁO QUAN TRỌNG:\n\nBạn có chắc chắn muốn XÓA TOÀN BỘ bài làm của tất cả thí sinh để làm mới kỳ thi không?\nThao tác này không thể hoàn tác!")) return;
    try {
      const res = await fetch('/api/admin/submissions', { method: 'DELETE' });
      const data = await res.json();
      if (!res.ok) throw new Error(data.detail || "Không thể xóa bài làm.");
      alert(data.message);
      this.loadLeaderboard();
      this.loadUsers();
    } catch (err) {
      alert("Lỗi xóa bài làm: " + err.message);
    }
  },

  copyLeaderboard() {
    const list = this.cachedLeaderboard || [];
    if (list.length === 0) {
      alert("Chưa có dữ liệu bảng điểm để sao chép!");
      return;
    }

    let text = "BẢNG VÀNG XẾP HẠNG ĐIỂM THI ĐÁNH GIÁ NĂNG LỰC (TỪ CAO XUỐNG THẤP)\n";
    text += "Hạng\tHọ và tên\tTài khoản\tLớp\tTrường\tĐề thi\tĐiểm số\tTỷ lệ\tThời gian\tNgày nộp\n";
    list.forEach((r, idx) => {
      text += `${idx + 1}\t${r.candidate_name}\t${r.username}\t${r.student_class}\t${r.school}\t${r.exam_title}\t${r.total_score}/${r.max_score}\t${r.percentage}%\t${Math.round(r.time_spent_seconds / 60)}p\t${r.submitted_at}\n`;
    });

    if (navigator.clipboard && navigator.clipboard.writeText) {
      navigator.clipboard.writeText(text).then(() => {
        alert("✅ ĐÃ SAO CHÉP TOÀN BỘ BẢNG ĐIỂM XẾP HẠNG!\n\nBạn có thể dán (Ctrl + V) trực tiếp vào Excel, Google Sheets, Zalo hoặc Word.");
      });
    } else {
      prompt("Sao chép thủ công bảng điểm dưới đây (Ctrl + C):", text);
    }
  },

  exportLeaderboardCSV() {
    const list = this.cachedLeaderboard || [];
    if (list.length === 0) {
      alert("Chưa có dữ liệu để xuất file Excel!");
      return;
    }

    let csvContent = "\uFEFF"; // UTF-8 BOM
    csvContent += "Thứ hạng,Họ và tên thí sinh,Tài khoản,Lớp,Trường THPT,Tên đề thi,Điểm đạt được,Điểm tối đa,Tỷ lệ phần trăm,Thời gian làm (phút),Ngày nộp bài\n";

    list.forEach((r, idx) => {
      const rank = idx + 1;
      const name = `"${(r.candidate_name || '').replace(/"/g, '""')}"`;
      const uname = `"${(r.username || '').replace(/"/g, '""')}"`;
      const sclass = `"${(r.student_class || '').replace(/"/g, '""')}"`;
      const school = `"${(r.school || '').replace(/"/g, '""')}"`;
      const examTitle = `"${(r.exam_title || '').replace(/"/g, '""')}"`;
      const timeMins = Math.round((r.time_spent_seconds || 0) / 60);
      const date = `"${r.submitted_at || ''}"`;

      csvContent += `${rank},${name},${uname},${sclass},${school},${examTitle},${r.total_score},${r.max_score},${r.percentage}%,${timeMins},${date}\n`;
    });

    const blob = new Blob([csvContent], { type: "text/csv;charset=utf-8;" });
    const url = URL.createObjectURL(blob);
    const link = document.createElement("a");
    const dateStr = new Date().toISOString().slice(0, 10);
    link.setAttribute("href", url);
    link.setAttribute("download", `Bang_Vang_Xep_Hang_DGNL_${dateStr}.csv`);
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
  }
};

window.authManager = authManager;

document.addEventListener('DOMContentLoaded', () => {
  authManager.init();
  app.init();
});
