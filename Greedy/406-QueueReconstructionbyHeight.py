class Solution:
    def reconstructQueue(self, people: list[list[int]]) -> list[list[int]]:

        #first sort according to the heights in decreasing manner and then according to ki in non decreasing manner
        people.sort(key = lambda x : (-x[0], x[1]))
        result = []

        #for all people, insert them into the result at their kth position
        #we use python's insert for this as - if a record already exists in the list at the given index, all records are shifted one step to right to make space for the current element
        for person in people:
            result.insert(person[1], person)
        return result

if __name__ == '__main__':
    s = Solution()
    print(s.reconstructQueue(people = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]))

#Time Complexity - O(n^2)
#Space Complexity - O(1)