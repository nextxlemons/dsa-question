# Last updated: 7/30/2026, 11:19:09 PM
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i = m - 1          # Last valid element in nums1
        k = n - 1          # Last element in nums2
        j = m + n - 1      # Last position in nums1

        while k >= 0:
            if i >= 0 and nums1[i] > nums2[k]:
                nums1[j] = nums1[i]
                i -= 1
            else:
                nums1[j] = nums2[k]
                k -= 1
            j -= 1