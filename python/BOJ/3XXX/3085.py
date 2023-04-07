'''
3085번 사탕게임
실버4
브루트포스
풀이3.280ms
'''
import sys


def check(x, y):
    global max_length
    length = 1
    for i in range(1, N):
        if board[x][i] == board[x][i - 1]:
            length += 1
            max_length = max(max_length, length)
        else:
            length = 1

    length = 1
    for i in range(1, N):
        if board[i][y] == board[i - 1][y]:
            length += 1
            max_length = max(max_length, length)
        else:
            length = 1

    if x < N - 1:
        length = 1
        for i in range(1, N):
            if board[x + 1][i] == board[x + 1][i - 1]:
                length += 1
                max_length = max(max_length, length)
            else:
                length = 1

    if y < N - 1:
        length = 1
        for i in range(1, N):
            if board[i][y + 1] == board[i - 1][y + 1]:
                length += 1
                max_length = max(max_length, length)
            else:
                length = 1


input = sys.stdin.readline
N = int(input())
board = [list(input().rstrip()) for _ in range(N)]
max_length = 0

for i in range(N):
    for j in range(N):
        if i < N - 1:
            board[i][j], board[i + 1][j] = board[i + 1][j], board[i][j]
            check(i, j)
            board[i][j], board[i + 1][j] = board[i + 1][j], board[i][j]
        if j < N - 1:
            board[i][j], board[i][j + 1] = board[i][j + 1], board[i][j]
            check(i, j)
            board[i][j], board[i][j + 1] = board[i][j + 1], board[i][j]
print(max_length)