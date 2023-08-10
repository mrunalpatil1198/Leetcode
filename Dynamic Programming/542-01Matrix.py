class Solution:
    def updateMatrix(self, mat: list[list[int]]) -> list[list[int]]:

        #copying matrix into dp
        dp = [row[:] for row in mat]

        #going from top left to bottom right cell
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                min_dist = float('inf')
                if dp[i][j] != 0:
                    #updating the distance by checking dp of top and left cells
                    if i > 0:
                        min_dist = min(min_dist, dp[i-1][j])
                    if j > 0:
                        min_dist = min(min_dist, dp[i][j-1])
                    dp[i][j] = min_dist + 1
        
        #going from bottom right to top left cell
        for i in range(len(mat)-1, -1, -1):
            for j in range(len(mat[0])-1, -1, -1):
                min_dist = float('inf')
                if dp[i][j] != 0:
                    #updating the distance by checking dp of bottom and right cells
                    if i < len(mat)-1:
                        min_dist = min(min_dist, dp[i+1][j])
                    if j < len(mat[0])-1:
                        min_dist = min(min_dist, dp[i][j+1])
                    dp[i][j] = min(dp[i][j], min_dist+1)

        return dp
    
if __name__ == '__main__':
    s = Solution()
    print(s.updateMatrix(mat = [[0,0,0],[0,1,0],[0,0,0]]))
        
#Time Complexity - O(m*n)
#Space Complexity - O(m*n)
