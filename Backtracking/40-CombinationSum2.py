class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        result = []

        #sort the elements so that we can skip the duplicates while recursing
        candidates.sort()
        
        #index: the current index of candidates list to start considering elements from
        #elements: list to store the current combination being formed
        #remainder: the remaining target value that we need to achieve
        def backtracking(index, elements, remainder):

            #base case: If the target is achieved (remainder becomes 0), add the current combination to the result list and return
            if remainder == 0:
                result.append(list(elements))
                return
            
            #base case: If the current index goes beyond the length of candidates list or the remainder becomes negative (target exceeded), return
            if index >= len(candidates) or remainder < 0:
                return
            
            #try each candidate from the current index onwards
            for i in range(index, len(candidates)):

                #skip duplicates to avoid duplicate combinations
                if i > 0 and i > index and candidates[i] == candidates[i-1]:
                    continue

                #add the current candidate to the combination
                elements.append(candidates[i])

                #recur with the next index and update the remainder
                backtracking(i+1, elements, remainder-candidates[i])

                #backtrack by removing the last added candidate so we can try other combinations with different candidates
                elements.pop()
        
        #start the backtracking process from the beginning (index 0), with an empty combination and the target value
        backtracking(0, [], target)

        return result
    
if __name__ == '__main__':
    s = Solution()
    print(s.combinationSum2(candidates = [10,1,2,7,6,1,5], target = 8))

#Time Complexity - Exponential