class Solution:
    def change(self, amount: int, coins: list[int]) -> int:
        dp = [[0 for x in range(amount+1)] for y in range(len(coins)+1)]
        for i in range(0, len(dp)):
            dp[i][0] = 1
        
        for i in range(1, len(dp)):
            for j in range(1, len(dp[0])):
                if j < coins[i-1]:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-coins[i-1]]
        
        return dp[-1][-1]
    
if __name__ == '__main__':
    s = Solution()
    print(s.change(5, [1,2,5]))