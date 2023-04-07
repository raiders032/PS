"""
https://www.acmicpc.net/problem/17626
17626.Four Squares
실버4
풀이1.148ms
"""
import math

n = int(input())
dp = [0] * (n + 1)

for i in range(1, n + 1):
    dp[i] = dp[i - 1]

    for j in range(int(math.sqrt(i)) + 1):
        dp[i] = min(dp[i], dp[i - j * j])

    dp[i] += 1

print(dp[n])