# Last updated: 7/21/2026, 3:35:59 PM
# more efficient method using binary search method
1class Solution:
2    def mySqrt(self, x: int) -> int:
3        if x < 2:
4            return x
5
6        l, r = 1, x // 2
7
8        while l <= r:
9            m = (l + r) // 2
10        
11            if m * m == x:
12                return m
13            elif m * m < x:
14                l = m + 1
15            else:
16                r = m - 1
17
18        return r