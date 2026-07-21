# Last updated: 7/21/2026, 6:04:21 PM
# Good Program
1class Solution:
2    def generate(self, numRows: int) -> List[List[int]]:
3        pascalList = []
4        for i in range(numRows):
5            innerList = []
6
7            for j in range(i + 1):
8                if j == 0 or j == i:
9                    innerList.append(1)
10                else:
11                    k = pascalList[i - 1][j - 1] + pascalList[i - 1][j]
12                    innerList.append(k)
13            pascalList.append(innerList)
14
15        return pascalList
16        