class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        numbers = {}
        for i, num in enumerate(nums):
            
            #checking if we have num in dict and calculating the diff between the indices
            if num in numbers:
                if i - numbers[num] <= k:
                    return True
            #storing the recent index of num into the dict
            numbers[num] = i
        return False
    
if __name__ == '__main__':
    s = Solution()
    print(s.containsNearbyDuplicate(nums = [1,2,3,1], k = 3))

#Time Complexity - O(n)
#Space Complexity - O(n)