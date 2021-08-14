"""
https://www.acmicpc.net/problem/9465
9465.스티커
실버2
풀이1.1060ms
"""
import sys

input = sys.stdin.readline
for _ in range(int(input())):
    N = int(input())
    stickers = [list(map(int, input().rstrip().split())) for _ in range(2)]

    dp = [[0] * N for _ in range(2)]
    dp[0][0] = stickers[0][0]
    dp[1][0] = stickers[1][0]
    if N > 1:
        dp[0][1] = stickers[1][0] + stickers[0][1]
        dp[1][1] = stickers[0][0] + stickers[1][1]

    for i in range(2, N):
        dp[0][i] = max(dp[1][i - 1], dp[1][i - 2]) + stickers[0][i]
        dp[1][i] = max(dp[0][i - 1], dp[0][i - 2]) + stickers[1][i]

    print(max(dp[0][N - 1], dp[1][N - 1]))