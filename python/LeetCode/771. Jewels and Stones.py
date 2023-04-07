"""
https://leetcode.com/problems/jewels-and-stones/
771. Jewels and Stones
Easy
Hash
풀이2.32ms
"""


class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        stone_count = collections.defaultdict(int)
        count = 0

        for stone in stones:
            stone_count[stone] += 1

        for jewel in jewels:
            count += stone_count[jewel]

        return count
