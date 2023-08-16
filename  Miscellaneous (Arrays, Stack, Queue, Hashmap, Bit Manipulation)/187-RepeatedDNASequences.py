class Solution:
    def findRepeatedDnaSequences(self, s: str) -> list[str]:
        lst = []
        seq = set()
        for i in range(0, len(s)-9):
            temp = s[i : i+10]
            if temp not in seq:
                #adding to set if previously not seen
                seq.add(temp)
            else:
                #adding to result as it is seen before
                lst.append(temp)
        return list(set(lst))
    
if __name__ == '__main__':
    s = Solution()
    print(s.findRepeatedDnaSequences(s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"))

#Time Complexity - O(n)
#Space Complexity - O(n)