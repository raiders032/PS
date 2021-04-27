"""
https://leetcode.com/problems/diameter-of-binary-tree/
543.Diameter of Binary Tree
Easy
Tree
풀이1.40ms
"""


class Solution:
    answer = 0

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        def get_depth(node):
            if node is None:
                return 0

            left_depth = get_depth(node.left)
            right_depth = get_depth(node.right)
            self.answer = max(self.answer, left_depth + right_depth)

            return 1 + max(left_depth, right_depth)

        get_depth(root)
        return self.answer
