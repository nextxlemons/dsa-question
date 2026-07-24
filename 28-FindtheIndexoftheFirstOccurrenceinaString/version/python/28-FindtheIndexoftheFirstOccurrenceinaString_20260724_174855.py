# Last updated: 7/24/2026, 5:48:55 PM
# simple
1class Solution:
2    def strStr(self, haystack: str, needle: str) -> int:
3        if needle in haystack:
4            return haystack.index(needle)
5        return -1