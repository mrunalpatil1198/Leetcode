class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:

        #maintaing the position to insert next element of result at
        insert_at = 1
        i = 1
        count = 1


        while i < len(nums):
            #if duplicate found
            if nums[i] == nums[insert_at - 1]:
                if count == 2:
                    #skipping duplicates who occur more than twice
                    while i < len(nums) and nums[i] == nums[insert_at - 1]:
                        i += 1
                    if i >= len(nums):
                        break
                    #resetting count
                    count = 1
                else:
                    count = 2
            else:
                count = 1
            #inserting valid element
            nums[insert_at] = nums[i]
            insert_at += 1
            i += 1
        
        return insert_at
    
if __name__ == '__main__':
    s = Solution()
    print(s.removeDuplicates(nums = [1,1,1,2,2,3]))

#Time Complexity - O(n)
#Space Complexity - O(1)