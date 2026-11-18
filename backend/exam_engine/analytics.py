import io
import base64
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from typing import Dict, Any

def generate_radar_chart_base64(domain_stats: Dict[str, Any]) -> str:
    """
    Sử dụng matplotlib để vẽ Radar Chart (Biểu đồ mạng nhện) 10 cánh năng lực
    và trả về chuỗi ảnh dạng Base64 PNG.
    """
    labels = []
    values = []
    
    # Thứ tự chuẩn 10 năng lực
    order = [
        "vietnamese", "english", "math", "logic", "data_analysis",
        "chemistry", "physics", "biology", "history", "geography"
    ]
    
    for key in order:
        stat = domain_stats.get(key, {})
        labels.append(stat.get("name", key))
        values.append(stat.get("percentage", 0.0))
        
    num_vars = len(labels)
    # Tính góc cho từng trục
    angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
    # Khép kín đa giác
    values_closed = values + [values[0]]
    angles_closed = angles + [angles[0]]

    fig, ax = plt.subplots(figsize=(7, 7), subplot_kw=dict(polar=True), facecolor='#ffffff')
    
    # Thiết lập góc bắt đầu từ đỉnh (12h) và theo chiều kim đồng hồ
    ax.set_theta_offset(np.pi / 2)
    ax.set_theta_direction(-1)

    # Đặt nhãn cho các trục
    plt.xticks(angles, labels, color='#1e293b', size=10, weight='bold')

    # Trục y từ 0 đến 100%
    ax.set_rlabel_position(0)
    plt.yticks([25, 50, 75, 100], ["25%", "50%", "75%", "100%"], color="#64748b", size=8)
    plt.ylim(0, 100)

    # Vẽ đường polygon năng lực học sinh
    ax.plot(angles_closed, values_closed, color='#4f46e5', linewidth=2.5, linestyle='solid')
    ax.fill(angles_closed, values_closed, color='#6366f1', alpha=0.35)

    # Điểm mốc chuẩn trung bình (Benchmark 60%)
    benchmark = [60.0] * num_vars
    benchmark_closed = benchmark + [benchmark[0]]
    ax.plot(angles_closed, benchmark_closed, color='#94a3b8', linewidth=1.2, linestyle='dashed', label='Mức chuẩn TB (60%)')

    plt.legend(loc='upper right', bbox_to_anchor=(1.25, 1.1), fontsize=9)
    plt.title("Biểu Đồ Radar Đánh Giá 10 Miền Năng Lực", size=13, weight='bold', color='#0f172a', pad=20)
    plt.tight_layout()

    buf = io.BytesIO()
    plt.savefig(buf, format='png', dpi=120, bbox_inches='tight')
    plt.close(fig)
    buf.seek(0)
    img_b64 = base64.b64encode(buf.read()).decode('utf-8')
    return f"data:image/png;base64,{img_b64}"


def calculate_competency_insights(domain_stats: Dict[str, Any], total_score: float) -> Dict[str, Any]:
    """
    Phân tích ma trận điểm mạnh, điểm yếu và ước tính phân vị ĐGNL.
    """
    records = [
        {
            "key": k,
            "name": v["name"],
            "percentage": v["percentage"],
            "score": v["score"],
            "max_score": v["max_score"],
            "correct": v["correct"],
            "total": v["total"]
        }
        for k, v in domain_stats.items()
    ]

    if not records:
        return {"strong_areas": [], "weak_areas": [], "percentile": 50.0}

    # Sắp xếp theo phần trăm đạt được giảm dần
    sorted_records = sorted(records, key=lambda x: x["percentage"], reverse=True)
    
    strong_areas = [r for r in sorted_records if r["percentage"] >= 70.0]
    weak_areas = [r for r in sorted_records if r["percentage"] < 50.0]
    moderate_areas = [r for r in sorted_records if 50.0 <= r["percentage"] < 70.0]

    # Ước tính phân vị (Percentile) dựa trên phân phối phổ điểm ĐGNL ĐHQG (phân phối chuẩn quanh kỳ vọng 650, lệch chuẩn 140)
    import math
    # Mean = 650, Std = 135
    z = (total_score - 650) / 135.0
    percentile = round(float(0.5 * (1.0 + math.erf(z / math.sqrt(2.0))) * 100), 1)
    percentile = min(99.9, max(1.0, percentile))

    # Đánh giá xếp loại năng lực
    if total_score >= 950:
        tier = "Xuất sắc (Top 3% - Đủ điều kiện cạnh tranh các ngành hot nhất Y Đa khoa, KHMT ĐHQG)"
        color = "#10b981"
    elif total_score >= 800:
        tier = "Giỏi (Top 15% - Rất có lợi thế xét tuyển ĐH Bách Khoa, Kinh Tế Luật, KHTN)"
        color = "#3b82f6"
    elif total_score >= 650:
        tier = "Khá (Trên mức trung bình - Khả năng đỗ cao các trường khối ĐHQG)"
        color = "#f59e0b"
    else:
        tier = "Cần tăng cường rèn luyện (Dưới mức trung bình kỳ thi ĐGNL)"
        color = "#ef4444"

    return {
        "strong_areas": strong_areas,
        "weak_areas": weak_areas,
        "moderate_areas": moderate_areas,
        "estimated_percentile": percentile,
        "tier_rating": tier,
        "tier_color": color
    }
