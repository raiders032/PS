"""
https://www.acmicpc.net/problem/1535
1535.안녕
실버2
풀이3.68ms
"""
N = int(input())
W = [0] + list(map(int, input().split()))
T = [0] + list(map(int, input().split()))
dp = [[0] * 101 for _ in range(N + 1)]

for i in range(1, N + 1):
    for j in range(1, 101):
        dp[i][j] = dp[i - 1][j]
        if j - W[i] > 0:
            dp[i][j] = max(dp[i][j], dp[i - 1][j - W[i]] + T[i])

print(dp[N][100])
