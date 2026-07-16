# Last updated: 7/17/2026, 12:55:39 AM
# This solution use stack to track opening and closing brackets of input string
1class Solution:
2    def isValid(self, s: str) -> bool:
3        lstack = []
4
5        pairs = {
6            ')' : '(',
7            '}' : '{',
8            ']' : '['
9        }    
10        for i in s:
11            if i in "([{":
12                lstack.append(i)
13            else:
14                if not lstack or lstack[-1] != pairs[i]:
15                    return False
16                lstack.pop()
17
18        return len(lstack) == 0