"""
https://www.acmicpc.net/problem/2156
2156.포도주 시식
실버1
풀이1.88ms
"""
import sys

input = sys.stdin.readline

N = int(input())
wine = [int(input()) for _ in range(N)]

dp = [[0] * 3 for _ in range(N)]
dp[0][0] = 0
dp[0][1] = wine[0]
dp[0][1] = wine[0]

for i in range(1, N):
    dp[i][0] = max(dp[i - 1][0], dp[i - 1][1], dp[i - 1][2])
    dp[i][1] = dp[i - 1][0] + wine[i]
    dp[i][2] = dp[i - 1][1] + wine[i]

print(max(dp[N - 1]))
