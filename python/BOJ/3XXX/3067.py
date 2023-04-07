"""
https://www.acmicpc.net/problem/3067
3067.Coins
풀이2.76ms
"""
import sys
input = sys.stdin.readline

answer = []
for _ in range(int(input())):
    n = int(input())
    coins = list(map(int, input().split()))
    m = int(input())

    dp = [1] + [0] * m

    for coin in coins:
        for i in range(coin, m + 1):
            dp[i] += dp[i - coin]

    answer.append(str(dp[m]))

print('\n'.join(answer))