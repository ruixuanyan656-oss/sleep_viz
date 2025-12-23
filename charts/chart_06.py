# charts/chart_06.py
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def render(df: pd.DataFrame):
    """
    图06：身体活动水平与心率的关系（散点 + 趋势线）
    """

    df_plot = df[
        (df['Heart Rate'].between(40, 120)) &
        (df['Physical Activity Level'].between(0, 1440))
    ][['Physical Activity Level', 'Heart Rate']].dropna()

    corr = df_plot['Physical Activity Level'].corr(df_plot['Heart Rate'])

    fig, ax = plt.subplots(figsize=(10, 6))

    ax.scatter(
        df_plot['Physical Activity Level'],
        df_plot['Heart Rate'],
        alpha=0.6,
        s=45,
        color='#73AB84',
        edgecolors='white',
        linewidth=0.5
    )

    # 趋势线
    z = np.polyfit(
        df_plot['Physical Activity Level'],
        df_plot['Heart Rate'],
        1
    )
    p = np.poly1d(z)
    x = np.sort(df_plot['Physical Activity Level'])

    ax.plot(
        x,
        p(x),
        linestyle='--',
        linewidth=2.2,
        color='#F18F01',
        label=f'趋势线（r = {corr:.3f}）'
    )

    ax.set_title('身体活动水平与心率的关系', fontsize=14, fontweight='bold')
    ax.set_xlabel('身体活动水平（分钟/天）')
    ax.set_ylabel('心率（bpm）')
    ax.grid(True, linestyle='--', alpha=0.3)
    ax.legend()

    fig.tight_layout()
    return fig
