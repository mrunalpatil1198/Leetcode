class Solution:
    def findTheDifference(self, s: str, t: str) -> str:

        #sort both strings
        s = sorted(s)
        t = sorted(t)

        for i in range(len(s)):

            #checking if s[i] == t[i]
            if s[i] != t[i]:
                return t[i]
        
        #if already not found, t[-1] is the answer
        return t[-1]
    
if __name__ == '__main__':
    s = Solution()
    print(s.findTheDifference(s = "abcd", t = "abcde"))

#Time Complexity - O(nlogn) where n = len(t)
#Space Complexity - O(m) where m = len(s)