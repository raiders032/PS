'''
https://www.acmicpc.net/problem/11726
11726. 2×number 타일링
실버3
풀이1.84ms
'''
N = int(input())
dp = [0] * (N + 2)
dp[1] = 1
dp[2] = 2

for i in range(3, N + 1):
    dp[i] = (dp[i - 1] + dp[i - 2]) % 10007

print(dp[N])