# Last updated: 7/30/2026, 11:14:12 PM
# using Boyer-Moore Voting Algorithm
1class Solution:
2    def majorityElement(self, nums: List[int]) -> int:
3        cnt = 0
4        cand = 0
5
6        for n in nums:
7            if cnt == 0:
8                cand = n
9            if n == cand:
10                cnt += 1
11            else:
12                cnt -= 1
13
14        return cand
15        