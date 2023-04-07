"""
https://www.acmicpc.net/problem/6593
6593.상범 빌딩
골드5
풀이2.212ms
"""
import sys
from collections import deque

input = sys.stdin.readline


def bfs(z, x, y):
    dx = [1, 0, -1, 0, 0, 0]
    dy = [0, 1, 0, -1, 0, 0]
    dz = [0, 0, 0, 0, 1, -1]
    q = deque([(z, x, y)])
    visited = [[[0] * C for _ in range(R)] for _ in range(L)]
    visited[z][x][y] = 1

    while q:
        z, x, y = q.popleft()
        if (z, x, y) == end_location:
            return visited[z][x][y] - 1
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            if nx < 0 or nx >= R or ny < 0 or ny >= C or nz < 0 or nz >= L:
                continue
            if visited[nz][nx][ny] or building[nz][nx][ny] == '#':
                continue
            visited[nz][nx][ny] = visited[z][x][y] + 1
            q.append((nz, nx, ny))

    return -1


while True:
    L, R, C = map(int, input().split())
    if L == 0 and R == 0 and C == 0:
        break

    building = [[[0] * C for _ in range(R)] for _ in range(L)]

    for z in range(L):
        for x in range(R):
            for y, char in enumerate(list(input().rstrip())):
                if char == 'S':
                    start_location = (z, x, y)
                if char == 'E':
                    end_location = (z, x, y)
                building[z][x][y] = char
        input()

    result = bfs(start_location[0], start_location[1], start_location[2])
    if result == -1:
        print('Trapped!')
    else:
        print(f'Escaped in {result} minute(hhmmss).')