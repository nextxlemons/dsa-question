# Last updated: 7/17/2026, 11:24:28 PM
# solve using two pointer method
1class Solution:
2    def isPalindrome(self, s: str) -> bool:
3        l, r = 0, len(s)-1
4
5        while l < r:
6            while l < r and not s[l].isalnum():
7                l += 1
8            while l < r and not s[r].isalnum():
9                r -= 1
10
11            if s[l].casefold() != s[r].casefold():
12                return False
13
14            l += 1
15            r -= 1
16
17        return True