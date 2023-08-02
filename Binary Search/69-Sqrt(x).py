class Solution:
    def mySqrt(self, x: int) -> int:

        #setting lower and higher limits for binary search
        left = 1
        right = (x//2) + 1

        #binary search
        while left <= right:
            mid = left + (right - left) // 2

            #returning mid if mid*mid = x 
            if mid * mid == x:
                return mid
            
            #setting lower limit to mid + 1 as the square root lies in the right half
            if mid * mid < x:
                left = mid + 1

            #setting higher limit to mid - 1 as the square root lies in the left half
            else:
                right = mid - 1

        #returning right as left would have crossed right when exiting the above while loop and we need to rounded down to the nearest integer
        return right

if __name__ == '__main__':
    s = Solution()
    print(s.mySqrt(4))
    print(s.mySqrt(8))

#Time Complexity - O(logn)
#Space Complexity - O(1)