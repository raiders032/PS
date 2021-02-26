"""
14890.경사로
골드3
구현
풀이2.68ms
"""
import sys

input = sys.stdin.readline
N, L = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
row_check = [[False, False] * N for _ in range(N)]
col_check = [[False, False] * N for _ in range(N)]
dx = [0, 1]
dy = [1, 0]
res = 0


def make_ramp(x, y, dir):
    nx = x + dx[dir]
    ny = y + dy[dir]

    if board[x][y] == board[nx][ny]:
        return True

    elif abs(board[nx][ny] - board[x][y]) > 1:
        return False

    elif board[x][y] + 1 == board[nx][ny]:
        if dir == 0:
            start = y - L + 1
            end = y
            if start < 0:
                return False

            for i in range(start, end):
                if board[x][i] != board[x][i + 1]:
                    return False

            for i in range(start, end + 1):
                if row_check[x][i]:
                    return False

            for i in range(start, end + 1):
                row_check[x][i] = True
        else:
            start = x - L + 1
            end = x

            if start < 0:
                return False

            for i in range(start, end):
                if board[i][y] != board[i + 1][y]:
                    return False

            for i in range(start, end + 1):
                if col_check[i][y]:
                    return False

            for i in range(start, end + 1):
                col_check[i][y] = True
    else:
        if dir == 0:
            start = y + 1
            end = y + L

            if end >= N:
                return False

            for i in range(start, end):
                if board[x][i] != board[x][i + 1]:
                    return False

            for i in range(start, end + 1):
                row_check[x][i] = True
        else:
            start = x + 1
            end = x + L

            if end >= N:
                return False

            for i in range(start, end):
                if board[i][y] != board[i + 1][y]:
                    return False

            for i in range(start, end + 1):
                col_check[i][y] = True
    return True


for i in range(N):
    for j in range(N - 1):
        if not make_ramp(i, j, 0):
            break
    else:
        res += 1

    for j in range(N - 1):
        if not make_ramp(j, i, 1):
            break
    else:
        res += 1

print(res)