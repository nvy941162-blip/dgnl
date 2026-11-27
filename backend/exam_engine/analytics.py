import io
import base64
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from typing import Dict, Any

def generate_radar_chart_base64(domain_stats: Dict[str, Any], is_spt: bool = False) -> str:
    """
    Sử dụng matplotlib để vẽ Radar Chart (Biểu đồ mạng nhện) đánh giá đa chiều năng lực:
    - 10 miền năng lực cho kỳ thi V-ACT ĐHQG-HCM
    - Ma trận năng lực nhận thức & kỹ năng khảo thí chuyên sâu cho kỳ thi SPT ĐH Sư Phạm Hà Nội
    - Hoặc tự động thích ứng theo tập thuộc tính có trong domain_stats
    """
    labels = []
    values = []
    
    # Thứ tự chuẩn 10 năng lực V-ACT
    vact_order = [
        "vietnamese", "english", "math", "logic", "data_analysis",
        "chemistry", "physics", "biology", "history", "geography"
    ]
    
    # Kiểm tra xem domain_stats có chứa các key V-ACT hay không
    has_vact_keys = any(k in domain_stats for k in vact_order)
    
    if not is_spt and has_vact_keys:
        chart_title = "Biểu Đồ Radar Đánh Giá 10 Miền Năng Lực (V-ACT)"
        for key in vact_order:
            stat = domain_stats.get(key, {})
            labels.append(stat.get("name", key))
            values.append(stat.get("percentage", 0.0))
    else:
        chart_title = "Biểu Đồ Radar Đánh Giá Năng Lực Khảo Thí Môn Học (SPT)"
        for key, stat in domain_stats.items():
            name = stat.get("name", key)
            # Rút gọn tên nếu quá dài cho trục radar
            clean_name = name.split("(")[0].strip() if "(" in name else name
            labels.append(clean_name)
            values.append(stat.get("percentage", 0.0))
            
    if len(labels) < 3:
        # Polar chart cần tối thiểu 3 trục đa giác
        default_axes = ["Nhận biết", "Thông hiểu", "Vận dụng", "Vận dụng cao"]
        labels = default_axes
        values = [values[0] if values else 70.0] * 4

    num_vars = len(labels)
    # Tính góc cho từng trục
    angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
    # Khép kín đa giác
    values_closed = values + [values[0]]
    angles_closed = angles + [angles[0]]

    fig, ax = plt.subplots(figsize=(7.2, 7.2), subplot_kw=dict(polar=True), facecolor='#ffffff')
    
    # Thiết lập góc bắt đầu từ đỉnh (12h) và theo chiều kim đồng hồ
    ax.set_theta_offset(np.pi / 2)
    ax.set_theta_direction(-1)

    # Đặt nhãn cho các trục với khoảng cách hợp lý
    plt.xticks(angles, labels, color='#1e293b', size=9.5, weight='bold')

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
    plt.title(chart_title, size=13, weight='bold', color='#0f172a', pad=22)
    plt.tight_layout()

    buf = io.BytesIO()
    plt.savefig(buf, format='png', dpi=120, bbox_inches='tight')
    plt.close(fig)
    buf.seek(0)
    img_b64 = base64.b64encode(buf.read()).decode('utf-8')
    return f"data:image/png;base64,{img_b64}"


def calculate_competency_insights(
    domain_stats: Dict[str, Any], 
    total_score: float,
    max_score: float = 1200.0,
    is_spt: bool = False
) -> Dict[str, Any]:
    """
    Phân tích ma trận điểm mạnh, điểm yếu và ước tính phân vị ĐGNL (V-ACT hoặc SPT).
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

    import math
    if is_spt or max_score <= 20.0:
        # Thang điểm 10 chuẩn SPT ĐH Sư Phạm Hà Nội (Mean = 6.0, Std = 1.5)
        z = (total_score - 6.0) / 1.5
        percentile = round(float(0.5 * (1.0 + math.erf(z / math.sqrt(2.0))) * 100), 1)
        percentile = min(99.9, max(1.0, percentile))

        if total_score >= 8.5:
            tier = "Xuất sắc (Top 5% - Khả năng trúng tuyển rất cao vào các ngành mũi nhọn ĐH Sư Phạm Hà Nội)"
            color = "#10b981"
        elif total_score >= 7.0:
            tier = "Giỏi (Top 20% - Cơ hội xét tuyển thuận lợi vào ĐH Sư Phạm Hà Nội)"
            color = "#3b82f6"
        elif total_score >= 5.0:
            tier = "Khá / Đạt chuẩn (Đạt mức yêu cầu xét tuyển cơ bản)"
            color = "#f59e0b"
        else:
            tier = "Cần tăng cường rèn luyện (Dưới mức trung bình kỳ thi SPT)"
            color = "#ef4444"
    else:
        # Thang điểm 1200 chuẩn V-ACT ĐHQG-HCM (Mean = 650, Std = 135)
        z = (total_score - 650) / 135.0
        percentile = round(float(0.5 * (1.0 + math.erf(z / math.sqrt(2.0))) * 100), 1)
        percentile = min(99.9, max(1.0, percentile))

        # Đánh giá xếp loại năng lực V-ACT
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
