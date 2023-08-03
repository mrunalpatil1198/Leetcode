class Solution:
    def missingNumber(self, nums: list[int]) -> int:

        #calculating sum of first n numbers
        expected_sum = (len(nums) * (len(nums) + 1)) // 2
        actual_sum = 0
        
        #calculating sum of numbers in nums
        for num in nums:
            actual_sum += num
        
        #difference between the above two is the result
        return expected_sum - actual_sum
    
if __name__ == '__main__':
    s = Solution()
    print(s.missingNumber([3,0,1]))

#Time Complexity - O(n)
#Space Complexity - O(1)