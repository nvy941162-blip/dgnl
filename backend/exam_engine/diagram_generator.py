# -*- coding: utf-8 -*-
"""
HỆ THỐNG SINH HÌNH VẼ & BIỂU ĐỒ CHUẨN KHẢO THÍ (DIAGRAM & CHART GENERATOR)
Cung cấp hình vẽ trực quan tự động cho:
1. Công nghệ Công nghiệp (Hình chiếu vuông góc 3 hướng, hình chiếu trục đo, sơ đồ mạch)
2. Công nghệ Nông nghiệp (Mô hình nhà kính thông minh, hệ thống thủy canh hồi lưu NFT, chu trình biogas)
3. Địa lí (Biểu đồ khí hậu nhiệt độ & lượng mưa cột-đường, biểu đồ cơ cấu GDP, phân tích số liệu)
4. Toán học (Đồ thị hàm số bậc 3, phân thức có tiệm cận, bảng biến thiên, hình học không gian)
5. V-ACT (Mạng lưới đồ thị, sơ đồ tư duy logic)
"""

import io
import base64
import math
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.path import Path as MplPath
import numpy as np

def fig_to_base64(fig) -> str:
    buf = io.BytesIO()
    fig.savefig(buf, format="png", dpi=130, bbox_inches="tight")
    plt.close(fig)
    return "data:image/png;base64," + base64.b64encode(buf.getvalue()).decode("utf-8")


# =============================================================================
# 1. CÔNG NGHỆ CÔNG NGHIỆP: HÌNH CHIẾU VUÔNG GÓC & BẢN VẼ KỸ THUẬT
# =============================================================================
def draw_orthographic_projection(variant: int = 1) -> str:
    """
    Vẽ vật thể 3D mẫu và 4 phương án hình chiếu vuông góc 3 hướng (Hình a, b, c, d).
    Đáp án chuẩn: Hình b có nét đứt thể hiện rãnh xuyên suốt khuất.
    """
    fig, axs = plt.subplots(2, 3, figsize=(9.5, 6.2))
    fig.patch.set_facecolor("#ffffff")
    
    # 1. Ô góc trên-trái: Vẽ vật thể 3D (Isometric)
    ax_obj = plt.subplot2grid((2, 3), (0, 0), colspan=3)
    ax_obj.set_facecolor("#f8fafc")
    ax_obj.set_xlim(-0.5, 10.5)
    ax_obj.set_ylim(-0.5, 3.5)
    ax_obj.axis("off")
    ax_obj.set_title("VẬT THỂ MẪU CẦN XÁC ĐỊNH HÌNH CHIẾU VUÔNG GÓC", fontsize=11, fontweight="bold", pad=8, color="#1e293b")
    
    # Vẽ vật thể dạng bậc thang có rãnh khoét (Isometric block)
    # Mặt trước
    verts_front = [(1.5, 0.5), (4.5, 0.5), (4.5, 1.3), (3.0, 1.3), (3.0, 2.5), (1.5, 2.5)]
    poly_front = patches.Polygon(verts_front, closed=True, edgecolor="#0f172a", facecolor="#94a3b8", lw=2, zorder=3)
    ax_obj.add_patch(poly_front)
    
    # Mặt trên (bậc dưới và bậc trên)
    verts_top1 = [(4.5, 1.3), (5.5, 1.9), (4.0, 1.9), (3.0, 1.3)]
    poly_top1 = patches.Polygon(verts_top1, closed=True, edgecolor="#0f172a", facecolor="#cbd5e1", lw=2, zorder=3)
    ax_obj.add_patch(poly_top1)
    
    verts_top2 = [(1.5, 2.5), (3.0, 2.5), (4.0, 3.1), (2.5, 3.1)]
    poly_top2 = patches.Polygon(verts_top2, closed=True, edgecolor="#0f172a", facecolor="#e2e8f0", lw=2, zorder=3)
    ax_obj.add_patch(poly_top2)
    
    # Mặt bên (phải)
    verts_side = [(4.5, 0.5), (5.5, 1.1), (5.5, 1.9), (4.5, 1.3)]
    poly_side = patches.Polygon(verts_side, closed=True, edgecolor="#0f172a", facecolor="#64748b", lw=2, zorder=3)
    ax_obj.add_patch(poly_side)
    
    verts_side_top = [(3.0, 1.3), (4.0, 1.9), (4.0, 3.1), (3.0, 2.5)]
    poly_side_top = patches.Polygon(verts_side_top, closed=True, edgecolor="#0f172a", facecolor="#64748b", lw=2, zorder=3)
    ax_obj.add_patch(poly_side_top)

    # Nét đứt rãnh ngầm xuyên suốt
    ax_obj.plot([1.5, 2.5], [1.1, 1.7], color="#334155", lw=1.5, linestyle="--", zorder=4)
    ax_obj.plot([4.5, 5.5], [1.1, 1.7], color="#334155", lw=1.5, linestyle="--", zorder=4)
    
    # Mũi tên hướng chiếu: Đứng (Front), Bằng (Top), Cạnh (Side)
    ax_obj.annotate("Hướng chiếu đứng (1)", xy=(0.8, 1.5), xytext=(-0.3, 1.5),
                    arrowprops=dict(facecolor="#2563eb", edgecolor="#2563eb", shrink=0.08, width=2, headwidth=7),
                    fontsize=9, fontweight="bold", color="#1e40af")
    ax_obj.annotate("Hướng chiếu bằng (2)", xy=(2.7, 3.3), xytext=(2.7, 3.4),
                    arrowprops=dict(facecolor="#16a34a", edgecolor="#16a34a", shrink=0.08, width=2, headwidth=7),
                    fontsize=9, fontweight="bold", color="#15803d")
    ax_obj.annotate("Hướng chiếu cạnh (3)", xy=(5.8, 1.5), xytext=(6.5, 1.5),
                    arrowprops=dict(facecolor="#dc2626", edgecolor="#dc2626", shrink=0.08, width=2, headwidth=7),
                    fontsize=9, fontweight="bold", color="#b91c1c")

    # 4 phương án hình chiếu: Hình a, Hình b (Đúng), Hình c, Hình d
    options = [
        {"lbl": "Hình a", "dash": False, "note": "(Thiếu nét đứt rãnh khuất)"},
        {"lbl": "Hình b (Chuẩn)", "dash": True, "note": "(Đầy đủ nét liền & nét đứt)"},
        {"lbl": "Hình c", "dash": False, "swap": True, "note": "(Sai vị trí hình chiếu bằng)"},
        {"lbl": "Hình d", "dash": False, "inv": True, "note": "(Sai tỉ lệ bậc đối xứng)"}
    ]
    
    # Chia 4 ô bên dưới
    for idx, opt in enumerate(options):
        ax = plt.subplot2grid((2, 4), (1, idx))
        ax.set_facecolor("#ffffff")
        ax.set_xlim(-0.2, 3.2)
        ax.set_ylim(-0.2, 3.2)
        ax.axis("off")
        ax.set_title(f"{opt['lbl']}", fontsize=10, fontweight="bold", color="#1e293b", pad=4)
        
        # Đường bao ngoài khung hình
        rect_border = patches.Rectangle((0, 0), 3, 3, edgecolor="#94a3b8", facecolor="none", lw=1, linestyle=":")
        ax.add_patch(rect_border)
        
        # Hình chiếu đứng (Top-Left của mỗi khung)
        # Hình L ngược
        p_front = patches.Polygon([(0.3, 1.6), (1.3, 1.6), (1.3, 2.0), (0.8, 2.0), (0.8, 2.6), (0.3, 2.6)],
                                  closed=True, edgecolor="#0f172a", facecolor="#f1f5f9", lw=1.5)
        ax.add_patch(p_front)
        
        # Hình chiếu cạnh (Top-Right)
        p_side = patches.Rectangle((1.6, 1.6), 1.0, 1.0, edgecolor="#0f172a", facecolor="#f1f5f9", lw=1.5)
        ax.add_patch(p_side)
        ax.plot([1.6, 2.6], [2.0, 2.0], color="#0f172a", lw=1.5)
        if opt["dash"]:
            # Có đường nét đứt biểu diễn rãnh ngầm xuyên suốt
            ax.plot([1.6, 2.6], [1.8, 1.8], color="#ef4444", lw=1.5, linestyle="--")
        elif not opt.get("inv"):
            ax.plot([1.6, 2.6], [1.8, 1.8], color="#0f172a", lw=1.2) # Nét liền (sai tiêu chuẩn)
            
        # Hình chiếu bằng (Bottom-Left)
        p_top = patches.Rectangle((0.3, 0.3), 1.0, 1.0, edgecolor="#0f172a", facecolor="#f1f5f9", lw=1.5)
        ax.add_patch(p_top)
        ax.plot([0.8, 0.8], [0.3, 1.3], color="#0f172a", lw=1.5)

    plt.tight_layout()
    return fig_to_base64(fig)


# =============================================================================
# 2. CÔNG NGHỆ NÔNG NGHIỆP: MÔ HÌNH NHÀ KÍNH THÔNG MINH & THỦY CANH NFT & BIOGAS
# =============================================================================
def draw_smart_greenhouse_diagram(variant: int = 1) -> str:
    """
    Vẽ sơ đồ mô hình nhà kính thông minh (Smart IoT Greenhouse)
    """
    fig, ax = plt.subplots(figsize=(8.5, 5.2))
    ax.set_facecolor("#f8fafc")
    ax.set_xlim(-0.5, 10.5)
    ax.set_ylim(-0.5, 6.5)
    ax.axis("off")
    ax.set_title("SƠ ĐỒ HỆ THỐNG MÔ HÌNH NHÀ KÍNH THÔNG MINH (SMART IOT GREENHOUSE)", fontsize=11, fontweight="bold", color="#065f46", pad=12)

    # 1. Khung nhà kính (Greenhouse Frame)
    roof_poly = patches.Polygon([(1.0, 3.5), (5.0, 5.8), (9.0, 3.5)], closed=False, edgecolor="#047857", lw=3.5)
    body_poly = patches.Rectangle((1.0, 0.5), 8.0, 3.0, edgecolor="#047857", facecolor="#ecfdf5", lw=3.0, alpha=0.6)
    ax.add_patch(body_poly)
    ax.add_patch(roof_poly)
    
    # Khung đỡ mái
    ax.plot([5.0, 5.0], [3.5, 5.8], color="#047857", lw=2, linestyle="--")
    ax.plot([3.0, 5.0], [3.5, 4.65], color="#047857", lw=1.5, linestyle=":")
    ax.plot([7.0, 5.0], [3.5, 4.65], color="#047857", lw=1.5, linestyle=":")

    # 2. Quạt thông gió đối lưu (Ventilation Fan)
    fan_box = patches.Rectangle((8.6, 2.2), 0.7, 0.8, edgecolor="#b91c1c", facecolor="#fee2e2", lw=2)
    ax.add_patch(fan_box)
    ax.text(8.95, 2.6, "Quạt hút\nđối lưu", ha="center", va="center", fontsize=7.5, fontweight="bold", color="#b91c1c")

    # 3. Giàn tưới phun sương / nhỏ giọt (Misting pipe)
    ax.plot([1.5, 8.5], [3.2, 3.2], color="#0284c7", lw=2.5, linestyle="-")
    for nozzle_x in [2.5, 4.0, 5.5, 7.0]:
        ax.plot([nozzle_x, nozzle_x], [3.2, 2.9], color="#0284c7", lw=2)
        ax.plot(nozzle_x, 2.8, "v", color="#0284c7", markersize=6)
    ax.text(5.0, 3.45, "Hệ thống tưới tự động (Misting System)", ha="center", fontsize=8.5, color="#0369a1", fontweight="bold")

    # 4. Giàn cây trồng bên trong (Crops)
    for px in [2.2, 3.5, 4.8, 6.2, 7.5]:
        pot = patches.Rectangle((px - 0.35, 0.5), 0.7, 0.4, edgecolor="#92400e", facecolor="#d97706")
        ax.add_patch(pot)
        # Vẽ tán cây cách điệu bằng hình elip xanh
        plant = patches.Ellipse((px, 1.2), 0.6, 0.7, edgecolor="#047857", facecolor="#10b981")
        ax.add_patch(plant)
        ax.plot([px, px], [0.8, 1.2], color="#047857", lw=2)

    # 5. Cảm biến (Sensors)
    # Cảm biến độ ẩm đất
    ax.plot([3.5, 3.5], [0.9, 0.3], color="#7c3aed", lw=2)
    ax.text(3.5, 0.1, "[Cảm biến ẩm đất]", ha="center", fontsize=8, fontweight="bold", color="#6d28d9")

    # Cảm biến nhiệt độ & độ ẩm không khí
    ax.text(6.8, 2.2, "Cảm biến T/H", ha="center", fontsize=8, fontweight="bold", color="#b45309",
            bbox=dict(boxstyle="round,pad=0.2", facecolor="#fef3c7", edgecolor="#f59e0b"))

    # 6. Bộ điều khiển trung tâm vi xử lý (IoT Microcontroller Controller)
    controller_box = patches.FancyBboxPatch((0.2, 1.2), 1.8, 1.5, boxstyle="round,pad=0.1",
                                           edgecolor="#1e3a8a", facecolor="#dbeafe", lw=2)
    ax.add_patch(controller_box)
    ax.text(1.1, 2.1, "BỘ ĐIỀU KHIỂN\nTRUNG TÂM IoT", ha="center", va="center", fontsize=8, fontweight="bold", color="#1e40af")
    ax.text(1.1, 1.45, "[Vi điều khiển\nWi-Fi/Cloud]", ha="center", va="center", fontsize=7.5, color="#3b82f6")

    # Đường truyền tín hiệu
    ax.annotate("", xy=(1.5, 2.7), xytext=(2.0, 3.2),
                arrowprops=dict(arrowstyle="<->", color="#0284c7", lw=1.5, linestyle="--"))
    ax.annotate("", xy=(2.0, 1.8), xytext=(3.5, 0.5),
                arrowprops=dict(arrowstyle="<-", color="#7c3aed", lw=1.5, linestyle="--"))

    plt.tight_layout()
    return fig_to_base64(fig)


def draw_hydroponics_nft_diagram(variant: int = 1) -> str:
    """
    Vẽ sơ đồ hệ thống thủy canh hồi lưu NFT (Nutrient Film Technique)
    """
    fig, ax = plt.subplots(figsize=(8.5, 4.8))
    ax.set_facecolor("#ffffff")
    ax.set_xlim(-0.5, 10.5)
    ax.set_ylim(-0.5, 5.5)
    ax.axis("off")
    ax.set_title("SƠ ĐỒ HỆ THỐNG THỦY CANH HỒI LƯU NFT (NUTRIENT FILM TECHNIQUE)", fontsize=11, fontweight="bold", color="#0369a1", pad=12)

    # 1. Máng trồng cây dốc (Slanted Gullies)
    gully = patches.Polygon([(1.5, 3.8), (8.5, 2.8), (8.5, 2.4), (1.5, 3.4)], closed=True,
                            edgecolor="#0284c7", facecolor="#e0f2fe", lw=2.5)
    ax.add_patch(gully)
    ax.text(5.0, 3.4, "Máng trồng nghiêng (Dòng màng dinh dưỡng mỏng)", ha="center", fontsize=8.5, color="#0369a1", fontweight="bold", rotation=-7)

    # Các rọ trồng cây
    for i, x in enumerate([2.5, 4.0, 5.5, 7.0]):
        y_pos = 3.8 - (x - 1.5) * (1.0 / 7.0)
        cup = patches.Rectangle((x - 0.25, y_pos - 0.35), 0.5, 0.45, edgecolor="#0f172a", facecolor="#94a3b8")
        ax.add_patch(cup)
        leaf = patches.Ellipse((x, y_pos + 0.22), 0.5, 0.4, facecolor="#22c55e", edgecolor="#15803d", lw=1.5)
        ax.add_patch(leaf)
        ax.text(x, y_pos + 0.22, "Rau", ha="center", va="center", fontsize=7.5, color="#ffffff", fontweight="bold")
        # Bộ rễ tiếp xúc màng dinh dưỡng
        ax.plot([x, x], [y_pos - 0.35, y_pos - 0.55], color="#ca8a04", lw=1.5, linestyle=":")

    # 2. Bể chứa dung dịch dinh dưỡng (Nutrient Reservoir)
    tank = patches.Rectangle((7.0, 0.4), 2.5, 1.5, edgecolor="#0f172a", facecolor="#bfdbfe", lw=2)
    ax.add_patch(tank)
    ax.text(8.25, 1.15, "BỂ DUNG DỊCH\nDINH DƯỠNG\n(pH: 5.5 - 6.5)", ha="center", va="center", fontsize=8, fontweight="bold", color="#1e3a8a")

    # 3. Máy bơm chìm (Submersible Pump)
    pump = patches.Rectangle((7.2, 0.5), 0.6, 0.5, edgecolor="#1e293b", facecolor="#475569")
    ax.add_patch(pump)
    ax.text(7.5, 0.75, "Bơm", ha="center", va="center", fontsize=7, color="#ffffff", fontweight="bold")

    # 4. Đường ống cấp dinh dưỡng lên đầu máng (Supply Pipe)
    pipe_x = [7.5, 0.8, 0.8, 1.5]
    pipe_y = [1.0, 1.0, 4.2, 4.0]
    ax.plot(pipe_x, pipe_y, color="#2563eb", lw=2.5)
    ax.annotate("", xy=(1.5, 4.0), xytext=(1.2, 4.05),
                arrowprops=dict(facecolor="#2563eb", edgecolor="#2563eb", width=2, headwidth=6))
    ax.text(0.6, 2.5, "Ống cấp dinh dưỡng", rotation=90, va="center", fontsize=8, fontweight="bold", color="#2563eb")

    # 5. Đường ống hồi lưu về bể (Drain Return Pipe)
    ax.plot([8.5, 8.5], [2.4, 1.9], color="#0284c7", lw=2.5)
    ax.annotate("", xy=(8.5, 1.9), xytext=(8.5, 2.1),
                arrowprops=dict(facecolor="#0284c7", edgecolor="#0284c7", width=2, headwidth=6))
    ax.text(8.9, 2.1, "Hồi lưu", fontsize=8, fontweight="bold", color="#0284c7")

    plt.tight_layout()
    return fig_to_base64(fig)


def draw_nanosilver_chart() -> str:
    """
    Vẽ đồ thị tỉ lệ sống cá sau 7 ngày thử nghiệm nano bạc và Florfenicol (Câu 18 Tech Agriculture)
    """
    fig, ax = plt.subplots(figsize=(7.8, 4.5))
    fig.patch.set_facecolor("#ffffff")
    days = [1, 2, 3, 4, 5, 6, 7]
    ct1 = [100, 98, 96, 94, 93, 92, 92] # Flor 15 ppm
    ct2 = [100, 96, 94, 92, 90, 89, 88] # Flor 10 + nano 5
    ct3 = [100, 95, 90, 88, 85, 84, 82] # Flor 5 + nano 10
    ct4 = [100, 92, 85, 80, 78, 76, 75] # Nano 15
    dc  = [100, 85, 70, 62, 55, 52, 50] # Đối chứng

    ax.plot(days, ct1, "o-", color="#1d4ed8", lw=2.2, label="CT1: Florfenicol 15 ppm")
    ax.plot(days, ct2, "s--", color="#059669", lw=2.0, label="CT2: Flor 10 ppm + Nano bạc 5 ppm")
    ax.plot(days, ct3, "^-.", color="#d97706", lw=2.0, label="CT3: Flor 5 ppm + Nano bạc 10 ppm")
    ax.plot(days, ct4, "d:", color="#7c3aed", lw=2.0, label="CT4: Nano bạc 15 ppm")
    ax.plot(days, dc,  "x-", color="#dc2626", lw=2.5, label="ĐC: Đối chứng (Không điều trị)")

    ax.set_title("TỈ LỆ SỐNG (%) CỦA CÁ NHEO MỸ SAU 7 NGÀY THỬ NGHIỆM ĐIỀU TRỊ", fontsize=10.5, fontweight="bold", pad=10)
    ax.set_xlabel("Thời gian sau khi gây nhiễm bệnh (Ngày)", fontsize=9.5)
    ax.set_ylabel("Tỉ lệ sống (%)", fontsize=9.5)
    ax.set_ylim(40, 105)
    ax.set_xticks(days)
    ax.grid(True, linestyle="--", alpha=0.5)
    ax.legend(fontsize=8.5, loc="lower left")

    plt.tight_layout()
    return fig_to_base64(fig)


# =============================================================================
# 3. ĐỊA LÍ: BIỂU ĐỒ KHÍ HẬU (CỘT - ĐƯỜNG) & BIỂU ĐỒ CƠ CẤU GDP
# =============================================================================
def draw_climate_chart(station_name: str = "Trạm Khí tượng A (Miền Bắc)") -> str:
    """
    Vẽ biểu đồ kết hợp cột - đường chuẩn khảo thí môn Địa lí:
    - Cột màu xanh: Lượng mưa các tháng (mm)
    - Đường màu đỏ: Nhiệt độ trung bình các tháng (độ C)
    """
    months = [f"T{i}" for i in range(1, 13)]
    # Số liệu chuẩn của đề thi mẫu SPT (Trạm phía Bắc có mùa đông lạnh)
    temp = [16.4, 17.2, 20.1, 24.0, 27.5, 28.9, 28.9, 28.5, 27.2, 24.8, 21.4, 18.0]
    rain = [20.5, 28.2, 45.0, 90.1, 195.4, 255.8, 310.2, 335.0, 240.6, 120.4, 45.0, 21.0]

    fig, ax1 = plt.subplots(figsize=(8.5, 4.8))
    fig.patch.set_facecolor("#ffffff")
    
    # Trục 1: Lượng mưa (Cột xanh)
    color_rain = "#0284c7"
    ax1.set_xlabel("Các tháng trong năm", fontsize=10, fontweight="bold", labelpad=6)
    ax1.set_ylabel("Lượng mưa (mm)", color=color_rain, fontsize=10, fontweight="bold")
    bars = ax1.bar(months, rain, color=color_rain, width=0.55, alpha=0.85, label="Lượng mưa (mm)")
    ax1.tick_params(axis="y", labelcolor=color_rain)
    ax1.set_ylim(0, 420)
    ax1.grid(axis="y", linestyle="--", alpha=0.4)

    # Trục 2: Nhiệt độ (Đường đỏ)
    ax2 = ax1.twinx()
    color_temp = "#dc2626"
    ax2.set_ylabel("Nhiệt độ (°C)", color=color_temp, fontsize=10, fontweight="bold")
    lines = ax2.plot(months, temp, color=color_temp, lw=2.5, marker="o", markersize=6, label="Nhiệt độ (°C)")
    ax2.tick_params(axis="y", labelcolor=color_temp)
    ax2.set_ylim(10, 36)

    # Tiêu đề & Thông số tổng hợp
    ax1.set_title(f"BIỂU ĐỒ KHÍ HẬU NHIỆT ĐỘ VÀ LƯỢNG MƯA - {station_name.upper()}", fontsize=10.5, fontweight="bold", pad=12)
    
    # Hộp thông số khảo thí
    total_rain = sum(rain)
    avg_temp = round(sum(temp) / 12, 1)
    amplitude = round(max(temp) - min(temp), 1)
    meta_text = f"Nhiệt độ TB năm: {avg_temp}°C | Biên độ nhiệt: {amplitude}°C | Tổng lượng mưa: {total_rain:.1f} mm"
    fig.text(0.5, 0.01, meta_text, ha="center", fontsize=9, fontweight="bold",
             bbox=dict(boxstyle="round,pad=0.3", facecolor="#f1f5f9", edgecolor="#cbd5e1"))

    plt.tight_layout()
    return fig_to_base64(fig)


def draw_gdp_structure_chart() -> str:
    """
    Vẽ biểu đồ chuyển dịch cơ cấu GDP nước ta 2010 - 2022 (Câu 14 Địa lí)
    """
    years = ["2010", "2015", "2018", "2020", "2022"]
    nong_lam_thuy_san = [15.4, 14.5, 13.2, 12.7, 11.9]
    cong_nghiep_xaydung = [40.6, 41.2, 42.2, 41.8, 41.3]
    dich_vu = [33.0, 34.3, 35.8, 36.8, 38.2]
    thue_san_pham = [11.0, 10.0, 8.8, 8.7, 8.6]

    fig, ax = plt.subplots(figsize=(8.0, 4.6))
    fig.patch.set_facecolor("#ffffff")

    x = range(len(years))
    width = 0.55

    p1 = ax.bar(x, nong_lam_thuy_san, width, label="Nông, lâm nghiệp & thủy sản", color="#10b981")
    p2 = ax.bar(x, cong_nghiep_xaydung, width, bottom=nong_lam_thuy_san, label="Công nghiệp & xây dựng", color="#3b82f6")
    bottom_3 = [n + c for n, c in zip(nong_lam_thuy_san, cong_nghiep_xaydung)]
    p3 = ax.bar(x, dich_vu, width, bottom=bottom_3, label="Dịch vụ", color="#f59e0b")
    bottom_4 = [b + d for b, d in zip(bottom_3, dich_vu)]
    p4 = ax.bar(x, thue_san_pham, width, bottom=bottom_4, label="Thuế sản phẩm trừ trợ cấp", color="#8b5cf6")

    ax.set_title("CƠ CẤU GDP NƯỚC TA GIAI ĐOẠN 2010 - 2022 (%)", fontsize=11, fontweight="bold", pad=10)
    ax.set_xticks(x)
    ax.set_xticklabels(years, fontsize=10, fontweight="bold")
    ax.set_ylabel("Tỉ trọng (%)", fontsize=10)
    ax.set_ylim(0, 108)
    ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncol=2, fontsize=8.5)
    ax.grid(axis="y", linestyle="--", alpha=0.5)

    # Ghi nhãn phần trăm bên trong cột
    for i in range(len(years)):
        ax.text(i, nong_lam_thuy_san[i] / 2, f"{nong_lam_thuy_san[i]}%", ha="center", va="center", color="#ffffff", fontweight="bold", fontsize=8)
        ax.text(i, nong_lam_thuy_san[i] + cong_nghiep_xaydung[i] / 2, f"{cong_nghiep_xaydung[i]}%", ha="center", va="center", color="#ffffff", fontweight="bold", fontsize=8)
        ax.text(i, bottom_3[i] + dich_vu[i] / 2, f"{dich_vu[i]}%", ha="center", va="center", color="#ffffff", fontweight="bold", fontsize=8)

    plt.tight_layout()
    return fig_to_base64(fig)


# =============================================================================
# 4. TOÁN HỌC: ĐỒ THỊ HÀM SỐ & BẢNG BIẾN THIÊN & HÌNH HỌC KHÔNG GIAN
# =============================================================================
def draw_math_cubic_graph(variant: int = 1) -> str:
    """
    Vẽ đồ thị hàm số bậc ba y = x^3 - 3x^2 + 2 trên hệ trục Oxy
    """
    fig, ax = plt.subplots(figsize=(6.5, 5.0))
    fig.patch.set_facecolor("#ffffff")
    
    x = np.linspace(-1.5, 3.5, 400)
    y = x**3 - 3*x**2 + 2

    ax.plot(x, y, color="#2563eb", lw=2.5, label=r"$y = x^3 - 3x^2 + 2$")

    # Điểm cực đại (0, 2) và cực tiểu (2, -2)
    ax.plot(0, 2, "ro", markersize=6)
    ax.plot(2, -2, "ro", markersize=6)
    ax.plot(1, 0, "go", markersize=5) # Điểm uốn

    # Gióng tọa độ
    ax.plot([2, 2], [0, -2], "r--", lw=1.2)
    ax.plot([0, 2], [-2, -2], "r--", lw=1.2)
    ax.text(2.1, -2.1, r"$CT(2; -2)$", fontsize=9, fontweight="bold", color="#b91c1c")
    ax.text(0.15, 2.1, r"$CĐ(0; 2)$", fontsize=9, fontweight="bold", color="#b91c1c")
    ax.text(1.1, 0.2, r"$U(1; 0)$", fontsize=9, fontweight="bold", color="#15803d")

    # Trục tọa độ chuẩn
    ax.axhline(0, color="#0f172a", lw=1.2)
    ax.axvline(0, color="#0f172a", lw=1.2)
    ax.annotate("", xy=(3.8, 0), xytext=(3.5, 0), arrowprops=dict(arrowstyle="->", color="#0f172a", lw=1.5))
    ax.annotate("", xy=(0, 4.5), xytext=(0, 4.0), arrowprops=dict(arrowstyle="->", color="#0f172a", lw=1.5))
    ax.text(3.7, -0.35, r"$x$", fontsize=11, fontweight="bold")
    ax.text(-0.35, 4.3, r"$y$", fontsize=11, fontweight="bold")
    ax.text(-0.25, -0.35, r"$O$", fontsize=10, fontweight="bold")

    ax.set_xlim(-1.8, 4.0)
    ax.set_ylim(-3.5, 4.8)
    ax.grid(True, linestyle=":", alpha=0.5)
    ax.set_title("ĐỒ THỊ HÀM SỐ BẬC BA (C)", fontsize=11, fontweight="bold", pad=10)
    ax.legend(fontsize=9, loc="upper right")

    plt.tight_layout()
    return fig_to_base64(fig)


def draw_math_rational_graph(variant: int = 1) -> str:
    """
    Vẽ đồ thị hàm số phân thức y = (2x - 1) / (x + 1) với tiệm cận đứng x = -1 và ngang y = 2
    """
    fig, ax = plt.subplots(figsize=(6.5, 5.0))
    fig.patch.set_facecolor("#ffffff")

    x1 = np.linspace(-6, -1.08, 300)
    y1 = (2*x1 - 1) / (x1 + 1)
    x2 = np.linspace(-0.92, 5, 300)
    y2 = (2*x2 - 1) / (x2 + 1)

    ax.plot(x1, y1, color="#4f46e5", lw=2.2)
    ax.plot(x2, y2, color="#4f46e5", lw=2.2, label=r"$y = \frac{2x - 1}{x + 1}$")

    # Tiệm cận đứng x = -1 & ngang y = 2
    ax.axvline(-1, color="#dc2626", lw=1.5, linestyle="--", label="TCĐ: $x = -1$")
    ax.axhline(2, color="#059669", lw=1.5, linestyle="--", label="TCN: $y = 2$")

    # Trục tọa độ
    ax.axhline(0, color="#0f172a", lw=1.2)
    ax.axvline(0, color="#0f172a", lw=1.2)
    ax.text(5.2, -0.35, r"$x$", fontsize=11, fontweight="bold")
    ax.text(-0.35, 6.2, r"$y$", fontsize=11, fontweight="bold")
    ax.text(-0.25, -0.35, r"$O$", fontsize=10, fontweight="bold")

    ax.set_xlim(-6.5, 5.5)
    ax.set_ylim(-5.0, 6.5)
    ax.grid(True, linestyle=":", alpha=0.5)
    ax.set_title("ĐỒ THỊ HÀM PHÂN THỨC BẬC NHẤT / BẬC NHẤT", fontsize=10.5, fontweight="bold", pad=10)
    ax.legend(fontsize=8.5, loc="lower right")

    plt.tight_layout()
    return fig_to_base64(fig)


def draw_math_spatial_pyramid() -> str:
    """
    Vẽ hình chóp S.ABC đáy tam giác vuông tại B, SA vuông góc đáy
    """
    fig, ax = plt.subplots(figsize=(6.0, 5.0))
    fig.patch.set_facecolor("#ffffff")
    ax.axis("off")
    ax.set_xlim(-0.5, 6.5)
    ax.set_ylim(-0.5, 6.5)

    # Tọa độ các đỉnh: S, A, B, C
    S = (2.0, 5.5)
    A = (2.0, 1.8)
    B = (4.8, 0.8)
    C = (0.8, 0.8)

    # Các cạnh thấy (Nét liền)
    ax.plot([S[0], B[0]], [S[1], B[1]], color="#0f172a", lw=2) # SB
    ax.plot([S[0], C[0]], [S[1], C[1]], color="#0f172a", lw=2) # SC
    ax.plot([B[0], C[0]], [B[1], C[1]], color="#0f172a", lw=2) # BC

    # Các cạnh khuất (Nét đứt)
    ax.plot([S[0], A[0]], [S[1], A[1]], color="#dc2626", lw=2, linestyle="--") # SA vuông góc đáy
    ax.plot([A[0], B[0]], [A[1], B[1]], color="#0f172a", lw=1.5, linestyle="--") # AB
    ax.plot([A[0], C[0]], [A[1], C[1]], color="#0f172a", lw=1.5, linestyle="--") # AC

    # Nhãn các đỉnh
    ax.text(S[0], S[1] + 0.2, "S", fontsize=12, fontweight="bold", color="#b91c1c", ha="center")
    ax.text(A[0] - 0.25, A[1] + 0.1, "A", fontsize=11, fontweight="bold")
    ax.text(B[0] + 0.2, B[1], "B", fontsize=11, fontweight="bold")
    ax.text(C[0] - 0.25, C[1], "C", fontsize=11, fontweight="bold")

    # Ký hiệu vuông góc tại A (SA vuông góc đáy)
    ax.plot([2.0, 2.3, 2.3], [2.1, 2.1, 1.8], color="#dc2626", lw=1.2)
    # Ký hiệu vuông góc tại B (tam giác ABC vuông tại B)
    ax.plot([4.5, 4.4, 4.7], [0.9, 1.2, 1.1], color="#0f172a", lw=1.2)

    ax.set_title("HÌNH CHÓP S.ABC CÓ SA ⊥ (ABC), ĐÁY VUÔNG TẠI B", fontsize=10.5, fontweight="bold", pad=10)
    plt.tight_layout()
    return fig_to_base64(fig)


# =============================================================================
# 5. V-ACT: SƠ ĐỒ MẠNG LƯỚI KẾT NỐI VIỄN THÔNG (CÂU 96)
# =============================================================================
def draw_telecom_network() -> str:
    """
    Vẽ sơ đồ mạng lưới cáp ngầm 6 thị trấn A, B, C, D, E, F (Câu 96 Đề V-ACT 2026)
    """
    fig, ax = plt.subplots(figsize=(7.5, 4.8))
    fig.patch.set_facecolor("#ffffff")
    ax.axis("off")
    ax.set_xlim(-0.5, 8.5)
    ax.set_ylim(-0.5, 5.5)

    nodes = {
        "A": (1.0, 4.2),
        "B": (4.0, 4.8),
        "C": (7.0, 4.0),
        "D": (1.5, 1.2),
        "E": (4.5, 1.0),
        "F": (7.2, 1.5)
    }

    edges = [
        ("A", "B", 12), ("A", "D", 15), ("B", "C", 10),
        ("B", "E", 8),  ("B", "D", 9),  ("C", "F", 11),
        ("C", "E", 14), ("D", "E", 7),  ("E", "F", 6)
    ]

    # Vẽ các cạnh & trọng số chi phí
    for u, v, w in edges:
        p1 = nodes[u]
        p2 = nodes[v]
        ax.plot([p1[0], p2[0]], [p1[1], p2[1]], color="#94a3b8", lw=2, zorder=1)
        mx = (p1[0] + p2[0]) / 2
        my = (p1[1] + p2[1]) / 2
        ax.text(mx, my, str(w), fontsize=9, fontweight="bold", color="#1e3a8a",
                bbox=dict(boxstyle="circle,pad=0.2", facecolor="#ffffff", edgecolor="#cbd5e1", lw=1), zorder=3)

    # Vẽ các nút thị trấn
    for name, pos in nodes.items():
        circle = patches.Circle(pos, 0.45, edgecolor="#1e40af", facecolor="#3b82f6", lw=2, zorder=4)
        ax.add_patch(circle)
        ax.text(pos[0], pos[1], name, color="#ffffff", fontsize=11, fontweight="bold", ha="center", va="center", zorder=5)

    ax.set_title("SƠ ĐỒ CÁC TUYẾN CÁP KẾT NỐI VÀ CHI PHÍ (NGHÌN ĐÔ LA) GIỮA 6 THỊ TRẤN", fontsize=10.5, fontweight="bold", pad=12)
    plt.tight_layout()
    return fig_to_base64(fig)
