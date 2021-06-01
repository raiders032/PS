"""
https://leetcode.com/problems/array-partition-i/submissions/
561. Array Partition I
Easy
정렬
"""
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        answer = 0
        nums.sort()
        for i in range(0, len(nums), 2):
            answer += nums[i]
        return answer