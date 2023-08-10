class Solution:
    def maximalSquare(self, matrix: list[list[str]]) -> int:

        #dp[i][j] would represent the max square side possible as matrix[i][j] the bottom corner
        dp = [[0 for _ in range(len(matrix[0])+1)] for _ in range(len(matrix)+1)]
        max_side = 0

        #filling the dp array
        for i in range(0, len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == '1':
                    #checking the values of the cells to the left, top, and top-left of the current cell
                    dp[i+1][j+1] = min(dp[i][j+1], dp[i+1][j], dp[i][j]) + 1
                    #updating the max side seen so far
                    max_side = max(max_side, dp[i+1][j+1])
        
        #area of square is side^2
        return max_side ** 2

if __name__ == '__main__':
    s = Solution()
    print(s.maximalSquare(matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]))

#Time Complexity - O(m*n)
#Space Complexity - O(m*n)