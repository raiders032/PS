"""
https://leetcode.com/problems/valid-parentheses/
20. Valid Parentheses
Easy
Stack
풀이1.28ms
"""


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char == '(' or char == '{' or char == '[':
                stack.append(char)
            else:
                if stack and char == ')' and stack[-1] != '(':
                    return False
                elif stack and char == '}' and stack[-1] != '{':
                    return False
                elif stack and char == ']' and stack[-1] != '[':
                    return False
                elif not stack:
                    return False
                stack.pop()

        if stack:
            return False

        return True