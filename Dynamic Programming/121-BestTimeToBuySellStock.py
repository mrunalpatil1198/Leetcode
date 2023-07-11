class Solution:
    def maxProfit(self, prices) -> int:
        result = 0
        minimum = prices[0]

        for price in prices:
            minimum = min(minimum, price)
            result = max(result, price - minimum)
        
        return result

if __name__ == '__main__':
    s = Solution()
    print(s.maxProfit([7,1,5,3,6,4]))
    print(s.maxProfit([7,6,4,3,1]))