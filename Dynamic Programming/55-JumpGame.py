class Solution:
    def canJump(self, nums) -> bool:
        reach = nums[0]
        for i in range(1, len(nums)):
            if i > reach:
                return False
            reach = max(reach, i+nums[i])
        return True
    
if __name__ == '__main__':
    s = Solution()
    print(s.canJump([2,3,1,1,4]))
    print(s.canJump([3,2,1,0,4]))