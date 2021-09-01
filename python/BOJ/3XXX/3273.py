"""
https://www.acmicpc.net/problem/3273
3273.두 수의 합
실버3
풀이1.112ms
"""
N = int(input())
nums = list(map(int, input().split()))
nums.sort()
X = int(input())
nums_set = set(nums)
answer = 0

for i in range(N):
    if nums[i] >= X / 2:
        break
    if X - nums[i] in nums_set:
        answer += 1

print(answer)