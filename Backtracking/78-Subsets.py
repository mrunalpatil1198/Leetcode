class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        result = []

        #subset: list to store the current subset being formed
        #index: the current index in the 'nums'
        def backtracking(subset, index):

            #add the current subset to the result list
            result.append(list(subset))

            #base case: If the current index goes beyond the length of the 'nums' list, return
            if index >= len(nums):
                return
            
            #try each element from the current index onwards
            for i in range(index, len(nums)):

                #add the current element to the subset
                subset.append(nums[i])

                #recur with the next index to explore other possible subsets
                backtracking(subset, i+1)

                #backtrack by removing the last added element so we can try other subsets with different elements
                subset.pop()
        
        #start the backtracking process with an empty subset and index 0
        backtracking([], 0)
        return result

if __name__ == '__main__':
    s = Solution()
    print(s.subsets([1, 2, 3]))

#Time Complexity - Exponential - O(2^n)
