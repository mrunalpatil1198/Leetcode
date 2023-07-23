class Solution:

    #same like leetcode problem 78 - Subsets except use a set to avoid storing duplicate subsets becasue of the duplicate elements 
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        result = set()

        def backtracking(subset, index):
            result.add(tuple(sorted(subset)))
            if index >= len(nums):
                return
            for i in range(index, len(nums)):
                subset.append(nums[i])
                backtracking(subset, i+1)
                subset.pop()
        

        backtracking([], 0)
        return list(result)
    
if __name__ == '__main__':
    s = Solution()
    print(s.subsetsWithDup([1,2,2]))

#Time Complexity - Exponential - O(2^n)