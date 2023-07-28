class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        sign = True if (dividend < 0 and divisor >= 0 )or (divisor < 0 and dividend >= 0) else False
        dividend = abs(dividend)
        divisor = abs(divisor)

        #calculating the number of times we need to add divisor into 0 to reach the divided
        result = len(range(0, dividend - divisor + 1, divisor))

        #checking for the sign
        if sign:
            result = result * -1
        minus_limit = -(2**31)
        plus_limit = (2**31)-1

        #checking the integer limits
        result = min(max(result, minus_limit), plus_limit)
        return result
    
if __name__ == '__main__':
    s = Solution()
    print(s.divide(dividend = 10, divisor = 3))

#Time Complexity - O(n)
#Space Complexity - O(n)