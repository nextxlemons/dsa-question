# Last updated: 7/23/2026, 3:49:45 PM
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pascalList = []
        for i in range(numRows):
            innerList = []

            for j in range(i + 1):
                if j == 0 or j == i:
                    innerList.append(1)
                else:
                    k = pascalList[i - 1][j - 1] + pascalList[i - 1][j]
                    innerList.append(k)
            pascalList.append(innerList)

        return pascalList
        