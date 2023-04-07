"""
https://www.acmicpc.net/problem/2228
2228.구간 나누기
풀이1.
"""
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
numbers = [0] + [int(input()) for _ in range(N)]
dp = [[[-sys.maxsize] * 2 for _ in range(M + 1)] for _ in range(N + 1)]

for i in range(1, N + 1):
    dp[i][0][0] = 0
    dp[i][0][1] = 0
    for j in range(1, min(M, (i + 1) // 2) + 1):
        dp[i][j][0] = max(dp[i - 1][j])
        dp[i][j][1] = max(dp[i - 1][j][1], dp[i - 1][j - 1][0]) + numbers[i]
print(max(dp[N][M]))
for index, row in enumerate(dp):
    if index == 0:
        continue
    print(row[1:])
