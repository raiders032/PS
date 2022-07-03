"""
https://www.acmicpc.net/problem/2758
2758.로또
골드4
풀이1.2004ms
"""
import sys
input = sys.stdin.readline

dp = [[0] * 2001 for _ in range(11)]

for y in range(1, 2001):
    dp[1][y] = 1

for x in range(2, 11):
    for y in range(2, 2001):
        for z in range(1, y // 2 + 1):
            dp[x][y] += dp[x - 1][z]

for _ in range(int(input())):
    n, m = map(int, input().split())
    print(sum(dp[n][1:m+1]))