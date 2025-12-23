# utils/data.py
import pandas as pd

def load_data(csv_source) -> pd.DataFrame:
    """
    读取并返回睡眠健康数据
    csv_source 可以是：
    - 文件路径（str）
    - Streamlit 上传的文件对象
    """

    df = pd.read_csv(csv_source, encoding="utf-8")

    # ===== 系统级安全校验（轻量，不重复研究型清洗） =====
    numeric_ranges = {
        'Age': (0, 120),
        'Sleep Duration': (0, 24),
        'Quality of Sleep': (1, 10),
        'Stress Level': (1, 10),
        'Physical Activity Level': (0, 1440),
        'Daily Steps': (0, 50000),
        'Heart Rate': (30, 200)
    }

    for col, (low, high) in numeric_ranges.items():
        if col in df.columns:
            df[col] = df[col].clip(lower=low, upper=high)

    # 分类字段兜底
    if 'Gender' in df.columns:
        df['Gender'] = df['Gender'].astype(str).str.strip().replace({
            'M': 'Male', 'm': 'Male',
            'F': 'Female', 'f': 'Female'
        })

    if 'BMI Category' in df.columns:
        df['BMI Category'] = df['BMI Category'].astype(str).str.strip().str.capitalize()

    if 'Sleep Disorder' in df.columns:
        df['Sleep Disorder'] = df['Sleep Disorder'].astype(str).str.strip().str.capitalize()

    return df.dropna().reset_index(drop=True)
