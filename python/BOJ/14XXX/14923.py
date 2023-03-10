"""
https://www.acmicpc.net/problem/14923
14923.미로 탈출
풀이1.2532ms
"""
from collections import deque
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
start_x, start_y = map(lambda z: int(z) - 1, input().split())
end_x, end_y = map(lambda z: int(z) - 1, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
visited = [[[False] * 2 for _ in range(m)] for _ in range(n)]
visited[start_x][start_y][0] = True
queue = deque([(start_x, start_y, 0, 0)])
answer = -1

while queue:
    x, y, distance, wall_count = queue.popleft()

    if x == end_x and y == end_y:
        answer = distance
        break

    for direction in range(4):
        nx = x + dx[direction]
        ny = y + dy[direction]

        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue

        if board[nx][ny] == 1:
            if wall_count or visited[nx][ny][1]:
                continue

            visited[nx][ny][1] = True
            queue.append((nx, ny, distance + 1, wall_count + 1))
            continue

        if wall_count:
            if visited[nx][ny][1]:
                continue

            visited[nx][ny][1] = True
            queue.append((nx, ny, distance + 1, wall_count))
            continue

        if visited[nx][ny][0]:
            continue

        visited[nx][ny][0] = True
        queue.append((nx, ny, distance + 1, wall_count))

print(answer)
