class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        i = 0
        j = len(s) - 1

        #set containing all vowels
        vowels = set({'a', 'e', 'i', 'o', 'u'})

        while i <= j:
            #move i forward till a vowel is found
            while i <= j and s[i].lower() not in vowels:
                i += 1
            #move j backwards till a vowel is found
            while i <= j and s[j].lower() not in vowels:
                j -= 1
            #swap ith and jth element
            if i <= j:
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1

        return ''.join(s)
    
if __name__ == '__main__':
    s = Solution()
    print(s.reverseVowels("hello"))

#Time Complexity - O(n)
#Space Complexity - O(1)