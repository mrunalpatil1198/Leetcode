class Solution:
    def generate(self, numRows: int):
        dp = [[1] * x for x in range(1,numRows+1)]

        for i in range(2, numRows):
            for j in range(1, i):
                dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
        return dp

if __name__ == '__main__':
    s = Solution()
    print(s.generate(3))