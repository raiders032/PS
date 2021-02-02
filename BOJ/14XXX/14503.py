"""
14503. 로봇 청소기
골드5
구현,시뮬레이션
"""
import sys


def clean_and_search(x, y):
    global r, c, d, res
    if not visited[x][y]:
        visited[x][y] = True
        res += 1
    for i in range(1, 5):
        dir = d - i if d - i >= 0 else 4 - abs(d - i)
        nx = x + dx[dir]
        ny = y + dy[dir]
        if nx < 0 or nx >= N or ny < 0 or ny >= M:
            continue
        if not board[nx][ny] and not visited[nx][ny]:
            d = dir
            r = r + dx[dir]
            c = c + dy[dir]
            return True
    else:
        dir = (d + 2) % 4
        nx = x + dx[dir]
        ny = y + dy[dir]
        if 0 <= nx < N and 0 <= ny < M and not board[nx][ny]:
            r = r + dx[dir]
            c = c + dy[dir]
            return True
        else:
            return False


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
input = sys.stdin.readline
N, M = map(int, input().split())
r, c, d = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]
res = 0
while True:
    if not clean_and_search(r, c):
        break
print(res)