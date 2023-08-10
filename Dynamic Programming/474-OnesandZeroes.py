from collections import defaultdict
class Solution:
    def findMaxForm(self, strs: list[str], m: int, n: int) -> int:

        #dp[(i,j)] would represent the length of largest subset that can be formed with i zeroes and j ones
        dp = defaultdict(int)

        for s in strs:
            #counting number of ones and zeroes in curr string
            zeroes = s.count('0')
            ones = s.count('1')

            #traversing all the records with zeroes between m and zeroes and ones between n and ones
            for i in range(m, zeroes-1, -1):
                for j in range(n, ones-1, -1):
                    #updating dp
                    dp[(i,j)] = max(dp[(i,j)], dp[(i-zeroes, j-ones)]+1)

        return dp[(m, n)]

if __name__ == '__main__':
    s = Solution()
    print(s.findMaxForm(strs = ["10","0001","111001","1","0"], m = 5, n = 3))

#Time Complexity - O(l*m*n)
#Space Complexity - O(m*n)
