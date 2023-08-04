class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.isEndOfWord = False
        self.word = ''

class Trie():
    def __init__(self) -> None:
        self.root = TrieNode()
    
    #creating trie
    def insert(self, word):
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]    
        curr.isEndOfWord = True
        curr.word = word

    def bfs(self):
        curr = self.root
        result = ''
        q = [curr]
        while q:
            curr = q.pop(0)
            for child in curr.children.values():
                #considering children nodes with isEndOfWord set True as we are allowed to build by adding only one char at a time by other words
                if child.isEndOfWord:
                    q.append(child)

                    #updating result
                    if len(result) < len(child.word):
                        result = child.word
        return result
    
class Solution:
    def longestWord(self, words: list[str]) -> str:

        #sorting for lexicographical order
        words.sort()
        trie = Trie()

        #inserting all words into trie
        for word in words:
            trie.insert(word)
        return trie.bfs()

if __name__ == '__main__':
    s = Solution()
    print(s.longestWord(words = ["a","banana","app","appl","ap","apply","apple"]))
        
#Time Complexity - O(n)
#Space Complexity - O(n)


        