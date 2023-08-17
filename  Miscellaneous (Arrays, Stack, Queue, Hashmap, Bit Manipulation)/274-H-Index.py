class Solution:
    def hIndex(self, citations: list[int]) -> int:
        if len(citations) == 1:
            return min(len(citations), citations[0])
        
        #sorting in decreasing order
        citations.sort(key= lambda x: (-x))

        for i in range(len(citations)):
            #h-index is the first index where the citations[i] is less than or equal to i
            if citations[i] <= i:
                return i
        
        return len(citations)
    
if __name__ == '__main__':
    s = Solution()
    print(s.hIndex(citations = [3,0,6,1,5]))

#Time Complexity - O(nlogn)
#Space Complexity - O(1)
