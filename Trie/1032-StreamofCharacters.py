class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.isEndOfWord = False

class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()

    #creating trie for the words in reverse order
    def insert(self, word):
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.isEndOfWord = True

    #as we are sending words in reverse order and our trie is also in reverse order, we will have to match it like prefix
    def matchPrefix(self, word):
        curr = self.root
        for char in word:
            if char not in curr.children:
                return False
            curr = curr.children[char]
            if curr.isEndOfWord: 
                return True
        return False
    
class StreamChecker:
    def __init__(self, words: list[str]):
        self.trie = Trie()

        #inserting words into trie in reverse order
        for word in words:
            self.trie.insert(word[::-1])
        self.prefix = ''
    
    def query(self, letter: str) -> bool:
        #adding curr char to prefix
        self.prefix += letter
        return self.trie.matchPrefix(self.prefix[::-1])
    
if __name__ == '__main__':
    obj = StreamChecker(["cd", "f", "kl"])
    print(obj.query("a"))
    print(obj.query("b"))
    print(obj.query("c"))
    print(obj.query("d"))
    print(obj.query("e"))
    print(obj.query("f"))
    print(obj.query("g"))
    print(obj.query("h"))
    print(obj.query("i"))
    print(obj.query("j"))
    print(obj.query("k"))
    print(obj.query("l"))

#Time Complexity - O(n)
#Space Coplexity - O(n)