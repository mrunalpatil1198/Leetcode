class Solution:
    def nextGreatestLetter(self, letters: list[str], target: str) -> str:
        left = 0
        right = len(letters) - 1
        res = -1

        #binary search
        while left <= right:
            mid = left + (right - left)//2
            if letters[mid] > target:
                #this can be a possible solution
                res = mid
                #now, need to check if there is any letter smaller than curr solution hence, checking the left half
                right = mid - 1
            else:
                #result lies in the right half
                left = mid + 1
        
        return letters[res] if res != -1 else letters[0]

if __name__ == '__main__':
    s = Solution()
    print(s.nextGreatestLetter(letters = ["c","f","j"], target = "a"))

#Time Complexity - O(logn)
#Space Complexity - O(1)