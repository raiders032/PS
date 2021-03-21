N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
total = 0
for r in range(N // 2):
    for c in range(N//2-r, N//2+r+1):
        total += board[r][c] + board[N-r-1][c]
total += sum(board[N//2])
print(total)
