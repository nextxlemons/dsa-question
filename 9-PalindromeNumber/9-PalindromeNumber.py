# Last updated: 7/12/2026, 11:47:18 PM
class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        return True if s == s[::-1] else False