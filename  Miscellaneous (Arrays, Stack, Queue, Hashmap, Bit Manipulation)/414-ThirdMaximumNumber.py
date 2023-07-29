class Solution:
    def thirdMax(self, nums: list[int]) -> int:

        #create set of nums to avoid duplicates
        distincts = set(nums)

        if len(distincts) < 3:
            return max(distincts)
        else: 
            #sort and return the third last element
            return sorted(list(distincts))[-3]
        
if __name__ == '__main__':
    s = Solution()
    print(s.thirdMax([3,2,1]))

#Time Complexity - O(nlogn)
#Space Complexity - O(n)