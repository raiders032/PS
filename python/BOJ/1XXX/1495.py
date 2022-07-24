"""
https://www.acmicpc.net/problem/1495
1495.기타리스트
풀이1.88ms
"""
import sys
input = sys.stdin.readline

N, S, M = map(int, input().split())
volume = list(map(int, input().split()))
dp = [[False] * (M + 1) for _ in range(N + 1)]
dp[0][S] = True

for i in range(N):
    for j in range(M + 1):
        if not dp[i][j]:
            continue
        if j + volume[i] <= M:
            dp[i + 1][j + volume[i]] = True
        if j - volume[i] >= 0:
            dp[i + 1][j - volume[i]] = True

answer = -1
for j in range(M + 1):
    if dp[N][j]:
        answer = j
print(answer)
