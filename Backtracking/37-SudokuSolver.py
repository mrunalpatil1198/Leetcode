import collections

class Solution:
    def solveSudoku(self, board: list[list[str]]):

        #create sets to store the numbers present in each row, column, and 3x3 squares
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        squares = collections.defaultdict(set)
        solved = False

        #populate the sets with the existing numbers in the board
        for i in range(0, 9):
            for j in range(0, 9):
                if board[i][j] != '.':
                    num = int(board[i][j])
                    rows[i].add(num)
                    cols[j].add(num)
                    squares[(i // 3, j // 3)].add(num)


        #start filling the board using bactracking for every cell in every row
        def backtrack(i, j):
            nonlocal solved

            #if we have reached row index 9, it means we were able to solve the sudoku, set solved to True and return
            if i == 9:
                solved = True
                return
            
            #calculate next cell indices
            new_i = i + 1 if j == 8 else i
            new_j = (j + 1) % 9

            #if the cell is already filled, move to the next cell
            if board[i][j] != '.':
                backtrack(new_i, new_j)

            else:
                #try placing numbers from 1 to 9 in the cell and check if it's valid
                for n in range(1, 10):
                    
                    #if valid, set board[i][j] to n and add it to respective row, col and squares set
                    if n not in rows[i] and n not in cols[j] and n not in squares[(i // 3, j // 3)]:
                        board[i][j] = str(n)
                        rows[i].add(n)
                        cols[j].add(n)
                        squares[(i // 3, j // 3)].add(n)

                        #recurse for the next cell
                        backtrack(new_i, new_j)

                        #if the Sudoku is not solved, backtrack by removing the number from the cell
                        if not solved:
                            board[i][j] = '.'
                            rows[i].remove(n)
                            cols[j].remove(n)
                            squares[(i // 3, j // 3)].remove(n)

        #start the backtracking process from the top-left cell (0, 0)
        solved = False
        backtrack(0, 0)
        return board

if __name__ == '__main__':
    s = Solution()
    print(s.solveSudoku(board=[["5", "3", ".", ".", "7", ".", ".", ".", "."],
                               ["6", ".", ".", "1", "9", "5", ".", ".", "."],
                               [".", "9", "8", ".", ".", ".", ".", "6", "."],
                               ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
                               ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
                               ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                               [".", "6", ".", ".", ".", ".", "2", "8", "."],
                               [".", ".", ".", "4", "1", "9", ".", ".", "5"],
                               [".", ".", ".", ".", "8", ".", ".", "7", "9"]]))

#Time Complexity - Exponential - O(9^n)