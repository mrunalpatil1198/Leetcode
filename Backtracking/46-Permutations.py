class Solution:

    #at each function call, we swap elements and fix one element at a time and explore all combinations from next index.
    def permute(self, nums: list[int]) -> list[list[int]]:
        result = []

        # index: the current index to consider swapping elements with
        def backtracking(index):

            #base case: If we have reached the end of the list, add the current permutation to the result list and return
            if index == len(nums):
                result.append(list(nums))
                return
            
            #base case: If the current index goes beyond the length of the list, return
            if index > len(nums):
                return
            
            #try each element from the current index onwards and swap it with the current index
            for i in range(index, len(nums)):

                #swap the elements at the current index and index i
                nums[index], nums[i] = nums[i], nums[index]

                #recurse from index+1
                backtracking(index+1)

                #backtrack by swapping the elements back to their original positions
                nums[index], nums[i] = nums[i], nums[index]
        
        #start the backtracking process from index 0
        backtracking(0)
        return result
    
if __name__ == '__main__':
    s = Solution()
    print(s.permute([1,2,3]))
            
#Time Complexity - Exponential