import collections
class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:

        #create a dictionary and store count of all letters in p
        p_map = collections.defaultdict(int)
        for char in p:
            p_map[char] += 1
        
        #initialize 'match' to keep track of the number of characters in the window that match to the characters in p 
        match = 0
        result = []

        #traverse through the string s
        for i in range(len(s)):

            #check if s[i] is in the p_map
            if s[i] in p_map:

                #if yes, decrement the count of that character in the p_map
                p_map[s[i]] -= 1

                #if p_map[s[i]] becomes 0, it means we have found a match, increment match
                if p_map[s[i]] == 0:
                    match += 1
            
            #if the window size exceeds length of p, shrink the window from the left side
            if i >= len(p):
                
                #if the character at the start of window is present in p_map, increment the counter as we are moving the start one step towards right
                if s[i-len(p)] in p_map:
                    p_map[s[i-len(p)]] += 1

                    #if it was a match before shrinking, decrement the match to reflect the change
                    if p_map[s[i-len(p)]] == 1:
                        match -= 1
            
            #if number of match is equal to len(p), we have found an anagram
            if match == len(p_map):

                #add the starting index of the window to result
                result.append(i-len(p)+1)
        return result
    
if __name__ == '__main__':
    s = Solution()
    print(s.findAnagrams(s = "cbaebabacd", p = "abc"))

#Time Complexity - O(n)
#Space Complexity - O(len(p))