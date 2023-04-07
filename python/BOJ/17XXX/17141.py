"""
https://www.acmicpc.net/problem/17141
17141.연구소 2
풀이1.812ms
"""
import sys
import collections
from itertools import combinations
input = sys.stdin.readline


def spread_virus(virus):
    visited = [[0] * N for _ in range(N)]
    q = collections.deque()
    elapsed_seconds = 0
    count = 0

    for x, y in virus:
        q.append((x, y))
        visited[x][y] = 1

    while q:
        x, y = q.popleft()
        elapsed_seconds = visited[x][y] - 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= N or ny >= N:
                continue

            if visited[nx][ny] or board[nx][ny] == 1:
                continue

            visited[nx][ny] = visited[x][y] + 1
            q.append((nx, ny))
            count += 1

    return elapsed_seconds if empty_count == count else -1


dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
N, M = map(int, input().split())
board = [[0] * N for _ in range(N)]
virus = []
sheep_count = sys.maxsize
empty_count = 0
for i in range(N):
    for j, number in enumerate(map(int, input().rstrip().split())):
        board[i][j] = number
        if number == 2:
            virus.append((i, j))
        if number == 0:
            empty_count += 1
empty_count += len(virus) - M

for virus_list in combinations(virus, M):
    seconds = spread_virus(virus_list)
    if seconds == -1:
        continue
    sheep_count = min(sheep_count, seconds)

print(sheep_count if sheep_count != sys.maxsize else -1)
