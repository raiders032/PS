"""
https://www.acmicpc.net/problem/11049
11049.행렬 곱셈 순서
골드3
풀이1.3144ms(PyPy3)
"""
import sys

input = sys.stdin.readline
N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]
dp = [[sys.maxsize] * N for _ in range(N)]
for i in range(N):
    dp[i][i] = 0

for j in range(N):
    for i in range(N - j):
        for k in range(i + j):
            dp[i][i + j] = min(dp[i][i + j], dp[i][k] + dp[k + 1][i + j] + matrix[i][0] * matrix[k][1] * matrix[i + j][1])

print(dp[0][N - 1])