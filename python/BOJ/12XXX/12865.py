"""
https://www.acmicpc.net/problem/12865
12865.평범한 배낭
골드5
풀이1.7712ms
"""
N, K = map(int, input().split())
W = [0]
V = [0]
dp = [[0] * (K + 1) for _ in range(N + 1)]

for _ in range(N):
    w, v = map(int, input().split())
    W.append(w)
    V.append(v)

for i in range(1, N + 1):
    for j in range(1, K + 1):
        dp[i][j] = dp[i - 1][j]
        if W[i] <= j:
            dp[i][j] = max(dp[i][j], dp[i - 1][j - W[i]] + V[i])

print(dp[N][K])