class Solution:
    def canJump(self, nums) -> bool:
        #initialize the variable 'reach' to store the maximum index that can be reached
        reach = nums[0]

        #iterate over each index starting from 1
        for i in range(1, len(nums)):
            #if the current index is beyond the maximum reachable index, return False
            if i > reach:
                return False
            
             #update the maximum reachable index based on the current index and its jump value
            reach = max(reach, i+nums[i])

        #if the loop completes without returning False, it means the end of the array can be reached
        return True
    
if __name__ == '__main__':
    s = Solution()
    print(s.canJump([2,3,1,1,4]))
    print(s.canJump([3,2,1,0,4]))

#Time Complexity - O(n)
#Space Complexity - O(1)