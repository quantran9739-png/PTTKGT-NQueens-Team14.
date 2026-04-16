import time

def solve_nqueens_pruned(row, N, cols, diag1, diag2, count):
    if row == N:
        count[0] += 1
        return
        
    for col in range(N):
        d1 = row - col + N - 1
        d2 = row + col
        
        if cols[col] or diag1[d1] or diag2[d2]:
            continue
            
        cols[col] = diag1[d1] = diag2[d2] = True
        solve_nqueens_pruned(row + 1, N, cols, diag1, diag2, count)
        cols[col] = diag1[d1] = diag2[d2] = False

N = 12
cols = [False] * N
diag1 = [False] * (2 * N - 1)
diag2 = [False] * (2 * N - 1)
count = [0]

start_time = time.time()
solve_nqueens_pruned(0, N, cols, diag1, diag2, count)
end_time = time.time()

print(f"--- BẢN CẮT TỈA (PRUNING) ---")
print(f"Số cách giải cho N={N}: {count[0]}")
print(f"Thời gian chạy: {(end_time - start_time) * 1000:.2f} milliseconds")
