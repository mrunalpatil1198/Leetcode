"""
Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
IV 4
IX 9
XL 40
XC 90
CD 400
CM 900

s = "LVIII"
Output: 58
s = "MCMXCIV"
Output: 1994
"""

class Solution:
    def romanToInt(self, s):

        #create a dict for storing the mapping of fixed roman to integers
        conversions = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C':100, 'D':500, 'M':1000,
        'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}
        result = 0
        i = 0

        #traverse s using i as pointer
        while i < len(s):

            #first check if the char at curr and curr+1 form a valid roman we have in our dict
            if i+2 <= len(s) and s[i:i+2] in conversions:

                #if yes, simply add the it's integer mapping to the result and increment i by 2 
                result += conversions[s[i:i+2]]
                i += 2
            else:

                #read just the curr char and add its mapping to the result and increment i by 1
                result += conversions[s[i]]
                i += 1
        return result
    
if __name__ == '__main__':
    s = Solution()
    print(s.romanToInt("III"))

#Time Complexity - O(n)
#Space Complexity - O(1)