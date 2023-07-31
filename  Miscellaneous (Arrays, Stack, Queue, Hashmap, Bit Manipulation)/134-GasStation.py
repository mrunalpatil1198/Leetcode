class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        #checking if solution exists
        if sum(gas) < sum(cost):
            return -1
        total = 0
        start = 0

        for i in range(len(gas)):
            #calculating total from curr start point
            total += gas[i] - cost[i]

            #if total goes below 0, solution does not exist from the curr start point
            if total < 0:
                total = 0
                start = i+1

        return start
    
if __name__ == '__main__':
    s = Solution()
    print(s.canCompleteCircuit(gas = [1,2,3,4,5], cost = [3,4,5,1,2]))

#Time Complexity - O(n)
#Space Complexity - O(1)