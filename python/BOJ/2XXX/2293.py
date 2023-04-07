"""
https://www.acmicpc.net/problem/2293
2293.동전 1
실버1
풀이1.260ms
"""
import sys

input = sys.stdin.readline
N, K = map(int, input().split())
dp = [0] * (K + 1)
coins = [int(input()) for _ in range(N)]

for coin in coins:
    if coin > K:
        continue
    dp[coin] += 1
    for i in range(coin + 1, K + 1):
        dp[i] += dp[i - coin]

print(dp[K])