class Solution:

    #same like leetcode problem 46 - Permutations expect maintain a set (instead of a list) to store the result to avoid storing duplicate permutations becasue of the duplicate elements 
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        result = set()

        def backtracking(index):
            if index == len(nums):
                result.add(tuple(nums))
                return
            for i in range(index, len(nums)):
                nums[index], nums[i] = nums[i], nums[index]
                backtracking(index+1)
                nums[index], nums[i] = nums[i], nums[index]
        
        backtracking(0)
        return list(result)
    
if __name__ == '__main__':
    s = Solution()
    print(s.permuteUnique([1,1,2]))

#Time Complexity - Exponential