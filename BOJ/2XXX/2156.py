"""
2156.포도주 시식
실버1
다이나믹프로그래밍
"""
import sys

input = sys.stdin.readline
N = int(input())
wines = [0]
for _ in range(N):
    wine = int(input())
    wines.append(wine)

dp = [[0] * (N + 1) for _ in range(3)]

dp[0][1], dp[1][1], dp[2][1] = 0, wines[1], wines[1]

for col in range(2, N + 1):
    dp[0][col] = max(dp[0][col - 1], dp[1][col - 1], dp[2][col - 1])
    dp[1][col] = dp[0][col - 1] + wines[col]
    dp[2][col] = dp[1][col - 1] + wines[col]

print(max(dp[0][N], dp[1][N], dp[2][N]))
