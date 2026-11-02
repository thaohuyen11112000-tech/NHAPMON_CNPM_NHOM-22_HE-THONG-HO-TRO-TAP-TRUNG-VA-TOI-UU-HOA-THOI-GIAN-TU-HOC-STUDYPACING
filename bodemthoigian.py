import time
from datetime import datetime

def countdown(minutes, session_type="Học tập"):
    """
    Hàm đếm ngược thời gian cho phiên học hoặc nghỉ ngơi.
    Hiển thị thời gian trực quan dạng MM:SS trên cùng một dòng.
    """
    total_seconds = minutes * 60
    print(f"\n--- Bắt đầu phiên {session_type} ({minutes} phút) ---")
    
    try:
        while total_seconds > 0:
            mins, secs = divmod(total_seconds, 60)
            timer_format = f"{mins:02d}:{secs:02d}"
            # Sử dụng \r và flush=True để cập nhật thời gian liên tục trên một dòng
            print(f"\rThời gian còn lại: {timer_format}", end="", flush=True)
            time.sleep(1)
            total_seconds -= 1
            
        print(f"\n\a[THÔNG BÁO] Đã hoàn thành phiên {session_type}! 🔔 Chúc mừng bạn!")
    except KeyboardInterrupt:
        print("\n\n[Cảnh báo] Phiên làm việc đã bị hủy giữa chừng.")
        return False
    return True

def run_pomodoro():
    # Danh sách lưu trữ các phiên học theo đúng yêu cầu: {"date": "YYYY-MM-DD", "duration": 25}
    sessions = []
    
    while True:
        print("\n==============================")
        print("      POMODORO TIMER          ")
        print("==============================")
        print("1. Bắt đầu phiên học (25 phút)")
        print("2. Bắt đầu phiên nghỉ (5 phút)")
        print("3. Xem danh sách phiên học đã lưu")
        print("4. Thoát chương trình")
        
        choice = input("👉 Lựa chọn của bạn (1-4): ").strip()
        
        if choice == '1':
            # Chạy đồng hồ 25 phút học
            success = countdown(25, "Học tập")
            if success:
                # Lấy ngày hiện tại theo định dạng YYYY-MM-DD
                current_date = datetime.now().strftime("%Y-%m-%d")
                
                # Tạo dictionary lưu thông tin phiên học
                session_record = {
                    "date": current_date, 
                    "duration": 25
                }
                
                # Thêm vào danh sách sessions
                sessions.append(session_record)
                print(f"💾 Đã ghi nhận phiên học: {session_record}")
                
                # --- GỢI Ý TÍCH HỢP VỚI storage.py (Thành viên 4) ---
                # Bạn có thể gọi hàm lưu file từ storage.py tại đây, ví dụ:
                # from storage import save_session
                # save_session(session_record)
                
        elif choice == '2':
            # Chạy đồng hồ 5 phút nghỉ
            countdown(5, "Nghỉ ngơi")
            
        elif choice == '3':
            print("\n--- DANH SÁCH PHIÊN HỌC ĐÃ HOÀN THÀNH ---")
            if not sessions:
                print("Chưa có phiên học nào được ghi nhận.")
            else:
                for idx, session in enumerate(sessions, 1):
                    print(f"{idx}. Ngày: {session['date']} | Thời lượng: {session['duration']} phút")
                    
        elif choice == '4':
            print("👋 Cảm ơn bạn đã sử dụng Pomodoro Timer. Hẹn gặp lại!")
            break
        else:
            print("❌ Lựa chọn không hợp lệ. Vui lòng nhập từ 1 đến 4.")

if __name__ == "__main__":
    run_pomodoro()