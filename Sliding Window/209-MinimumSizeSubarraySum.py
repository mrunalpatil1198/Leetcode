class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:

        #initialize the left pointer to the start of the window
        left = 0
        result = float('inf')

        #initialize sum to keep track of the current sum of elements in the window
        sum = 0

        #traverse the array using the right pointer
        for right in range(len(nums)):

            #add the current element to sum
            sum += nums[right]

            #check if the sum is greater than or equal to the target
            while sum >= target:

                # if yes, update result with the minimum of its current value and the window size (right - left + 1).
                result = min(result, right-left+1)

                #shrink the window from the left side by removing the element at left from the sum
                sum -= nums[left]
                
                #move the left pointer to the right to shrink the window further
                left += 1
        
        return result if result != float('inf') else 0
    
if __name__ == '__main__':
    s = Solution()
    print(s.minSubArrayLen(target = 7, nums = [2,3,1,2,4,3]))

#Time Complexity - O(n)
#Space Complexity - O(1)