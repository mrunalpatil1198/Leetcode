class Solution:
    def nthUglyNumber(self, n: int) -> int:

        #starting with 1 as 1st ugly number
        ugly = [1]
        p2 = p3 = p5 = 0

        while len(ugly) < n:
            #finding out the next smallest number that can be formed using 2, 3 or 5
            next_ugly = min(ugly[p2]*2, ugly[p3]*3, ugly[p5]*5)
            ugly.append(next_ugly)

            ##increasing pointer for which the number matches
            if next_ugly == ugly[p2]*2:
                p2 += 1
            if next_ugly == ugly[p3]*3:
                p3 += 1
            if next_ugly == ugly[p5]*5:
                p5 += 1
        
        return ugly[-1]
    
if __name__ == '__main__':
    s = Solution()
    print(s.nthUglyNumber(10))

#Time Complexity - O(n)
#Space Complexity - O(n)