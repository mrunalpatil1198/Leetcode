class Solution:
    def minDominoRotations(self, tops: list[int], bottoms: list[int]) -> int:

        #function to calculate the swaps required to make all tiles same as target
        def greedy(target):
            t = b = 0
            for top, bottom in zip(tops, bottoms):
                if top != target and bottom != target:
                    return -1
                
                #increament top if we need to swap to match the top to target 
                elif top != target:
                    t += 1
                
                #increament bottom if we need to swap to match bottom to the target
                elif bottom != target:
                    b += 1

            #return min number of swaps 
            return min(t, b)
        
        #first try with top[0] as target
        top_swaps = greedy(tops[0])

        #if we did not reach a solution with top[0], try with bottom[0] as target
        if top_swaps == -1:
            return greedy(bottoms[0])
        else:
            return top_swaps
        
if __name__ == '__main__':
    s = Solution()
    print(s.minDominoRotations(tops = [2,1,2,4,2,2], bottoms = [5,2,6,2,3,2]))

#Time Complexity - O(n)
#Space Complexity - O(1)

