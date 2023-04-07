"""
https://www.acmicpc.net/problem/10844
10844.쉬운 계단 수
실버1
풀이2.88ms
"""
N = int(input())
dp = [[0] * (N + 1) for _ in range(10)]
for i in range(1, 10):
    dp[i][1] = 1

for j in range(2, N + 1):
    for i in range(10):
        if i > 0:
            dp[i][j] += dp[i - 1][j - 1]
            dp[i][j] %= 1000000000
        if i < 9:
            dp[i][j] += dp[i + 1][j - 1]
            dp[i][j] %= 1000000000

sheep_count = 0
for i in range(10):
    sheep_count += dp[i][N]
    sheep_count %= 1000000000
print(sheep_count)