import collections
from collections import deque
from math import inf


class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        if not wordList or endWord not in wordList:
            return 0
        self.dict = self.construct_dict(wordList)
        self.length = len(beginWord)
        # return self.bfs(beginWord, endWord)
        return self.bidirection_bfs(beginWord, endWord)

    def bidirection_bfs(self, beginWord, endWord):
        left = set([beginWord])
        right = set([endWord])
        used_left = set([beginWord])
        used_right = set([endWord])
        left_step, right_step = 1, 1
        flag = True
        while left and right:
            if left.intersection(right):
                return left_step + right_step - 1
            queue = left if flag else right
            used = used_left if flag else used_right
            temp = set()
            for word in queue:
                for i in range(self.length):
                    key = word[:i] + '*' + (word[i + 1:] if i < self.length - 1 else '')
                    if key not in self.dict:
                        continue
                    for w in self.dict[key]:
                        if w in used:
                            continue
                        used.add(w)
                        temp.add(w)
            if flag:
                left = temp
                left_step += 1
            else:
                right = temp
                right_step += 1
            flag = not flag
        return 0




    """
    shortest path usually use BFS, when this is a solution, then return. No need to check all solutions. 
    """
    def bfs(self, beginWord, endWord):
        queue = deque([(beginWord,1)])
        used = set()
        used.add(beginWord)
        while queue:
            word, step = queue.popleft()
            for i in range(self.length):
                key = word[:i] + '*' + (word[i + 1:] if i < self.length - 1 else '')
                if key not in self.dict:
                    continue
                for w in self.dict[key]:
                    if w in used:
                        continue
                    used.add(w)
                    if w == endWord:
                        return step + 1
                    queue.append((w, step + 1))
        return 0

    """
    DFS will be timeout.
    """
    def dfs(self, beginWord, endWord, steps, used):
        if beginWord == endWord:
            return steps

        steps += 1
        next_words = set()
        for i in range(self.length):
            key = beginWord[:i] + '*' + (beginWord[i+1:] if i < self.length-1 else '')
            if key in self.dict:
                next_words.update(self.dict[key])
        if not next_words:
            return 0
        res = float(inf)
        for word in next_words:
            if word in used:
                continue
            used.add(word)
            vals = self.bfs(word, endWord, steps, used)
            if vals > 0:
                res = min(res, vals)
            used.remove(word)

        return 0 if res == float(inf) else res

    def construct_dict(self, wordList):
        dict = collections.defaultdict(set)
        for word in wordList:
            length = len(word)
            for i in range(length):
                key = word[:i] + '*' + (word[i+1:] if i < length -1 else '')
                dict[key].add(word)
        return dict
