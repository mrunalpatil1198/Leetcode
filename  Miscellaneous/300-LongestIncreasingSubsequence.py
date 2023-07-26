class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        dp = [0 for _ in range(len(nums))]
        dp[0] = 1
        for i in range(1, len(nums)):
            maxi = 0
            for j in range(0, i):
                if nums[i] > nums[j]:
                    maxi = max(maxi, dp[j])
            dp[i] = maxi + 1
        return max(dp)
    
if __name__ == '__main__':
    s = Solution()
    print(s.lengthOfLIS(nums = [10,9,2,5,3,7,101,18]))