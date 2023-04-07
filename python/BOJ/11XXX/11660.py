"""
https://www.acmicpc.net/problem/11660
11660.구간 합 구하기 5
풀이1.1240ms
"""
import sys

input = sys.stdin.readline
N, M = map(int, input().split())
prefix_sum = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    for j in range(1, N):
        prefix_sum[i][j] += prefix_sum[i][j - 1]

for i in range(1, N):
    for j in range(N):
        prefix_sum[i][j] += prefix_sum[i - 1][j]

for _ in range(M):
    x1, y1, x2, y2 = map(lambda x: int(x) - 1, input().split())
    result = prefix_sum[x2][y2]
    if x1:
        result -= prefix_sum[x1 - 1][y2]
    if y1:
        result -= prefix_sum[x2][y1 - 1]
    if x1 and y1:
        result += prefix_sum[x1 - 1][y1 - 1]
    print(result)