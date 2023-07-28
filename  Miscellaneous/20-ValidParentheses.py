class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False

        stack = []
        opening = {'(', '{', '['}
        for c in s:
            #push into stack if any opening bracket is found
            if c in opening:
                stack.append(c)
            else:
                #check if the corresponding open bracket is present at the stack top
                if not stack:
                    return False
                top = stack.pop()
                if (c == ')' and top != '(') or (c == '}' and top != '{') or (c == ']' and top != '['):
                    return False
        
        return len(stack) == 0
    
if __name__ == '__main__':
    s = Solution()
    print(s.isValid("(]"))

#Time Complexity - O(n)
#Space Complexity - O(n)
