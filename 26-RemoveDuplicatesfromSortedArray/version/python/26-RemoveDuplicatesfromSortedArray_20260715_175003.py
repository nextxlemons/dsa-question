# Last updated: 7/15/2026, 5:50:03 PM
# this solution use simple list
1class Solution:
2    def removeDuplicates(self, nums: List[int]) -> int:
3        if not nums:
4            return 0
5
6        i = 1
7
8        for j in range(1, len(nums)):
9            if nums[j] != nums[j - 1]:
10                nums[i] = nums[j]
11                i += 1
12
13        return i