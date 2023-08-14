class Solution:
    def maxCoins(self, nums: list[int]) -> int:

        #adding 2 dummy balloons each with value 1 to handle the corner balloons in the nums
        nums = [1] + nums + [1]
        dp = {}

        def dfs(l ,r):
            if l > r:
                return 0
            
            #checking if solution is already stored for this subproblem
            if (l, r) in dp:
                return dp[(l ,r)]
            
            dp[(l ,r)] = 0

            #choosing the ith balloon as the last one to be burst
            for i in range(l, r+1):
                #the profit will be nums[l - 1] * nums[i] * nums[r + 1] as balloons in the range (l, i - 1) and (i + 1, r) will be burst before ith balloon
                coins = nums[l-1] * nums[i] * nums[r+1]
                #calculating the profit by solving the subproblems recursively
                coins += dfs(l, i-1) + dfs(i+1, r)
                dp[(l ,r)] = max(dp[(l ,r)], coins)
            return dp[(l, r)]
        return dfs(1, len(nums) - 2)
        
if __name__ == '__main__':
    s = Solution()
    print(s.maxCoins(nums = [3,1,5,8]))
                
#Time Complexity - O(n^3)
#Space Complexity - O(n^2)