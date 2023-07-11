class Solution:
    def rob(self, nums) -> int:

        #same as Leetcode 198 - House Robber 
        def dp(start, end):
            #create a dp list to store the maximum stolen amount at each house
            dp = [0 for _ in range(end+1)]

            #base cases
            if start == 0:
                dp[0] = nums[0]
                dp[1] = max(dp[0], nums[1])
            else:
                dp[1] = nums[1]

            for i in range(2, end+1):
                #maximum amount at house i is the maximum between robbing the previous house or robbing the current house and the house two steps back
                dp[i] = max(dp[i-1], dp[i-2] + nums[i])

            #return the last house amount
            return dp[-1]
        

        #maximum stolen amount can be calculated by considering two cases:
        #1-robbing houses from the first house to the second-to-last house
        #2-robbing houses from the second house to the last house
        #the maximum of the above two is the result
        return max(dp(0, len(nums)-2), dp(1, len(nums)-1))
    
if __name__ == '__main__':
    s = Solution()
    print(s.rob([2,3,2]))
    print(s.rob([1,2,3,1]))