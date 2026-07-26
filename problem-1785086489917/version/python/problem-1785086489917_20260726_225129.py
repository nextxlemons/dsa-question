# Last updated: 7/26/2026, 10:51:29 PM
# from weekly contest
1class Solution:
2    def largestInteger(self, n: int, s: int) -> int:
3        if s == 0:
4            return 0
5        if s > 9 * n:
6            return -1
7
8        digits = []
9        for _ in range(n):
10            d = min(9, s)
11            digits.append(str(d))
12            s -= d
13
14        return int("".join(digits))