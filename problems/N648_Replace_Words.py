class TrieNode:
    def __init__(self):
        self.is_root = False
        self.next = [None] * 26
        self.val = ''

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        current = self.root
        for i in range(len(word)):
            index = ord(word[i]) - ord('a')
            if not current.next[index]:
                current.next[index] = TrieNode()
            current = current.next[index]
        current.is_root = True
        current.val = word

    def search(self, word):
        current = self.root
        for i in range(len(word)):
            index = ord(word[i]) - ord('a')
            if current.is_root:
                return current.val
            if not current.next[index]:
                return word
            current = current.next[index]
        if current.is_root:
            return current.val
        return word

class Solution(object):
    def replaceWords(self, dict, sentence):
        """
        :type dict: List[str]
        :type sentence: str
        :rtype: str
        """
        trie = Trie()
        for word in dict:
            trie.insert(word)

        res = []
        words = sentence.split()
        for word in words:
            res.append(trie.search(word))
        return ' '.join(res)



