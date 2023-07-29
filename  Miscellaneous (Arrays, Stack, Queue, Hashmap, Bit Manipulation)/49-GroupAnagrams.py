import collections
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        words = collections.defaultdict(list)
        for word in strs:
            #sorting words according to alphabetical order
            words[tuple(sorted(word))].append(word)
        return words.values()
    
if __name__ == '__main__':
    s = Solution()
    print(s.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))

#Time Complexity - O(n) 
#Space Complexity - O(n)

