class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.is_end = False

class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        current = self.root
        for i in range(len(word)):
            index = ord(word[i]) - ord('a')
            if not current.children[index]:
                current.children[index] = TrieNode()
            current = current.children[index]
        current.is_end = True

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        current = self.root
        return self.search_helper(current, word)

    def search_helper(self, current, word):
        if not word:
            return current.is_end

        if word[0] != '.':
            index = ord(word[0]) - ord('a')
            if not current.children[index]:
                return False
            else:
                return self.search_helper(current.children[index], word[1:])
        else:
            for node in current.children:
                if not node:
                    continue
                if self.search_helper(node, word[1:]):
                    return True
            return False





# Your WordDictionary object will be instantiated and called as such:
obj = WordDictionary()
obj.addWord("bad")
obj.addWord("dad")
obj.addWord("mad")
print(obj.search('pad'))
print(obj.search('bad'))
print(obj.search('.ad'))
print(obj.search('b..'))