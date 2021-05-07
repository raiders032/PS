"""
https://www.acmicpc.net/problem/17142
17142.연구소 3
골드4
너비우선탐색,브루트포스,그래프이론,그래프탐색
풀이1.1004ms
"""
import sys
from collections import deque


def spread():
    time = 0
    visited = [[0] * N for _ in range(N)]
    viruses = deque()
    spread_count = 0
    for virus in active_viruses:
        viruses.append(virus)
        visited[virus[0]][virus[1]] = 1

    while viruses:
        virus = viruses.popleft()
        x = virus[0]
        y = virus[1]

        for dir in range(4):
            nx = x + dx[dir]
            ny = y + dy[dir]

            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue

            if board[nx][ny] == 1 or visited[nx][ny]:
                continue

            if board[nx][ny] == 0:
                time = visited[x][y]
                spread_count += 1
            visited[nx][ny] = visited[x][y] + 1
            viruses.append((nx, ny))

    if spread_count == empty_count:
        return time
    else:
        return sys.maxsize


def activate(index):
    global ans
    if len(active_viruses) == M:
        time = spread()
        ans = min(ans, time)
        return

    for i in range(index, len(viruses)):
        active_viruses.append(viruses[i])
        activate(i + 1)
        active_viruses.pop()


ans = sys.maxsize
input = sys.stdin.readline
N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
viruses = []
active_viruses = []
empty_count = 0
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
for x in range(N):
    for y in range(N):
        if board[x][y] == 2:
            viruses.append((x, y))
        elif board[x][y] == 0:
            empty_count += 1

activate(0)
if ans == sys.maxsize:
    print(-1)
else:
    print(ans)