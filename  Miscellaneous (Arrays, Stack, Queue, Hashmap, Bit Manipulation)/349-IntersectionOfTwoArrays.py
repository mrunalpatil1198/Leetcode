class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:

        #removing duplicates from both the lists
        nums1 = set(nums1)
        nums2 = set(nums2)
        result = []

        #finding common between the above two sets
        for num in nums1:
            if num in nums2:
                result.append(num)

        return result
    
if __name__ == '__main__':
    s = Solution()
    print(s.intersection(nums1 = [1,2,2,1], nums2 = [2,2]))

#Time Complexity - O(n)
#Space Complexity - O(1)
