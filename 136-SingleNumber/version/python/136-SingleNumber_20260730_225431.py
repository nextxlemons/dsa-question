# Last updated: 7/30/2026, 10:54:31 PM
# using XOR bitwise operator
1class Solution:
2    def singleNumber(self, nums: List[int]) -> int:
3        ans = 0
4        for n in nums:
5            ans ^= n
6        return ans