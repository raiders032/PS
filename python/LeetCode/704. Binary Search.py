"""
https://leetcode.com/problems/binary-search/
704. Binary Search
Easy
이진탐색
풀이2.232ms
"""


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def bi_search(left, right):
            mid = (left + right) // 2

            if left > right:
                return -1

            if nums[mid] < target:
                return bi_search(mid + 1, right)
            elif target < nums[mid]:
                return bi_search(left, mid - 1)
            else:
                return mid

        return bi_search(0, len(nums) - 1)