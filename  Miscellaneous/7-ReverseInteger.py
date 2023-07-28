class Solution:
    def reverse(self, x: int) -> int:
        def cal(x):

            #converting into string to reverse
            x = str(x)
            if x[0] == '-':
                x = x[1:]
                return -int(x[::-1])
            else:
                return int(x[::-1])
            
        #checking limits
        if x<=((2**31)-1) and x >= -2**31:
            y = cal(x)
            if y<=((2**31)-1) and y >= -2**31:
                return y
            else:
                return 0
        else:
            return 0
        
if __name__ == '__main__':
    s = Solution()
    print(s.reverse(-123))

#Time Complexity - O(n)
#Space Complexity - O(n)