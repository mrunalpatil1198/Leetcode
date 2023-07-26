import collections
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        
        #create dictionaries of both strings containing count of all chars
        s_map = collections.defaultdict(int)
        t_map = collections.defaultdict(int)

        for i in range(len(s)):
            s_map[s[i]] += 1
            t_map[t[i]] += 1
        return s_map == t_map
    
if __name__ == '__main__':
    s = Solution()
    print(s.isAnagram(s = "anagram", t = "nagaram"))

#Time Complexity - O(n) where n = len(s)
#Space Complexity - O(n) where n = len(s)

