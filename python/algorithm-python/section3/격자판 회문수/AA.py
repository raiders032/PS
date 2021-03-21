board = [list(map(int, input().split())) for _ in range(7)]
cnt = 0
for r in range(7):
    for c in range(3):
        if board[r][c] == board[r][c+4] and board[r][c+1] == board[r][c+3]:
            cnt += 1
for c in range(7):
    for r in range(3):
        if board[r][c] == board[r+4][c] and board[r+1][c] == board[r+3][c]:
            cnt += 1
print(cnt)
