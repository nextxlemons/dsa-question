# Last updated: 7/26/2026, 11:07:39 PM
# simple but takes more memory
1class Solution:
2    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
3            n1 = set(nums1)
4            n2 = set(nums2)
5
6            return list(n1.intersection(n2))
7
8        
9        