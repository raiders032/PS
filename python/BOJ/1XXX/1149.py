"""
1149.RGB거리
실버1
다이나믹프로그래밍
"""
import sys

input = sys.stdin.readline
N = int(input())
rgbs = []
dp = [[sys.maxsize] * 3 for _ in range(N)]
for _ in range(N):
    r, g, b = map(int, input().rstrip().split())
    rgbs.append((r, g, b))

dp[0] = [rgbs[0][0], rgbs[0][1], rgbs[0][2]]
for i in range(1, N):
    for j in range(3):
        for k in range(3):
            if j == k:
                continue
            dp[i][j] = min(dp[i][j], dp[i - 1][k] + rgbs[i][j])
print(min(dp[N-1]))
