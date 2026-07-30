# Last updated: 7/30/2026, 11:19:03 PM
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cnt = 0
        cand = 0

        for n in nums:
            if cnt == 0:
                cand = n
                cnt += 1
            elif n == cand:
                cnt += 1
            else:
                cnt -= 1

        return cand
        