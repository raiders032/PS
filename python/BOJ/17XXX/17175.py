"""
https://www.acmicpc.net/problem/17175
17175.피보나치는 지겨웡~
풀이1.72ms
"""
n = int(input())
dp = [1] * (n + 1)

for i in range(2, n + 1):
    dp[i] += dp[i - 1] + dp[i - 2]
    dp[i] %= 1000000007

print(dp[n])