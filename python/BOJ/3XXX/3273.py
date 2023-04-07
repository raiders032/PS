"""
https://www.acmicpc.net/problem/3273
3273.두 수의 합
실버3
풀이2
"""
N = int(input())
nums = list(map(int, input().split()))
X = int(input())
nums.sort()
num_set = set(nums)
i = 0
count = 0

while i < N:
    if nums[i] >= X / 2:
        break
    if X - nums[i] in num_set:
        count += 1
    i += 1
print(count)