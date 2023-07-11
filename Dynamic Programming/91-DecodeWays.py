class Solution:
    def numDecodings(self, s: str) -> int:

        if s[0] == '0':
            return 0
        
        #create a dp list to store the number of decodings at each index
        dp = [0 for _ in range(len(s)+1)]

        #base cases
        dp[0] = 1
        dp[1] = 1

        #iterate from the second character up to the end of the string
        for i in range(2, len(dp)):
            #check if the current character can be decoded individually (not '0')
            if s[i-1] != '0':
                dp[i] += dp[i-1]
            #check if the current character, along with the previous character, can be decoded as a two-digit number
            if int(s[i-2:i]) >= 10 and int(s[i-2:i]) <= 26:
                dp[i] += dp[i-2] 
        
        #return last element of dp
        return dp[-1]
    
if __name__ == '__main__':
    s = Solution()
    print(s.numDecodings('226'))
    print(s.numDecodings('10'))

#Time Complexity - O(n)
#SpaceComplexity - O(n)