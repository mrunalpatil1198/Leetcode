class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:

        #sorting according to start time 
        intervals.sort(key = lambda x : (x[0], x[1]))
        result = []
        i = 0

        while i < len(intervals):
            start = intervals[i][0]
            end = intervals[i][1]
            i += 1

            #keep merging intervals till start time of curr interval is less than the curr end time
            while i < len(intervals) and intervals[i][0] <= end:

                #update curr end time
                end = max(end, intervals[i][1])
                i += 1
            result.append([start, end])
        return result

if __name__ == '__main__':
    s = Solution()
    print(s.merge(intervals = [[1,3],[2,6],[8,10],[15,18]]))


#Time Complexity - O(nlogn)
#Space Complexity - O(1)