class Solution:
    def climbStairs(self, n: int) -> int:
        
        #create a dp list to store the number of ways to climb each step
        dp = [0] * (n+3)
        
        #base cases
        dp[1] = 1
        dp[2] = 2

        #iterate from the third step till the end
        for i in range(3,n+1):
            #for each stair, we can either climb from the previous by making 1 jump or make 2 jumps from the second last 
            dp[i] = dp[i-1]+dp[i-2]
        
        #return the last element of dp
        return dp[n]
    
if __name__ == '__main__':
    s = Solution()
    print(s.climbStairs(3))

#Time Complexity - O(n)
#Space Complexity - O(n)

