# utils/fonts.py
import os
import matplotlib.pyplot as plt
from matplotlib import font_manager, rcParams

def setup_chinese_font():
    """
    全局设置中文字体（Windows）
    """
    font_path = r"C:\Windows\Fonts\simhei.ttf"

    if os.path.exists(font_path):
        font_manager.fontManager.addfont(font_path)
        font_prop = font_manager.FontProperties(fname=font_path)
        rcParams['font.family'] = font_prop.get_name()
        rcParams['axes.unicode_minus'] = False
    else:
        print("⚠ 未找到 simhei.ttf，中文可能显示异常")
