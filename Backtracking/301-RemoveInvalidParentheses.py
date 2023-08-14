class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:

        #calculating the number of extra left and right paranthesis
        left = right = 0
        for char in s:
            if char == '(':
                left += 1
            elif char == ')':
                right = right+1 if left == 0 else right
                left = left-1 if left > 0 else left

        result = set()

        def backtracking(index, left_count, right_count, remaining_left_remove, remaining_right_remove, exp):
            if index == len(s):
                if remaining_left_remove == 0 and remaining_right_remove == 0:
                    result.add(''.join(exp))
                return
            
            #removing '(' or ')' if we have enough removals left
            if (s[index] == '(' and remaining_left_remove > 0) or (s[index] == ')' and remaining_right_remove > 0):
                backtracking(index+1, left_count, right_count, remaining_left_remove-(s[index]== '('), remaining_right_remove-(s[index]==')'), exp)

            #adding s[index] to curr expression
            exp.append(s[index])

            if s[index] != '(' and s[index] != ')':
                #recursively calling backtracking for next index
                backtracking(index+1, left_count, right_count, remaining_left_remove, remaining_right_remove, exp)

            elif s[index] == '(':
                #adding 1 to left count so far in exp and recursively calling backtracking for next index
                backtracking(index+1, left_count+1, right_count, remaining_left_remove, remaining_right_remove, exp)
            
            elif s[index] == ')' and left_count > right_count:
                #adding 1 to right count so far in exp and recursively calling backtracking for next index
                backtracking(index+1, left_count, right_count+1, remaining_left_remove, remaining_right_remove, exp)

            #backtracking
            exp.pop()
        
        backtracking(0, 0, 0, left, right, [])
        
        return result

if __name__ == '__main__':
    s = Solution()
    print(s.removeInvalidParentheses(s = "()())()"))

#Time Complexity - O(2^n)
#Space Complexity - O(1) - not considering recursion stack space