"""
https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/
108. Convert Sorted Array to Binary Search Tree
Easy
BST
풀이1.60ms
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def to_BST(left, right):
            if left > right:
                return None
            mid = (left + right) // 2

            root = TreeNode(nums[mid])
            root.left = to_BST(left, mid - 1)
            root.right = to_BST(mid + 1, right)

            return root

        return to_BST(0, len(nums) - 1)