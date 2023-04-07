"""
https://www.acmicpc.net/problem/7576
7576.토마토
실버1
풀이1.3428ms
"""
import sys
from collections import deque

input = sys.stdin.readline
M, N = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
count = 0
que = deque()
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
ans = 0
for i in range(N):
    for j in range(M):
        if board[i][j] == 1:
            que.append((i, j))
            visited[i][j] = 1
        elif board[i][j] == 0:
            count += 1

while que:
    (x, y) = que.popleft()
    ans = visited[x][y]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= N or ny < 0 or ny >= M:
            continue
        if board[nx][ny] != 0 or visited[nx][ny] > 0:
            continue

        visited[nx][ny] = visited[x][y] + 1
        count -= 1
        que.append((nx, ny))

if count:
    print(-1)
else:
    print(ans - 1)
