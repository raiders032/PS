"""
2193. 이친수 실버3
다이나믹프로그래밍
"""

N = int(input())
dp = [[0] * 2 for _ in range(N + 1)]
dp[1][0], dp[1][1] = 0, 1
for i in range(2, N + 1):
    dp[i][0] = dp[i - 1][0] + dp[i - 1][1]
    dp[i][1] = dp[i - 1][0]
print(dp[N][0] + dp[N][1])