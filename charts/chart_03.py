# charts/chart_03.py
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def render(df: pd.DataFrame):
    """
    图03：每日步数与压力水平的关系（按性别分组箱线图）
    输入：df（已完成预处理）
    输出：fig（matplotlib Figure）
    """

    # ===============================
    # 1. 构建压力水平分组
    # ===============================
    df_plot = df[['Stress Level', 'Gender', 'Daily Steps']].dropna().copy()

    df_plot['压力水平'] = pd.cut(
        df_plot['Stress Level'],
        bins=[0, 4, 7, 10],
        labels=['低压力 (1–4)', '中等压力 (5–7)', '高压力 (8–10)']
    )

    df_plot = df_plot.dropna(subset=['压力水平'])

    # ===============================
    # 2. 创建图形
    # ===============================
    fig, ax = plt.subplots(figsize=(10, 6))

    sns.boxplot(
        data=df_plot,
        x='压力水平',
        y='Daily Steps',
        hue='Gender',
        ax=ax,
        palette=['#4C72B0', '#DD8452']
    )

    # ===============================
    # 3. 图表样式
    # ===============================
    ax.set_title("每日步数与压力水平的关系（按性别）", fontsize=14, fontweight='bold')
    ax.set_xlabel("压力水平")
    ax.set_ylabel("每日步数")

    ax.legend(title='性别')
    ax.grid(axis='y', linestyle='--', alpha=0.4)

    fig.tight_layout()
    return fig
