# Last updated: 7/18/2026, 10:30:06 PM
# two pointer
1class Solution:
2    def reverseString(self, s: List[str]) -> None:
3        """
4        Do not return anything, modify s in-place instead.
5        """
6        j = len(s) - 1
7        for i in range(len(s) // 2):
8            s[i], s[j] = s[j], s[i]
9            j -= 1
10
11        