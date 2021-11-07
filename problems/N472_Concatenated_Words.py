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
            visited = [0] * length # visited[index] means word[index:] is not in the words.
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

    # update at 20111107
    def findAllConcatenatedWordsInADict_after(self, words: List[str]) -> List[str]:
        words.sort(key=lambda x: len(x))
        root = Trie()

        def check(index, word):
            if index == len(word):
                return True
            if (index, word) in memo:
                return memo[(index, word)]
            cur = root
            flag = False
            for i in range(index, len(word)):
                idx = ord(word[i]) - ord('a')
                if not cur.children[idx]:
                    break
                cur = cur.children[idx]
                if cur.end and check(i + 1, word):
                    flag = True
            memo[(index, word)] = flag
            return flag

        res = []
        memo = {}
        for word in words:

            if word and check(0, word):
                res.append(word)
            cur = root
            for c in word:
                idx = ord(c) - ord('a')
                if not cur.children[idx]:
                    cur.children[idx] = Trie()
                cur = cur.children[idx]
            cur.end = True
        return res