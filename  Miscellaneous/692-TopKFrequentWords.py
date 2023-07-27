from collections import Counter
class Solution:

    def topKFrequent(self, words: list[str], k: int) -> list[str]:

        #creating dictionary of counts for words and sorting according to the value (freq) and then alphabetical order of keys and returning the top k keys
        return [k for k, v in sorted(Counter(words).items(), key = lambda x : (-x[1], x[0]))[:k]]
        
if __name__ == '__main__':
    s = Solution()
    print(s.topKFrequent(words = ["i","love","leetcode","i","love","coding"], k = 2))

#Time Complexity - O(nlogn)
#Space Complexity - O(n)