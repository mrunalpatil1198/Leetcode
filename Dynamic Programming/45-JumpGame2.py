class Solution:
    def jump(self, nums: list[int]) -> int:
        #create a dp table to store the minimum number of jumps to reach each position
        dp = [-1 for _ in range(len(nums))]
        dp[0] = 0

        #iterate over each position in the input list
        for i in range(0, len(nums)):
            #determine the maximum jump from the current position
            jump = nums[i]
            #iterate over each possible jump length from 1 to the maximum jump
            for j in range(1, jump+1):
                if i+j < len(nums):
                    #if the next position is not yet reached, update the minimum number of jumps needed to reach it
                    if dp[i+j] == -1:
                        dp[i+j] = dp[i] + 1
                    #if the next position is already reached, update the minimum jumps only if the new path requires fewer jumps
                    else:
                        dp[i+j] = min(dp[i+j], dp[i]+1)

        #return last value of dp as it has minimum number of jumps needed to reach the last position
        return dp[-1]
    
if __name__ == '__main__':
    s = Solution()
    print(s.jump([2,3,1,1,4]))
    print(s.jump([2,3,0,1,4]))

#Time Complexity - O(n^2)
#Space Complexity - O(n)