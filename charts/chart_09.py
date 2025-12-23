# charts/chart_09.py
import pandas as pd
import matplotlib.pyplot as plt

def render(df: pd.DataFrame):
    """
    图09：睡眠质量与收缩压（SBP）的关系
    """

    # 拆分血压字段
    df_plot = df[['Blood Pressure', 'Quality of Sleep']].dropna().copy()
    bp = df_plot['Blood Pressure'].str.split('/', expand=True)
    df_plot['SBP'] = pd.to_numeric(bp[0], errors='coerce')

    # 合理范围过滤
    df_plot = df_plot[
        (df_plot['SBP'].between(80, 200)) &
        (df_plot['Quality of Sleep'].between(1, 10))
    ]

    fig, ax = plt.subplots(figsize=(8, 6))

    ax.scatter(
        df_plot['Quality of Sleep'],
        df_plot['SBP'],
        alpha=0.7,
        edgecolors='k'
    )

    ax.set_title("睡眠质量与收缩压的关系", fontsize=14, fontweight='bold')
    ax.set_xlabel("睡眠质量（1–10）")
    ax.set_ylabel("收缩压（mmHg）")
    ax.grid(True, linestyle='--', alpha=0.3)

    fig.tight_layout()
    return fig
