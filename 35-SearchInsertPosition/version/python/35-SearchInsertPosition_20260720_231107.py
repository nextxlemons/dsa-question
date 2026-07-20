# Last updated: 7/20/2026, 11:11:07 PM
# simple hai
1class Solution:
2    def plusOne(self, digits: List[int]) -> List[int]:
3        nl = []
4        carry = 1
5
6        for i in digits[::-1]:
7
8            totl = i + carry
9            nl.insert(0, totl % 10)
10            carry = totl // 10
11
12        if carry:
13            nl.insert(0, carry)
14
15        return nl