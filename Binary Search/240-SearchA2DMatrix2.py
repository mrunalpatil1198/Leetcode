class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:

        #starting from last col of first row
        i = 0
        j = len(matrix[0]) - 1

        #binary search
        while i < len(matrix) and j >= 0:
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] > target:
                #moving to left side
                j -= 1
            else:
                #moving downwards
                i += 1
        
        return False

if __name__ == '__main__':
    s = Solution()
    print(s.searchMatrix([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 5))

#Time Complexity - O(logn)
#Space Complexity - O(1)