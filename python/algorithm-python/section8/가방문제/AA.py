import sys

N, W = map(int, sys.stdin.readline().split())
dp = [0] * (W + 1)

for i in range(N):
    w, p = map(int, sys.stdin.readline().split())
    for j in range(w, W + 1):
        dp[j] = max(dp[j], dp[j - w] + p)

print(dp[W])
