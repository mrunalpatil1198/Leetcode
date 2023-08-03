class Solution:
    def search(self, nums: list[int], target: int) -> int:

        #setting left and right limits as 0 and len(target) - 1
        left = 0
        right = len(nums) - 1
        
        #binary search
        while left <= right:
            #calculating index of mid element
            mid = left + (right - left) // 2

            #if target found at mid, return
            if nums[mid] == target:
                return mid

            if nums[mid] < target:
                #target lies in right half hence changing the lower limit
                left = mid + 1
            else:
                #target lies in left half, changing the upper limit
                right = mid - 1

        return -1

if __name__ == '__main__':
    s = Solution()
    print(s.search(nums = [-1,0,3,5,9,12], target = 9))

#Time Complexity - O(logn)
#Space Complexity - O(1)
            