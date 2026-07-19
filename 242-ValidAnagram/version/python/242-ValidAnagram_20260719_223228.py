# Last updated: 7/19/2026, 10:32:28 PM
# using ord method
1class Solution:
2    def isAnagram(self, s: str, t: str) -> bool:
3        cnt = [0] * 26
4
5        for ch in s:
6            cnt[ord(ch) - ord('a')] += 1
7        for ch in t:
8            cnt[ord(ch) - ord('a')] -= 1
9
10        return all(x == 0 for x in cnt)
11        