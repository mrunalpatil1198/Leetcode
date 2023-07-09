class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        #Keep track of at what position to insert element when its not equal to the given number
        insert_at = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[insert_at] = nums[i]
                insert_at += 1
        return insert_at
    
if __name__ == '__main__':
    s = Solution()
    print(s.removeElement(nums = [3,2,2,3], val = 3))

#Time Complexity - O(n)
#Space Complexity - O(1)