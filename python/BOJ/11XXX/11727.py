"""
11727. 2×number 타일링 2 실버3
다이나믹프로그래밍
"""
N = int(input())
dp = [0] * (N+2)
dp[1] = 1
dp[2] = 3
for i in range(3, N+1):
    dp[i] = (dp[i-1] + 2 * dp[i-2]) % 10007
print(dp[N])