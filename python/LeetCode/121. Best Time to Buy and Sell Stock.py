"""
카데인 알고리즘
import sys
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        min_price = sys.maxsize
        for i in range(len(prices)):
            min_price = min(min_price, prices[i])
            res = max(res, prices[i] - min_price)
        return res
"""
import sys
prices = []
res = 0
min_price = sys.maxsize
for i in range(len(prices)):
    min_price = min(min_price, prices[i])
    res = max(res, prices[i] - min_price)
print(res)
