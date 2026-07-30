# Last updated: 7/30/2026, 11:18:56 PM
class Solution:
    def largestInteger(self, n: int, s: int) -> int:
        if s == 0:
            return 0
        if s > 9 * n:
            return -1

        digits = []
        for _ in range(n):
            d = min(9, s)
            digits.append(str(d))
            s -= d

        return int("".join(digits))