import collections
class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        result = []

        #initialize pointers to keep track of start and end of current window
        left = right = 0

        #create a doubly ended queue which would keep track of index of largest element in the window
        q = collections.deque()

        #traverse nums using right pointer
        while right < len(nums):

            #while the last elements added in the queue are smaller than the current, pop them as we do not need them anymore
            while q and nums[q[-1]] < nums[right]:
                q.pop()

            #add index of curr element to the queue
            q.append(right)

            #if q[0] if less than our current window start, pop
            if left > q[0]:
                q.popleft()
            
            #chekc if we have a valid window size
            if right+1 >= k:

                #add element at q[0] to the result as it would be the largest of the current window
                result.append(nums[q[0]])

                #shift window start by 1 towards right for next iteration
                left += 1
            
            #shift window end by 1 towards right for next iteration
            right += 1
        return result
    
if __name__ == '__main__':
    s = Solution()
    print(s.maxSlidingWindow(nums = [1,3,-1,-3,5,3,6,7], k = 3))

#Time complexity - O(n)
#Space Complexity - O(k)