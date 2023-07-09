class Solution:
    def sortColors(self, nums: list[int]) -> None:
        #initialize red to 0, white to 0 and blue to n-1 as we need all reds first then whites and blues at the end
        #each of them represent the position at which the next element having that color should be placed
        red = 0
        white = 0
        blue = len(nums)-1

        #use white as curr pointer
        while white <= blue:
            #if curr is red, swap curr and red pointer in order to place red in the front
            if nums[white] == 0:
                nums[white], nums[red] = nums[red], nums[white]
                #increment red and curr
                red += 1
                white += 1
            #if cur points to white, just increment curr
            elif nums[white] == 1:
                white += 1
            #if curr points to blue, swap curr and blue
            else:
                nums[blue], nums[white] = nums[white], nums[blue]
                #decrement blue
                blue -= 1
        
        return nums
if __name__ == '__main__':
    s = Solution()
    print(s.sortColors(nums = [2,0,2,1,1,0]))

#Time Complexity - O(n)
#Space Complexity - O(1)