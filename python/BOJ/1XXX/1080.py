"""
https://www.acmicpc.net/problem/1080
1080.행렬
실버2
풀이2.348ms
"""
import sys


def operate(x, y):
    for i in range(x, x + 3):
        for j in range(y, y + 3):
            board[i][j] = '1' if board[i][j] == '0' else '0'


def is_same():
    for i in range(N):
        for j in range(M):
            if board[i][j] != target[i][j]:
                return False
    return True


input = sys.stdin.readline
N, M = map(int, input().split())
board = [list(input().rstrip()) for _ in range(N)]
target = [list(input().rstrip()) for _ in range(N)]
count = 0

if is_same():
    print(0)
    exit()

for i in range(N - 2):
    for j in range(M - 2):
        if board[i][j] == target[i][j]:
            continue

        count += 1
        operate(i, j)
        if is_same():
            print(count)
            exit()
print(-1)