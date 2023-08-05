import collections, heapq
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:

        #counting the frequency of all elements in nums
        freq = collections.Counter(nums)

        #creating a min heap
        minheap = []
        for key,v in freq.items():
            #inserting the count and the number into heap
            heapq.heappush(minheap, (v,key))
            if len(minheap) > k:
                #removing the record with smallest count from the heap is the heap size exceeds k
                heapq.heappop(minheap)

        return [key for _,key in minheap]

if __name__ == '__main__':
    s = Solution()
    print(s.topKFrequent(nums = [1,1,1,2,2,3], k = 2))

#Time Complexity - O(nlogk)
#Space Complexity - O(k)
        