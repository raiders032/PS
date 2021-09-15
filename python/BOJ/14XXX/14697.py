"""
https://www.acmicpc.net/problem/14697
14697.방 배정하기
브론즈2
풀이1.84ms
"""
nums = list(map(int, input().split()))
N = nums[3]
nums = nums[:3]
dp = [0] * 301

for num in nums:
    dp[num] = 1

for i in range(1, 301):
    for j in range(3):
        if i - nums[j] < 0:
            continue
        dp[i] = max(dp[i], dp[i - nums[j]])

print(1 if dp[N] else 0)