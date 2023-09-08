class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        counter = 0
        result = 0
        for num in nums:
            if num == 1:
                counter += 1
                result = max(counter, result)
            else:
                counter = 0
        return result

if __name__ == '__main__':
    s = Solution()
    print(s.findMaxConsecutiveOnes(nums = [1,1,0,1,1,1]))