"""
https://www.acmicpc.net/problem/2225
2225.합분해
골드5
다이나믹프로그래밍
풀이2.1024ms
"""
import sys

input = sys.stdin.readline
N, K = map(int, input().split())
dp = [[1] * (N + 1) for _ in range(K + 1)]

for i in range(2, K + 1):
    for j in range(1, N + 1):
        dp[i][j] = 0
        for k in range(j + 1):
            dp[i][j] += dp[i - 1][j - k]
        dp[i][j] = dp[i][j] % 1000000000

print(dp[K][N])
