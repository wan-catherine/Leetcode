import collections
"""
Key point:
    1. use visited to record all before visited words.
    2. use local_visited to record all words for this run . 
    
{A} ==> {B, C} ==> {D}
here , for B, C , both of them can move to D , so here need to use local_visited . 
use visited , so B,C won't move to A. 
"""

class Solution(object):
    def findLadders_bfs(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        if not endWord or not beginWord or not wordList or endWord not in wordList \
                or beginWord == endWord:
            return []

        wordList = set(wordList)
        wordList.add(beginWord)
        l = len(beginWord)
        graph = collections.defaultdict(set)
        for word in wordList:
            for i in range(l):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    if c == word[i]:
                        continue
                    new_word = word[0:i] + c + word[i + 1:]
                    if new_word not in wordList:
                        continue
                    graph[word].add(new_word)

        stack = [beginWord]

        previous = collections.defaultdict(set)
        is_end = False
        visited = set([beginWord])
        while stack and not is_end:
            new_stack = set()
            local_visited = set()
            for word in stack:
                if word == endWord:
                    is_end = True
                    break
                for new_word in graph[word]:
                    if new_word in visited:
                        continue
                    local_visited.add(new_word)
                    new_stack.add(new_word)
                    previous[new_word].add(word)
            visited.update(local_visited)
            stack = new_stack

        print(previous)
        ans = []

        # both of below dfs can work
        def dfs(word, cur):
            if word == beginWord:
                cur.append(word)
                ans.append(cur[::-1])
                return
            cur.append(word)
            for next in previous[word]:
                dfs(next, cur[:])
        dfs(endWord, [])

        # def dfs(word, cur):
        #     if word == beginWord:
        #         ans.append(cur[::-1])
        #         return
        #     for next in previous[word]:
        #         cur.append(next)
        #         dfs(next, cur)
        #         cur.pop()
        # dfs(endWord, [endWord])
        return ans

    def findLadders(self, beginWord, endWord, wordList):
        if not wordList or endWord not in wordList or beginWord == endWord:
            return []

        wordList = set(wordList)
        wordList.add(beginWord)
        l = len(beginWord)
        graph = collections.defaultdict(set)
        for word in wordList:
            for i in range(l):
                for c in "abcdefghijklmnopqrstuvwxyz":
                    if c == word[i]:
                        continue
                    new_word = word[:i] + c + word[i+1:]
                    if new_word not in wordList:
                        continue
                    graph[word].add(new_word)

        bstack, estack = set([beginWord]), set([endWord])
        bvisited, evisited = set([beginWord]), set([endWord])
        flag = True
        prev = collections.defaultdict(set)
        while bstack and estack:
            if bstack.intersection(estack):
                break
            stack = bstack if flag else estack
            visited = bvisited if flag else evisited
            new_stack = set()
            local_visited = set()
            for word in stack:
                for w in graph[word]:
                    if w in visited:
                        continue
                    local_visited.add(w)
                    if flag:
                        prev[w].add(word)
                    else:
                        prev[word].add(w)
                    new_stack.add(w)
            visited.update(local_visited)
            if flag:
                bvisited = visited
                bstack = new_stack
            else:
                evisited = visited
                estack = new_stack
            flag = not flag

        print(prev)
        ans = []
        def dfs(word, cur):
            if word == beginWord:
                ans.append(cur[::-1])
                return
            for w in prev[word]:
                cur.append(w)
                dfs(w, cur)
                cur.pop()
        dfs(endWord, [endWord])
        return ans