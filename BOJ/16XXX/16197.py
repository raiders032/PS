"""
16197.두 동전
골드4
그래프이론,그래프탐색,너비우선탐색,백트래킹
풀이1. 100ms(너비우선탐색)
"""
import sys
from collections import deque


def bfs():
    q = deque()
    q.append((coins[0][0], coins[0][1], coins[1][0], coins[1][1]))
    visited[coins[0][0]][coins[0][1]][coins[1][0]][coins[1][1]] = 1

    while q:
        x1, y1, x2, y2 = q[0]
        q.popleft()

        if visited[x1][y1][x2][y2] > 10:
            return -1

        for dir in range(4):
            nx1 = x1 + dx[dir]
            ny1 = y1 + dy[dir]
            nx2 = x2 + dx[dir]
            ny2 = y2 + dy[dir]

            if (nx1 < 0 or nx1 >= N or ny1 < 0 or ny1 >= M) and (nx2 < 0 or nx2 >= N or ny2 < 0 or ny2 >= M):
                continue

            if (nx1 < 0 or nx1 >= N or ny1 < 0 or ny1 >= M) or (nx2 < 0 or nx2 >= N or ny2 < 0 or ny2 >= M):
                return visited[x1][y1][x2][y2]

            if board[nx1][ny1] == '#':
                nx1 = x1
                ny1 = y1

            if board[nx2][ny2] == '#':
                nx2 = x2
                ny2 = y2

            if visited[nx1][ny1][nx2][ny2]:
                continue

            visited[nx1][ny1][nx2][ny2] = visited[x1][y1][x2][y2] + 1
            q.append((nx1, ny1, nx2, ny2))
    return -1


input = sys.stdin.readline
N, M = map(int, input().split())
board = [list() for _ in range(N)]
coins = []
visited = [[[[0] * M for _ in range(N)] for _ in range(M)] for _ in range(N)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for x in range(N):
    row = list(input().rstrip())
    for y in range(len(row)):
        if row[y] == 'o':
            coins.append((x, y))
        board[x].append(row[y])

print(bfs())
