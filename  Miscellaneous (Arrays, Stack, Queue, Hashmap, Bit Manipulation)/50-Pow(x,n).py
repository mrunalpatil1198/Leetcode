class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        
        #checking the sign
        if n < 0:
            n = -1 * n
            x = 1/x
        result = 1
        while n != 0:
            #if odd power, multiplying result by x
            if n % 2 == 1:
                result *= x
                n -= 1
            #doubling x and halving the power
            x *= x
            n //= 2
        return result
    
if __name__ == '__main__':
    s = Solution()
    print(s.myPow(x = 2.00000, n = 10))

#Time Complexity - O(logn)
#Space Complexity - O(1)