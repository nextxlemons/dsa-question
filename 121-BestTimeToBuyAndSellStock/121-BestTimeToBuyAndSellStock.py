# Last updated: 7/30/2026, 11:19:06 PM
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        profit = 0
        for price in prices:
            min_price = min(min_price, price)
            profit = max(profit, price - min_price) 

        return profit