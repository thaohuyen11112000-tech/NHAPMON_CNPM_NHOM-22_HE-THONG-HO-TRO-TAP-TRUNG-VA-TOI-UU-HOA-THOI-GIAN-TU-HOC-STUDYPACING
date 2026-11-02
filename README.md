# NHAPMON_CNPM_NHOM-22_HE-THONG-HO-TRO-TAP-TRUNG-VA-TOI-UU-HOA-THOI-GIAN-TU-HOC-STUDYPACING
Dành cho học sinh, sinh viên tự học, những người thường xuyên mất tập trung và khó sắp xếp thời gian, StudyPacing là một hệ thống web giúp tập trung, lập kế hoạch và theo dõi thời gian học. Khác với các bộ đếm giờ đơn thuần, sản phẩm kết hợp Pomodoro, quản lý nhiệm vụ theo môn học và thống kê tiến độ trong một nơi duy nhất.

## Thống kê & Báo cáo hiệu suất học tập

Mở `analytics.html` trực tiếp bằng trình duyệt để xem giao diện Analytics mẫu. File `analytics.py` cung cấp báo cáo chạy trên terminal, nhận CSV đầu vào và có thể xuất dữ liệu CSV. Cả hai bản có thống kê theo 7/30 ngày, thời gian học, phiên học, phân bổ theo môn và mục tiêu tuần.

Chạy báo cáo với dữ liệu minh họa:

```bash
python analytics.py
```

Đọc dữ liệu thật và xuất các phiên trong 30 ngày gần nhất:

```bash
python analytics.py --input sessions.csv --days 30 --export report.csv
```

CSV đầu vào cần có tiêu đề `date,subject,minutes`; ngày dùng định dạng `YYYY-MM-DD`, mỗi dòng là một phiên học đã hoàn thành.
