# charts/chart_08.py
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def plot(df: pd.DataFrame):
    """
    图08：身体活动水平与睡眠质量（气泡=每日步数，按睡眠障碍分组）
    """

    df_plot = df[
        ['Physical Activity Level', 'Quality of Sleep', 'Daily Steps', 'Sleep Disorder']
    ].dropna().copy()

    # 气泡大小映射（截断极端值）
    steps = df_plot['Daily Steps'].astype(float)
    low, high = steps.quantile(0.05), steps.quantile(0.95)
    steps_clip = steps.clip(lower=low, upper=high)

    size = (steps_clip - steps_clip.min()) / (steps_clip.max() - steps_clip.min() + 1e-9)
    bubble_size = 40 + size * 560

    fig, ax = plt.subplots(figsize=(10, 6))

    if 'Sleep Disorder' in df_plot.columns:
        for disorder, g in df_plot.groupby('Sleep Disorder'):
            ax.scatter(
                g['Physical Activity Level'],
                g['Quality of Sleep'],
                s=bubble_size.loc[g.index],
                alpha=0.55,
                edgecolors='k',
                linewidths=0.3,
                label=str(disorder)
            )
        ax.legend(title="睡眠障碍类型")
    else:
        ax.scatter(
            df_plot['Physical Activity Level'],
            df_plot['Quality of Sleep'],
            s=bubble_size,
            alpha=0.55,
            edgecolors='k',
            linewidths=0.3
        )

    ax.set_title("身体活动水平与睡眠质量关系（气泡=每日步数）", fontsize=14, fontweight='bold')
    ax.set_xlabel("身体活动水平（分钟/天）")
    ax.set_ylabel("睡眠质量（1–10）")
    ax.grid(True, linestyle='--', alpha=0.3)

    fig.tight_layout()
    return fig
