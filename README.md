# Bài tập lớn: Phân tích Thiết kế Giải thuật
**Chủ đề:** Xây dựng giải thuật Quay lui giải trò chơi trí tuệ N-Queens (Xếp hậu).
**Nhóm:** 14

##  Giới thiệu dự án
Dự án này cài đặt và đánh giá hiệu năng của thuật toán Quay lui (Backtracking) cho bài toán N-Queens. Đặc biệt, dự án áp dụng **Kỹ thuật Cắt tỉa (Pruning - Sử dụng mảng đánh dấu O(1))** để tối ưu hóa thời gian thực thi và so sánh với thuật toán cơ bản.

## 📂 Cấu trúc thư mục
* `src/`: Chứa mã nguồn Python.
  * `basic_nqueens.py`: Thuật toán Backtracking thuần túy.
  * `pruned_nqueens.py`: Thuật toán Backtracking có áp dụng Cắt tỉa.
  * `main_demo.py`: Kịch bản chạy test tự động và in bàn cờ trực quan.
* `data/`: Chứa các file dữ liệu thống kê thời gian chạy (milliseconds).
* `docs/`: Chứa tài liệu báo cáo Word, lưu đồ thuật toán và Slide thuyết trình.

##  Hướng dẫn chạy thử nghiệm (Dành cho Tester)
1. Cài đặt Python 3.x trên máy tính.
2. Mở Terminal / Command Prompt tại thư mục `src/`.
3. Chạy lệnh: `python main_demo.py` để xem kết quả đánh giá tự động.
