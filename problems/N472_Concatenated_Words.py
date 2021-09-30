import collections
from typing import List

class Trie:
    def __init__(self):
        self.children = [None] * 26
        self.isend = False
class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        root = Trie()
        res = []
        words.sort(key=lambda x: len(x))
        def dfs(word, index, visited):
            l = len(word)
            if index == l:
                return True
            if visited[index]:
                return False
            cur = root
            for i in range(index, l):
                idx = ord(word[i]) - ord('a')
                if not cur.children[idx]:
                    break
                cur = cur.children[idx]
                if cur.isend and dfs(word, i+1, visited):
                    return True
            visited[index] = 1
            return False
        def check(word):
            length = len(word)
            visited = [0] * length
            return dfs(word, 0, visited)
        for word in words:
            if word and check(word):
                res.append(word)
            cur = root
            for c in word:
                index = ord(c) - ord('a')
                if not cur.children[index]:
                    cur.children[index] = Trie()
                cur = cur.children[index]
            cur.isend = True
        return res
