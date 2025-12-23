# charts/chart_10.py
import pandas as pd
import matplotlib.pyplot as plt

def plot(df: pd.DataFrame):
    """
    图10：不同压力水平下的睡眠质量分布（箱线图）
    """

    df_plot = df[['Stress Level', 'Quality of Sleep']].dropna().copy()

    # 合理范围过滤
    df_plot = df_plot[
        df_plot['Stress Level'].between(1, 10) &
        df_plot['Quality of Sleep'].between(1, 10)
    ]

    # 压力分组
    df_plot['压力分组'] = pd.cut(
        df_plot['Stress Level'],
        bins=[0, 3, 6, 10],
        labels=['低压力', '中压力', '高压力']
    )

    fig, ax = plt.subplots(figsize=(8, 6))

    df_plot.boxplot(
        column='Quality of Sleep',
        by='压力分组',
        ax=ax,
        grid=False
    )

    ax.set_title("不同压力水平下的睡眠质量分布", fontsize=14, fontweight='bold')
    ax.set_xlabel("压力水平分组")
    ax.set_ylabel("睡眠质量（1–10）")

    # 去掉 pandas 自动生成的副标题
    plt.suptitle("")

    ax.grid(axis='y', linestyle='--', alpha=0.3)

    fig.tight_layout()
    return fig
