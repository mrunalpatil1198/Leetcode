class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:

        #create a list to store the result
        result = [1 for _ in range(len(nums))]

        #calculate the prefix product up to each element
        for i in range(1, len(nums)):
            result[i] = result[i-1] * nums[i-1]

        #initialize a variable to store the postfix product starting from the last element
        postfix = nums[len(nums)-1]
        
        #calculate the product of the postfix and multiply it with the result
        for i in range(len(nums) -2, -1, -1):
            result[i] *= postfix
            postfix *= nums[i]

        #retur the result
        return result
    
if __name__ == '__main__':
    s = Solution()
    print(s.productExceptSelf([1,2,3,4]))
    print(s.productExceptSelf([-1,1,0,-3,3]))

#Time Complexity - O(n)
#Space Complexity - O(1) - not considering the result as 'extra'
