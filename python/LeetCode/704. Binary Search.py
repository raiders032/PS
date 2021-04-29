"""
https://leetcode.com/problems/binary-search/
704. Binary Search
Easy
이진탐색
풀이1.236ms
"""


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        answer = -1
        while left <= right:
            mid = (left + right) // 2

            if nums[mid] < target:
                left = mid + 1

            elif nums[mid] > target:
                right = mid - 1

            else:
                answer = mid
                break

        return answer
