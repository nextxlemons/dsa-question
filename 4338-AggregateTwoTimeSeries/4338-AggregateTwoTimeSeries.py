# Last updated: 7/30/2026, 11:18:54 PM
class Solution:
    def aggregateTimeSeries(self, series1: list[list[int]], series2: list[list[int]]) -> list[list[int]]:
        i = j = 0
        n, m = len(series1), len(series2)
        ans = []

        while i < n or j < m:
            if j == m or (i < n and series1[i][0] < series2[j][0]):
                t = series1[i][0]
            elif i == n or series2[j][0] < series1[i][0]:
                t = series2[j][0]
            else:
                t = series1[i][0]

            while i < n and series1[i][0] < t:
                i += 1
            while j < m and series2[j][0] < t:
                j += 1

            v1 = series1[i][1] if i < n else 0
            v2 = series2[j][1] if j < m else 0
            ans.append([t, v1 + v2])

            if i < n and series1[i][0] == t:
                i += 1
            if j < m and series2[j][0] == t:
                j += 1

        return ans
        