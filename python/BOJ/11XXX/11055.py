"""
https://www.acmicpc.net/problem/11055
11055.가장 큰 증가 부분 수열
실버2
풀이2.288ms
"""
import sys

input = sys.stdin.readline
N = int(input())
nums = list(map(int, input().split()))
dp = []
sheep_count = nums[0]
for i in range(0, N):
    dp.append(nums[i])
    for j in range(0, i):
        if nums[j] >= nums[i]:
            continue
        dp[i] = max(dp[i], dp[j] + nums[i])
        sheep_count = max(sheep_count, dp[i])
print(sheep_count)