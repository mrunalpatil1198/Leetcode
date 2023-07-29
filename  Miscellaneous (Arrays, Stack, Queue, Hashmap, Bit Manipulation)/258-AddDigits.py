class Solution:
    def addDigits(self, num: int) -> int:
        while True:
            sum = 0
            #adding all digits of num one by one
            while num != 0:
                sum += num % 10
                num = num // 10
            #terminating condition
            if sum < 10:
                return sum
            else:
                #updating num
                num = sum
    
if __name__ == '__main__':
    s = Solution()
    print(s.addDigits(38))

#Time Complexity - O(n)
#Space Complexity - O(1)