class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        #initialize variables to store the minimum product, maximum product, and the overall result
        minimum = nums[0]
        maximum = nums[0]
        result = nums[0]

        for i in range(1, len(nums)):
            #store the current minimum value to use it for calculating the new maximum as the minimum value will be changed to new minimum
            temp = minimum
            #update the minimum and maximum values based on three possible scenarios:
            #1-current number multiplied by the previous minimum value
            #2-current number multiplied by the previous maximum value
            #3-current number alone
            minimum = min(minimum*nums[i], maximum*nums[i], nums[i])
            maximum = max(temp*nums[i], maximum*nums[i], nums[i])

            #update the overall result by taking the maximum value between the result and the current maximum
            result = max(result, maximum)

        return result
    
if __name__ == '__main__':
    s = Solution()
    print(s.maxProduct([2,3,-2,4]))
    print(s.maxProduct([-2,0,-1]))

#Time Complexity - O(n)
#Space Complexity - O(1)