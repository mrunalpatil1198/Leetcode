class Solution:
    def addOperators(self, num: str, target: int) -> list[str]:
        result = []

        def dfs(index, prev, total, path):
            if index == len(num):
                if total == target:
                    result.append(''.join(path))
                return
            
            for i in range(index, len(num)):
                if i > index and num[index] == '0':
                    return
                s = num[index : i+1]
                operand = int(s)

                if index == 0:
                    path.append(str(operand))
                    dfs(i+1, operand, operand, path)
                    path.pop()
                else:
                    for op in ['+', '-', '*']:
                        path.append(op + s)

                        if op == '+':
                            dfs(i+1, operand, total + operand, path)
                        elif op == '-':
                            dfs(i+1, -operand, total - operand, path)
                        else:
                            dfs(i+1, prev*operand, total - prev + prev * operand, path)
                        
                        path.pop()
        
        dfs(0, 0, 0, [])
        return result

      

if __name__ == '__main__':
    s = Solution()
    print(s.addOperators(num = "123", target = 6))