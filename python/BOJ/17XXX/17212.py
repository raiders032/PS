"""
https://www.acmicpc.net/problem/17212
17212.달나라 토끼를 위한 구매대금 지불 도우미
풀이1.264ms
"""
import sys
input = sys.stdin.readline

N = int(input())
dp = [sys.maxsize] * (N + 1)
dp[0] = 0
coins = [1, 2, 5, 7]

for i in range(1, N + 1):
    for coin in coins:
        if i - coin < 0:
            continue
        dp[i] = min(dp[i], dp[i - coin] + 1)

print(dp[N])