class Solution:
    def change(self, amount: int, coins: list[int]) -> int:
        #create a dp matrix to store the number of combinations for each amount and coin type
        dp = [[0 for x in range(amount+1)] for y in range(len(coins)+1)]

        #base case - there is one way to make amount 0 using any number of coin types
        for i in range(0, len(dp)):
            dp[i][0] = 1
        
        for i in range(1, len(dp)):
            for j in range(1, len(dp[0])):
                #if the current amount is less than the current coin value, the number of combinations remains the same as the previous coin type
                if j < coins[i-1]:
                    dp[i][j] = dp[i-1][j]
                else:
                    #take the sum of the number of combinations using the previous coin type and the number of combinations using the current coin type with the remaining amount
                    dp[i][j] = dp[i-1][j] + dp[i][j-coins[i-1]]
        
        #return the number of combinations for the desired amount
        return dp[-1][-1]
    
if __name__ == '__main__':
    s = Solution()
    print(s.change(5, [1,2,5]))

#Time Complexity - O(amount*n) where n is the number of coin types
#Space Complexity - O(amount*n) where n is the number of coin types