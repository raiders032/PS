"""
16926.배열 돌리기 1
실버4
구현
풀이1. 220ms
"""
import sys
from collections import deque

input = sys.stdin.readline
N, M, R = map(int, input().split())
group_num = min(N, M) // 2
board = [list(map(int, input().split())) for _ in range(N)]
group = [deque() for _ in range(group_num)]

for gn in range(group_num):
    for i in range(gn, M - gn - 1):
        group[gn].append(board[gn][i])

    for i in range(gn, N - gn - 1):
        group[gn].append(board[i][M - gn - 1])

    for i in range(M - gn - 1, gn, -1):
        group[gn].append(board[N - gn - 1][i])

    for i in range(N - gn - 1, gn, -1):
        group[gn].append(board[i][gn])

for gn in range(len(group)):
    r = R % len(group[gn])

    for j in range(r):
        group[gn].append(group[gn].popleft())

    for j in range(gn, M - gn - 1):
        board[gn][j] = group[gn].popleft()

    for j in range(gn, N - gn - 1):
        board[j][M - gn - 1] = group[gn].popleft()

    for j in range(M - gn - 1, gn, -1):
        board[N - gn - 1][j] = group[gn].popleft()

    for j in range(N - gn - 1, gn, -1):
        board[j][gn] = group[gn].popleft()

for i in range(N):
    for j in range(M):
        print(board[i][j], end=' ')
    print()
