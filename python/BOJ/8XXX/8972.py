"""
https://www.acmicpc.net/problem/8972
8972.미친 아두이노
풀이1.
"""
import sys
from collections import deque

input = sys.stdin.readline

R, C = map(int, input().split())
arduino_x = 0
arduino_y = 0
crazy_arduinos = deque()
board = [[0] * C for _ in range(R)]
dx = [0, 1, 1, 1, 0, 0, 0, -1, -1, -1]
dy = [0, -1, 0, 1, -1, 0, 1, -1, 0, 1]

for x in range(R):
    for y, value in enumerate(input().rstrip()):
        board[x][y] = value
        if value == 'I':
            arduino_x = x
            arduino_y = y
        elif value == 'R':
            crazy_arduinos.append((x, y))

commands = deque(map(int, input().rstrip()))
# print(f'arduino: ({arduino_x, arduino_y}), crazy_arduinos:{crazy_arduinos}')

sheep_count = 0
game_over = False
while commands:
    command = commands.popleft()

    nx = arduino_x + dx[command]
    ny = arduino_y + dy[command]

    if board[nx][ny] == 'R':
        break

    board[arduino_x][arduino_y] = '.'
    board[nx][ny] = 'I'
    arduino_x = nx
    arduino_y = ny

    duplicate_arduinos = set()
    for _ in range(len(crazy_arduinos)):
        crazy_arduino = crazy_arduinos.popleft()
        min_distance = sys.maxsize
        direction = 0

        for i in range(1, 10):
            nx = crazy_arduino[0] + dx[i]
            ny = crazy_arduino[1] + dy[i]
            distance = abs(arduino_x - nx) + abs(arduino_y - ny)
            if distance < min_distance:
                min_distance = distance
                direction = i

        nx = crazy_arduino[0] + dx[direction]
        ny = crazy_arduino[1] + dy[direction]
        if direction != 5 and board[nx][ny] == 'R':
            duplicate_arduinos.add((nx, ny))

        if board[nx][ny] == 'I':
            game_over = True
            break

        board[crazy_arduino[0]][crazy_arduino[1]] = '.'
        board[nx][ny] = 'R'
        crazy_arduinos.append((nx, ny))

    for _ in range(len(crazy_arduinos)):
        crazy_arduino = crazy_arduinos.popleft()
        if crazy_arduino in duplicate_arduinos:
            board[crazy_arduino[0]][crazy_arduino[1]] = '.'
            continue
        crazy_arduinos.append(crazy_arduino)

    sheep_count += 1

if game_over:
    print(f'kraj {sheep_count}')
else:
    for row in board:
        print(*row, sep="")
