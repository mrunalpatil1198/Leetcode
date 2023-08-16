class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        
        #constant space solution with bit manipulation
        ones = 0
        twos = 0
        for num in nums:
            ones = (ones ^ num) & ~twos
            twos = (twos ^ num) & ~ones
        return ones

        #O(n) extra space solution using math
        #return ((3*sum(set(nums)) - sum(nums))) // 2
    
if __name__ == '__main__':
    s = Solution()
    print(s.singleNumber(nums = [2,2,3,2]))

#Time Complexity - O(n)
#Space Complexity - O(1)