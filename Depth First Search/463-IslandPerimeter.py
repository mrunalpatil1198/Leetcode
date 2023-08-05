class Solution:
    def islandPerimeter(self, grid: list[list[int]]) -> int:
        perimeter = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                #calculating perimeter for each cell marked as land
                if grid[i][j] == 1:
                    #checking all four adjacent cells for water
                    if i == 0 or grid[i-1][j] == 0:
                        perimeter += 1
                    if i == len(grid)-1 or grid[i+1][j] == 0:
                        perimeter += 1
                    if j == 0 or grid[i][j-1] == 0:
                        perimeter += 1
                    if j == len(grid[0])-1 or grid[i][j+1] == 0:
                        perimeter += 1
        return perimeter
    
if __name__ == '__main__':
    s = Solution()
    print(s.islandPerimeter([[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]))
    print(s.islandPerimeter([[1]]))
    print(s.islandPerimeter([[1,0]]))

#Time Complexity - O(m*n)
#Space Complexity - O(1)
