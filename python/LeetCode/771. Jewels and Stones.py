"""
https://leetcode.com/problems/jewels-and-stones/
771. Jewels and Stones
Easy
Hash
풀이1.32ms
"""


class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewels_set = set(jewels)
        count = 0
        for stone in stones:
            if stone in jewels_set:
                count += 1
        return count
