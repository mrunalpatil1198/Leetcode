class Solution:

    def search(self, nums: list[int], target: int) -> bool:
        left = 0
        right = len(nums) - 1

        #binary search
        while left <= right:
            mid = left + (right - left) // 2

            #returning if target found
            if nums[mid] == target:
                return True
            
            #checking if left to mid is sorted
            if nums[mid] > nums[left]:

                #setting upper limit to mid-1 if target lies between left and mid
                if target < nums[mid] and target >= nums[left]:
                    right = mid - 1
                else:
                    #target lies in the right half
                    left = mid + 1
            
            elif nums[mid] < nums[left]:
                #checking if target lies between sorted half - mid to right
                if target > nums[mid] and target <= nums[right]:
                    left = mid + 1
                else:
                    #target lies in the unsorted left half
                    right = mid - 1
            else:
                #linearly incrementing left if nums[mid] == nums[left]
                left += 1
        return False

if __name__ == '__main__':
    s = Solution()
    print(s.search(nums = [2,5,6,0,0,1,2], target = 0))

#Time Complexity - O(n)
#Space Complexity - O(1)