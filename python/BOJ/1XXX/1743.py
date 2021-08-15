"""
https://www.acmicpc.net/problem/1743
1743.음식물 피하기
실버1
풀이1.104ms
"""
import sys
from collections import deque


def bfs(x, y):
    global count
    visited[x][y] = True
    que = deque([(x, y)])
    while que:
        x, y = que.popleft()
        count += 1

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if visited[nx][ny] or board[nx][ny] == 0:
                continue
            visited[nx][ny] = True
            que.append((nx, ny))



input = sys.stdin.readline
N, M, K = map(int, input().split())
board = [[0] * M for _ in range(N)]
visited = [[False] * M for _ in range(N)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
ans = 0

for _ in range(K):
    x, y = map(int, input().split())
    board[x - 1][y - 1] = 1

for i in range(N):
    for j in range(M):
        if not visited[i][j] and board[i][j]:
            count = 0
            bfs(i, j)
            ans = max(ans, count)

print(ans)