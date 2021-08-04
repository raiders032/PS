"""
https://leetcode.com/problems/two-sum/
1.Two Sum
easy
풀이1.4024ms
"""
nums = [3, 2, 4]
target = 6


def solve(nums, target):
    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]


print(solve(nums, target))