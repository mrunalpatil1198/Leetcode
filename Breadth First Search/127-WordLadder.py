from collections import defaultdict, deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        next_words = defaultdict(list)
        letters = "abcdefghijklmnopqrstuvwxyz"
        words = wordList + [beginWord]
        word_set = set(wordList)

        #preparing a dictionary of next possible words for all the words in wordlist
        for word in words:
            for i in range(len(word)):
                word_1 = word[:i]
                word_2 = word[i+1:]
                for letter in letters:
                    #next possible word can be formed by adding just one letter at any position in the curr word
                    next_word = word_1 + letter + word_2
                    if next_word in word_set:
                        next_words[word].append(next_word)

        q = deque()
        q.append((1, beginWord))
        visited = set()

        #bfs
        while q:
            length, curr = q.popleft()

            #checking if we have reached end word
            if curr == endWord:
                return length
            if curr not in visited:
                #search from all the next words
                for next_word in next_words[curr]:
                    q.append((length+1, next_word))
                #updating visited
                visited.add(curr)
        return 0
    
if __name__ == '__main__':
    s = Solution()
    print(s.ladderLength(beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]))

#Time Complexity - O(n^2) - preparing the dictionary of next words
#Space Complexity - O(n*k) - where k = next possible words in wordlist
        



