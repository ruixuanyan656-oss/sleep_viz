# charts/chart_13.py
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def plot(df: pd.DataFrame):
    """
    图13：睡眠健康综合四图展示
    """
    fig, axes = plt.subplots(2, 2, figsize=(16, 12))
    fig.suptitle("睡眠健康多维度综合分析", fontsize=18, fontweight='bold')

    # ① 活动 × 睡眠质量
    axes[0, 0].scatter(
        df['Physical Activity Level'],
        df['Quality of Sleep'],
        alpha=0.6, edgecolors='k'
    )
    axes[0, 0].set_title("身体活动水平与睡眠质量")
    axes[0, 0].set_xlabel("身体活动（分钟/天）")
    axes[0, 0].set_ylabel("睡眠质量")

    # ② 压力 × 睡眠时长
    axes[0, 1].scatter(
        df['Stress Level'],
        df['Sleep Duration'],
        alpha=0.6, edgecolors='k'
    )
    axes[0, 1].set_title("压力水平与睡眠时长")
    axes[0, 1].set_xlabel("压力水平")
    axes[0, 1].set_ylabel("睡眠时长（小时）")

    # ③ 活动 × 心率
    axes[1, 0].scatter(
        df['Physical Activity Level'],
        df['Heart Rate'],
        alpha=0.6, edgecolors='k'
    )
    axes[1, 0].set_title("身体活动水平与静息心率")
    axes[1, 0].set_xlabel("身体活动（分钟/天）")
    axes[1, 0].set_ylabel("心率（bpm）")

    # ④ BMI × 睡眠质量
    sns.boxplot(
        data=df,
        x='BMI Category',
        y='Quality of Sleep',
        ax=axes[1, 1]
    )
    axes[1, 1].set_title("BMI类别与睡眠质量分布")
    axes[1, 1].set_xlabel("BMI类别")
    axes[1, 1].set_ylabel("睡眠质量")

    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    return fig
