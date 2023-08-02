class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:

        #considering the 2D-matrix as 1D space, setting lower and higher limit as 0 and the total number of cells respectively
        left = 0
        right = len(matrix) * len(matrix[0]) - 1

        #binary search
        while left < right:
            mid = left + (right - left) // 2

            #diving mid by number of columns for row index and taking mod for col index
            if matrix[mid // len(matrix[0])][mid % len(matrix[0])] == target:
                return True
            
            if matrix[mid // len(matrix[0])][mid % len(matrix[0])] < target:
                #setting lower limit as mid+1 as the target lies in right half
                left = mid + 1
            else:
                #setting higher limit as mid-1 as the target lies in left half
                right = mid - 1

        return False
    
if __name__ == '__main__':
    s = Solution()
    print(s.searchMatrix(matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3))

#Time Complexity - O(logn)
#Space Complexity - O(1)