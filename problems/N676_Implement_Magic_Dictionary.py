import collections

class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = collections.defaultdict(TrieNode)

class MagicDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, word):
        current = self.root
        for ch in word:
            if ch not in current.children.keys():
                current.children[ch] = TrieNode()
            current = current.children[ch]
        current.is_end = True

    def find(self, word, current, remain):
        if not word:
            return True if current.is_end and remain == 0 else False

        for key in current.children.keys():
            if key == word[0]:
                if self.find(word[1:], current.children[key], remain):
                    return True
            else:
                if remain and self.find(word[1:], current.children[key], 0):
                    return True
        return False

    def buildDict(self, dict) -> None:
        """
        Build a dictionary through a list of words
        """
        for word in dict:
            self.insert(word)

    def search(self, word: str) -> bool:
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        """
        return self.find(word, self.root, 1)
