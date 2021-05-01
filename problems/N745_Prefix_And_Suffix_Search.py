from typing import List

class TrieNode:
    def __init__(self):
        self.children = [None]*27
        self.is_word = False
        self.index = []

class WordFilter_TLE:
    def __init__(self, words: List[str]):
        self.proot = TrieNode()
        for i, word in enumerate(words):
            node = self.proot
            for c in word:
                if not node.children[ord(c) - ord('a')]:
                    node.children[ord(c) - ord('a')] = TrieNode()
                node = node.children[ord(c) - ord('a')]
            node.is_word = True
            node.index.append(i)
        self.sroot = TrieNode()
        for i, word in enumerate(words):
            node = self.sroot
            for c in word[::-1]:
                if not node.children[ord(c) - ord('a')]:
                    node.children[ord(c) - ord('a')] = TrieNode()
                node = node.children[ord(c) - ord('a')]
            node.is_word = True
            node.index.append(i)
        self.memo = {}

    def f(self, prefix: str, suffix: str) -> int:
        if prefix in self.memo or suffix in self.memo or (prefix, suffix) in self.memo:
            return self.memo[(prefix, suffix)]
        rp, rs = [], []
        p = self.proot
        for c in prefix:
            if not p.children[ord(c) - ord('a')]:
                break
            p = p.children[ord(c) - ord('a')]
        else:
            nodes = [p]
            while nodes:
                new_nodes = []
                for node in nodes:
                    if node.is_word:
                        rp.extend(node.index)
                    for child in node.children:
                        if child:
                            new_nodes.append(child)
                nodes = new_nodes
        s = self.sroot
        for c in suffix[::-1]:
            if not s.children[ord(c) - ord('a')]:
                break
            s = s.children[ord(c) - ord('a')]
        else:
            nodes = [s]
            while nodes:
                new_nodes = []
                for node in nodes:
                    if node.is_word:
                        rs.extend(node.index)
                    for child in node.children:
                        if child:
                            new_nodes.append(child)
                nodes = new_nodes
        res = -1
        if not rp:
            self.memo[prefix] = res
        if not rs:
            self.memo[suffix] = res

        for i in rp:
            if i in rs and i > res:
                res = i
        self.memo[(prefix, suffix)] = res
        return self.memo[(prefix, suffix)]
"""
First, I tried to use two Trie to save prefix ans suffix, TLE. 
Then according to the hint : For a word like "test", 
consider "#test", "t#test", "st#test", "est#test", "test#test". 
Then if we have a query like prefix = "te", suffix = "t", 
we can find it by searching for something we've inserted starting with "t#te".

Use one Trie and memo, pass all tests.
"""
class WordFilter:
    def __init__(self, words: List[str]):
        self.root = TrieNode()
        for i, w in enumerate(words):
            for j in range(len(w)-1, -1, -1):
                word = w[j:] + '#' + w
                node = self.root
                for c in word:
                    index = ord(c) - ord('a') if c != '#' else 26
                    if not node.children[index]:
                        node.children[index] = TrieNode()
                    node = node.children[index]
                node.is_word = True
                node.index.append(i)
        self.memo = {}

    def f(self, prefix: str, suffix: str) -> int:
        s = suffix + '#' + prefix
        if s in self.memo:
            return self.memo[s]
        cur = self.root
        res = -1
        for c in s:
            index = ord(c) - ord('a') if c != '#' else 26
            if not cur.children[index]:
                return -1
            cur = cur.children[index]
        else:
            nodes = [cur]
            while nodes:
                new_nodes = []
                for node in nodes:
                    if node.is_word:
                        res = max(res, max(node.index))
                    for child in node.children:
                        if child:
                            new_nodes.append(child)
                nodes = new_nodes
        self.memo[s] = res
        return res

f = ["WordFilter","f","f","f","f","f","f","f","f","f","f"]
l = [[["cabaabaaaa","ccbcababac","bacaabccba","bcbbcbacaa","abcaccbcaa","accabaccaa","cabcbbbcca","ababccabcb","caccbbcbab","bccbacbcba"]],["bccbacbcba","a"],["ab","abcaccbcaa"],["a","aa"],["cabaaba","abaaaa"],["cacc","accbbcbab"],["ccbcab","bac"],["bac","cba"],["ac","accabaccaa"],["bcbb","aa"],["ccbca","cbcababac"]]
obj = None
for i in range(len(f)):
    if i == 0:
        obj = WordFilter(*l[0])
    else:
        res = obj.f(*l[i])
        print(res)
