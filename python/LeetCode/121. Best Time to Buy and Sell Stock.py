"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
121. Best Time to Buy and Sell Stock
Easy
풀이2.1008ms
"""


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        answer = 0
        min = 10001
        for price in prices:
            if price < min:
                min = price
            else:
                answer = max(answer, price - min)
        return answer