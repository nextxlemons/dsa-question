# Last updated: 7/30/2026, 11:19:12 PM
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            r = []
            c = []
        
            for j in range(9):
                if board[i][j] != ".":
                    r.append(board[i][j])
                if board[j][i] != ".":
                    c.append(board[j][i])
            
            if len(r) != len(set(r)) or len(c) != len(set(c)):
                return False

        for i in range(0,9,3):
            for j in range(0,9,3):
                mat = []
                for r in range(i,i+3):
                    for c in range(j,j+3):
                        if board[r][c] != ".":
                            mat.append(board[r][c])
                if len(mat) != len(set(mat)):
                    return False
        return True
        