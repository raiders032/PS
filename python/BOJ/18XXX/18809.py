"""
https://www.acmicpc.net/problem/18809
18809.Gaaaaaaaaaarden
풀이1.
"""
import sys
import itertools
from collections import deque

input = sys.stdin.readline


def get_flower_count():
    count = 0
    red_queue = deque()
    red_visited = [[sys.maxsize] * M for _ in range(N)]
    green_queue = deque()
    green_visited = [[sys.maxsize] * M for _ in range(N)]
    dx = [1, 0, -1, 0]
    dy = [0, -1, 0, 1]

    for i in range(N):
        for j in range(M):
            if board[i][j] == 'R':
                red_queue.append((i, j))
                red_visited[i][j] = 0
            elif board[i][j] == "G":
                green_queue.append((i, j))
                green_visited[i][j] = 0

    while red_queue or green_queue:
        red_temp = set()

        for _ in range(len(red_queue)):
            x, y = red_queue.popleft()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if nx < 0 or nx >= N or ny < 0 or ny >= M:
                    continue

                if board[nx][ny] == 0:
                    continue

                if red_visited[x][y] + 1 >= red_visited[nx][ny] or red_visited[x][y] + 1 >= green_visited[nx][ny]:
                    continue

                red_visited[nx][ny] = red_visited[x][y] + 1
                red_temp.add((nx, ny))

        for _ in range(len(green_queue)):
            x, y = green_queue.popleft()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if nx < 0 or nx >= N or ny < 0 or ny >= M:
                    continue

                if board[nx][ny] == 0:
                    continue

                if green_visited[x][y] + 1 > red_visited[nx][ny] or green_visited[x][y] + 1 >= green_visited[nx][ny]:
                    continue

                if green_visited[x][y] + 1 == red_visited[nx][ny]:
                    count += 1
                    red_temp.remove((nx, ny))
                else:
                    green_queue.append((nx, ny))
                green_visited[nx][ny] = green_visited[x][y] + 1

        for red in red_temp:
            red_queue.append(red)

    return count


N, M, G, R = map(int, input().split())
yellow_zone = list()
original_board = [[0] * M for _ in range(N)]

for i in range(N):
    for j, value in enumerate(map(int, input().split())):
        original_board[i][j] = value
        if value == 2:
            yellow_zone.append((i, j))

red_green = []
for _ in range(R):
    red_green.append("R")

for _ in range(G):
    red_green.append("G")

for _ in range(len(yellow_zone) - R - G):
    red_green.append(1)

sheep_count = 0
for r in itertools.permutations(red_green):
    board = original_board.copy()

    for index, RG in enumerate(r):
        board[yellow_zone[index][0]][yellow_zone[index][1]] = RG

    sheep_count = max(sheep_count, get_flower_count())

print(sheep_count)
