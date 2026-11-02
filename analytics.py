import os
import json

HISTORY_FILE = "history.json"

def thong_ket_tong_quan():
    """Hàm thống kê năng suất học tập đơn giản và gọn nhẹ."""
    if not os.path.exists(HISTORY_FILE):
        print("\n❌ Chưa có dữ liệu học tập (history.json).")
        return
    
    try:
        with open(HISTORY_FILE, "r", encoding="utf-8") as f:
            history = json.load(f)
    except Exception:
        history = []
        
    if not history:
        print("\n❌ Chưa có phiên học nào được ghi nhận.")
        return

    tong_so_phien = len(history)
    tong_phut = sum(item.get("duration", 0) for item in history)
    
    print("\n========== BÁO CÁO THỐNG KÊ NĂNG SUẤT ==========")
    print(f"🎯 Tổng số phiên : {tong_so_phien} phiên")
    print(f"⏳ Tổng thời gian: {tong_phut} phút (~ {round(tong_phut/60, 1)} giờ)")
    print("==================================================")

if __name__ == "__main__":
    thong_ket_tong_quan()