#Floyd's Tortoise and Hare Cycle Detection
class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        
        #initialize both, slow and fast pointer to 0
        slow = fast = 0
        while True:
            #increment slow by pointing to next number
            slow = nums[slow]
            #increment fast by pointing to next of next number
            fast = nums[nums[fast]]
            #if slow meets fast, break
            if slow == fast:
                break
        
        #to find the duplicate number, change slow to 0. Increment both pointers by next pointer untill they meet.
        slow = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        #return slow or fast pointer
        return slow

if __name__ == '__main__':
    s = Solution()
    print(s.findDuplicate([1,3,4,2,2]))   

#Time Complexity - O(n)     
#Space Complexity - O(1)
