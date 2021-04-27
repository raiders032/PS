"""
https://leetcode.com/problems/maximum-depth-of-binary-tree/
104. Maximum Depth of Binary Tree
Easy
Tree
풀이1
"""
from collections import deque


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0

        depth = 0
        q = deque([root])

        while q:
            depth += 1
            for _ in range(len(q)):
                cur_node = q.popleft()
                if cur_node.right:
                    q.append(cur_node.right)
                if cur_node.left:
                    q.append(cur_node.left)

        return depth