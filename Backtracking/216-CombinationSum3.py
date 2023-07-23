class Solution:
    def combinationSum3(self, k: int, n: int) -> list[list[int]]:
        result = []

        #index: the current index
        #elements: list to store the current combination being formed
        #remainder: the remaining sum that needs to be achieved
        def backtracking(index, elements, remainder):

            #base case: If the combination size reaches 'k' and the sum is equal to 'n', add the current combination to the result list
            if len(elements) == k and remainder == 0:
                result.append(list(elements))
                return
            
            #base case: If the combination size exceeds 'k' or the remaining sum becomes negative, backtrack and return from the current recursive call
            if len(elements) > k or remainder < 0:
                return
            
            #try each number from the current index (ranging from 1 to 9)
            for i in range(index, 10):

                #add the current number to the combination
                elements.append(i)

                #recur with the next index and update the remaining sum
                backtracking(i+1, elements, remainder-i)

                #backtrack by removing the last added number so we can try other combinations with different numbers
                elements.pop()

        #start the backtracking process with an empty combination and index 1
        backtracking(1, [], n)
        return result
    
if __name__ == '__main__':
    s = Solution()
    print(s.combinationSum3(k = 3, n = 7))

#Time Complexity = Exponential