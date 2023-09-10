class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        result = 0
        prefix_sum = 0
        d = {0 : 1}

        for num in nums:
            prefix_sum += num
            if prefix_sum - k in d:
                result += d[prefix_sum - k]
            if prefix_sum in d:
                d[prefix_sum] += 1
            else:
                d[prefix_sum] = 1
        
        return result

if __name__ == '__main__':
    s = Solution()
    print(s.subarraySum(nums = [1,1,1], k = 2))

#Time Complexity - O(n)
#Space Compelxity - O(n)
