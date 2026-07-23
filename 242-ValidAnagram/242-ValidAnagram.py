# Last updated: 7/23/2026, 3:49:41 PM
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        cnt = [0] * 26

        for ch in s:
            cnt[ord(ch) - ord('a')] += 1
        for ch in t:
            cnt[ord(ch) - ord('a')] -= 1

        return all(x == 0 for x in cnt)
        