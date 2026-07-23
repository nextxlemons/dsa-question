# Last updated: 7/23/2026, 3:49:35 PM
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        j = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[j],nums[i] = nums[i],nums[j]
                j += 1
        return nums