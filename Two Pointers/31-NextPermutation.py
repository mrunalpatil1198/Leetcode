class Solution:
    def nextPermutation(self, nums: list[int]) -> None:

        #starting from right, finding a pair of nums[i] and nums[i+1] such that nums[i] < nums[i+1]
        i = len(nums) - 2
        while i >= 0 and nums[i+1] <= nums[i]:
            i -= 1
        
        #starting from right, finding an index j such that nums[j] > nums[i]
        if i >= 0:
            j = len(nums) - 1
            while nums[j] <= nums[i]:
                j -= 1
            #swapping ith and jth element
            nums[i], nums[j] = nums[j], nums[i]

        #sorting elements between i+1 and the end of the array
        i += 1
        j = len(nums) - 1
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
            
if __name__ == '__main__':
    s = Solution()
    nums = [1,2,3]
    s.nextPermutation(nums)
    print(nums)

#Time Complexity - O(n)
#Space Complexity - O(1)