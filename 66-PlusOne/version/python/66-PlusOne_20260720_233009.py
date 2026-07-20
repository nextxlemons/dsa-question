# Last updated: 7/20/2026, 11:30:09 PM
# more efficient method
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        number = 0
        for i in range(len(digits) - 1, -1, -1):
            number += 10**i * digits[len(digits)-i-1]
        number += 1
        number = str(number)
        return [int(i) for i in number]