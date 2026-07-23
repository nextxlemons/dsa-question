# Last updated: 7/23/2026, 3:49:52 PM
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
            for i in range(len(nums)):
                if target == nums[i]:
                    return i

            if target < nums[0]:
                return 0
            elif target > nums[-1]:
                return len(nums)
            else:
                for i in range(len(nums)):
                    if target > nums[i - 1] and target < nums[i]:
                        return i