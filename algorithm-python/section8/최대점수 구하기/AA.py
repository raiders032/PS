import sys

N, M = map(int, sys.stdin.readline().split())
dp = [0] * (M + 1)
for _ in range(N):
    s, t = map(int, sys.stdin.readline().split())
    for i in range(M, t - 1, -1):
        dp[i] = max(dp[i], dp[i - t] + s)
print(dp[M])
