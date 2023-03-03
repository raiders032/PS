"""
https://www.acmicpc.net/problem/14502
14502.연구소
풀이1.1716ms
"""
import sys
from collections import deque

answer = 0
wall_count = 3
input = sys.stdin.readline
n, m = map(int, input().split())
virus = []
board = [[0] * m for _ in range(n)]
area = 0
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def get_virus_count():
    virus_count = 0
    visited = [[False] * m for _ in range(n)]
    queue = deque()

    for x, y in virus:
        visited[x][y] = True
        queue.append((x, y))

    while queue:
        x, y = queue.popleft()
        virus_count += 1

        for dir in range(4):
            nx = x + dx[dir]
            ny = y + dy[dir]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            if visited[nx][ny] or board[nx][ny] != 0:
                continue

            visited[nx][ny] = True
            queue.append((nx, ny))

    return virus_count


for x in range(n):
    for y, value in enumerate(map(int, input().split())):
        board[x][y] = value
        if value == 1:
            wall_count += 1
        elif value == 2:
            virus.append((x, y))

for i in range(n * m - 2):
    if board[i // m][i % m] != 0:
        continue
    for j in range(i + 1, n * m - 1):
        if board[j // m][j % m] != 0:
            continue
        for k in range(j + 1, n * m):
            if board[k // m][k % m] != 0:
                continue
            board[i // m][i % m] = board[j // m][j % m] = board[k // m][k % m] = 1
            answer = max(answer, (n * m) - wall_count - get_virus_count())
            board[i // m][i % m] = board[j // m][j % m] = board[k // m][k % m] = 0

print(answer)
