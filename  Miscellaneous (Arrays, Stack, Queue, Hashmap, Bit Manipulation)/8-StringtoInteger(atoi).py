class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        sign = 1
        i = 0
        num = 0
        if not s:
            return num
        
        if not s[0].isdigit():
            if s[0] != '-' and s[0] != '+':
                return num
            sign = sign*-1 if s[0] == '-' else sign
            i += 1
        
        while i < len(s) and s[i].isdigit():
            num = num * 10 + int(s[i])
            i += 1
        
        num = sign * num
        return min(2**31-1, max(-2**31, num))
    
if __name__ == '__main__':
    s = Solution()
    print(s.myAtoi(s = "42"))

#Time Complexity - O(n)
#Space Complexity - O(1)