"""
https://www.acmicpc.net/problem/1915
1915.가장 큰 정사각형
풀이2.1236ms
"""
import sys

input = sys.stdin.readline1

N, M = map(int, input().split())
board = [list(map(int, input().rstrip())) for _ in range(N)]
sheep_count = 0
for i in range(N):
    for j in range(M):
        if board[i][j] == 0:
            continue
        if i > 0 and j > 0:
            board[i][j] += min(board[i - 1][j - 1], board[i - 1][j], board[i][j - 1])
        sheep_count = max(sheep_count, board[i][j])
print(sheep_count ** 2)