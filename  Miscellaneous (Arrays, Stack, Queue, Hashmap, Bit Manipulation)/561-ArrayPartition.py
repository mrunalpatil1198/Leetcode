class Solution:
    def arrayPairSum(self, nums: list[int]) -> int:
        nums.sort()
        result = 0
        for i in range(0, len(nums), 2):
            result += nums[i]
        return result

if __name__ == '__main__':
    s = Solution()
    print(s.arrayPairSum(nums = [1,4,3,2]))

#Time Complexity - O(nlogn)
#Space Complexity - O(1)