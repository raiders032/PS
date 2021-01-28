"""
2133.타일 채우기
실버2
다이나막프로그래밍
"""

N = int(input())
dp = [0] * 31
dp[0] = 1
dp[2] = 3
dp[4] = 11
for i in range(5, N + 1):
    dp[i] += 3 * dp[i - 2]
    j = 0
    while i - j - 4 >= 0:
        dp[i] += 2 * dp[i - j - 4]
        j += 2
print(dp[N])
