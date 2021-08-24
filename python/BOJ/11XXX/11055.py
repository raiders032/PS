"""
https://www.acmicpc.net/problem/11055
11055.가장 큰 증가 부분 수열
실버2
풀이1.272ms
"""
N = int(input())
nums = list(map(int, input().split()))
dp = nums[:]
answer = nums[0]

for i in range(1, N):
    for j in range(0, i):
        if nums[j] >= nums[i]:
            continue
        if dp[j] + nums[i] > dp[i]:
            dp[i] = dp[j] + nums[i]
            answer = max(answer, dp[i])
print(answer)