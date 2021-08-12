"""
https://www.acmicpc.net/problem/2240
2240.자두나무
실버1
풀이1.112ms
"""
import sys

input = sys.stdin.readline
N, C = map(int, input().split())
nums = [int(input()) - 1 for _ in range(N)]
dp = [[[0] * (C + 1) for _ in range(2)] for _ in range(N)]

dp[0][0][0] = 1 if nums[0] == 0 else 0
dp[0][1][1] = 1 if nums[0] == 1 else 0

for i in range(N - 1):
    for count in range(C + 1):
        dp[i + 1][0][count] = max(dp[i + 1][0][count], dp[i][0][count] + 1 if nums[i + 1] == 0 else dp[i][0][count])
        dp[i + 1][1][count] = max(dp[i + 1][1][count], dp[i][1][count] + 1 if nums[i + 1] == 1 else dp[i][1][count])

        if count + 1 > C:
            continue

        dp[i + 1][0][count + 1] = max(dp[i + 1][0][count + 1], dp[i][1][count] + 1 if nums[i + 1] == 0 else dp[i][1][count])
        dp[i + 1][1][count + 1] = max(dp[i + 1][1][count + 1], dp[i][0][count] + 1 if nums[i + 1] == 1 else dp[i][0][count])

print(max(max(dp[N-1][0]), max(dp[N-1][1])))