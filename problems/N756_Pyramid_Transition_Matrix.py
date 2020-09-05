import collections
import itertools
from collections import defaultdict


class Solution(object):
    def pyramidTransition(self, bottom, allowed):
        """
        :type bottom: str
        :type allowed: List[str]
        :rtype: bool
        """
        if not allowed:
            return False
        graph = collections.defaultdict(set)
        for s in allowed:
            graph[s[:2]].add(s[-1])
        return self.dfs(bottom, graph)


    def dfs(self, bottom, graph):
        length = len(bottom)
        if length == 1:
            return True
        temp = []
        for i in range(1, length):
            if bottom[i-1] + bottom[i] not in graph:
                return False
        self.get_bottoms(0, bottom, graph, temp, [])
        for s in temp:
            if self.dfs(s, graph):
                return True
        return False

    # how to create next bottom
    def get_bottoms(self,index, bottom, graph, res, temp):
        if index == len(bottom) - 1:
            res.append(''.join(temp))
            return

        for s in graph[bottom[index:index+2]]:
            temp.append(s)
            self.get_bottoms(index+1, bottom, graph, res, temp)
            temp.pop()

    def pyramidTransition(self, bottom, allowed):
        f = collections.defaultdict(lambda: defaultdict(list))
        for a, b, c in allowed: f[a][b].append(c)

        def pyramid(bottom):
            if len(bottom) == 1: return True
            # a pythonic way to create next bottom
            for i in itertools.product(*(f[a][b] for a, b in zip(bottom, bottom[1:]))):
                if pyramid(i): return True
            return False

        return pyramid(bottom)