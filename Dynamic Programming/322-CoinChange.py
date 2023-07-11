class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:

        #create a dp matrix to store the minimum number of coins required for each amount and initialize it to 'inf' or amount+1
        dp = [[amount+1 for x in range(amount+1)] for y in range(len(coins)+1)]

        #base case 
        dp[0][0] = 0

        #set the number of coins required for amount 0 for each coin type to 0
        for i in range(1, len(coins)+1):
            dp[i][0] = 0

        #fill in the dp
        for i in range(1, len(dp)):
            for j in range(1, len(dp[0])):
                #if the current amount is less than the current coin value, the minimum number of coins required remains the same as the previous coin type
                if j < coins[i-1]:
                    dp[i][j] = dp[i-1][j]
                else:
                    #take the minimum between using the previous coin type's dp and using the current coin type(+1) plus the dp for the remaining amount
                    dp[i][j] = min(dp[i-1][j], dp[i][j-coins[i-1]]+1)
        
        #if it's not possible to make the desired amount, return -1; otherwise, return the minimum number of coins
        return dp[-1][-1] if dp[-1][-1] != amount+1 else -1
    

if __name__ == '__main__':
    s = Solution()
    print(s.coinChange([1,2,5], 11))

#Time Complexity - O(amount*n) where n is the number of coin types
#Space Complexity - O(amount*n) where n is the number of coin types
