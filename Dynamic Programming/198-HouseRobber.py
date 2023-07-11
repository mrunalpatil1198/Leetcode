class Solution:
    def rob(self, nums) -> int:
        
        #create a dp list to store the maximum stolen amount at each house
        dp = [0 for _  in range(len(nums))]

        #base cases
        dp[0] = nums[0]
        dp[1] = max(dp[0], nums[1])

        for i in range(2, len(nums)):
            #maximum amount at house i is the maximum between robbing the previous house or robbing the current house and the house two steps back
            dp[i] = max(dp[i-1], dp[i-2]+nums[i])

        #return the last house amount
        return dp[-1]
    
if __name__ == '__main__':
    s = Solution()
    print(s.rob([1,2,3,1]))
    print(s.rob([2,7,9,3,1]))

#Time Complexity - O(n)
#Space Complexity - O(n)