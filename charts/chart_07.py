# charts/chart_07.py
import pandas as pd
import matplotlib.pyplot as plt

def plot(df: pd.DataFrame):
    """
    图07：不同年龄段的睡眠障碍风险分布（堆叠柱状图）
    """

    # 年龄分段
    bins = [0, 29, 39, 49, 59, 120]
    labels = ['≤29岁', '30–39岁', '40–49岁', '50–59岁', '≥60岁']
    df_plot = df[['Age', 'Sleep Disorder']].dropna().copy()
    df_plot['年龄段'] = pd.cut(df_plot['Age'], bins=bins, labels=labels)

    # 统计比例
    count_table = (
        df_plot.groupby(['年龄段', 'Sleep Disorder'])
        .size()
        .unstack(fill_value=0)
    )
    ratio = count_table.div(count_table.sum(axis=1), axis=0)

    # 绘图
    fig, ax = plt.subplots(figsize=(8, 6))
    ratio.plot(kind='bar', stacked=True, ax=ax)

    ax.set_title("不同年龄段睡眠障碍风险分布", fontsize=14, fontweight='bold')
    ax.set_xlabel("年龄段")
    ax.set_ylabel("比例")
    ax.legend(title="睡眠障碍类型")
    ax.grid(axis='y', linestyle='--', alpha=0.4)

    fig.tight_layout()
    return fig
