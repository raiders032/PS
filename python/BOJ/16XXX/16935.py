"""
16935.배열 돌리기 3
실버3
"""
import sys
from collections import deque

input = sys.stdin.readline
N, M, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]


def operation(op_num):
    global board, N, M
    tmp_board = deque()
    if op_num == 1:
        for row in board:
            tmp_board.appendleft(row)
    elif op_num == 2:
        for row in board:
            tmp_board.append(row[::-1])
    elif op_num == 3:
        tmp_board = [[] for _ in range(M)]
        for r in range(N - 1, -1, -1):
            for c in range(M):
                tmp_board[c].append(board[r][c])
        N, M = M, N
    elif op_num == 4:
        tmp_board = [[] for _ in range(M)]
        for r in range(N):
            for c in range(M - 1, -1, -1):
                tmp_board[M - c - 1].append(board[r][c])
        N, M = M, N
    elif op_num == 5:
        tmp_board = [[] for _ in range(N)]
        for r in range(N // 2, N):
            for c in range(0, M // 2):
                tmp_board[r - N // 2].append(board[r][c])
        for r in range(0, N // 2):
            for c in range(0, M // 2):
                tmp_board[r].append(board[r][c])
        for r in range(N // 2, N):
            for c in range(M // 2, M):
                tmp_board[r].append(board[r][c])
        for r in range(0, N // 2):
            for c in range(M // 2, M):
                tmp_board[r + N // 2].append(board[r][c])
    elif op_num == 6:
        tmp_board = [[] for _ in range(N)]
        for r in range(0, N // 2):
            for c in range(M // 2, M):
                tmp_board[r].append(board[r][c])
        for r in range(N // 2, N):
            for c in range(M // 2, M):
                tmp_board[r - N // 2].append(board[r][c])
        for r in range(0, N // 2):
            for c in range(0, M // 2):
                tmp_board[r + N // 2].append(board[r][c])
        for r in range(N // 2, N):
            for c in range(0, M // 2):
                tmp_board[r].append(board[r][c])
    board = tmp_board


op_list = list(map(int, input().split()))
for op in op_list:
    operation(op)
for row in board:
    for item in row:
        print(item, end=' ')
    print()
