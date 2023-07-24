class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        #initialize left as the start for the  window
        left = 0

        #create a dictionary to store the count of each fruit in the current window
        basket = {}  

        #traverse through the array using the right pointer
        for right, fruit in enumerate(fruits):
            
            #update the count of the current fruit in dictionary
            basket[fruit] = basket.get(fruit, 0) + 1
            
            #if the number of distinct fruits in the basket exceeds 2, we need to shrink the window
            if len(basket) > 2:

                #decrement the count of the fruit at the left pointer from the dictionary
                basket[fruits[left]] -= 1

                if basket[fruits[left]] == 0:
                    #if the count becomes zero after decrementing, remove the fruit from the dictionary
                    del basket[fruits[left]]

                #move the left pointer to the right to shrink the window
                left += 1

        #at the end, the window's size represents the maximum number of fruits that can be collected
        return right - left + 1

if __name__ == '__main__':
    s = Solution()
    print(s.totalFruit([1, 2, 1]))

#Time Complexity - O(n)
#Space Complexity - O(1)
