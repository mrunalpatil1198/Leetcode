class Solution:
    def trap(self, height: list[int]) -> int:
        #using two pointers left and right on indices 1 and n-1
        left = 0
        right = len(height) - 1

        #initializing leftmax and rightmax to 0
        left_max = 0
        right_max = 0
        result = 0

        while left < right:
            #fill water upto leftmax level for index left if height of left is smaller than right and move left to the right
            if height[left] < height[right]:
                #update leftmax
                if height[left] > left_max:
                    left_max = height[left]
                else:
                    result += (left_max - height[left])
                left += 1
            #fill water upto rightmax level for index right and move right to the left
            else:
                #update rightmax
                if height[right] > right_max:
                    right_max = height[right]
                else:
                    result += (right_max - height[right])
                right -= 1

        return result
    
if __name__ == '__main__':
    s = Solution()
    print(s.trap(height = [0,1,0,2,1,0,1,3,2,1,2,1]))


#Time Complexity - O(n)
#Space Complexity - O(1)