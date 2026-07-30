# Last updated: 7/30/2026, 10:42:27 PM
# other way
1class Solution:
2    def maxProfit(self, prices: List[int]) -> int:
3        min_price = float('inf')
4        profit = 0
5        for price in prices:
6            min_price = min(min_price, price)
7            profit = max(profit, price - min_price) 
8
9        return profit