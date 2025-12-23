# charts/chart_05.py
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def plot(df: pd.DataFrame):
    """
    图05：年龄与睡眠时长的分布密度（KDE + 散点）
    """

    df_plot = df[['Age', 'Sleep Duration']].dropna()

    fig, ax = plt.subplots(figsize=(10, 7))

    kde = sns.kdeplot(
        data=df_plot,
        x='Age',
        y='Sleep Duration',
        fill=True,
        cmap='viridis',
        thresh=0.05,
        alpha=0.8,
        ax=ax
    )

    ax.scatter(
        df_plot['Age'],
        df_plot['Sleep Duration'],
        alpha=0.35,
        s=18,
        color='black',
        edgecolors='white',
        linewidth=0.3
    )

    ax.set_title('年龄与睡眠时长的分布密度', fontsize=14, fontweight='bold')
    ax.set_xlabel('年龄（岁）')
    ax.set_ylabel('睡眠时长（小时）')
    ax.grid(True, linestyle='--', alpha=0.3)

    fig.tight_layout()
    return fig
