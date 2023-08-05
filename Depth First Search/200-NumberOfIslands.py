class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        
        #doing depth frist search on the grid
        def dfs(i, j):

            #terminating conditions
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == '0':
                return 0
            
            #marking the cell as visited by setting it to '0'
            grid[i][j] = '0'

            #performing dfs in all 4 directions
            dfs(i-1, j)
            dfs(i+1, j)
            dfs(i, j-1)
            dfs(i, j+1)

            #adding the island to final count by returning 1
            return 1

        count = 0

        #perform dfs on every '1' ecnountered in the grid
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    count += dfs(i, j)
        
        return count
    
if __name__ == '__main__':
    s = Solution()
    print(s.numIslands( [["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]]))
    
    print(s.numIslands( [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]))


#Time Complexity - O(m*n)
#Space Complexity - O(1) - not considering recursive stack space