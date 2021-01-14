"""
1699.제곱수의 합
실버3
다이나믹프로그래밍
"""
import sys

N = int(input())
dp = [sys.maxsize] * (N + 1)
dp[0], dp[1] = 0, 1

for cur in range(2, N + 1):
    pre = 1
    while cur - pow(pre, 2) >= 0:
        dp[cur] = min(dp[cur], dp[cur - pow(pre, 2)] + 1)
        pre += 1

print(dp[N])
