from functools import cmp_to_key
class Solution:
    def largestNumber(self, nums: list[int]) -> str:

        #defining comparator by concatenating strings of elements in nums
        def compare(str1, str2):
            return int(str(str1) + str(str2)) - int(str(str2) + str(str1))
        
        #sorting using above comparator in reverse order
        nums.sort(key = cmp_to_key(compare), reverse= True)
        result = ''.join(map(str, nums))
        if int(result) == 0:
            return "0"
        return result

if __name__ == '__main__':
    s = Solution()
    print(s.largestNumber([10,2]))

#Time Complexity - O(nlogn)
#Space Complexity - O(1)