"""
https://www.acmicpc.net/problem/16926
16926.배열 돌리기 1
실버4
풀이2.
"""
import sys

input = sys.stdin.readline

N, M, R = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(M)]
print(board)


def rotate(x, y, width, height):
    print(f'x:{x}, y:{y}, width:{width}, height:{height}')
    tmp = board[x][y]

    for j in range(y, y + width - 1):
        board[x][j] = board[x][j + 1]

    for i in range(x, x + height - 2):
        board[i][y + width - 1] = board[i + 1][y + width - 1]

    for j in range(y + width - 1, y, -1):
        board[x + height - 1][j] = board[x + height - 1][j - 1]

    for i in range(x + height - 1, x, -1):
        board[i][y] = board[i - 1][y]

    board[x + 1][y] = tmp


i = 0
while i < min(N, M) // 2:
    for _ in range(R):
        rotate(i, i, M - (2 * i), N - (2 * i))
    i += 1

print(board)
