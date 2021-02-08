"""
1463. 1로 만들기
실버3
다이나믹프로그래밍
"""
n = int(input())
dp = [1] * (n+1)
dp[1] = 0
for i in range(4, n+1):
    dp[i] = dp[i-1]
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2])
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3])
    dp[i] += 1
print(dp[n])
