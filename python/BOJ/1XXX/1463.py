"""
https://www.acmicpc.net/problem/1463
1463.1로 만들기
실버3
풀이2.1060ms
"""
N = int(input())
dp = [1234567899] * (N + 1)
dp[1] = 0

for i in range(1, N + 1):
    if i + 1 > N:
        continue
    dp[i + 1] = min(dp[i + 1], dp[i] + 1)
    if 2 * i > N:
        continue
    dp[2 * i] = min(dp[2 * i], dp[i] + 1)
    if 3 * i > N:
        continue
    dp[3 * i] = min(dp[3 * i], dp[i] + 1)

print(dp[N])