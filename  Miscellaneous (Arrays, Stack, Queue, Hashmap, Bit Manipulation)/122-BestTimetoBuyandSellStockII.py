class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        profit = 0
        #profit is the sum of all the increases in the prices 
        for i in range(1,len(prices)):
            if prices[i] > prices[i-1]:
                profit += prices[i] - prices[i-1]
        return profit
    
if __name__ == '__main__':
    s = Solution()
    print(s.maxProfit(prices = [7,1,5,3,6,4]))

#Time Complexity - O(n)
#Space Complexity - O(1)