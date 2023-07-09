class Solution:
    def maxArea(self, height: list[int]) -> int:
        
        #Initialize i to 0 and j to last element
        i = 0
        j = len(height) - 1
        #to keep track of max area every time
        result = 0

        while i < j:
            #calculate area covered between ith and jth element 
            #area would be the product of the horizontal distance (j-i) between the two poles and the vertical distance which is min of the height of ith and jth pole
            result = max(result, min(height[i], height[j]) * (j-i))
            #if height of i is less than that of j, move i forward as we might get another element having greater height than ith element and hence would contain more water with jth element else decrement j
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return result

if __name__ == '__main__':
    s = Solution()
    print(s.maxArea(height = [1,8,6,2,5,4,8,3,7]))

#Time Complexity - O(n)
#Space Complexity - O(1)
