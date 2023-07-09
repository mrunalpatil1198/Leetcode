class Solution:
    def reverseString(self, s: list[str]):
        i = 0
        j = len(s)-1
        #swap first word with last word and so on
        while i <= j:
            s[i], s[j] = s[j],s[i]
            j -= 1
            i += 1
        return s

if __name__ == '__main__':
    s = Solution()
    print(s.reverseString(["h","e","l","l","o"]))
    
#Time Complexity - O(n)
#Space Complexity - O(1)