# Last updated: 8/1/2026, 9:47:49 AM
# faster execution
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
12                totl = nums[f] + nums[l] + nums[r]
13                if totl < 0:
14                    l += 1
15                elif totl > 0:
16                    r -= 1
17                else:
18                    res.append([nums[f], nums[l], nums[r]])
19                    while l < r and nums[l] == nums[l + 1]:
20                        l += 1
21                    while r > l and nums[r] == nums[r - 1]:
22                        r -= 1
23
24                    l += 1
25                    r -= 1
26        return res