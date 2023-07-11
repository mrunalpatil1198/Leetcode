class Solution:
    def rob(self, nums) -> int:

        def dp(start, end):
            dp = [0 for _ in range(end+1)]
            if start == 0:
                dp[0] = nums[0]
                dp[1] = max(dp[0], nums[1])
            else:
                dp[1] = nums[1]

            for i in range(2, end+1):
                dp[i] = max(dp[i-1], dp[i-2] + nums[i])

            return dp[-1]
        
        return max(dp(0, len(nums)-2), dp(1, len(nums)-1))
    
if __name__ == '__main__':
    s = Solution()
    print(s.rob([2,3,2]))
    print(s.rob([1,2,3,1]))