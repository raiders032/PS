"""
https://www.acmicpc.net/problem/2206
2206.벽 부수고 이동하기
풀이2.5076ms
"""
import sys
from collections import deque

input = sys.stdin.readline


def solve():
    dx = [1, 0, -1, 0]
    dy = [0, -1, 0, 1]
    visited[0][0][0] = 1
    q = deque()
    q.append((0, 0, 0))
    while q:
        x, y, count = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                continue

            if not count:
                if board[nx][ny]:
                    if visited[nx][ny][1] != -1:
                        continue
                    visited[nx][ny][1] = visited[x][y][0] + 1
                    q.append((nx, ny, count + 1))
                else:
                    if visited[nx][ny][0] != -1:
                        continue
                    visited[nx][ny][0] = visited[x][y][0] + 1
                    q.append((nx, ny, count))
                continue

            if board[nx][ny] or visited[nx][ny][1] != -1:
                continue
            visited[nx][ny][1] = visited[x][y][1] + 1
            q.append((nx, ny, count))


N, M = map(int, input().split())
board = [list(map(int, input().rstrip())) for _ in range(N)]
visited = [[[-1, -1] for _ in range(M)] for _ in range(N)]
solve()
if visited[N - 1][M - 1][1] == -1:
    print(visited[N-1][M-1][0])
else:
    print(visited[N-1][M-1][1])


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

---
3 3
000
000
000
"""
