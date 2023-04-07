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
                if cur_node.high:
                    q.append(cur_node.high)
                if cur_node.low:
                    q.append(cur_node.low)

        return depth