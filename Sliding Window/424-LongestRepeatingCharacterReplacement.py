import collections
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        #create a dict to store count of all characters in the window
        count = collections.defaultdict(int)
        result = 0

        #pointer to start of window
        left = 0

        #stores the max count or frequency in the window
        freq = 0

        #traverse s using right pointer
        for right in range(len(s)):

            #update the count of s[right] in dict
            count[s[right]] += 1

            #update the max frequency
            freq = max(freq, count[s[right]])

            #Note - number of characters to be replaced = window_size - max_freq as we need to replace all the characters that are not equal to the char with max freq
            #shrink the window size by moving left to right until we have only k different characters
            while  (right-left+1) - freq > k:
                count[s[left]] -= 1
                left += 1
            
            #update the result to store the max window size so far
            result = max(result, right-left+1)
        return result

if __name__ == '__main__':
    s = Solution()
    print(s.characterReplacement(s = "ABAB", k = 2))

#Time Complexity - O(n)
#Space Complexity - O(n)
