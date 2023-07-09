class Solution:
    def isPalindrome(self, s: str) -> bool:

        #start comparing from first and last position
        s = s.lower()
        i = 0
        j = len(s)-1

        while i <= j:
            #if not alphanumeric, go to next element
            if not s[i].isalnum():
                i += 1
                continue
            #if not alphanumeric, go to next element
            if not s[j].isalnum():
                j -= 1
                continue
            #check if equal
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True

if __name__ == '__main__':
    s = Solution()
    print(s.isPalindrome("A man, a plan, a canal: Panama"))


#Time Complexity - O(n)
#Space Complexity - O(1)

