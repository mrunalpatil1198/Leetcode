class Solution:
    def jump(self, nums: list[int]) -> int:
        dp = [-1 for _ in range(len(nums))]
        dp[0] = 0
        #jkbdvkd
        for i in range(0, len(nums)):
            jump = nums[i]
            for j in range(1, jump+1):
                if i+j < len(nums):
                    if dp[i+j] == -1:
                        dp[i+j] = dp[i] + 1
                    else:
                        dp[i+j] = min(dp[i+j], dp[i]+1)

        return dp[-1]
    
if __name__ == '__main__':
    s = Solution()
    print(s.jump([2,3,1,1,4]))
    print(s.jump([2,3,0,1,4]))