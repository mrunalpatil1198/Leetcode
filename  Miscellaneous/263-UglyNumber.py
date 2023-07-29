class Solution:
    def isUgly(self, n: int) -> bool:

        #checking if the num if divisible by 2, 3 or 5 till it becomes 1
        while n > 1:
            if n % 2 == 0: n //= 2
            elif n % 3 == 0: n //= 3
            elif n % 5 == 0: n //= 5
            else: return False

        return n == 1
    
if __name__ == '__main__':
    s = Solution()
    print(s.isUgly(n=6))
    
#Time Complexity - O(logn)
#Space Complexity - O(1)