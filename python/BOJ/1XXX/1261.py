"""
https://www.acmicpc.net/problem/1261
1261.알고스팟
골드4
풀이1.312ms
"""
import sys
from collections import deque

input = sys.stdin.readline
M, N = map(int, input().split())
board = [list(input().rstrip()) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

q = deque([(0, 0)])
visited[0][0] = 1

while q:
    (x, y) = q.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= N or ny < 0 or ny >= M:
            continue

        if board[nx][ny] == '1':
            if visited[nx][ny] == 0 or visited[x][y] + 1 < visited[nx][ny]:
                visited[nx][ny] = visited[x][y] + 1
                q.append((nx, ny))

        else:
            if visited[nx][ny] == 0 or visited[x][y] < visited[nx][ny]:
                visited[nx][ny] = visited[x][y]
                q.append((nx, ny))

print(visited[N - 1][M - 1] - 1)