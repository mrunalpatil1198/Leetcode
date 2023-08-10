class Solution:
    def minimumTotal(self, triangle: list[list[int]]) -> int:

        #dp[(i, j)] would represent the minimum path sum at triangle[i][j]
        dp = {(0, 0) : triangle[0][0]}

        for i in range(1, len(triangle)):
            for j in range(i+1):
                #adding curr to path from previous row same col or col-1
                dp[(i, j)] = triangle[i][j] + min(dp.get((i-1, j), float('inf')), dp.get((i-1, j-1), float('inf')))
        
        #returning minimum from last row of dp
        return min(dp[len(triangle)-1, j] for j in range(len(triangle[-1])))
    
if __name__ == '__main__':
    s = Solution()
    print(s.minimumTotal(triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]))

#Time Complexity - O(m*n)
#Space Complexity - O(m*n)

