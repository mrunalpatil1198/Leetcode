class Solution:
    def candy(self, ratings: list[int]) -> int:

        #each child will initially have at least one candy
        result = [1 for _ in range(len(ratings))]

        #traverse from left to right and assign one more candy to the current child than the previous one if the current has more rating
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i-1]:
                result[i] = result[i-1] + 1
        
        #traverse from right to left and assign one more candy to the current child than the one next to him if the current has more rating
        for i in range(len(ratings) - 2, -1, -1):
            if ratings[i] > ratings[i+1] and result[i] <= result[i+1]:
                result[i] = result[i+1] + 1
        
        #result is the sum of all candies
        return sum(result)
    
if __name__ == '__main__':
    s = Solution()
    print(s.candy(ratings=[1, 0, 2]))

#Time Complexity - O(n) 
#Space Complexity - O(n)