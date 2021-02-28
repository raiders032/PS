"""
15988. 1, 2, 3 더하기 3
실버2
다이나믹프로그래밍
"""
import sys

input = sys.stdin.readline
N = int(input())
dp = [0] * 1000001
dp[1], dp[2], dp[3] = 1, 2, 4
for i in range(4, 1000001):
    dp[i] = (dp[i - 1] + dp[i - 2] + dp[i - 3]) % 1000000009

for _ in range(N):
    num = int(input())
    print(dp[num])
