"""
13398.연속합 2
골드5
다이나믹프로그래밍, 누적합
"""

N = int(input())
arr = list(map(int, input().split()))
dp = [[0] * N for _ in range(4)]
dp[0][0] = arr[0]
dp[1][0] = arr[0]
res = arr[0]
for i in range(1, N):
    dp[0][i] = arr[i]
    dp[1][i] = max(dp[0][i - 1], dp[1][i - 1]) + arr[i]
    dp[2][i] = max(dp[0][i - 1], dp[1][i - 1])
    dp[3][i] = max(dp[2][i - 1], dp[3][i - 1]) + arr[i]
    res = max(res, dp[0][i], dp[1][i], dp[2][i], dp[3][i])
print(res)