class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        #keep track at what position to insert element when its not seen before
        insert_at = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[insert_at] = nums[i]
                insert_at += 1
        return insert_at
    
if __name__ == '__main__':
    s = Solution()
    print(s.removeDuplicates([1,1,2]))

#Time Complexity - O(n)
#Space Complexity - O(1)