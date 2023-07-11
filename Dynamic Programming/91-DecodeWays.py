class Solution:
    def numDecodings(self, s: str) -> int:

        if s[0] == '0':
            return 0
        
        dp = [0 for _ in range(len(s)+1)]

        dp[0] = 1
        dp[1] = 1

        for i in range(2, len(dp)):
            if s[i-1] != '0':
                dp[i] += dp[i-1]
            if int(s[i-2:i]) >= 10 and int(s[i-2:i]) <= 26:
                dp[i] += dp[i-2] 
        
        return dp[-1]
    
if __name__ == '__main__':
    s = Solution()
    print(s.numDecodings('226'))
    print(s.numDecodings('10'))
