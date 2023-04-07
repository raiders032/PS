"""
https://www.acmicpc.net/problem/5427
5427.불
풀이1.956ms(PyPy3)
"""
import sys
from collections import deque
input = sys.stdin.readline

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

for _ in range(int(input())):
    w, h = map(int, input().split())
    fire_queue = deque()
    fire_visited = [[-1] * w for _ in range(h)]
    human_queue = deque()
    human_visited = [[-1] * w for _ in range(h)]
    board = [[0] * w for _ in range(h)]

    for i in range(h):
        for j, value in enumerate(input().rstrip()):
            board[i][j] = value
            if value == '*':
                fire_visited[i][j] = 0
                fire_queue.append((i, j))
            elif value == '@':
                human_visited[i][j] = 0
                human_queue.append((i, j))

    while fire_queue:
        x, y = fire_queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= h or ny < 0 or ny >= w:
                continue

            if fire_visited[nx][ny] != -1 or board[nx][ny] == "#":
                continue

            fire_visited[nx][ny] = fire_visited[x][y] + 1
            fire_queue.append((nx, ny))

    is_valid = False
    while human_queue:
        x, y = human_queue.popleft()

        if x == 0 or x == h - 1 or y == 0 or y == w - 1:
            is_valid = True
            print(human_visited[x][y] + 1)
            break

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= h or ny < 0 or ny >= w:
                continue

            if human_visited[nx][ny] != -1 or board[nx][ny] == "#":
                continue

            if 0 <= fire_visited[nx][ny] <= human_visited[x][y] + 1:
                continue

            human_visited[nx][ny] = human_visited[x][y] + 1
            human_queue.append((nx, ny))

    if not is_valid:
        print("IMPOSSIBLE")



"""
1
3 3
...
@..
***

1
---
1
7 7
#.#####
#.....#
#####.#
#....*#
####.##
#@....#
#####.#

IMPOSSIBLE
---
1
4 5
####
#*##
#...
#@##
####

IMPOSSIBLE
---
1
12 5
############
#.#....@..##
#....#.#...#
.#..##...##.
.#..#####.#.

7
---
1
5 7
...#*
..##.
##.#.
#@...
##.#.
..##.
...#*

IMPOSSIBLE
---
1
7 6
###.###
#*#.#*#
#.....#
#.....#
#..@..#
#######

5
"""
