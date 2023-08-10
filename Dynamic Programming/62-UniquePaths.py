class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # #Approach 1: dfs + memoization
        # #creating 2D matrix of m*n size where each cell would store total number of unique paths till that point
        # dp = [[-1 for _ in range(n)] for _ in range(m)]
        # def solve(i, j):
        #     if i >= m or j >= n:
        #         return 0
        #     #finish point
        #     if i == m-1 and j == n-1:
        #         return 1
        #     if dp[i][j] != -1:
        #         return dp[i][j]
        #     #recursively calling for side and bottom cell
        #     dp[i][j] = solve(i+1, j) + solve(i, j+1)
        #     return dp[i][j]
        # return solve(0, 0)

        #Approach 2: bottom-up
        #bottom row of all 1s
        old_row = [1] * n

        for i in range(m-1, 0, -1):
            #calculating new row for each row
            new_row = [1] * n
            #traversing cols in reverse
            for j in range(n-2, -1, -1):
                #at each postion ' answer is answer at j+1 block of same row + answer at j position of bottom row 
                new_row[j] = new_row[j+1] + old_row[j]
            old_row = new_row
        return old_row[0]
    
        #Approach 3: top-bottom
        # dp = [[0 for _ in range(n)]for _ in range(m)]
        # dp[0][0] = 1
        # for i in range(m):
        #     for j in range(n):
        #         if i-1 >= 0:
        #             dp[i][j] += dp[i-1][j]
        #         if j-1 >= 0:
        #             dp[i][j] += dp[i][j-1]
        # return dp[-1][-1]

if __name__ == '__main__':
    s = Solution()
    print(s.uniquePaths(m = 3, n = 7))

#Time Complexity - O(m*n)
#Space Complexity - O(m*n)