"""
https://www.acmicpc.net/problem/2240
2240.자두나무
실버1
풀이2.116ms
"""
T, W = map(int, input().split())
positions = [0] + [int(input()) - 1 for _ in range(T)]
dp = [[[0] * (W + 1) for _ in range(2)] for _ in range(T + 1)]
dp[1][0][0] = 1 if positions[1] == 0 else 0
dp[1][1][1] = 1 if positions[1] == 1 else 0

for i in range(2, T + 1):
    for j in range(min(i + 1, W + 1)):
        dp[i][0][j] = max(dp[i][0][j], dp[i - 1][0][j])
        dp[i][1][j] = max(dp[i][1][j], dp[i - 1][1][j])
        if j:
            dp[i][0][j] = max(dp[i][0][j], dp[i - 1][1][j - 1])
            dp[i][1][j] = max(dp[i][1][j], dp[i - 1][0][j - 1])

        if positions[i] == 0:
            dp[i][0][j] += 1
        else:
            dp[i][1][j] += 1

print(max(max(dp[T][0]), max(dp[T][1])))