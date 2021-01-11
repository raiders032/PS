import sys
N, M = map(int, sys.stdin.readline().split())
board = [[sys.maxsize] * N for _ in range(N)]

for i in range(N):
    board[i][i] = 0

for _ in range(M):
    v1, v2, w = map(int, sys.stdin.readline().split())
    board[v1-1][v2-1] = w

for i in range(N):
    for r in range(N):
        for c in range(N):
            board[r][c] = min(board[r][c], board[r][i] + board[i][c])

for r in range(N):
    for c in range(N):
        if board[r][c] == sys.maxsize:
            print('M', end=' ')
        else:
            print(board[r][c], end=' ')
    print()