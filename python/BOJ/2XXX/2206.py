"""
https://www.acmicpc.net/problem/2206
2206.벽 부수고 이동하기
골드4
풀이1.4620ms
"""
import sys
from collections import deque


def bfs():
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    visited[0][0][0] = 1
    q = deque([(0, 0, 0)])
    while q:
        x, y, count = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue

            if not count and board[nx][ny] == '0' and visited[nx][ny][0] == -1:
                visited[nx][ny][0] = visited[x][y][0] + 1
                q.append((nx, ny, count))

            if not count and board[nx][ny] == '1' and visited[nx][ny][1] == -1:
                visited[nx][ny][1] = visited[x][y][0] + 1
                q.append((nx, ny, count + 1))

            if count and board[nx][ny] == '0' and visited[nx][ny][1] == -1:
                visited[nx][ny][1] = visited[x][y][1] + 1
                q.append((nx, ny, count))


input = sys.stdin.readline
N, M = map(int, input().split())
board = [input().rstrip() for _ in range(N)]
visited = [[[-1] * 2 for _ in range(M)] for _ in range(N)]
bfs()
if min(visited[N-1][M-1]) == -1:
    print(max(visited[N-1][M-1]))
else:
    print(min(visited[N-1][M-1]))

"""
5 5
01000
01010
01010
01011
00010
---

5 5
01000
01010
01010
01010
00010
"""