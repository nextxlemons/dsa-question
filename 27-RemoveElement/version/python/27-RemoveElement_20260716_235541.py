# Last updated: 7/16/2026, 11:55:41 PM
# This solution uses startswith() method and list to see prefix
1class Solution:
2    def longestCommonPrefix(self, strs: List[str]) -> str:
3        prefix = strs[0]
4
5        for s in strs[1:]:
6            while not s.startswith(prefix):
7                prefix = prefix[:-1]
8                if not prefix:
9                    return ""
10
11        return prefix