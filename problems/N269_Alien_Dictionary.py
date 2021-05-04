import collections
from typing import List


class Solution:
    def alienOrder(self, words: List[str]) -> str:
        graph = collections.defaultdict(set)
        indegrees = collections.defaultdict(int)
        length = len(words)
        chars = set()
        for w in words:
            chars.update(set(w))
        def helper(aw, bw):
            if aw != bw and aw.startswith(bw):
                return False
            if bw.startswith(aw):
                return None
            i = 0
            while i < len(aw) and i < len(bw):
                if aw[i] == bw[i]:
                    i += 1
                else:
                    break
            return [aw[i], bw[i]]

        for i in range(1, length):
            l = helper(words[i-1], words[i])
            if l == False:
                return ""
            if l == None:
                continue
            if l[1] not in graph[l[0]]:
                graph[l[0]].add(l[1])
                indegrees[l[1]] += 1

        zero = [i for i in chars if i not in indegrees.keys()]
        res = []
        while zero:
            new_zero = []
            for i in zero:
                res.append(i)
                for nxt in graph[i]:
                    indegrees[nxt] -= 1
                    if indegrees[nxt] == 0:
                        new_zero.append(nxt)
            zero = new_zero
        if sum(indegrees.values()) != 0:
            return ""
        return ''.join(res) if len(chars) > 1 else ''.join(chars)

