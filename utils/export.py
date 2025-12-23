# utils/export.py
import os

def save_figure(fig, filename: str, out_dir="exports"):
    """
    保存 matplotlib 图像
    """
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, filename)
    fig.savefig(path, dpi=300, bbox_inches="tight")
    return path
