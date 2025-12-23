# charts/chart_10.py
import pandas as pd
import matplotlib.pyplot as plt

def render(df: pd.DataFrame):
    """
    不同职业的睡眠障碍类型分布对比（百分比分组柱状图）
    等价于原始 三.10.py
    """

    # 1️⃣ 只保留样本量最多的前 8 个职业
    top_occupations = (
        df['Occupation']
        .value_counts()
        .head(8)
        .index
    )
    df_filtered = df[df['Occupation'].isin(top_occupations)]

    # 2️⃣ 构建交叉表（职业 × 睡眠障碍类型，占比）
    cross_tab = (
        pd.crosstab(
            df_filtered['Occupation'],
            df_filtered['Sleep Disorder'],
            normalize='index'
        ) * 100
    )

    # 3️⃣ 画图（严格还原原图）
    fig, ax = plt.subplots(figsize=(14, 8))

    cross_tab.plot(
        kind='bar',
        ax=ax,
        width=0.8,
        color=['#FF6B6B', '#4ECDC4'],
        edgecolor='black',
        linewidth=0.5
    )

    ax.set_title(
        '不同职业的睡眠障碍类型分布对比',
        fontsize=16,
        fontweight='bold',
        pad=20
    )
    ax.set_xlabel('职业', fontsize=14)
    ax.set_ylabel('占比（%）', fontsize=14)

    ax.legend(
        title='睡眠障碍类型',
        fontsize=12,
        title_fontsize=13
    )

    ax.set_xticklabels(
        ax.get_xticklabels(),
        rotation=45,
        ha='right',
        fontsize=11
    )
    ax.tick_params(axis='y', labelsize=11)

    ax.grid(axis='y', linestyle='--', alpha=0.3)

    # 4️⃣ 百分比标签（原图关键点）
    for container in ax.containers:
        ax.bar_label(container, fmt='%.1f%%', fontsize=9, padding=3)

    plt.tight_layout()

    return fig
