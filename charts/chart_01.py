# charts/chart_01.py
import matplotlib.pyplot as plt
import pandas as pd

def plot(df: pd.DataFrame):
    """
    图01：BMI类别与睡眠障碍分布（百分比堆叠柱状图）
    输入：df（已完成预处理）
    输出：fig（matplotlib Figure）
    """

    # ===============================
    # 1. 构建交叉表（百分比）
    # ===============================
    cross_tab = (
        pd.crosstab(
            df['BMI Category'],
            df['Sleep Disorder'],
            normalize='index'
        ) * 100
    )

    bmi_order = ['Underweight', 'Normal', 'Overweight', 'Obese']
    cross_tab = cross_tab.reindex(bmi_order)

    # ===============================
    # 2. 创建图形
    # ===============================
    fig, ax = plt.subplots(figsize=(8, 5))

    colors = ['#2E86AB', '#A23B72', '#F18F01']
    cross_tab.plot(
        kind='bar',
        stacked=True,
        ax=ax,
        color=colors,
        width=0.75
    )

    # ===============================
    # 3. 图表美化
    # ===============================
    ax.set_title("BMI类别与睡眠障碍分布", fontsize=14, fontweight='bold')
    ax.set_xlabel("BMI 类别")
    ax.set_ylabel("比例（%）")

    ax.legend(
        title="睡眠障碍类型",
        fontsize=10,
        title_fontsize=11
    )

    # ===============================
    # 4. 添加百分比标签
    # ===============================
    for container in ax.containers:
        ax.bar_label(
            container,
            fmt='%.1f%%',
            label_type='center',
            fontsize=9
        )

    ax.grid(axis='y', linestyle='--', alpha=0.4)

    fig.tight_layout()
    return fig
