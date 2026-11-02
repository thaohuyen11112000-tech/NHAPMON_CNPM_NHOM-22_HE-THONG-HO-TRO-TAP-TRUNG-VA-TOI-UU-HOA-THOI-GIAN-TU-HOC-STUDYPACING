import os
from datetime import datetime

# Tên file lưu lịch sử học tập (đồng bộ với module storage.py)
HISTORY_FILE = "history.json"

def load_history_data():
    """Hàm phụ trợ để đọc dữ liệu lịch sử từ file JSON."""
    if not os.path.exists(HISTORY_FILE):
        return []
    
    import json
    try:
        with open(HISTORY_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        print(f"⚠️ Lỗi khi đọc dữ liệu thống kê: {e}")
        return []

def thong_ket_tong_quan():
    """Hiển thị tổng quan các chỉ số năng suất học tập."""
    history = load_history_data()
    
    print("\n==================================================")
    print("📊                  BÁO CÁO THỐNG KÊ NĂNG SUẤT           ")
    print("==================================================")
    
    if not history:
        print("❌ Chưa có dữ liệu học tập nào được ghi nhận.")
        print("💡 Gợi ý: Hãy hoàn thành một vài phiên Pomodoro để xem thống kê nhé!")
        print("==================================================")
        return

    # Tính toán các chỉ số
    tong_so_phien = len(history)
    tong_phut = sum(item.get("duration", 0) for item in history)
    tong_gio = round(tong_phut / 60, 2)
    
    # Thống kê theo ngày (Dictionary lưu trữ tổng phút mỗi ngày)
    thong_ke_ngay = {}
    for item in history:
        ngay = item.get("date", "Không rõ")
        thoi_luong = item.get("duration", 0)
        thong_ke_ngay[ngay] = thong_ke_ngay.get(ngay, 0) + thoi_luong

    # Hiển thị số liệu tổng quát
    print(f"🎯 Tổng số phiên Pomodoro hoàn thành : {tong_so_phien} phiên")
    print(f"⏳ Tổng thời gian tập trung         : {tong_phut} phút (~ {tong_gio} giờ)")
    print("-" * 50)
    
    # Hiển thị chi tiết theo từng ngày
    print("📅 THỜI GIAN TẬP TRUNG THEO NGÀY:")
    for ngay, phut in sorted(thong_ke_ngay.items()):
        gio = round(phut / 60, 2)
        # Tạo thanh biểu đồ trực quan bằng ký tự '█' (mỗi block tương ứng 25 phút hoặc 1 phiên)
        so_block = phut // 25
        bieu_do = "█" * int(so_block) if so_block > 0 else "▌"
        
        print(f"  • Ngày {ngay}: {phut:3d} phút (~ {gio:4.1f}h) | {bieu_do}")
        
    print("==================================================")

if __name__ == "__main__":
    # Cho phép chạy thử độc lập module analytics.py
    thong_ket_tong_quan()