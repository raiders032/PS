"""
https://www.acmicpc.net/problem/1535
1535.안녕
실버2
풀이1.84ms
"""
N = int(input())
W = [0] + list(map(int, input().split()))
V = [0] + list(map(int, input().split()))
dp = [[0] * 101 for _ in range(N + 1)]

for i in range(1, N + 1):
    for j in range(1, 101):
        dp[i][j] = dp[i - 1][j]
        if W[i] < j:
            dp[i][j] = max(dp[i][j], dp[i - 1][j - W[i]] + V[i])

print(dp[N][100])