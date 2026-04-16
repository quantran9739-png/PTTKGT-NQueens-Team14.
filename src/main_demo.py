import time

# --- HÀM IN BÀN CỜ TRỰC QUAN (DÀNH CHO DEMO) ---
def print_board(board, N):
    print("\nVí dụ 1 đáp án hợp lệ:")
    for i in range(N):
        row_str = ""
        for j in range(N):
            if board[i][j] == 1:
                row_str += "[Q] " # Q là Quân hậu
            else:
                row_str += "[.] " # . là ô trống
        print(row_str)
    print("-" * 30)

# --- THUẬT TOÁN 1: BACKTRACKING CƠ BẢN ---
def is_safe_basic(board, row, col, N):
    for i in range(row):
        if board[i][col] == 1: return False
    for i, j in zip(range(row-1, -1, -1), range(col-1, -1, -1)):
        if board[i][j] == 1: return False
    for i, j in zip(range(row-1, -1, -1), range(col+1, N)):
        if board[i][j] == 1: return False
    return True

def solve_basic(board, row, N, count, save_first_board):
    if row == N:
        count[0] += 1
        # Lưu lại đáp án đầu tiên để in ra xem thử
        if count[0] == 1:
            for r in range(N):
                for c in range(N):
                    save_first_board[r][c] = board[r][c]
        return
    for col in range(N):
        if is_safe_basic(board, row, col, N):
            board[row][col] = 1 
            solve_basic(board, row + 1, N, count, save_first_board) 
            board[row][col] = 0 

# --- THUẬT TOÁN 2: BACKTRACKING CẮT TỈA (TỐI ƯU) ---
def solve_pruned(row, N, cols, diag1, diag2, count):
    if row == N:
        count[0] += 1
        return
    for col in range(N):
        d1 = row - col + N - 1
        d2 = row + col
        if cols[col] or diag1[d1] or diag2[d2]:
            continue
        cols[col] = diag1[d1] = diag2[d2] = True
        solve_pruned(row + 1, N, cols, diag1, diag2, count)
        cols[col] = diag1[d1] = diag2[d2] = False

# --- KỊCH BẢN CHẠY TEST ĐỒNG LOẠT ---
def run_automation_test():
    print("="*60)
    print(f"{'KÍCH THƯỚC (N)':<15} | {'CODE CƠ BẢN (ms)':<20} | {'CODE CẮT TỈA (ms)':<20}")
    print("="*60)
    
    # Test tự động các mốc N từ 4 đến 12 (N=12 chạy cơ bản sẽ bắt đầu chậm)
    test_cases = [4, 8, 10, 12] 
    
    for N in test_cases:
        # Đo thời gian Code Cơ Bản
        board = [[0] * N for _ in range(N)]
        count_basic = [0]
        save_board = [[0] * N for _ in range(N)]
        
        start_time = time.time()
        solve_basic(board, 0, N, count_basic, save_board)
        time_basic = (time.time() - start_time) * 1000

        # Đo thời gian Code Cắt tỉa
        cols = [False] * N
        diag1 = [False] * (2 * N - 1)
        diag2 = [False] * (2 * N - 1)
        count_pruned = [0]
        
        start_time = time.time()
        solve_pruned(0, N, cols, diag1, diag2, count_pruned)
        time_pruned = (time.time() - start_time) * 1000

        # In kết quả dạng bảng
        print(f"Bàn cờ {N}x{N:<8} | {time_basic:<20.2f} | {time_pruned:<20.2f}")
        
        # In hình bàn cờ minh họa cho N=8
        if N == 8:
            print_board(save_board, N)

if __name__ == "__main__":
    run_automation_test()
