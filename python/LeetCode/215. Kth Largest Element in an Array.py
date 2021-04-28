"""
https://leetcode.com/problems/kth-largest-element-in-an-array/
215. Kth Largest Element in an Array
Medium
Heap, Sort
풀이1.64ms
"""
import heapq


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        max_heap = []

        for number in nums:
            heapq.heappush(max_heap, -number)

        for _ in range(k - 1):
            heapq.heappop(max_heap)

        return -max_heap[0]