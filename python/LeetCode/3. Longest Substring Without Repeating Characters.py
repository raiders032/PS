"""
https://leetcode.com/problems/longest-substring-without-repeating-characters/
3.Longest Substring Without Repeating Characters
Medium
해시
풀이1.268 ms
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = len(s)
        answer = 0
        left, right = 0, 0
        while right != length:
            string_length = right - left + 1
            unique_count = len(set(s[left:right+1]))
            if string_length != unique_count:
                    left += 1
            else:
                answer = max(answer, string_length)
                right += 1
        return answer