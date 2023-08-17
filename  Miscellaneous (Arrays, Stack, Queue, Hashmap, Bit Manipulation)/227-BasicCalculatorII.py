class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        curr = 0
        op = '+'

        #appending '+' at the end of s
        for c in s + '+':
            if c == ' ':
                continue
            if c.isdigit():
                #add to existing curr
                curr = (curr*10) + int(c)
            else:
                #adding current operand to the stack according to the current operator
                if op == '+':
                    stack.append(curr)
                elif op == '-':
                    stack.append(-curr)
                elif op == '*':
                    stack.append(stack.pop() * curr)
                elif op == '/':
                    stack.append(int(stack.pop() / curr))
                op = c
                curr = 0
        
        return sum(stack)
    
if __name__ == '__main__':
    s = Solution()
    print(s.calculate(s = "3+2*2"))

#Time Complexity - O(n)
#Space Complexity - O(n)