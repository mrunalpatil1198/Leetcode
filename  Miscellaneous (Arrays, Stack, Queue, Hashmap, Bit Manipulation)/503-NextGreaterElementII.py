class Solution:
    def nextGreaterElements(self, nums: list[int]) -> list[int]:
        stack = []
        result = [-1 for _ in range(len(nums))]

        for i in range(2*len(nums)-2, -1, -1):
            while stack and stack[-1] <= nums[i % len(nums)]:
                stack.pop()
            if i < len(nums):
                result[i] = stack[-1] if stack else -1
            stack.append(nums[i % len(nums)])
        
        return result

if __name__ == '__main__':
    s = Solution()
    print(s.nextGreaterElements(nums = [1,2,1]))

