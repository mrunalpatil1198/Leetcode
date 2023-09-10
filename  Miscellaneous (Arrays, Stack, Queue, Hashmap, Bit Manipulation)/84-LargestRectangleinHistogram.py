class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        stack = []
        area = 0
        heights.append(0)

        for i, height in enumerate(heights):
            start = i
            while stack and stack[-1][1] > height:
                index, ht = stack.pop()
                area = max(area, ht * (i - index))
                start = index
            stack.append([start, height])
        
        return area
    
if __name__ == '__main__':
    s = Solution()
    print(s.largestRectangleArea(heights = [2,1,5,6,2,3]))

#Time Complexity - O(n)
#Space Complexity - O(n)