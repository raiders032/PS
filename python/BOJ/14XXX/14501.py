"""
14501번 퇴사 실버4
브루트포스, 다이나믹프로그래밍
브루트포스 풀이
"""
import sys

N = int(sys.stdin.readline())
T = [0]
P = [0]
dp = [0] * (N + 2)
ans = 0

for i in range(N):
    t, p = map(int, sys.stdin.readline().split())
    T.append(t)
    P.append(p)

for i in range(1, N + 2):
    for j in range(1, i):
        if j + T[j] <= i:
            dp[i] = max(dp[i], dp[j] + P[j])

print(max(dp))
