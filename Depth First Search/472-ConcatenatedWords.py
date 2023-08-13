class Solution:
    def findAllConcatenatedWordsInADict(self, words: list[str]) -> list[str]:
        wordset = set(words)

        #dp[word] would represent if word can be formed using wordset
        dp = {}

        def dfs(word):
            if word in dp:
                return dp[word]
            
            for i in range(1, len(word)):

                #breaking the word at ith index
                prefix = word[:i]
                suffix = word[i:]

                #checking if both prefix and suffix can be formed using given words
                if ((prefix in wordset and suffix in wordset) or (prefix in wordset and dfs(suffix))):
                    dp[word] = True
                    return dp[word]
                
            dp[word] = False
            return dp[word]
        
        result = []
        for word in words:
            if dfs(word):
                result.append(word)

        return result
    
if __name__ == '__main__':
    s = Solution()
    print(s.findAllConcatenatedWordsInADict(words = ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]))

#Time Complexity - O(n*m^2)
#Space Complexity - O(n*m)