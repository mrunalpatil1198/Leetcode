class Solution:
    def thirdMax(self, nums: list[int]) -> int:
        distincts = set(nums)
        if len(distincts) < 3:
            return max(distincts)
        else: 
            return sorted(list(distincts))[-3]
        
if __name__ == '__main__':
    s = Solution()
    print(s.thirdMax([3,2,1]))