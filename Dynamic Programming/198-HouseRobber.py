class Solution:
    def rob(self, nums) -> int:
        # dp = [] * len(nums)
        dp = [0 for _  in range(len(nums))]
        dp[0] = nums[0]
        dp[1] = max(dp[0], nums[1])

        for i in range(2, len(nums)):
            dp[i] = max(dp[i-1], dp[i-2]+nums[i])

        return dp[-1]
    
if __name__ == '__main__':
    s = Solution()
    print(s.rob([1,2,3,1]))
    print(s.rob([2,7,9,3,1]))
