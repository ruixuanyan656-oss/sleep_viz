# app.py
import streamlit as st
from utils.data import load_data
from utils.fonts import setup_chinese_font

# ===== 中文字体 =====
setup_chinese_font()

# ===== 页面配置 =====
st.set_page_config(
    page_title="睡眠健康数据可视化系统",
    layout="wide"
)

st.title("睡眠健康数据分析与可视化系统")

# ===== 上传数据 =====
uploaded_file = st.file_uploader(
    "请上传【已完成预处理】的睡眠健康数据 CSV 文件",
    type="csv"
)

if uploaded_file is None:
    st.info("👆 请先上传 CSV 文件后再进行分析")
    st.stop()

# ===== 加载数据 =====
df = load_data(uploaded_file)
st.success(f"数据加载成功，共 {len(df)} 条记录")

# ===== 图表选择 =====
chart_map = {
    "01 身体活动 × 睡眠质量": "charts.chart_01",
    "02 睡眠时长 × 睡眠质量（职业）": "charts.chart_02",
    "03 每日步数 × 压力（性别）": "charts.chart_03",
    "04 性别 × 睡眠质量": "charts.chart_04",
    "05 年龄 × 睡眠时长密度": "charts.chart_05",
    "06 活动 × 心率": "charts.chart_06",
    "07 年龄 × 睡眠障碍": "charts.chart_07",
    "08 活动 × 睡眠质量（气泡）": "charts.chart_08",
    "09 睡眠质量 × 血压": "charts.chart_09",
    "10 压力 × 睡眠质量": "charts.chart_10",
    "11 睡眠障碍 × 睡眠时长": "charts.chart_11",
    "12 年龄 × 睡眠质量": "charts.chart_12",
    "13 综合分析": "charts.chart_13",
}

option = st.selectbox("请选择要查看的图表：", list(chart_map.keys()))

# ===== 动态加载并绘图 =====
module_path = chart_map[option]
module = __import__(module_path, fromlist=["plot"])
fig = module.plot(df)

st.pyplot(fig)
