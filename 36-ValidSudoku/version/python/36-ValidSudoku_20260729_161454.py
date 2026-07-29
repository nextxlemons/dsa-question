# Last updated: 7/29/2026, 4:14:54 PM
# took very much time
1class Solution:
2    def isValidSudoku(self, board: List[List[str]]) -> bool:
3        for i in range(9):
4            r = []
5            c = []
6        
7            for j in range(9):
8                if board[i][j] != ".":
9                    r.append(board[i][j])
10                if board[j][i] != ".":
11                    c.append(board[j][i])
12            
13            if len(r) != len(set(r)) or len(c) != len(set(c)):
14                return False
15
16        for i in range(0,9,3):
17            for j in range(0,9,3):
18                mat = []
19                for r in range(i,i+3):
20                    for c in range(j,j+3):
21                        if board[r][c] != ".":
22                            mat.append(board[r][c])
23                if len(mat) != len(set(mat)):
24                    return False
25        return True
26        