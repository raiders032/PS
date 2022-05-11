"""
https://www.acmicpc.net/problem/1018
1018.체스판 다시 칠하기
실버5
풀이1.108ms
"""

import sys


def get_count(i, j):
    count1 = 0
    count2 = 0

    for x in range(8):
        for y in range(8):
            if board[i + x][j + y] != filter1[x][y]:
                count1 += 1
            if board[i + x][j + y] != filter2[x][y]:
                count2 += 1

    return min(count1, count2)


filter1 = [
    ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
    ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
    ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
    ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
    ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
    ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
    ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
    ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W']
]

filter2 = [
    ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
    ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
    ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
    ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
    ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
    ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
    ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
    ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B']
]

input = sys.stdin.readline
N, M = map(int, input().split())
board = [list(input().strip()) for _ in range(N)]
min_count = sys.maxsize

for i in range(N - 7):
    for j in range(M - 7):
        min_count = min(min_count, get_count(i, j))

print(min_count)
