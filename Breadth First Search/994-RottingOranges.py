class Solution:
    
    def orangesRotting(self, grid: list[list[int]]) -> int:
        rotten = []
        fresh = set()
        minutes = 0

        #adding oranges into rotten and fresh sets
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    fresh.add((i,j))
                elif grid[i][j] == 2:
                    rotten.append((i,j))

        #directions in which oranges can get rotten
        dimensions = [[1,0], [-1,0], [0,1], [0,-1]]
        
        #bfs
        while len(fresh) > 0:
            prev_len = len(fresh)
            #changing all the oranges that will become rotten this minute
            for _ in range(len(rotten)):
                curr_i, curr_j = rotten.pop(0)
                #updating neighbor oranges as they will become rotten now
                for d in dimensions:
                    new_i = curr_i + d[0]
                    new_j = curr_j + d[1]
                    #updating our sets
                    if (new_i, new_j) in fresh:
                        rotten.append((new_i, new_j))
                        fresh.remove((new_i, new_j))
            minutes += 1
            #if no new orange became rotten, it is impossible to reach the final condition
            if prev_len == len(fresh):
                return -1

        return minutes
    
if __name__ == '__main__':
    s = Solution()
    print(s.orangesRotting([[2,1,1],[1,1,0],[0,1,1]]))

#Time Complexity - O(m*n) 
#Space Complexity - O(k) - where k = total number of oranges