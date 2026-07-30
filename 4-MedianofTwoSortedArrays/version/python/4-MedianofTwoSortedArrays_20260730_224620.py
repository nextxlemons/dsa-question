# Last updated: 7/30/2026, 10:46:20 PM
# using buildin method
1class Solution:
2    def singleNumber(self, nums: List[int]) -> int:
3        for n in nums:
4            if nums.count(n) == 1:
5                return n