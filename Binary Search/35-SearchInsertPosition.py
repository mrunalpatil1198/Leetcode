class Solution:

    def searchInsert(self, nums: list[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        #edge cases
        if target < nums[left]:
            return left
        if target > nums[right]:
            return right + 1

        #binary search
        while left <= right:
            mid = left + (right - left) // 2
            #returning mid if correct position is found
            if nums[mid] == target or (nums[mid] > target and nums[mid-1] < target):
                return mid
            
            #setting low limit to mid+1 as target lies in the second half
            elif nums[mid] < target:
                left = mid + 1

            #setting high limit to mid-1 as target lies in the first half
            else:
                right = mid - 1
        return -1
    
if __name__ == '__main__':
    s = Solution()
    print(s.searchInsert(nums = [1,3,5,6], target = 5))

#Time Complexity - O(logn)
#Space Complexity - O(1)