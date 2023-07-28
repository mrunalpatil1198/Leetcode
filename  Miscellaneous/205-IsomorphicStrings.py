import collections
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_map = collections.defaultdict(lambda: -1)
        t_map = collections.defaultdict(lambda: -1)

        for i in range(len(s)):
            #checking the previous occurence index of char at curr index in both the strings
            if s_map[s[i]] != t_map[t[i]]:
                return False
            s_map[s[i]] = t_map[t[i]] = i
        
        return True
    
if __name__ == '__main__':
    s = Solution()
    print(s.isIsomorphic(s = "egg", t = "add"))

#Time Complexity - O(n)
#Space Complexity - O(n)