from collections import defaultdict

class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        stack = []
        mapping = defaultdict(lambda: -1)
        stack.append(nums2[0])
        result = []

        for i in range(1, len(nums2)):
            while stack and stack[-1] < nums2[i]:
                mapping[stack.pop()] = nums2[i]
            stack.append(nums2[i])
        
        for num in nums1:
            result.append(mapping[num])
        
        return result
    
if __name__ == '__main__':
    s = Solution()
    print(s.nextGreaterElement(nums1 = [4,1,2], nums2 = [1,3,4,2]))