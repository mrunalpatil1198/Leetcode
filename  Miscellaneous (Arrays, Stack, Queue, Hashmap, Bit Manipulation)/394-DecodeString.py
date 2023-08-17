class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        curr = ''
        num = 0

        for c in s:
            if c.isdigit():
                #appending to current num
                num = (num * 10) + int(c)
            elif c == '[':
                #pushing current num and string to stack
                stack.append(num)
                stack.append(curr)
                #resetting num and curr
                num = 0
                curr = ''
            elif c == ']':
                #getting previous string and num and appending current string to it
                prev_s = stack.pop()
                prev_num = stack.pop()
                curr = prev_s + curr * prev_num
            else:
                #appending to curr char
                curr += c
        
        return curr
    
if __name__ == '__main__':
    s = Solution()
    print(s.decodeString(s = "3[a]2[bc]"))

#Time Complexity - O(n)
#Space Complexity - O(n)