class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        result = []

        #elements: list to store the current combination being formed
        #index: the current index in the range of 1 to 'n' to consider adding elements from
        def backtracking(elements, index):

            #base case: If the combination size reaches 'k', add the current combination to the result list and return
            if len(elements) == k:
                result.append(list(elements))
                return
            
            #base case: If the combination size exceeds 'k', return from the current recursive call
            if len(elements) > k:
                return
            
            #try each element from the current index onwards
            for i in range(index, n+1):

                #add the current element to the combination
                elements.append(i)

                #recurse from next index
                backtracking(elements, i+1)

                #backtrack by removing the last added element
                elements.pop()
        
        #start the backtracking process with an empty combination and index as 1
        backtracking([], 1)
        return result

if __name__ == '__main__':
    s = Solution()
    print(s.combine(n = 4, k = 2))

#Time Complexity = Exponential
