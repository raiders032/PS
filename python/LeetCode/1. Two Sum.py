"""
https://leetcode.com/problems/two-sum/
1.Two Sum
easy
풀이2.52ms
"""
nums = [3, 2, 4]
target = 6


def solve(nums, target):
    num_index = dict()

    for index, num in enumerate(nums):
        num_index[num] = index

    for index, num in enumerate(nums):
        num2 = target - num
        if num2 in num_index and index != num_index[num2]:
            return [index, num_index[num2]]


print(solve(nums, target))

"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_index = dict()

        for index, num in enumerate(nums):
            num_index[num] = index

        for index, num in enumerate(nums):
            num2 = target - num
            if num2 in num_index and index != num_index[num2]:
                return [index, num_index[num2]]
"""