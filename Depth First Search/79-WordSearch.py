class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:

        def dfs(i, j, k):
            #word exists
            if k == len(word):
                return True
            
            #curr index out of bound or curr char does not match
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] != word[k]:
                return False
            
            #marking board[i][j] as visited
            temp = board[i][j]
            board[i][j] = '.'
            
            #recursively calling dfs on adjacent cells
            if dfs(i-1, j, k+1) or dfs(i, j-1, k+1) or dfs(i+1, j, k+1) or dfs(i, j+1, k+1):
                return True
            
            #marking board[i][j] as unvisited if word not found
            board[i][j] = temp

        
        #dfs on every possible starting point in board
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if dfs(i, j, 0):
                        #word found
                        return True
        
        return False

if __name__ == '__main__':
    s = Solution()
    print(s.exist(board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"))

#Time Complexity - O(m*n)
#Space Complexity - O(1) - not considering the recursive stack space