class Solution:
    def numberOfArithmeticSlices(self, nums: list[int]) -> int:
        count = 0
        curr = 0

        for i in range(2, len(nums)):
            if nums[i] - nums[i-1] == nums[i-1] - nums[i-2]:
                curr += 1
                count += curr
            else:
                curr = 0

        return count

if __name__ == '__main__':
    s = Solution()
    print(s.numberOfArithmeticSlices(nums = [1,2,3,4])) 

#Time Complexity - O(n)
#Space Complexity - O(1)