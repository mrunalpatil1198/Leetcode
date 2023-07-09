class Solution:
    def reverseWords(self, s: str) -> str:
        #create list containg all words present in s
        s = s.split()

        #initialize i to 0 and j to n-1
        i = 0
        j = len(s) - 1

        #swap first word with last word and so on
        while i <= j:
            #swap ith word with jth word
            s[i], s[j] = s[j], s[i]
            #move i forward
            i += 1
            #move j backward
            j -= 1

        return " ".join(s)
    
if __name__ == '__main__':
    s = Solution()
    print(s.reverseWords("the sky is blue"))

#Time Complexity - O(n)
#Space Complexity - O(1)