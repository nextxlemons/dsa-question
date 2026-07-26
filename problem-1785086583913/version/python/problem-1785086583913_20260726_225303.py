# Last updated: 7/26/2026, 10:53:03 PM
# solved by ai
1class Solution:
2    def aggregateTimeSeries(self, series1: list[list[int]], series2: list[list[int]]) -> list[list[int]]:
3        i = j = 0
4        n, m = len(series1), len(series2)
5        ans = []
6
7        while i < n or j < m:
8            if j == m or (i < n and series1[i][0] < series2[j][0]):
9                t = series1[i][0]
10            elif i == n or series2[j][0] < series1[i][0]:
11                t = series2[j][0]
12            else:
13                t = series1[i][0]
14
15            while i < n and series1[i][0] < t:
16                i += 1
17            while j < m and series2[j][0] < t:
18                j += 1
19
20            v1 = series1[i][1] if i < n else 0
21            v2 = series2[j][1] if j < m else 0
22            ans.append([t, v1 + v2])
23
24            if i < n and series1[i][0] == t:
25                i += 1
26            if j < m and series2[j][0] == t:
27                j += 1
28
29        return ans
30        