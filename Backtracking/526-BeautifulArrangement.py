class Solution:
    def countArrangement(self, n: int) -> int:
        nums = [i for i in range(1, n+1)]
        result = 0

        def backtracking(index):
            if index == len(nums):
                nonlocal result
                result += 1
                return
                        
            for i in range(index, len(nums)):
                if nums[i] % (index+1) == 0 or (index+1) % nums[i] == 0:
                    nums[i], nums[index] = nums[index], nums[i]
                    backtracking(index+1)
                    nums[i], nums[index] = nums[index], nums[i]

        backtracking(0)
        return result

if __name__ == '__main__':
    s = Solution()
    print(s.countArrangement(n = 2))