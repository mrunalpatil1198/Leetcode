class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        operators = {'+', '-', '/', '*'}

        for token in tokens:
            #adding to stack directly if token is an operand
            if token not in operators:
                stack.append(token)
            else:
                #getting top two operands from stack and evaluating the result with current token operator and pushing it back to stack
                operand2 = int(stack.pop())
                operand1 = int(stack.pop())
                if token == '+':
                    stack.append(operand1+operand2)
                elif token == '-':
                    stack.append(operand1-operand2)
                elif token == '*':
                    stack.append(operand1*operand2)
                elif token == '/':
                    stack.append(operand1/operand2)
        return int(stack[0])
    
if __name__ == '__main__':
    s = Solution()
    print(s.evalRPN(tokens = ["2","1","+","3","*"]))

#Time Complexity - O(n)
#Space Complexity - O(n)