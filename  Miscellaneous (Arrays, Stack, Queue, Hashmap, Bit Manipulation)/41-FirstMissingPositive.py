class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:

        #replacing all negative numbers by 0
        for i in range(len(nums)):
            if nums[i] < 0:
                nums[i] = 0

        for i in range(len(nums)):
            val = abs(nums[i])
            if val >= 1 and val <= len(nums):
                #marking index 'val-1' with negative sign to show that 'val' number exists in the list 
                if nums[val-1] > 0:
                    nums[val-1] = -1 * nums[val-1]
                if nums[val-1] == 0:
                    nums[val-1] = - 1 * (len(nums)+1)
        
        for i in range(len(nums)):
            #returning index of first non-positive number from the list
            if nums[i] >= 0:
                return i+1
        return len(nums) + 1
    
if __name__ == '__main__':
    s = Solution()
    print(s.firstMissingPositive([1,2,0]))

#Time Complexity - O(n)
#Space Complexity - O(1)
