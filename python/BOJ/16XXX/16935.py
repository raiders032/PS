"""
https://www.acmicpc.net/problem/16935
16935.배열 돌리기 3
풀이1.924ms
"""
import sys

input = sys.stdin.readline

n, m, r = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

for command in input().rstrip().split():
    if command == '1':
        board = board[::-1]

    elif command == '2':
        board = [row[::-1] for row in board]

    elif command == '3':
        board = list(map(list, map(reversed, zip(*board))))
        n, m = m, n

    elif command == '4':
        board = list(map(list, zip(*board)))
        board = board[::-1]
        n, m = m, n

    elif command == '5':
        temp_board = [[0] * m for _ in range(n)]

        for i in range(n // 2):
            for j in range(m // 2):
                temp_board[i][j + m // 2] = board[i][j]

        for i in range(n // 2):
            for j in range(m // 2, m):
                temp_board[i + n // 2][j] = board[i][j]

        for i in range(n // 2, n):
            for j in range(m // 2, m):
                temp_board[i][j - m // 2] = board[i][j]

        for i in range(n // 2, n):
            for j in range(m // 2):
                temp_board[i - n // 2][j] = board[i][j]

        board = temp_board

    elif command == '6':
        temp_board = [[0] * m for _ in range(n)]

        for i in range(n // 2):
            for j in range(m // 2):
                temp_board[i + n // 2][j] = board[i][j]

        for i in range(n // 2, n):
            for j in range(m // 2):
                temp_board[i][j + m // 2] = board[i][j]

        for i in range(n // 2, n):
            for j in range(m // 2, m):
                temp_board[i - n // 2][j] = board[i][j]

        for i in range(n // 2):
            for j in range(m // 2, m):
                temp_board[i][j - m // 2] = board[i][j]

        board = temp_board

for row in board:
    print(' '.join(map(str, row)))
