class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        minimum = nums[0]
        maximum = nums[0]
        result = nums[0]

        for i in range(1, len(nums)):
            temp = minimum
            minimum = min(minimum*nums[i], maximum*nums[i], nums[i])
            maximum = max(temp*nums[i], maximum*nums[i], nums[i])
            result = max(result, maximum)

        return result
    
if __name__ == '__main__':
    s = Solution()
    print(s.maxProduct([2,3,-2,4]))
    print(s.maxProduct([-2,0,-1]))