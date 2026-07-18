# Last updated: 7/18/2026, 11:13:24 PM
# used ascci values and string methods
1class Solution:
2    def addStrings(self, num1: str, num2: str) -> str:
3        i = len(num1) - 1
4        j = len(num2) - 1
5        carry = 0
6
7        ans = []
8
9        while i >= 0 or j >= 0 or carry:
10            n1 = ord(num1[i]) - ord('0') if i >= 0 else 0
11            n2 = ord(num2[j]) - ord('0') if j >= 0 else 0
12
13            totl = n1 + n2 + carry
14            ans.append(str(totl % 10))
15            carry = totl // 10
16
17            i -= 1
18            j -= 1
19
20        
21        s = "".join(ans)
22
23        return s[::-1]
24
25        