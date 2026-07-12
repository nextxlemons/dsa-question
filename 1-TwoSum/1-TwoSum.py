# Last updated: 7/12/2026, 11:47:10 PM
class Solution:
    def twoSum(self,nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]