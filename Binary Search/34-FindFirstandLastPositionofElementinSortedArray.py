class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:

        def binarySearch(target):
            low = 0
            high = len(nums)-1
            #binary search algorithm returns the first occurrence index of the element if present, else returns index of smallest element greater than the target
            while low <= high:
                mid = low + (high-low)//2
                if nums[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1
            return low
        
        #getting the first occurrence
        first = binarySearch(target)

        #getting the last occurence by passing target+1 and then -1 from the returned index
        last = binarySearch(target+1) - 1

        #checking if a valid solution
        if first <= last:
            return [first, last]
        return [-1, -1]
    
if __name__ == '__main__':
    s = Solution()
    print(s.searchRange(nums = [5,7,7,8,8,10], target = 8))

#Time Complexity - O(logn)
#Space Complexity - O(1)