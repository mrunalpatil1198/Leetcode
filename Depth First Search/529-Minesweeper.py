class Solution:
    def updateBoard(self, board: list[list[str]], click: list[int]) -> list[list[str]]:

        #game over
        if board[click[0]][click[1]] == 'M':
            board[click[0]][click[1]] = 'X'
            return board
        
        #adjacent squares
        directions = [(-1, -1), (-1, 1), (-1, 0), (1, 1), (1, 0), (1, -1), (0, 1), (0, -1)]

        #counting adjacent mines
        def countAdjMines(i, j):
            count = 0
            for r, c in directions:
                if 0 <= i+r < len(board) and 0 <= j+c < len(board[0]) and board[i+r][j+c] == 'M':
                    count += 1
            return count
        
        def dfs(i ,j):
            if not 0 <= i < len(board) or not 0 <= j < len(board[0]) or board[i][j] != 'E':
                return
            mines = countAdjMines(i ,j)
            
            if mines > 0:
                board[i][j] = str(mines)
            else:
                board[i][j] = 'B'
                #recursively revealing the adjacent squares
                for r,c in directions:
                    dfs(i+r, j+c)
        
        dfs(click[0], click[1])
        return board
    
if __name__ == '__main__':
    s = Solution()
    print(s.updateBoard(board = [["E","E","E","E","E"],["E","E","M","E","E"],["E","E","E","E","E"],["E","E","E","E","E"]], click = [3,0]))
    
#Time Complexity - O(m*n)
#Space Complexity - O(1) - not considering recursive stack space