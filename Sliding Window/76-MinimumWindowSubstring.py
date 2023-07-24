import collections
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": return ""

        #create a dict to store count of all characters in t
        t_map = collections.defaultdict(int)

        #create a dict to store count of all characters in s
        s_map = collections.defaultdict(int)

        #fill values in t_map
        for char in t:
            t_map[char] += 1

        #pointer to the start of window
        left = 0

        #stores starting and ending index of window containing the string
        result = [-1, -1]

        #keeps track of min length so far
        min_len = float('inf')

        #keeps track of matches(number of chars in window that have same count in t) found so far
        match = 0

        #traverse s using right pointer
        for right in range(len(s)):

            #update the count of curr char in s_map
            s_map[s[right]] += 1

            #if the count of curr char is same in s_map and t_map, we have found a match
            if s[right] in t_map and s_map[s[right]] == t_map[s[right]]:
                match += 1

            #shrink the window size in order to get the min length of window till we have all the char matches
            while match == len(t_map):

                #update min_len and result according to curr window size
                if right - left + 1 < min_len:
                    min_len = right-left+1
                    result[0], result[1] = left, right

                #as we are shrink by moving left pointer to right, we need to decrement the count of s[left]
                s_map[s[left]] -= 1

                #if we are moving past a character who was member of the characters matching, we need to update the match by decrementing it
                if s[left] in t_map and s_map[s[left]] < t_map[s[left]]:
                    match -= 1
                
                #move left pointer towards right
                left += 1

        return s[result[0] : result[1]+1] if min_len != float('inf') else ""

if __name__ == '__main__':
    s = Solution()
    print(s.minWindow(s = "ADOBECODEBANC", t = "ABC"))

#Time Complexity - O(n)
#Space Complexity - O(n)