# charts/chart_11.py
import pandas as pd
import matplotlib.pyplot as plt

def plot(df: pd.DataFrame):
    """
    图11：不同睡眠障碍类型下的睡眠时长分布
    """
    df_plot = df[['Sleep Disorder', 'Sleep Duration']].dropna().copy()
    df_plot = df_plot[df_plot['Sleep Duration'].between(3, 14)]

    fig, ax = plt.subplots(figsize=(8, 6))
    df_plot.boxplot(
        column='Sleep Duration',
        by='Sleep Disorder',
        ax=ax,
        grid=False
    )

    ax.set_title("不同睡眠障碍类型下的睡眠时长分布", fontsize=14, fontweight='bold')
    ax.set_xlabel("睡眠障碍类型")
    ax.set_ylabel("睡眠时长（小时）")
    plt.suptitle("")
    ax.grid(axis='y', linestyle='--', alpha=0.3)

    fig.tight_layout()
    return fig
