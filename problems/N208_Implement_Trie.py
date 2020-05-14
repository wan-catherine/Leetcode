class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.is_end_of_word = False

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        current_node = self.root
        for i in range(len(word)):
            index = ord(word[i]) - ord('a')
            if not current_node.children[index]:
                current_node.children[index] = TrieNode()
            current_node = current_node.children[index]
        current_node.is_end_of_word = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        current_node = self.root
        for i in range(len(word)):
            index = ord(word[i]) - ord('a')
            if not current_node.children[index]:
                return False
            current_node = current_node.children[index]
        return current_node and current_node.is_end_of_word

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        current_node = self.root
        for i in range(len(prefix)):
            index = ord(prefix[i]) - ord('a')
            if not current_node.children[index]:
                return False
            current_node = current_node.children[index]
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
if __name__ == "__main__":
    obj = Trie()
    obj.insert("apple")
    res = obj.search("apple")
