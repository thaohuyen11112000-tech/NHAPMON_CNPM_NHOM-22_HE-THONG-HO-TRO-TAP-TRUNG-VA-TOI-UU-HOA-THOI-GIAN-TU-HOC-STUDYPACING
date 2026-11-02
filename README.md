# NHAPMON_CNPM_NHOM-22_HE-THONG-HO-TRO-TAP-TRUNG-VA-TOI-UU-HOA-THOI-GIAN-TU-HOC-STUDYPACING
Dành cho học sinh, sinh viên tự học, những người thường xuyên mất tập trung và khó sắp xếp thời gian, StudyPacing là một hệ thống web giúp tập trung, lập kế hoạch và theo dõi thời gian học. Khác với các bộ đếm giờ đơn thuần, sản phẩm kết hợp Pomodoro, quản lý nhiệm vụ theo môn học và thống kê tiến độ trong một nơi duy nhất.

# task_manager.py
# Thành viên 3: Quản lý công việc cần học

tasks = []


def add_task():
    title = input("Nhập tên công việc: ").strip()

    if not title:
        print("Tên công việc không được để trống!")
        return

    print("Mức độ ưu tiên: 1. Cao | 2. Trung bình | 3. Thấp")
    choice = input("Chọn mức độ ưu tiên: ")

    priorities = {"1": "Cao", "2": "Trung bình", "3": "Thấp"}

    if choice not in priorities:
        print("Mức độ ưu tiên không hợp lệ!")
        return

    task = {
        "id": max((t["id"] for t in tasks), default=0) + 1,
        "title": title,
        "priority": priorities[choice],
        "completed": False
    }

    tasks.append(task)
    print("Đã thêm công việc thành công!")


def list_tasks():
    if not tasks:
        print("Danh sách công việc đang trống!")
        return

    print("\n===== DANH SÁCH CÔNG VIỆC =====")
    for task in tasks:
        status = "Hoàn thành" if task["completed"] else "Chưa hoàn thành"
        print(
            f"ID: {task['id']} | {task['title']} | "
            f"Ưu tiên: {task['priority']} | {status}"
        )


def complete_task():
    try:
        task_id = int(input("Nhập ID công việc cần hoàn thành: "))
    except ValueError:
        print("ID phải là số nguyên!")
        return

    for task in tasks:
        if task["id"] == task_id:
            task["completed"] = True
            print("Đã cập nhật trạng thái hoàn thành!")
            return

    print("Không tìm thấy công việc!")


def delete_task():
    try:
        task_id = int(input("Nhập ID công việc cần xóa: "))
    except ValueError:
        print("ID phải là số nguyên!")
        return

    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            print("Đã xóa công việc thành công!")
            return

    print("Không tìm thấy công việc!")


def task_menu():
    while True:
        print("\n===== STUDYPACING - TASK MANAGER =====")
        print("1. Thêm công việc")
        print("2. Xem danh sách công việc")
        print("3. Đánh dấu hoàn thành")
        print("4. Xóa công việc")
        print("0. Quay lại")

        choice = input("Chọn chức năng: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            list_tasks()
        elif choice == "3":
            complete_task()
        elif choice == "4":
            delete_task()
        elif choice == "0":
            break
        else:
            print("Lựa chọn không hợp lệ!")


if __name__ == "__main__":
    task_menu()
