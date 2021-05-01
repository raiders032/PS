"""
https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/
108. Convert Sorted Array to Binary Search Tree
Easy
BST
풀이2.56ms
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def to_BST(nums):
            if not nums:
                return None
            mid = len(nums) // 2

            root = TreeNode(nums[mid])
            root.left = to_BST(nums[:mid])
            root.right = to_BST(nums[mid + 1:])

            return root

        return to_BST(nums)
