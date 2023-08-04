class TrieNode:

    #storing children as dictionary and keeping track of end of word as boolean
    def __init__(self) -> None:
        self.children = {}
        self.isEndOfWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        #starting from the root
        temp = self.root
        
        #inserting one char at a time
        for char in word:
            if char not in temp.children:
                #creating new node if not present
                temp.children[char] = TrieNode()
            #moving pointer to next node
            temp = temp.children[char]
        
        #seeting end of word to true
        temp.isEndOfWord = True

    def search(self, word: str) -> bool:
        temp = self.root

        #searching char by char
        for char in word:
            if char not in temp.children:
                #word not present in the trie
                return False
            #moving pointer to next node
            temp = temp.children[char]
        
        #returning True only if it is end of a word
        return temp.isEndOfWord

    def startsWith(self, prefix: str) -> bool:
        temp = self.root
        #searching char by char
        for char in prefix:
            if char not in temp.children:
                #prefix not present in the trie
                return False
            #moving pointer to next node
            temp = temp.children[char]

        return True
    
if __name__ == '__main__':
    obj = Trie()
    obj.insert("apple")
    print(obj.search("apple"))
    print(obj.search("app"))
    print(obj.startsWith("app"))

#Time Complexity - O(n)
#Space Complexity - O(n)
