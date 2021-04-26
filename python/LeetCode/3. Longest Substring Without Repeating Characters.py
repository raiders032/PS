"""
https://leetcode.com/problems/longest-substring-without-repeating-characters/
3.Longest Substring Without Repeating Characters
Medium
해시
풀이2.52ms
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_index = dict()
        answer = 0
        start_index = 0
        for index, char in enumerate(s):
            if char in char_index and start_index <= char_index[char]:
                start_index = char_index[char] + 1
            else:
                answer = max(answer, index - start_index + 1)

            char_index[char] = index
        return answer