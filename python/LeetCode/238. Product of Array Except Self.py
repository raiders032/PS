"""
https://leetcode.com/problems/product-of-array-except-self/
238. Product of Array Except Self
Medium
풀이1
"""


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = []
        length = len(nums)
        left_product = [1] * length
        right_product = [1] * length

        for i in range(length - 1):
            left_product[i + 1] = left_product[i] * nums[i]
            right_product[length - 2 - i] = right_product[length - 1 - i] * nums[length - 1 - i]

        for i in range(length):
            answer.append(left_product[i] * right_product[i])

        return answer