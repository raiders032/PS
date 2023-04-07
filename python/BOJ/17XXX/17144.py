"""
https://www.acmicpc.net/problem/17144
17144.미세먼지 안녕!
골드4
풀이1.740ms
"""
import sys
input = sys.stdin.readline


def diffuse():
    global board
    temp_board = [[0] * C for _ in range(R)]
    temp_board[upper_x][0] = -1
    temp_board[lower_x][0] = -1

    for x in range(R):
        for y in range(C):
            if board[x][y] <= 0:
                continue
            count = get_count(x, y)
            temp_board[x][y] += board[x][y] - (board[x][y] // 5) * count
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or ny < 0 or nx >= R or ny >= C:
                    continue
                if board[nx][ny] == -1:
                    continue
                temp_board[nx][ny] += board[x][y] // 5

    board = temp_board


def get_count(x, y):
    count = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or ny < 0 or nx >= R or ny >= C:
            continue

        if board[nx][ny] == -1:
            continue

        count += 1
    return count


def clean_air():
    for x in range(upper_x - 1, 0, -1):
        board[x][0] = board[x - 1][0]

    for y in range(C - 1):
        board[0][y] = board[0][y + 1]

    for x in range(upper_x):
        board[x][C - 1] = board[x + 1][C - 1]

    for y in range(C - 1, 1, -1):
        board[upper_x][y] = board[upper_x][y - 1]

    for x in range(lower_x + 1, R - 1):
        board[x][0] = board[x + 1][0]

    for y in range(C - 1):
        board[R - 1][y] = board[R - 1][y + 1]

    for x in range(R - 1, lower_x, -1):
        board[x][C - 1] = board[x - 1][C - 1]

    for y in range(C - 1, 1, -1):
        board[lower_x][y] = board[lower_x][y - 1]

    board[upper_x][1] = 0
    board[lower_x][1] = 0


R, C, T = map(int, input().split())
board = [[0] * C for _ in range(R)]
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
upper_x = 0
lower_x = 0

for i in range(R):
    for j, value in enumerate(map(int, input().rstrip().split())):
        board[i][j] = value
        if value == -1:
            lower_x = i


upper_x = lower_x - 1

for _ in range(T):
    diffuse()
    clean_air()

sheep_count = 2
for row in board:
    sheep_count += sum(row)
print(sheep_count)