"""
14503. 로봇 청소기
골드5
구현,시뮬레이션
풀이2 64ms
"""
import sys

input = sys.stdin.readline
N, M = map(int, input().split())
x, y, d = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
is_cleaned = [[False] * M for _ in range(N)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
res = 0

while True:
    if not is_cleaned[x][y]:
        res += 1
        is_cleaned[x][y] = True

    for i in range(4):
        d = (d + 3) % 4
        nx = x + dx[d]
        ny = y + dy[d]

        if not board[nx][ny] and not is_cleaned[nx][ny]:
            x = nx
            y = ny
            break
    else:
        x = x - dx[d]
        y = y - dy[d]
        if board[x][y]:
            break
print(res)

