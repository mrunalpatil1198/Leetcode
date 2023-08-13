class Solution:
    def addOperators(self, num: str, target: int) -> list[str]:
        result = []

        #index: curr index in num
        #prev: previous operand, needed in case of multiplication
        #total: evaluation of path till curr point
        #path: string of curr path
        def dfs(index, prev, total, path):
            if index == len(num):
                if total == target:
                    result.append(''.join(path))
                return
            
            for i in range(index, len(num)):
                #number cannot start with 0
                if i > index and num[index] == '0':
                    return
                
                #getting the curr operand
                s = num[index : i+1]
                operand = int(s)

                if index == 0:
                    #appending to path and going to next number
                    path.append(str(operand))
                    dfs(i+1, operand, operand, path)
                    path.pop()
                else:
                    #backtracking by appending each of the operator and curr number
                    for op in ['+', '-', '*']:
                        path.append(op + s)

                        if op == '+':
                            #adding to curr total
                            dfs(i+1, operand, total + operand, path)
                        elif op == '-':
                            #subtracting from curr total
                            dfs(i+1, -operand, total - operand, path)
                        else:
                            #multplying with previous number and adding it back to the curr total
                            dfs(i+1, prev*operand, total - prev + prev * operand, path)
                        
                        path.pop()
        
        dfs(0, 0, 0, [])
        return result

      

if __name__ == '__main__':
    s = Solution()
    print(s.addOperators(num = "123", target = 6))

#Time Complexity - O(3^n)
#Space Complexity - O(N)