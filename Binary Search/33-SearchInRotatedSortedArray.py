class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        #binary search
        while left <= right:
            mid = left + (right - left) // 2

            #returning if target found at mid
            if nums[mid] == target:
                return mid

            #checking if left to mid is sorted in non-decreasing order
            if nums[mid] >= nums[left]:

                #checking if target lies between left and mid
                if target >= nums[left] and target <= nums[mid]:
                    right = mid - 1
                else:
                    #setting lower limit to mid+1 as target lies in the other half
                    left = mid + 1
            else:
                #setting lower limit to mid+1 as target lies between sorted half - mid to right
                if target >= nums[mid] and target <= nums[right]:
                    left = mid + 1
                else:
                    #target lies in the unsorted left half
                    right = mid - 1
        return -1
    
if __name__ == '__main__':
    s = Solution()
    print(s.search(nums = [4,5,6,7,0,1,2], target = 0))

#Time Complexity - O(logn)
#Space Complexity - O(1)