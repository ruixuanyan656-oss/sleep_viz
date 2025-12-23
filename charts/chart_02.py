# charts/chart_02.py
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def plot(df: pd.DataFrame, top_n: int = 6):
    """
    图02：睡眠时长与睡眠质量的关系（按职业分类）
    输入：
        df      - 已完成预处理的数据
        top_n   - 展示样本数最多的前 N 个职业
    输出：
        fig     - matplotlib Figure
    """

    # ===============================
    # 1. 选择样本数最多的职业
    # ===============================
    occupation_counts = df['Occupation'].value_counts()
    top_occupations = occupation_counts.head(top_n).index.tolist()
    df_top = df[df['Occupation'].isin(top_occupations)]

    # ===============================
    # 2. 创建画布
    # ===============================
    fig, ax = plt.subplots(figsize=(10, 7))

    # 职业配色（与原脚本风格一致）
    occupation_colors = {
        'Doctor': '#2E86AB',
        'Nurse': '#A23B72',
        'Engineer': '#F18F01',
        'Teacher': '#73AB84',
        'Accountant': '#C14953',
        'Lawyer': '#6D597A'
    }

    markers = ['o', 's', '^', 'D', 'v', 'X']

    # ===============================
    # 3. 绘制散点（按职业）
    # ===============================
    for i, occupation in enumerate(top_occupations):
        subset = df_top[df_top['Occupation'] == occupation]

        ax.scatter(
            subset['Sleep Duration'],
            subset['Quality of Sleep'],
            s=90,
            alpha=0.7,
            edgecolors='white',
            linewidth=1,
            marker=markers[i % len(markers)],
            color=occupation_colors.get(occupation, '#7F8C8D'),
            label=occupation,
            zorder=2
        )

    # ===============================
    # 4. 添加总体趋势线
    # ===============================
    sns.regplot(
        data=df_top,
        x='Sleep Duration',
        y='Quality of Sleep',
        scatter=False,
        ax=ax,
        color='gray',
        line_kws={'linestyle': '--', 'alpha': 0.6}
    )

    # ===============================
    # 5. 图表样式
    # ===============================
    ax.set_title(
        "睡眠时长与睡眠质量的关系（按职业分类）",
        fontsize=15, fontweight='bold'
    )
    ax.set_xlabel("睡眠时长（小时）")
    ax.set_ylabel("睡眠质量（1–10）")

    ax.grid(True, linestyle='--', alpha=0.3)

    # ===============================
    # 6. 相关系数标注
    # ===============================
    corr = df_top['Sleep Duration'].corr(df_top['Quality of Sleep'])
    ax.text(
        0.02, 0.95,
        f"相关系数: {corr:.3f}",
        transform=ax.transAxes,
        fontsize=11,
        verticalalignment='top',
        bbox=dict(boxstyle='round', facecolor='white', alpha=0.8)
    )

    # ===============================
    # 7. 图例
    # ===============================
    ax.legend(
        title="职业",
        fontsize=10,
        title_fontsize=11,
        framealpha=0.9
    )

    fig.tight_layout()
    return fig
