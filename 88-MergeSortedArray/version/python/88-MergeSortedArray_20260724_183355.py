# Last updated: 7/24/2026, 6:33:55 PM
# simple
1class Solution:
2    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
3        i = m - 1          # Last valid element in nums1
4        k = n - 1          # Last element in nums2
5        j = m + n - 1      # Last position in nums1
6
7        while k >= 0:
8            if i >= 0 and nums1[i] > nums2[k]:
9                nums1[j] = nums1[i]
10                i -= 1
11            else:
12                nums1[j] = nums2[k]
13                k -= 1
14            j -= 1