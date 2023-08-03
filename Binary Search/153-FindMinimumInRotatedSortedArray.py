class Solution:
    def findMin(self, nums: list[int]) -> int:
        left = 0
        right = len(nums) - 1

        if len(nums) == 1:
            return nums[0]

        #if already sorted without rotation
        if nums[right] > nums[0]:
            return nums[0]

        #binary search
        while left <= right:
            mid = left + (right - left) //2
            #if the element next to mid is smaller, we have found the smallest 
            if nums[mid+1] < nums[mid]:
                return nums[mid+1]
            #if the element before to mid is greater, we have found the smallest 
            if nums[mid] < nums[mid-1]:
                return nums[mid]
            #if mid to right is not sorted, the smallest lies in this half
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                #smallest lies in the left half
                right = mid - 1
        return -1

if __name__ == '__main__':
    s = Solution()
    print(s.findMin([3,4,5,1,2])) 

#Time Complexity - O(logn)
#Space Complexity - O(1)