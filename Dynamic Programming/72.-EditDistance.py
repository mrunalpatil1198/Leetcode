class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if word1 == word2:
            return 0
        
        if len(word1) == 0 or len(word2) == 0:
            return max(len(word1), len(word2))

        #dp[i][j] would represent the minimum number of operations required to transform the substring word1[0...i-1] into the substring word2[0...j-1]
        dp = [[0 for _ in range(len(word2) + 1)] for _ in range(len(word1) + 1)]

        #transforming word1[0...i-1] into an empty string requires i deletions
        for i in range(len(word1)+1):
            dp[i][0] = i
        
        #transforming an empty string into word2[0...j-1] requires j insertions
        for i in range(len(word2)+1):
            dp[0][i] = i

        for i in range(1, len(word1)+1):
            for j in range(1, len(word2)+1):
                if word1[i-1] == word2[j-1]:
                    #no operation is required because the characters at positions i-1 and j-1 are already the same
                    dp[i][j] = dp[i-1][j-1]
                else:
                    #dp[i-1][j-1] + 1: replacing the character at position i-1 in word1 with the character at position j-1 in word2
                    #dp[i-1][j] + 1: deleting the character at position i-1 in word1
                    #dp[i][j-1] + 1: inserting the character at position j-1 in word2 into word1 at position i
                    dp[i][j] = min(dp[i-1][j], dp[i-1][j-1], dp[i][j-1]) + 1

        return dp[-1][-1]
    
if __name__ == '__main__':
    s = Solution()
    print(s.minDistance(word1 = "horse", word2 = "ros"))

#Time Complexity - O(m*n)
#Space Complexity - O(m*n)