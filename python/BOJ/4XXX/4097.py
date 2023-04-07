"""
https://www.acmicpc.net/problem/4097
4097.수익
풀이1.1204ms
"""
import sys
input = sys.stdin.readline

while True:
    n = int(input())
    if n == 0:
        break
    numbers = [int(input()) for _ in range(n)]
    dp = [0] * n
    dp[0] = numbers[0]
    max_profit = dp[0]

    for i in range(1, n):
        dp[i] = max(dp[i - 1] + numbers[i], numbers[i])
        max_profit = max(max_profit, dp[i])

    print(max_profit)