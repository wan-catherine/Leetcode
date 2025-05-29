import collections
from typing import List

'''
Key point: 
    no matter loop from which node, the number of even/odd will keep same.
    So we can only loop both of trees just one time.
'''
class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]]) -> List[int]:
        fl, sl = len(edges1) + 1, len(edges2) + 1
        fg, sg = collections.defaultdict(list), collections.defaultdict(list)
        for u, v in edges1:
            fg[u].append(v)
            fg[v].append(u)
        for u, v in edges2:
            sg[u].append(v)
            sg[v].append(u)

        def bfs(graph, length):
            arr = [False] * length
            nodes = [(0,-1,0)]

            while nodes:
                nnodes = []
                for cur, parent, level in nodes:
                    if level % 2 == 0:
                        arr[cur] = True
                    for nxt in graph[cur]:
                        if nxt == parent:
                            continue
                        nnodes.append((nxt, cur, level + 1))
                nodes = nnodes
            return arr

        farr, barr = bfs(fg, fl), bfs(sg, sl)
        odd, even = 0, 0
        for c in barr:
            if c == True:
                even += 1
            else:
                odd += 1
        val = max(odd, even)
        odd, even = 0, 0
        for c in farr:
            if c == True:
                even += 1
            else:
                odd += 1
        res = []
        for c in farr:
            if c == True:
                res.append(even + val)
            else:
                res.append(odd + val)
        return res

