class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:

        result = [1 for _ in range(len(nums))]

        for i in range(1, len(nums)):
            result[i] = result[i-1] * nums[i-1]

        postfix = nums[len(nums)-1]
        for i in range(len(nums) -2, -1, -1):
            result[i] *= postfix
            postfix *= nums[i]
        
        return result
    
if __name__ == '__main__':
    s = Solution()
    print(s.productExceptSelf([1,2,3,4]))
    print(s.productExceptSelf([-1,1,0,-3,3]))
