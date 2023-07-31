class Solution:
    def hammingWeight(self, n: int) -> int:
        result = 0
        while n > 0:
            #checking if the least significant bit is set
            if n & 1 == 1:
                result += 1
            
            #right shifting the number by 1
            n = n >> 1
        return result
    
if __name__ == '__main__':
    s = Solution()
    print(s.hammingWeight(n = 00000000000000000000000000001011))

#Time Complexity - O(n)
#Space Complexity - O(1)