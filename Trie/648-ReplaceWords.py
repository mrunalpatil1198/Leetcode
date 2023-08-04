class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.isEndOfWord = False
    
class Trie:
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

    def replace(self, word):
        curr = self.root
        root = ''
        #searching for preixes of word in trie
        for char in word:
            root += char
            if char not in curr.children:
                return word
            curr = curr.children[char]
            if curr.isEndOfWord:
                return root
        return word
    
class Solution:
    def replaceWords(self, dictionary: list[str], sentence: str) -> str:
        sentence = sentence.split(" ")
        trie = Trie()
        result = []

        #inserting all words into trie
        for word in dictionary:
            trie.insert(word)

        #searching for roots in trie
        for word in sentence:
            result.append(trie.replace(word))
        return ' '.join(result)
    
if __name__ == '__main__':
    s = Solution()
    print(s.replaceWords(dictionary = ["cat","bat","rat"], sentence = "the cattle was rattled by the battery"))
    
#Time Complexity - O(n)
#Space Complexity - O(n)