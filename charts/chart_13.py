# charts/chart_13.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def render(df: pd.DataFrame):
    """
    生活方式、心理压力与睡眠健康的综合可视化分析（2×2）
    等价于原始 三.13.py
    """

    # ===============================
    # 1️⃣ 数据清洗（统一标准）
    # ===============================
    df = df[
        (df['Physical Activity Level'].between(0, 1440)) &
        (df['Quality of Sleep'].between(1, 10)) &
        (df['Sleep Duration'].between(4, 12)) &
        (df['Stress Level'].between(1, 10)) &
        (df['Heart Rate'].between(40, 120))
    ].dropna()

    # ===============================
    # 2️⃣ 创建画布
    # ===============================
    fig, axes = plt.subplots(2, 2, figsize=(18, 14))

    fig.suptitle(
        "生活方式、心理压力与睡眠健康的综合可视化分析",
        fontsize=20,
        fontweight='bold'
    )

    # =========================================================
    # 图 1：身体活动 × 睡眠质量（气泡 = 每日步数）
    # =========================================================
    steps = df['Daily Steps']
    size = (steps - steps.min()) / (steps.max() - steps.min()) * 500 + 50

    axes[0, 0].scatter(
        df['Physical Activity Level'],
        df['Quality of Sleep'],
        s=size,
        alpha=0.6,
        edgecolors='k'
    )

    axes[0, 0].set_title("身体活动水平与睡眠质量（气泡 = 每日步数）")
    axes[0, 0].set_xlabel("身体活动水平（分钟/天）")
    axes[0, 0].set_ylabel("睡眠质量（1–10）")

    # =========================================================
    # 图 2：压力 × 睡眠时长 × 睡眠质量
    # =========================================================
    quality = df['Quality of Sleep']
    bubble_size = (
        (quality - quality.min()) /
        (quality.max() - quality.min()) * 500 + 50
    )

    scatter = axes[0, 1].scatter(
        df['Stress Level'],
        df['Sleep Duration'],
        s=bubble_size,
        c=quality,
        cmap='viridis',
        alpha=0.6,
        edgecolors='white'
    )

    z = np.polyfit(df['Stress Level'], df['Sleep Duration'], 1)
    p = np.poly1d(z)
    x_sorted = np.sort(df['Stress Level'])
    axes[0, 1].plot(x_sorted, p(x_sorted), 'r--')

    axes[0, 1].set_title("压力水平、睡眠时长与睡眠质量的关系")
    axes[0, 1].set_xlabel("压力水平（1–10）")
    axes[0, 1].set_ylabel("睡眠时长（小时）")

    cbar = fig.colorbar(scatter, ax=axes[0, 1])
    cbar.set_label("睡眠质量")

    # =========================================================
    # 图 3：身体活动 × 静息心率
    # =========================================================
    axes[1, 0].scatter(
        df['Physical Activity Level'],
        df['Heart Rate'],
        alpha=0.6,
        edgecolors='k'
    )

    z_hr = np.polyfit(df['Physical Activity Level'], df['Heart Rate'], 1)
    p_hr = np.poly1d(z_hr)
    x = np.sort(df['Physical Activity Level'])
    axes[1, 0].plot(x, p_hr(x), 'r--')

    axes[1, 0].set_title("身体活动水平与静息心率的关系")
    axes[1, 0].set_xlabel("身体活动水平（分钟/天）")
    axes[1, 0].set_ylabel("心率（bpm）")

    # =========================================================
    # 图 4：BMI × 活动水平 × 睡眠质量
    # =========================================================
    df_bmi = df[df['BMI Category'].isin(['Normal', 'Overweight', 'Obese'])].copy()

    df_bmi['活动水平分组'] = pd.cut(
        df_bmi['Physical Activity Level'],
        bins=[0, 30, 60, 1440],
        labels=['低活动', '中活动', '高活动']
    )

    sns.boxplot(
        data=df_bmi,
        x='BMI Category',
        y='Quality of Sleep',
        hue='活动水平分组',
        ax=axes[1, 1],
        palette='Set2'
    )

    axes[1, 1].set_title("BMI、身体活动水平与睡眠质量分布")
    axes[1, 1].set_xlabel("BMI 类别")
    axes[1, 1].set_ylabel("睡眠质量（1–10）")
    axes[1, 1].legend(title="活动水平")

    # ===============================
    # 3️⃣ 布局
    # ===============================
    plt.tight_layout(rect=[0, 0.03, 1, 0.95])

    return fig
