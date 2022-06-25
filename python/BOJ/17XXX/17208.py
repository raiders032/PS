"""
https://www.acmicpc.net/problem/17208
17208.카우버거 알바생
골드4
풀이2.556ms(pypy3)
"""
import sys

input = sys.stdin.readline

N, M, K = map(int, input().split())
orders = [0] + [tuple(map(int, input().split())) for _ in range(N)]
dp = [[[0] * (K + 1) for _ in range(M + 1)] for _ in range(N + 1)]

for i in range(1, N + 1):
    for j in range(1, M + 1):
        for k in range(1, K + 1):
            dp[i][j][k] = dp[i - 1][j][k]
            if j - orders[i][0] < 0 or k - orders[i][1] < 0:
                continue
            dp[i][j][k] = max(dp[i][j][k], dp[i - 1][j - orders[i][0]][k - orders[i][1]] + 1)

print(dp[N][M][K])
