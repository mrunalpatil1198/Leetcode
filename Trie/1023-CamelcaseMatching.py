class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.isEndOfWord = False

class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()
    
    #creating trie for the given pattern
    def insert(self, pattern):
        curr = self.root
        for char in pattern:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.isEndOfWord = True

    def matchCamelcase(self, word):
        curr = self.root
        for char in word:
            if char not in curr.children and char >= 'A' and char <= 'Z':
                #it does not match the pattern
                return False
            if char in curr.children:
                #moving pointer to next node in trie
                curr = curr.children[char]

        #returning true if pattern has ended
        return True if curr.isEndOfWord else False
    
class Solution:
    def camelMatch(self, queries: list[str], pattern: str) -> list[bool]:
        trie = Trie()
        trie.insert(pattern)
        result = []

        #matching one word at a time with the pattern trie
        for word in queries:
            result.append(trie.matchCamelcase(word))
        return result

if __name__ == '__main__':
    s = Solution()
    print(s.camelMatch(queries = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], pattern = "FoBa"))

#Time Complexity - O(n)
#Space Complexity - O(n)