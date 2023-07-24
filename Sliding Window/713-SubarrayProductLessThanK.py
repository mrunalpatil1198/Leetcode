class Solution:
    def numSubarrayProductLessThanK(self, nums: list[int], k: int) -> int:
        if k <= 1:
            return 0
        
        #initialize left as the start for the  window
        left = 0

        #maintain a variable to store the product so far
        product = 1

        #maintain a variable for result
        result = 0

        #traverse through the array using the right pointer
        for right in range(len(nums)):

            #update the product so far
            product *= nums[right]

            #if product exceeds k, shrink the window till the product becomes less than k
            while product >= k:
                product /= nums[left]
                left += 1
            
            #add the window size to result as the window size is equal to the number of subarrays present in the window having product less than k
            result += right-left+1
        
        return result
    
if __name__ == '__main__':
    s = Solution()
    print(s.numSubarrayProductLessThanK(nums = [10,5,2,6], k = 100))

#Time Complexity - O(n)
#Space Complexity - O(1)