class Solution:
    def findMaxLength(self, nums: list[int]) -> int:
        diff = result = 0
        count = {0: -1}

        for i in range(len(nums)):
            diff += 1 if nums[i] == 1 else -1
            if diff in count:
                result = max(result, i - count[diff])
            else:
                count[diff] = i
        
        return result

if __name__ == '__main__':
    s = Solution()
    print(s.findMaxLength(nums = [0,1]))

#Time Complexity - O(n)
#Space Complexity - O(n)
