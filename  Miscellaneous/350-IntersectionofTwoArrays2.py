import collections
class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        n_1 = collections.defaultdict(int)
        result = []

        for num in nums1:
            n_1[num] += 1

        for num in nums2:
            if num in n_1 and n_1[num] != 0:
                result.append(num)
                n_1[num] -= 1
        
        return result
    
if __name__ == '__main__':
    s = Solution()
    print(s.intersect(nums1 = [1,2,2,1], nums2 = [2,2]))

            