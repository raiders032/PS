"""
https://www.acmicpc.net/problem/3187
3187.양치기 꿍
풀이1.116ms
"""
import sys
from collections import deque

input = sys.stdin.readline


def visit(start_x, start_y):
    queue = deque([(start_x, start_y)])
    visited[start_x][start_y] = True
    sheep_count = 0
    wolf_count = 0

    while queue:
        x, y = queue.popleft()

        if board[x][y] == 'v':
            wolf_count += 1
        elif board[x][y] == 'k':
            sheep_count += 1

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= r or ny < 0 or ny >= c:
                continue

            if visited[nx][ny] or board[nx][ny] == '#':
                continue

            visited[nx][ny] = True
            queue.append((nx, ny))

    if wolf_count < sheep_count:
        wolf_count = 0
    else:
        sheep_count = 0

    return sheep_count, wolf_count


r, c = map(int, input().split())
board = [list(input().rstrip()) for _ in range(r)]
visited = [[False] * c for _ in range(r)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
answer = [0, 0]

for i in range(r):
    for j in range(c):
        if visited[i][j] or board[i][j] == '#':
            continue
        sheep_count, wolf_count = visit(i, j)
        answer[0] += sheep_count
        answer[1] += wolf_count

print(' '.join(map(str, answer)))
