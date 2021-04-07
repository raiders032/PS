"""
https://www.acmicpc.net/problem/7562
7562.나이트의 이동
실버2
BFS,그래프이론,그래프탐색
풀이2. 2648ms
"""
import sys
from collections import deque


def bfs(start_x, start_y):
    visited = [[0] * length for _ in range(length)]
    queue = deque([(start_x, start_y)])
    visited[start_x][start_y] = 1
    while queue:
        x, y = queue.popleft()

        if x == end_x and y == end_y:
            return visited[x][y] - 1

        for dir in range(8):
            nx = x + dx[dir]
            ny = y + dy[dir]
            if nx < 0 or nx >= length or ny < 0 or ny >= length:
                continue

            if visited[nx][ny]:
                continue

            visited[nx][ny] = visited[x][y] + 1
            queue.append((nx, ny))



input = sys.stdin.readline
N = int(input())
dx = [-2, -1, 1, 2, 2, 1, -1, -2]
dy = [1, 2, 2, 1, -1, -2, -2, -1]

for _ in range(N):
    length = int(input())
    start_x, start_y = map(int, input().split())
    end_x, end_y = map(int, input().split())
    print(bfs(start_x, start_y))
