# Last updated: 7/22/2026, 11:34:26 PM
# simple two pointer solution
1class Solution:
2    def moveZeroes(self, nums: List[int]) -> None:
3        """
4        Do not return anything, modify nums in-place instead.
5        """
6        j = 0
7
8        for i in range(len(nums)):
9            if nums[i] != 0:
10                nums[j],nums[i] = nums[i],nums[j]
11                j += 1
12        return nums