class Solution:
    def findClosestElements(self, arr: list[int], k: int, x: int) -> list[int]:
        left = 0
        right = len(arr) - 1 - k

        #binary search
        #we need to find a window as the result - [left:left+k] 
        while left <= right:
            mid = left + (right - left) //2
            #checking the difference between x and mid and element after the window ends
            if x - arr[mid] > arr[mid + k] - x:
                #shifting window start to right
                left = mid + 1
            else:
                #shifting window end to left
                right = mid - 1
        #returning the window
        return arr[left : left + k] 
    
if __name__ == '__main__':
    s = Solution()
    print(s.findClosestElements(arr = [1,2,3,4,5], k = 4, x = 3))

#Time Complexity - O(logn)
#Space Complexity - O(1)