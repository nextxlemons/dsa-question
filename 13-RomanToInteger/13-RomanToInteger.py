# Last updated: 7/12/2026, 11:47:24 PM
class Solution:
    def romanToInt(self, s: str) -> int:
        res = 0
        rom = {"I" : 1, "V" : 5,"X" : 10,"L" : 50,"C" : 100,"D" : 500,"M" : 1000}
        i = 0
        while i < len(s):
            if i + 1 < len(s) and rom[s[i]] < rom[s[i+1]]:    
                res = res + rom[s[i+1]] - rom[s[i]]
                i = i + 2
            else:
                res += rom[s[i]]
                i = i + 1

        return res