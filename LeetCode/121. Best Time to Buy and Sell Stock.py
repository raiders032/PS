"""
브루트 포스 -> Time Limit Exceeded
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        for i in range(len(prices)-1):
            for j in range(i+1, len(prices)):
                if prices[i] < prices[j]:
                    res = max(res, prices[j] - prices[i])
        return res
"""

prices = [7, 6, 4, 3, 1]
res = 0
for i in range(len(prices)-1):
    for j in range(i+1, len(prices)):
        if prices[i] < prices[j]:
            res = max(res, prices[j] - prices[i])
print(res)
