# Last updated: 7/30/2026, 11:15:42 PM
# faster
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ele=0
        coun=0
        for x in nums:
            if coun==0:
                ele=x
                coun+=1
            elif ele==x:
                coun+=1
            else:
                coun-=1
        return ele


        