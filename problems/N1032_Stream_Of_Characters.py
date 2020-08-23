class TrieNode:
    def __init__(self):
        self.isword = False
        self.arr = {}
"""
Surprise, I used list : [None]*26 to crate Trie, the tests are timeout. 
But use dictionary , passed . 
"""
class StreamChecker_slow(object):

    def __init__(self, words):
        """
        :type words: List[str]
        """
        self.root = TrieNode()
        cur = self.root
        for word in words:
            for c in word:
                if c not in cur.arr:
                    cur.arr[c] = TrieNode()
                cur = cur.arr[c]
            cur.isword = True
            cur = self.root
        self.previous = [self.root]

    def query(self, letter):
        """
        :type letter: str
        :rtype: bool
        """
        new_previous = [self.root]
        flag = False
        for node in self.previous:
            if letter in node.arr:
                new_previous.append(node.arr[letter])
                if node.arr[letter].isword:
                    flag = True
        self.previous = new_previous
        return flag

"""
use reverse order to create Trie. 
First use list to save previous letters , timeout. 
Then change to string passed. 
"""
class StreamChecker(object):

    def __init__(self, words):
        """
        :type words: List[str]
        """
        self.root = TrieNode()
        cur = self.root
        for word in words:
            for c in word[::-1]:
                if c not in cur.arr:
                    cur.arr[c] = TrieNode()
                cur = cur.arr[c]
            cur.isword = True
            cur = self.root
        self.previous = ''

    def query(self, letter):
        """
        :type letter: str
        :rtype: bool
        """
        self.previous = letter + self.previous
        cur = self.root
        flag = False
        for c in self.previous:
            if c not in cur.arr:
                break
            cur = cur.arr[c]
            if cur.isword:
                flag = True
                break
        return flag

obj = StreamChecker(["cd","f","kl"])
obj.query('a')
obj.query('b')
obj.query('c')
obj.query('d')
obj.query('e')
obj.query('f')
obj.query('g')
obj.query('h')
obj.query('i')
obj.query('j')
obj.query('k')
obj.query('l')


