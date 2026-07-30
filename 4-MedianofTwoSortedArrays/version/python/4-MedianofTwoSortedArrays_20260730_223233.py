# Last updated: 7/30/2026, 10:32:33 PM
# simple
1class Solution:
2    def maxProfit(self, prices: List[int]) -> int:
3        i = 0
4        profit = 0
5        for j in range(1, len(prices)):
6
7            if prices[i] < prices[j]:
8                cur = prices[j] - prices[i]
9                profit = max(cur, profit)
10            else:
11                i = j
12
13        return profit