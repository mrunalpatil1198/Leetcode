class Solution:
    def maxProfit(self, prices) -> int:
        #initialize variables to store the maximum profit and the minimum price
        result = 0
        minimum = prices[0]

        #iterate through the prices list
        for price in prices:
            #update the minimum price seen so far
            minimum = min(minimum, price)
            #update the maximum profit seen so far by calculating the potential profit if we sell at the current price
            result = max(result, price - minimum)
        
        #return the maximum profit
        return result

if __name__ == '__main__':
    s = Solution()
    print(s.maxProfit([7,1,5,3,6,4]))
    print(s.maxProfit([7,6,4,3,1]))

#Time Complexity - O(n)
#Space Complexity - O(1)