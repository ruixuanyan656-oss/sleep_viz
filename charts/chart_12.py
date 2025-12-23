# charts/chart_12.py
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def plot(df: pd.DataFrame):
    """
    图12：年龄与睡眠质量的关系
    """
    df_plot = df[['Age', 'Quality of Sleep']].dropna().copy()
    df_plot = df_plot[
        df_plot['Age'].between(10, 100) &
        df_plot['Quality of Sleep'].between(1, 10)
    ]

    fig, ax = plt.subplots(figsize=(8, 6))
    ax.scatter(df_plot['Age'], df_plot['Quality of Sleep'], alpha=0.7, edgecolors='k')

    # 趋势线
    z = np.polyfit(df_plot['Age'], df_plot['Quality of Sleep'], 1)
    p = np.poly1d(z)
    x = np.sort(df_plot['Age'])
    ax.plot(x, p(x), 'r--')

    ax.set_title("年龄与睡眠质量的关系", fontsize=14, fontweight='bold')
    ax.set_xlabel("年龄（岁）")
    ax.set_ylabel("睡眠质量（1–10）")
    ax.grid(True, linestyle='--', alpha=0.3)

    fig.tight_layout()
    return fig
