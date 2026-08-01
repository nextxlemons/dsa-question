# Last updated: 8/1/2026, 9:45:27 AM
# solved but take too much time
1class Solution:
2    def threeSum(self, nums: list[int]) -> list[list[int]]:
3        nums = sorted(nums)
4        res = []
5        for f in range(len(nums) - 2):
6            l = f + 1
7            r = len(nums) - 1
8            if f > 0 and nums[f] == nums[f - 1]:
9                continue
10
11            while l < r:
12
13                if nums[f] + nums[l] + nums[r] == 0:
14                    res.append([nums[f], nums[l], nums[r]])
15
16                    while l < r and nums[l] == nums[l + 1]:
17                        l += 1
18                    while r > l and nums[r] == nums[r - 1]:
19                        r -= 1
20                    l += 1
21                    r -= 1
22
23                elif nums[f] + nums[l] + nums[r] < 0:
24                    l += 1
25                else:
26                    r -= 1
27
28        return res