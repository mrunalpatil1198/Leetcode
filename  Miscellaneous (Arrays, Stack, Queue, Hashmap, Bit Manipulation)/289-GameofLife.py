class Solution:
    def gameOfLife(self, board: list[list[int]]) -> None:
        directions = [(1,0), (1,-1), (0,-1), (-1,-1), (-1,0), (-1,1), (0,1), (1,1)]

        for i in range(len(board)):
            for j in range(len(board[0])):
                live = 0
                for x,y in directions:
                    #calculating originally live neighbors
                    if (i+x < len(board) and i+x >= 0) and (j+y < len(board[0]) and j+y >= 0) and abs(board[i+x][j+y]) == 1:
                        live += 1
                    #updating to -1 if curr live is becoming dead
                if board[i][j] == 1 and (live < 2 or live > 3):
                    board[i][j] = -1
                #updating to 2 if curr dead is becoming live
                if board[i][j] == 0 and live == 3:
                    board[i][j] = 2

        #now, lives are denoted by 1 and 2 and dead by -1 and 0
        for i in range(len(board)):
            for j in range(len(board[0])):
                #updating 1 and 2 to 1 and -1 and 0 to 0
                board[i][j] = 1 if board[i][j]>0 else 0
        
        return board

if __name__ == '__main__':
    s = Solution()
    print(s.gameOfLife(board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]))

#Time Complexity - O(m*n)
#Space Complexity - O(1)