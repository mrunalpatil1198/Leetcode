class Solution:
    def singleNumber(self, nums: list[int]) -> list[int]:
        if len(nums) == 2:
            return nums
        
        #xoring all the numbers which results in xor of two unique numbers at the end
        x = 0
        for num in nums:
            x ^= num
        
        #finding the first set bit in x
        mask = x & -x

        #dividing the numbers into two groups based on the set bit with each group having excatly one of the unique numbers
        #the problem becomes same as SingleNumberI from here
        group1 = group2 = 0
        for num in nums:
            if num & mask:
                group1 ^= num
            else:
                group2 ^= num
        
        return [group1, group2]
    
if __name__ == '__main__':
    s = Solution()
    print(s.singleNumber(nums = [1,2,1,3,2,5]))

#Time Complexity - O(n)
#Space Complexity - O(1)