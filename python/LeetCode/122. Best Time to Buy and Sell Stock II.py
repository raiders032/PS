"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
122. Best Time to Buy and Sell Stock II
Easy
Greedy
풀이1.56ms
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        answer = 0
        for i in range(len(prices) -  1):
            if prices[i] < prices[i + 1]:
                answer += prices[i + 1] - prices[i]
        return answer