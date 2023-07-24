class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        result = 0

        #pointer pointing to the start of window
        left = 0

        #traverse num using right pointer
        for right in range(len(nums)):

            if nums[right] == 0:
                #if the current element is 0, we need to consider it for flipping
                #if we have flips left, decrement flips available and continue
                if k > 0:
                    k -= 1

                else:
                    #move the left pointer to the right to shrink the window until we encounter a 0.
                    while nums[left] == 1:
                        left += 1
                    
                    #increment left by 1 to move it past the first 0 in window in order to accomodate current 0
                    left += 1

            #update the 'result' with the maximum window size seen so far
            result = max(result, right-left+1)

        return result

if __name__ == '__main__':
    s = Solution()
    print(s.longestOnes(nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2))

#Time Complexity - O(n)
#Space Complexity - O(1)