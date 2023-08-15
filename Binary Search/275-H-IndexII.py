class Solution:
    def hIndex(self, citations: list[int]) -> int:

        left = 0
        right = len(citations)

        #binary search
        while left <= right:
            mid = left + (right-left) //2
            if citations[mid] == len(citations) - mid:
                return len(citations) - mid
            elif citations[mid] < len(citations) - mid:
                left = mid + 1
            else:
                right = mid - 1
        
        return len(citations) - left

if __name__ == '__main__':
    s = Solution()
    print(s.hIndex(citations = [0,1,3,5,6]))

#Time Complexity - O(logn)
#Space Complexity - O(1)