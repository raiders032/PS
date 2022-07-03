"""
https://www.acmicpc.net/problem/2234
2234.성곽
골드4
풀이1.100ms
"""
import sys
from collections import deque
input = sys.stdin.readline


def visit(x, y, room_number):
    area = 1
    q = deque()
    q.append((x, y))
    visited[x][y] = room_number

    while q:
        x, y = q.popleft()

        for i in range(4):
            if board[x][y][i]:
                continue
            nx = x + dx[i]
            ny = y + dy[i]
            if visited[nx][ny]:
                continue

            q.append((nx, ny))
            visited[nx][ny] = room_number
            area += 1

    return area


M, N = map(int, input().split())
board = [[[0] * 4 for _ in range(M)] for _ in range(N)]
visited = [[0] * M for _ in range(N)]
room_area = [0]
dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]
for i in range(N):
    for j, value in enumerate(map(int, input().split())):
        for k in range(4):
            board[i][j][k] = value % 2
            value = value // 2

answer = [0, 0, 0]
room_count = 0
max_area = 0
max_two_area = 0
for i in range(N):
    for j in range(M):
        if visited[i][j]:
            continue
        room_count += 1
        room_area.append(visit(i, j, room_count))
        max_area = max(max_area, room_area[-1])

adjacent_rooms = [set() for _ in range(room_count + 1)]

for i in range(N):
    for j in range(M - 1):
        if visited[i][j] == visited[i][j + 1]:
            continue
        adjacent_rooms[visited[i][j]].add(visited[i][j + 1])

for j in range(M):
    for i in range(N - 1):
        if visited[i][j] == visited[i + 1][j]:
            continue
        adjacent_rooms[visited[i][j]].add(visited[i + 1][j])

for i in range(1, room_count):
    for adjacent_room in adjacent_rooms[i]:
        max_two_area = max(max_two_area, room_area[i] + room_area[adjacent_room])

print(room_count)
print(max_area)
print(max_two_area)