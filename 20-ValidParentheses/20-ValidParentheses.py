# Last updated: 7/23/2026, 3:49:57 PM
class Solution:
    def isValid(self, s: str) -> bool:
        lstack = []

        pairs = {
            ')' : '(',
            '}' : '{',
            ']' : '['
        }    
        for i in s:
            if i in "([{":
                lstack.append(i)
            else:
                if not lstack or lstack[-1] != pairs[i]:
                    return False
                lstack.pop()

        return len(lstack) == 0