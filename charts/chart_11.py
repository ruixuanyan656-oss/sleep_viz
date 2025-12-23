# charts/chart_11.py
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def render(df: pd.DataFrame):
    """
    压力水平 × 睡眠时长 × 睡眠质量（三维气泡图）
    等价于原始 三.11.py
    """

    # 1️⃣ 数据清洗（严格对齐原代码）
    df_clean = df[
        (df['Stress Level'].between(1, 10)) &
        (df['Sleep Duration'].between(4, 12)) &
        (df['Quality of Sleep'].between(1, 10))
    ].copy()

    # 2️⃣ 气泡大小映射（睡眠质量 → 面积）
    quality = df_clean['Quality of Sleep']
    bubble_size = (
        (quality - quality.min()) /
        (quality.max() - quality.min()) * 500 + 50
    )

    # 3️⃣ 绘图
    fig, ax = plt.subplots(figsize=(12, 8))

    scatter = ax.scatter(
        df_clean['Stress Level'],
        df_clean['Sleep Duration'],
        s=bubble_size,
        c=df_clean['Quality of Sleep'],
        cmap='viridis',
        alpha=0.6,
        edgecolors='white',
        linewidth=0.8
    )

    # 4️⃣ 趋势线（压力 → 睡眠时长）
    x = df_clean['Stress Level']
    y = df_clean['Sleep Duration']
    z = np.polyfit(x, y, 1)
    p = np.poly1d(z)

    x_sorted = np.sort(x)
    ax.plot(
        x_sorted,
        p(x_sorted),
        color='red',
        linestyle='--',
        linewidth=2,
        label=f'趋势线（斜率={z[0]:.3f}）'
    )

    # 5️⃣ 图表样式
    ax.set_title(
        '压力水平与睡眠时长、睡眠质量的三维关联',
        fontsize=16,
        fontweight='bold',
        pad=20
    )
    ax.set_xlabel('压力水平（1–10分）', fontsize=14)
    ax.set_ylabel('睡眠时长（小时）', fontsize=14)

    ax.set_xticks(range(1, 11))
    ax.tick_params(axis='both', labelsize=11)

    ax.legend(fontsize=12)
    ax.grid(alpha=0.3, linestyle='--')

    # 6️⃣ 颜色条（睡眠质量）
    cbar = plt.colorbar(scatter, ax=ax)
    cbar.set_label('睡眠质量（1–10分）', fontsize=12)

    plt.tight_layout()
    return fig
