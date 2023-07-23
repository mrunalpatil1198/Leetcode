class Solution:

    def letterCombinations(self, digits: str) -> list[str]:
        result = []

        #map each digit to its corresponding letters on a phone keypad
        letters = {
            1: [],  # We don't have any letters mapped to digit 1
            2: ['a', 'b', 'c'],
            3: ['d', 'e', 'f'],
            4: ['g', 'h', 'i'],
            5: ['j', 'k', 'l'],
            6: ['m', 'n', 'o'],
            7: ['p', 'q', 'r', 's'],
            8: ['t', 'u', 'v'],
            9: ['w', 'x', 'y', 'z'],
            0: []   # We don't have any letters mapped to digit 0
        }

        def backtracking(elements, index):
            #if all the digits are processed, add the current combination to the result list
            if index == len(digits):
                result.append(''.join(elements))
                return
            
            #base case - if the current index goes beyond the length of the digits, return
            if index > len(digits):
                return

            #for each letter corresponding to the current digit, add it to the combination
            for letter in letters[int(digits[index])]:

                #add current letter to the combination
                elements.append(letter)
                
                #recur with the next digit
                backtracking(elements, index + 1)
                
                #backtrack by removing the last letter, so we can try the next letter for the current digit
                elements.pop()

        #start with the first digit
        backtracking([], 0)

        #return the result list
        return result

if __name__ == '__main__':
    s = Solution()
    print(s.letterCombinations("23"))

#Time Complexity - Exponential - O(4^n) as we have at most 4 choices of alphabets for each digit