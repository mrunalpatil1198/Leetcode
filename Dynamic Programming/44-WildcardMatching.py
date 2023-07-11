class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if p == '*' or s == p:
            return True
        
        #Create a dynamic programming table with dimensions (len(s) + 1) x (len(p) + 1)
        #dp[i][j] represents whether s[:i] matches p[:j]
        dp = [[False for _ in range(len(p)+1)] for _ in range(len(s)+1)]

        #Empty pattern matches empty string
        dp[0][0] = True
        
        #Check if the '*' character can match an empty string
        #dp[0][j] is True if p[:j] consists of '*' characters only
        for j in range(1, len(p)+1):
            if p[j-1] == '*':
                dp[0][j] = dp[0][j-1]

        #Iterate over each character in the string s and p
        for i in range(1, len(s)+1):
            for j in range(1, len(p)+1):
                #If the current characters match or p[j-1] is '?', check if s[:i-1] matches p[:j-1]
                if p[j-1] == '?' or p[j-1] == s[i-1]:
                    dp[i][j] = dp[i-1][j-1]
                #If the current character is '*', there are two possibilities:
                #'*' matches an empty string: dp[i][j-1]
                #'*' matches one or more characters in s: dp[i-1][j]
                elif p[j-1] == '*':
                    dp[i][j] = dp[i-1][j] or dp[i][j-1]

        #bottom-right cell of the table contains the answer
        return dp[-1][-1] 

if __name__ == '__main__':
    s = Solution()
    print(s.isMatch(s = "aa", p = "a"))


