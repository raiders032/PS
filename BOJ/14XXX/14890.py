"""
14890.경사로
골드3
구현
"""
import sys

input = sys.stdin.readline
N, L = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
check = [[False] * N for _ in range(N)]
res = 0

for r in range(N):
    is_ok = True
    for c in range(N - 1):
        if abs(board[r][c] - board[r][c + 1]) > 1:
            is_ok = False
            break
        if board[r][c] == board[r][c + 1]:
            continue
        elif board[r][c] - 1 == board[r][c + 1]:
            if c + L >= N:
                is_ok = False
                break
            for i in range(c + 1, c + L):
                if board[r][i] != board[r][i + 1]:
                    is_ok = False
                    break
            if is_ok:
                for i in range(c + 1, c + L + 1):
                    check[r][i] = True
        elif board[r][c] + 1 == board[r][c + 1]:
            if c - L + 1 < 0:
                is_ok = False
                break
            for i in range(c - L + 1, c):
                if board[r][i] != board[r][i + 1]:
                    is_ok = False
                    break
            for i in range(c - L + 1, c + 1):
                if check[r][i]:
                    is_ok = False
                    break
            if is_ok:
                for i in range(c - L + 1, c + 1):
                    check[r][i] = True
    if is_ok:
        res += 1

check = [[False] * N for _ in range(N)]
for c in range(N):
    is_ok = True
    for r in range(N - 1):
        if abs(board[r][c] - board[r + 1][c]) > 1:
            is_ok = False
            break

        if board[r][c] == board[r + 1][c]:
            continue

        elif board[r][c] - 1 == board[r + 1][c]:
            if r + L >= N:
                is_ok = False
                break
            for i in range(r + 1, r + L):
                if board[i][c] != board[i + 1][c]:
                    is_ok = False
                    break
            if is_ok:
                for i in range(r + 1, r + L + 1):
                    check[i][c] = True

        elif board[r][c] + 1 == board[r + 1][c]:
            if r - L + 1 < 0:
                is_ok = False
                break
            for i in range(r - L + 1, r):
                if board[i][c] != board[i + 1][c]:
                    is_ok = False
                    break
            for i in range(r - L + 1, r + 1):
                if check[i][c]:
                    is_ok = False
                    break
            if is_ok:
                for i in range(r - L + 1, r + 1):
                    check[i][c] = True
    if is_ok:
        res += 1

print(res)
