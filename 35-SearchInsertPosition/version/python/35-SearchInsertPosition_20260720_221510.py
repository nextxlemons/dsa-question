# Last updated: 7/20/2026, 10:15:10 PM
# using indexing
1class Solution:
2    def searchInsert(self, nums: List[int], target: int) -> int:
3            for i in range(len(nums)):
4                if target == nums[i]:
5                    return i
6
7            if target < nums[0]:
8                return 0
9            elif target > nums[-1]:
10                return len(nums)
11            else:
12                for i in range(len(nums)):
13                    if target > nums[i - 1] and target < nums[i]:
14                        return i