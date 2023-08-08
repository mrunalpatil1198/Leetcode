from collections import deque
class Solution:

    def wordBreak(self, s: str, wordDict: list[str]) -> bool:

        q = deque()
        q.append(0)
        visited = set()
        words = set(wordDict)

        #bfs
        while q:
            #getting the starting index of remaining string
            start = q.popleft()
            #we do not need to visit start again as if an answer existed from this point, we would have only got it
            if start not in visited:
                #trying all possible indices for end
                for end in range(start+1, len(s)+1):
                    #if the substring exists in word set, we can choose this word
                    if s[start : end] in words:
                        #checking if we have reached the end of string
                        if end == len(s):
                            return True

                        #appending the curr end as next start into the queue
                        q.append(end)
                #updating visited
                visited.add(start)
        
        return False
    
if __name__ == '__main__':
    s = Solution()
    print(s.wordBreak("leetcode", ["leet","code"]))

#Time Complexity - O(n^3+m*k) where n = length of s, m = length of word dict, k = avg length of word in word dict
#Space Complexity - O(n+m*k)


