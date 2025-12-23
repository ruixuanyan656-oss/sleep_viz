# charts/chart_04.py
import pandas as pd
import matplotlib.pyplot as plt

def render(df: pd.DataFrame):
    """
    图04：不同性别的平均睡眠质量对比（含标准差）
    """

    # 按性别统计
    stats = (
        df.groupby('Gender')['Quality of Sleep']
        .agg(['mean', 'std'])
        .reset_index()
    )

    fig, ax = plt.subplots(figsize=(8, 6))

    bars = ax.bar(
        stats['Gender'],
        stats['mean'],
        yerr=stats['std'],
        capsize=6,
        color=['#73AB84', '#F18F01'],
        edgecolor='black',
        linewidth=1.1
    )

    # 数值标签
    for bar, val in zip(bars, stats['mean']):
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            bar.get_height(),
            f'{val:.2f}',
            ha='center',
            va='bottom',
            fontsize=11
        )

    ax.set_title('不同性别的平均睡眠质量对比', fontsize=14, fontweight='bold')
    ax.set_xlabel('性别')
    ax.set_ylabel('平均睡眠质量评分')
    ax.grid(axis='y', linestyle='--', alpha=0.4)

    fig.tight_layout()
    return fig
