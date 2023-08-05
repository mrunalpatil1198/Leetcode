import heapq
class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:

        #creating a minimum heap
        minheap = []
        for num in nums:
            #inserting num into the heap
            heapq.heappush(minheap, num)
            if len(minheap) > k:
                #removing the smallest element from heap if the heap size exceeds k
                heapq.heappop(minheap)

        #returning smallest element from the heap
        return minheap[0]
    
if __name__ == '__main__':
    s = Solution()
    print(s.findKthLargest(nums = [3,2,3,1,2,4,5,5,6], k = 4))

#Time Complexity - O(nlogk)
#Space Complexity - O(k)
