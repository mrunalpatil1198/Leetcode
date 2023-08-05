class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:

        #returning if source already has color as target color
        if image[sr][sc] == color:
            return image
        
        start_color = image[sr][sc]

        def dfs(i, j):
            #performing dfs in all 4 directions if curr cell has start_color
            if image[i][j] == start_color:
                image[i][j] = color
                if i>0: dfs(i-1,j)
                if i<len(image)-1: dfs(i+1, j)
                if j>0: dfs(i, j-1)
                if j<len(image[0])-1: dfs(i, j+1) 
        
        dfs(sr, sc)
        return image
    
if __name__ == '__main__':
    s = Solution()
    print(s.floodFill([[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, color = 2))

#Time Complexity - O(m*n)
#Space Complexity - O(1) - not considering recurrsion stack