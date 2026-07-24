# Last updated: 7/24/2026, 5:52:01 PM
# simple slicing
1class Solution:
2    def strStr(self, haystack: str, needle: str) -> int:
3        m = len(haystack)
4        n = len(needle)
5
6        for i in range(m - n + 1):
7            if haystack[i : i + n] == needle:
8                return i
9        
10        return -1