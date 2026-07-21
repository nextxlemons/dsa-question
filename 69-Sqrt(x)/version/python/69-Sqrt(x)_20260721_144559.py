# Last updated: 7/21/2026, 2:45:59 PM
# simple but not efficient
1class Solution:
2    def mySqrt(self, x: int) -> int:
3        for i in range(1,x + 1):
4            if i * i == x:
5                return i
6
7            if i * i > x:
8                return i - 1
9
10        else:
11            return 0
12        