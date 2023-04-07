"""
https://leetcode.com/problems/remove-duplicate-letters/
316.Remove Duplicate Letters
Medium
풀이1.36ms
"""


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        counter = collections.Counter(s)
        stack = []
        seen = set()

        for char in s:
            counter[char] -= 1

            if char in seen:
                continue

            while stack and char < stack[-1] and counter[stack[-1]] > 0:
                seen.remove(stack.pop())

            stack.append(char)
            seen.add(char)

        return ''.join(stack)