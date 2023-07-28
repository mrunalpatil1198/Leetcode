class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        temp1 = 0
        temp2 = 1
        for i in range(2, n+1):
            #adding the previous two values of fibonacci
            temp = temp1 + temp2
            temp1 = temp2
            temp2 = temp
        return temp2

if __name__ == '__main__':
    s = Solution()
    print(s.fib(4))
    
#Time complexity - O(n)
#Space Complexity - O(1)