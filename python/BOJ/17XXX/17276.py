"""
https://www.acmicpc.net/problem/17276
17276.배열 돌리기
풀이1.256ms
"""
import sys
from collections import deque

input = sys.stdin.readline
answer = []

for _ in range(int(input())):
    n, d = map(int, input().split())
    board = [list(input().split()) for _ in range(n)]
    lines = [list() for _ in range(8)]

    for i in range(n // 2):
        lines[0].append(board[i][i])

    for i in range(n // 2):
        lines[1].append(board[i][n // 2])

    for i in range(n // 2):
        lines[2].append(board[i][n - i - 1])

    for i in range(n // 2):
        lines[3].append(board[n // 2][n - i - 1])

    for i in range(n // 2):
        lines[4].append(board[n - i - 1][n - i - 1])

    for i in range(n // 2):
        lines[5].append(board[n - i - 1][n // 2])

    for i in range(n // 2):
        lines[6].append(board[n - i - 1][i])

    for i in range(n // 2):
        lines[7].append(board[n // 2][i])

    lines = deque(lines)

    count = d // 45

    if count >= 0:
        for _ in range(count):
            lines.appendleft(lines.pop())
    else:
        for _ in range(-count):
            lines.append(lines.popleft())

    for i in range(n // 2):
        board[i][i] = lines[0][i]

    for i in range(n // 2):
        board[i][n // 2] = lines[1][i]

    for i in range(n // 2):
        board[i][n - i - 1] = lines[2][i]

    for i in range(n // 2):
        board[n // 2][n - i - 1] = lines[3][i]

    for i in range(n // 2):
        board[n - i - 1][n - i - 1] = lines[4][i]

    for i in range(n // 2):
        board[n - i - 1][n // 2] = lines[5][i]

    for i in range(n // 2):
        board[n - i - 1][i] = lines[6][i]

    for i in range(n // 2):
        board[n // 2][i] = lines[7][i]

    for row in board:
        answer.append(' '.join(row))

print("\n".join(answer))
