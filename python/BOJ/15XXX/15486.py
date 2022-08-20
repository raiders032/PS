"""
https://www.acmicpc.net/problem/15486
15486.퇴사 2
풀이1.3236ms
"""
import sys
input = sys.stdin.readline

N = int(input())
T = [0]
P = [0]

for _ in range(N):
    t, p = map(int, input().split())
    T.append(t)
    P.append(p)

dp = [0] * (N + 1)

for i in range(1, N + 1):
    dp[i] = max(dp[i], dp[i - 1])
    if i + T[i] - 1 > N:
        continue
    dp[i + T[i] - 1] = max(dp[i + T[i] - 1], dp[i - 1] + P[i])

print(dp[-1])
