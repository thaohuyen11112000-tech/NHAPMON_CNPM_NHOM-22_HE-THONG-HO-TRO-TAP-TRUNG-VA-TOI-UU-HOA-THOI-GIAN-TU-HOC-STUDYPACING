import json
import os

# Tên các file lưu trữ dữ liệu
TASKS_FILE = "tasks.json"
HISTORY_FILE = "history.json"

def save_json(file_path, data):
    """Hàm chung để ghi dữ liệu dạng dictionary/list vào file JSON"""
    try:
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        return True
    except Exception as e:
        print(f"Lỗi khi lưu dữ liệu vào {file_path}: {e}")
        return False

def load_json(file_path, default_value):
    """Hàm chung để đọc dữ liệu từ file JSON. Nếu file chưa tồn tại sẽ trả về giá trị mặc định."""
    if not os.path.exists(file_path):
        return default_value
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        print(f"Lỗi khi đọc file {file_path}: {e}")
        return default_value

# === CÁC HÀM XỬ LÝ CHO DỰ ÁN STUDYPACING ===

def save_tasks(tasks_list):
    """Lưu danh sách công việc (Task)"""
    return save_json(TASKS_FILE, tasks_list)

def load_tasks():
    """Tải danh sách công việc (Task) đã lưu"""
    return load_json(TASKS_FILE, [])

def save_history(history_list):
    """Lưu lịch sử các phiên học Pomodoro đã hoàn thành"""
    return save_json(HISTORY_FILE, history_list)

def load_history():
    """Tải lịch sử học tập đã lưu"""
    return load_json(HISTORY_FILE, [])