class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        result = []

        #start with row 0 upto last row. for each row, place queen in a safe position and backtrack
        def backtrack(row):

            #base case: If all queens have been placed, add the current configuration to the result list and return
            if row == n:
                nonlocal result
                result.append([''.join(row) for row in board])
                return
            
            #try placing a queen in each column of the current row
            for col in range(n):

                #check if placing a queen at the current position is valid
                if col not in cols and row+col not in positive and row-col not in negative:

                    #if valid, place the queen at the current position and update the sets
                    board[row][col] = 'Q'
                    cols.add(col)
                    positive.add(row+col)
                    negative.add(row-col)

                    #recur with the next row to explore other possible solutions
                    backtrack(row+1)

                    #backtrack by removing the queen and updating the sets
                    cols.remove(col)
                    positive.remove(row+col)
                    negative.remove(row-col)
                    board[row][col] = '.'
            

        #create an empty N x N chessboard (board) filled with '.'
        board = [['.' for _ in range(n)] for _ in range(n)]
        cols = set() #set to keep track of columns with queens
        positive = set() #set to keep track of above diagonals with queens (row+col)
        negative = set() #set to keep track of below diagonals with queens (row-col)

        #start the backtracking process from row 0
        backtrack(0)
        return result
    
if __name__ == '__main__':
    s = Solution()
    print(s.solveNQueens(n = 4))

#Time Complexity - Exponential - O(n^n)