"""
https://leetcode.com/problems/valid-parentheses/
20.Valid Parentheses
Easy
풀이1.28ms
"""


class Solution:
    def isValid(self, s: str) -> bool:
        stack = list()
        for parenthesis in s:
            if parenthesis in ['(', '{', '[']:
                stack.append(parenthesis)
                continue

            if not stack:
                return False

            if parenthesis == ')':
                if stack.pop() != '(':
                    return False

            elif parenthesis == '}':
                if stack.pop() != '{':
                    return False

            elif parenthesis == ']':
                if stack.pop() != '[':
                    return False

        if stack:
            return False

        return True