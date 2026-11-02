# menu.py - Hệ thống StudyPacing
# Xây dựng khung điều hướng chính (Core System & Menu)

import sys

def hien_thi_menu():
    print("\n==================================================")
    print("        STUDYPACING - TỐI ƯU HÓA THỜI GIAN TỰ HỌC     ")
    print("==================================================")
    print("1. Đồng hồ tập trung (Pomodoro Timer)")
    print("2. Quản lý việc cần làm (Task Manager)")
    print("3. Lưu trữ dữ liệu hệ thống (Storage)")
    print("4. Thống kê năng suất học tập (Analytics)")
    print("0. Thoát chương trình")
    print("==================================================")

def main():
    while True:
        hien_thi_menu()
        try:
            lua_chon = int(input("Nhập lựa chọn của bạn (0-4): "))
            
            if lua_chon == 1:
                print("\n--- ĐỒNG HỒ POMODORO ---")
                print("[Chức năng đang chờ module pomodoro.py từ Thành viên 2]")
                
            elif lua_chon == 2:
                print("\n--- QUẢN LÝ TASK ---")
                print("[Chức năng đang chờ module task_manager.py từ Thành viên 3]")
                
            elif lua_chon == 3:
                print("\n--- LƯU TRỮ DỮ LIỆU ---")
                print("[Chức năng đang chờ module storage.py từ Thành viên 4]")
                
            elif lua_chon == 4:
                print("\n--- THỐNG KÊ NĂNG SUẤT ---")
                print("[Chức năng đang chờ module analytics.py từ Thành viên 5]")
                
            elif lua_chon == 0:
                print("\nCảm ơn bạn đã sử dụng StudyPacing. Chúc bạn học tập hiệu quả!")
                sys.exit()
            else:
                print("\n⚠️ Lựa chọn không hợp lệ! Vui lòng chọn số từ 0 đến 4.")
                
        except ValueError:
            print("\n❌ Lỗi định dạng: Vui lòng chỉ nhập số nguyên từ 0 đến 4!")

if __name__ == "__main__":
    main()