"""
2468번 안전 영역 실버1
브루트포스, 깊이우선탐색, 그래프이론, 그래프탐색
"""

from collections import deque
import sys
sys.setrecursionlimit(10**6)
N = int(input())
board = []
visited = [[False] * N for _ in range(N)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
min_h = 1000
max_h = 0
res = 1


def bfs(x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = True
    while q:
        x = q[0][0]
        y = q[0][1]
        q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            if visited[nx][ny]:
                continue
            visited[nx][ny] = True
            q.append((nx, ny))


for i in range(N):
    row = list(map(int, input().split()))
    min_h = min(min_h, min(row))
    max_h = max(max_h, max(row))
    board.append(row)

for h in range(min_h, max_h):
    cnt = 0
    for x in range(N):
        for y in range(N):
            if board[x][y] <= h:
                visited[x][y] = True
            else:
                visited[x][y] = False

    for x in range(N):
        for y in range(N):
            if visited[x][y]:
                continue
            cnt += 1
            bfs(x, y)
    res = max(res, cnt)
print(res)
