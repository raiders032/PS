"""
https://www.acmicpc.net/problem/10026
10026.적록색약
골드5
풀이1.112ms
"""
import sys
sys.setrecursionlimit(10 ** 6)


def dfs(x, y):
    visited[x][y] = True
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= N or ny < 0 or ny >= N:
            continue
        if visited[nx][ny] or board[nx][ny] != board[x][y]:
            continue
        dfs(nx, ny)


input = sys.stdin.readline
N = int(input())
board = [list(input().rstrip()) for _ in range(N)]
visited = [[False] * N for _ in range(N)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
ans = [0] * 2

for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            dfs(i, j)
            ans[0] += 1

for i in range(N):
    for j in range(N):
        if board[i][j] == 'G':
            board[i][j] = 'R'

visited = [[False] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            dfs(i, j)
            ans[1] += 1

print(*ans)