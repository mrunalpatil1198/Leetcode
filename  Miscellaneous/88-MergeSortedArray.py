class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> list:

        #initialize a pointer to the end of the nums1 
        #this points to the index at which we need to insert the element in nums1
        insert_at = m+n-1

        #initailize i and j to the index of last element in nums1 and nums2 respectively
        i = m - 1
        j = n - 1

        #traverse the nums2
        while j >= 0:

            #we merge the lists from the end that is from largest to the smallest element

            #if nums1[i] is greater than nums2[j] we need to insert nums1[i] and the index pointed by insert_at and move i to left
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[insert_at] = nums1[i]
                i -= 1
            else:

                #insert nums2[j] in nums[1] at the insert_at index and move to left
                nums1[insert_at] = nums2[j]
                j -= 1
            
            #move the pointer one place to left as we have found our element at curr position of the final list
            insert_at -= 1
        return nums1

if __name__ == '__main__':
    s = Solution()
    print(s.merge(nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3))

#Time Complexity - O(m+n)
#Space Complexity - O(1)