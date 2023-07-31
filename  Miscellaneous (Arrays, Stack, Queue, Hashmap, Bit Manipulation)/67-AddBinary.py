class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        i = len(a)-1
        j = len(b) - 1
        result = []

        #adding bits of a and b from right towards left
        while i >= 0 or j >= 0 or carry:
            if i >= 0:
                carry += int(a[i])
                i -= 1
            if j >= 0:
                carry += int(b[j])
                j -= 1
            #adding sum to the final result
            result.append(str(carry % 2))
            carry //= 2
        
        #reversing the final answer
        return ''.join(reversed(result))
    
if __name__ == '__main__':
    s = Solution()
    print(s.addBinary(a="11", b="1"))

#Time Complexity - O(n)
#Space Complexity - O(1)

            