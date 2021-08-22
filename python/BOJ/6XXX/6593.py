"""
https://www.acmicpc.net/problem/6593
6593.상범 빌딩
골드5
풀이1.212ms
"""
import sys
from collections import deque

input = sys.stdin.readline
dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]
start_x = 0
start_y = 0
start_z = 0
end_x = 0
end_y = 0
end_z = 0


def bfs():
    q = deque([(start_x, start_y, start_z, 0)])
    visited = [[[False] * C for _ in range(R)] for _ in range(L)]
    visited[start_z][start_x][start_y] = True
    while q:
        x, y, z, dist = q.popleft()
        if x == end_x and y == end_y and z == end_z:
            print(f'Escaped in {dist} minute(s).')
            return

        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            if nx < 0 or ny < 0 or nz < 0 or nx >= R or ny >= C or nz >= L:
                continue

            if visited[nz][nx][ny] or building[nz][nx][ny] == '#':
                continue

            visited[nz][nx][ny] = True
            q.append((nx, ny, nz, dist + 1))
    print("Trapped!")


while True:
    L, R, C = map(int, input().split())

    if L == 0 and R == 0 and C == 0:
        break

    building = list()

    for k in range(L):
        raws = list()

        for i in range(R):
            raw = input().rstrip()
            raws.append(raw)
            for j, ch, in enumerate(raw):
                if ch == 'S':
                    start_x = i
                    start_y = j
                    start_z = k
                if ch == 'E':
                    end_x = i
                    end_y = j
                    end_z = k

        building.append(raws)
        input()
    bfs()