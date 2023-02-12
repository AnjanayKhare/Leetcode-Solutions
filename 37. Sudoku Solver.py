class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:        
        def isVaidMove(i, j):
            row = i//3
            col = j//3
            for r in range(3*row, 3*row+3):
                for c in range(3*col, 3*col+3):
                    if board[r][c] == board[i][j] and (i, j)!=(r, c):
                        return False
            for k in range(9):
                if i!=k and board[k][j] == board[i][j]:
                    return False
                if j!=k and board[i][k] == board[i][j]:
                    return False
            return True
        

        frozen = [[True]*9 for _ in range(9)]
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    frozen[i][j] = False
    
        def dfs(i, j):
            if i==9 and j==0:
                return True
            if j==8:
                i_next = i+1
                j_next = 0
            else:
                i_next = i
                j_next = j+1
            if frozen[i][j]:
                return dfs(i_next, j_next)
            for move in range(1, 10):
                board[i][j] = str(move)
                if isVaidMove(i, j) and dfs(i_next, j_next):
                    return True
                board[i][j] = '.'
            return False
        
        dfs(0, 0)
        return board
