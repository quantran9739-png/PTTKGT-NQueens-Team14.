import time

def is_safe_basic(board, row, col, N):
    for i in range(row):
        if board[i][col] == 1:
            return False
    for i, j in zip(range(row-1, -1, -1), range(col-1, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row-1, -1, -1), range(col+1, N)):
        if board[i][j] == 1:
            return False
    return True

def solve_nqueens_basic(board, row, N, count):
    if row == N:
        count[0] += 1
        return
    for col in range(N):
        if is_safe_basic(board, row, col, N):
            board[row][col] = 1 
            solve_nqueens_basic(board, row + 1, N, count) 
            board[row][col] = 0 

N = 12
board = [[0] * N for _ in range(N)]
count = [0]

start_time = time.time()
solve_nqueens_basic(board, 0, N, count)
end_time = time.time()

print(f"--- BẢN CƠ BẢN ---")
print(f"Số cách giải cho N={N}: {count[0]}")
print(f"Thời gian chạy: {(end_time - start_time) * 1000:.2f} milliseconds")
