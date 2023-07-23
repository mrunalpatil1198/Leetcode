class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        result = []

        #index: the current index of candidates list to start considering elements from
        #elements: list to store the current combination being formed
        #remainder: the remaining target value that we need to achieve
        def backtracking(index, elements, remainder):

            #if remainder becomes 0 (target reached) - add the current combination to the result list and return
            if remainder == 0:
                result.append(list(elements))
                return
            
            #if the current index goes beyond the length of candidates list or the remainder becomes negative (target exceeded), backtrack and return from this recursive call
            if index >= len(candidates) or remainder < 0:
                return
            
            #try each candidate from the current index onwards and recurse to find the combinations
            for i in range(index, len(candidates)):

                #add the current element to the combination
                elements.append(candidates[i])

                #recur with the same index, as the current candidate can be chosen again but reduce the remainder by the value of the current candidate
                backtracking(i, elements, remainder-candidates[i])

                #backtrack by removing the last added candidate so we can try other combinations with different candidates
                elements.pop()
        
        #start the backtracking process from index 0 with an empty combination and the target value
        backtracking(0, [], target)

        #return the result list
        return result

if __name__ == '__main__':
    s = Solution()
    print(s.combinationSum(candidates = [2,3,6,7], target = 7))

#Time Complexity - Exponential