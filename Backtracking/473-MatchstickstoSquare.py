class Solution:
    def makesquare(self, matchsticks: list[int]) -> bool:

        if not matchsticks:
            return False
        
        #checking if a solution exists
        perimeter = sum(matchsticks)
        side = perimeter // 4
        if side * 4 != perimeter:
            return False
        
        #sorting in decreasing order
        matchsticks.sort(key=lambda x: -x)

        #sums[i] would represent sum of length of matchsticks forming i side
        sums =[0 for _ in range(4)]

        def backtracking(index):
            if index == len(matchsticks):
                return sums[0] == sums[1] == sums[2] == sums[3] == side

            for i in range(4):
                #adding curr matchstick to all the sides one by one and recursively calling backtracking for next matchstick
                if sums[i] + matchsticks[index] <= side:
                    sums[i] += matchsticks[index]
                    if backtracking(index+1):
                        return True
                    
                    #popping if solution does not exist with the curr combination
                    sums[i] -= matchsticks[index]
        
        return backtracking(0)
    
if __name__ == '__main__':
    s = Solution()
    print(s.makesquare(matchsticks = [1,1,2,2,2]))

#Time Complexity - O(4^n)
#Space Complexity - O(1) - not considering recursion stack space
