"""
Check all possible to get a palindrome.
The new added can be in the left or right.
We need to check all the part . Here, in order to avoid duplication, when check another side, need to add i != 0.
"""
from typing import List


class TrieNode:
    def __init__(self) -> None:
        self.letters = {}
        self.index = set()
        self.suffix = set()

class Solution(object):
    def palindromePairs_hashtable(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        mapping = {}
        res = []
        for index, word in enumerate(words):
            mapping[word] = index

        for index, word in enumerate(words):
            length = len(word)
            for i in range(length + 1):
                left, right = word[:i], word[i:]
                if left[::-1] in mapping and mapping[left[::-1]] != index and right == right[::-1]:
                    res.append([index, mapping[left[::-1]]])
                if i != 0 and right[::-1] in mapping and mapping[right[::-1]] != index and left == left[::-1]:
                    res.append([mapping[right[::-1]], index])
        return res

    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        root = TrieNode()
        for i, word in enumerate(words):
            cur = root
            rword = word[::-1]
            lw = len(rword)
            for j in range(lw):
                if rword[j:] == rword[j:][::-1]:
                    cur.suffix.add(i)
                c = rword[j]
                if c not in cur.letters:
                    cur.letters[c] = TrieNode()
                cur = cur.letters[c]
            cur.index.add(i)
            cur.suffix.add(i)
        res = []
        for i, word in enumerate(words):
            cur = root

            for j, c in enumerate(word):
                if word[j:] == word[j:][::-1]:
                    for k in cur.index:
                        if k != i:
                            res.append([i, k])

                if c not in cur.letters:
                    break
                cur = cur.letters[c]
            else:
                for k in cur.suffix:
                    if k != i:
                        res.append([i, k])
        return res