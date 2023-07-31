class Solution:
    def findDiagonalOrder(self, mat: list[list[int]]) -> list[int]:
        i = j = 0
        m = len(mat)
        n = len(mat[0])
        direction = True
        result = []
        for _ in range(m*n):
            result.append(mat[i][j])

            #going upwards
            if direction:
                #changing direction
                if j == n-1:
                    i += 1
                    direction = False
                
                #changing direction
                elif i == 0:
                    j += 1
                    direction = False
                else:
                    i -= 1
                    j += 1
            #going downwards
            else:
                #changing direction
                if i == m-1:
                    j += 1
                    direction = True
                #changing direction
                elif j == 0:
                    i += 1
                    direction = True
                else:
                    i += 1
                    j -= 1
        return result
    
if __name__ == '__main__':
    s = Solution()
    print(s.findDiagonalOrder(mat = [[1,2,3],[4,5,6],[7,8,9]]))

#Time Complexity - O(m*n)
#Space Complexity - O(1) - not considering the space needed for result


