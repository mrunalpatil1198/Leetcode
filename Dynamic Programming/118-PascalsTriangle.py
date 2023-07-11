class Solution:
    def generate(self, numRows: int):
        #create a 2D list to store the Pascal's triangle
        dp = [[1] * x for x in range(1,numRows+1)]

        #iterate from the third row as first two are 1
        for i in range(2, numRows):
            #iterate through each element in the current row, excluding the first and last elements as they are = 1
            for j in range(1, i):
                #the value at the current position is the sum of values from the previous row's jth and j-1th col
                dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
        #return the triangle
        return dp

if __name__ == '__main__':
    s = Solution()
    print(s.generate(3))

#Time Complexity - O(numRows^2)
#Space Complexity - O(numRows^2)