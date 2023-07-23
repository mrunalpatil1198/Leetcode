class Solution:

    def generateParenthesis(self, n: int) -> list[str]:
        result = []

        #we need to keep track of both - number of open and close brackets while backtracking
        def backtracking(open, close, elements):
            #base case - if we do not have anymore brackets, add the current expression to result
            if open == 0 and close == 0:
                result.append(''.join(elements))
                return
            
            #if we have open brackets left, append them first
            if open > 0:

                #add '(' to the current exp
                elements.append('(')

                #recurse for rest of the brackets
                backtracking(open-1, close, elements)
                
                #backtrack by removing the last bracket, so we can try another combination of brackets
                elements.pop()

            #append ')' only when we have more open brackets already in the expression which forms a pair
            if close > open:

                #add ')' to the current exp
                elements.append(')')
                
                #recurse for rest of the brackets
                backtracking(open, close-1, elements)
                
                #backtrack by removing the last bracket, so we can try another combination of brackets
                elements.pop()
        
        #start with 'n' number of open and close brackets
        backtracking(n, n, [])

        #return the result list
        return result

if __name__ == '__main__':
    s = Solution()
    print(s.generateParenthesis(3))

#Time Complexity - Exponential