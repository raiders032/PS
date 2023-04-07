"""
https://www.acmicpc.net/problem/22944
22944.죽음의 비
풀이1.1544ms
"""
import sys
from collections import deque

input = sys.stdin.readline

n, h, d = map(int, input().split())
board = [list() for _ in range(n)]
visited = set()
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
start_x = 0
start_y = 0
answer = -1

for i in range(n):
    for j, value in enumerate(list(input().rstrip())):
        if value == 'S':
            start_x = i
            start_y = j

        board[i].append(value)

visited = [[0] * n for _ in range(n)]
visited[start_x][start_y] = h
queue = deque([(start_x, start_y, h, 0, 0)])

while queue:
    x, y, current_h, current_d, dist = queue.popleft()

    if board[x][y] == 'E':
        answer = dist
        break

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue

        if board[nx][ny] == 'U':
            next_h = current_h
            next_d = d - 1

        elif board[nx][ny] == 'E':
            next_h = current_h
            next_d = current_d

        else:
            if current_d:
                next_d = current_d - 1
                next_h = current_h
            else:
                next_h = current_h - 1
                next_d = current_d

        if next_h == 0:
            continue

        if next_h <= visited[nx][ny]:
            continue

        visited[nx][ny] = next_h
        queue.append((nx, ny, next_h, next_d, dist + 1))

print(answer)
