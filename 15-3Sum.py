#Aprroach - sort the numbers in non decreasing order. for every element, caculate sum of current, next element(j) and the last element(k). If sum is 0 add to the result. Else if sum is greater than 0, decrement k as we need some smaller element else increment j as we need some bigger element.
class Solution:

    def threeSum(self, nums: list[int]) -> list[list[int]]:
        #sort in non-decreasing order
        nums.sort()
        result = set()
        
        #visit every element
        for i in range(len(nums)):
            #check for next all elements as discussed in the approach above 
            j = i+1
            k = len(nums) - 1
            while j < k:
                sum = nums[i] + nums[j] + nums[k]
                if sum == 0:
                    result.add((nums[i], nums[j], nums[k]))
                    j += 1
                    k -= 1
                elif sum > 0:
                    k -= 1
                else:
                    j += 1
        return list(result)
    
if __name__ == '__main__':
    s = Solution()
    print(s.threeSum(nums = [-1,0,1,2,-1,-4]))

#Time Complexity - O(n^2)
#Space Complexity - O(1) (not considering the result)
