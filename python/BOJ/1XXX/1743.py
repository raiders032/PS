"""
https://www.acmicpc.net/problem/1743
1743.음식물 피하기
실버1
풀이2.108ms
"""
import sys
from collections import deque


def visit(x, y):
    q = deque([(x, y)])
    visited[x][y] = True
    area = 0
    while q:
        x, y = q.popleft()
        area += 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if board[nx][ny] == 0 or visited[nx][ny]:
                continue
            visited[nx][ny] = True
            q.append((nx, ny))
    return area


input = sys.stdin.readline
N, M, K = map(int, input().split())
board = [[0] * M for _ in range(N)]
visited = [[False] * M for _ in range(N)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for _ in range(K):
    x, y = map(int, input().split())
    board[x - 1][y - 1] = 1

sheep_count = 0
for x in range(N):
    for y in range(M):
        if visited[x][y] or board[x][y] == 0:
            continue
        sheep_count = max(sheep_count, visit(x, y))
print(sheep_count)
