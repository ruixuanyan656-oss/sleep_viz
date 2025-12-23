# charts/chart_12.py
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def render(df: pd.DataFrame):
    """
    不同 BMI 类别下：
    身体活动水平 × 睡眠质量 的分组箱线图
    等价于原始 三.12.py
    """

    # 1️⃣ 仅保留有效 BMI 类别
    valid_bmi = ['Normal', 'Overweight', 'Obese']
    df_filtered = df[df['BMI Category'].isin(valid_bmi)].copy()

    # 2️⃣ 身体活动水平分组（严格对齐原分箱）
    df_filtered['活动水平分组'] = pd.cut(
        df_filtered['Physical Activity Level'],
        bins=[0, 30, 60, 120],
        labels=[
            '低活动（≤30分钟）',
            '中活动（31-60分钟）',
            '高活动（≥61分钟）'
        ]
    )

    # 3️⃣ 绘制箱线图
    fig, ax = plt.subplots(figsize=(14, 8))

    sns.boxplot(
        x='BMI Category',
        y='Quality of Sleep',
        hue='活动水平分组',
        data=df_filtered,
        ax=ax,
        palette=['#95A5A6', '#3498DB', '#2ECC71'],
        linewidth=1.2,
        flierprops=dict(marker='o', alpha=0.5)
    )

    # 4️⃣ 图表样式（逐项还原）
    ax.set_title(
        '不同BMI类别下身体活动水平与睡眠质量的关系',
        fontsize=16,
        fontweight='bold',
        pad=20
    )
    ax.set_xlabel('BMI类别', fontsize=14)
    ax.set_ylabel('睡眠质量（1–10分）', fontsize=14)

    ax.legend(
        title='身体活动水平',
        fontsize=12,
        title_fontsize=13
    )

    ax.set_yticks(range(1, 11))
    ax.tick_params(axis='x', labelsize=12)
    ax.tick_params(axis='y', labelsize=11)

    ax.grid(axis='y', alpha=0.3, linestyle='--')

    plt.tight_layout()
    return fig
