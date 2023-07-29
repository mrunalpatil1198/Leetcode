class Solution:
    def findMinDifference(self, timePoints: list[str]) -> int:

        #converting all time points into minutes and sorting in non decreasing order
        minutes = sorted([int(time[:2]) * 60 + int(time[3:]) for time in timePoints])
        result = float('inf')

        #calculating the diff between two consecutive time points
        for i in range(len(minutes)-1):
            result = min(result, minutes[i+1]-minutes[i])

        #calculating the time diff between the last and the first time point
        result = min(result, (24*60 - minutes[-1] + minutes[0])  % (24*60))
        return result
    
if __name__ == '__main__':
    s = Solution()
    print(s.findMinDifference(timePoints = ["00:00","23:59","00:00"]))

#Time Complexity - O(nlogn)
#Space Complexity - O(1)
