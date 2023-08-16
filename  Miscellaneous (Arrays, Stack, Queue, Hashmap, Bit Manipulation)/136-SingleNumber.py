class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        result = 0
        for num in nums:
            #xoring all the elements as xor of same numbers is = 0
            result ^= num
        return result
    
if __name__ == '__main__':
    s = Solution()
    print(s.singleNumber(nums = [2,2,1]))

#Time Complexity - O(n)
#Space Complexity - O(1)