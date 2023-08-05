class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        result = 0

        def dfs(i, j):
            #terminating conditions
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == 0:
                return 0
            
            #initializing area to 1
            area = 1

            #marking grid[i][j] as visited by setting it to '0'
            grid[i][j] = 0

            #calculating area in all 4 directions of the cell
            area += dfs(i-1, j)
            area += dfs(i+1, j)
            area += dfs(i, j-1)
            area += dfs(i, j+1)

            return area
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                #performing dfs and calculating area of each island in the grid
                if grid[i][j] == 1:
                    area = dfs(i, j)

                    #updating max area
                    result = max(result, area)

        return result
    
if __name__ == '__main__':
    s = Solution()
    print(s.maxAreaOfIsland([[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]))

#Time Complexity - O(n*m)
#Space Complexity - O(1) - not considering stack space