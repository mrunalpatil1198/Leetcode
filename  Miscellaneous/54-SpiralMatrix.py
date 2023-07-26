# Given an m x n matrix, return all elements of the matrix in spiral order.
#1 2 3
#4 5 6
#7 8 9        123698745

class Solution:

    def spiralTraversal(self, grid):
        top = 0
        bottom = len(grid)
        left = 0
        right = len(grid[0])
        result = []

        while top < bottom and left < right:

            #going from left to right column wise
            for i in range(left, right):
                result.append(grid[top][i])
            top += 1

            #going from top to bottom row wise
            for i in range(top, bottom):
                result.append(grid[i][right-1])
            right -= 1

            #checking if condition so that we do not parse same row again
            if top < bottom:
                #going from right to left col wise
                for i in range(right-1, left-1, -1):
                    result.append(grid[bottom-1][i])
                bottom -= 1
            
            #checking if condition so that we do not parse same col again
            if left < right:

                #going from bottom to top row wise
                for i in range(bottom-1, top-1, -1):
                    result.append(grid[i][left])
                left += 1
        return result
    
if __name__ == '__main__':
    s = Solution()
    print(s.spiralTraversal([[1,2,3], [4,5,6], [7,8,9]]))

#Time Complexity - O(n*m)
#Space Complexity - O(1)