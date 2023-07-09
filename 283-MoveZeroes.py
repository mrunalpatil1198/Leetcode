class Solution:
    def moveZeroes(self, nums: list[int]):
        #keep a track of at what position to insert a non-zero element
        insert_at = 0

        #scan entire list and replace 0 with next non-zero element
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[insert_at] = nums[i]
                insert_at += 1
        
        #set rest all elements after insert_at position to 0
        for i in range(insert_at, len(nums)):
            nums[i] = 0
        
        return nums

if __name__ == '__main__':
    s = Solution()
    s.moveZeroes([0,1,0,3,12])

#Time Complexity - O(n)
#Space Complexity - O(n)