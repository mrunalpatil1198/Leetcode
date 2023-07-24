from collections import Counter, deque
import heapq
class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        if n == 0:
            return len(tasks)
        
        #create a dict with counts of all the tasks
        tasks_count = Counter(tasks)

        #create a maxheap to store the counts of the tasks as at each time we would process task with maximum count left
        maxheap = [-count for count in tasks_count.values()]
        heapq.heapify(maxheap)

        #create a queue to maintain the number of tasks of each type and the time at which they can be scheduled
        q = deque()

        #maintain a counter for time
        time = 0

        while maxheap or q:
            time += 1
            if maxheap:

                #get the task with max count from the heap and schedule it
                remaining = 1 + heapq.heappop(maxheap)
                if remaining:

                    #if there are more tasks of same type, add remaning count with current time + cooldown to queue
                    q.append([remaining, time+n])
            
            #if we have a task in the queue that can be now scheduled, remove and add it to heap
            if q and q[0][1] == time:
                heapq.heappush(maxheap,  q.popleft()[0])
        
        return time
    
if __name__ == '__main__':
    s = Solution()
    print(s.leastInterval(tasks = ["A","A","A","B","B","B"], n = 2))
        
#Time Complexity - O(nlogn)
#Space Complexity - O(n)