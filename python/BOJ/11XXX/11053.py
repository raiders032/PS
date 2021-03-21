"""
11053.가장 긴 증가하는 부분 수열 실버2
다이나믹프로그래밍
"""
import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().rstrip().split()))
dp = [1] * N
res = 1
for i in range(1, N):
    for j in range(i):
        if arr[j] < arr[i]:
            dp[i] = max(dp[i], dp[j] + 1)
            res = max(res, dp[i])

print(res)