from collections import defaultdict
from typing import List

'''
Key points : how to get tree diameter 
    1. pick random node and run BFS to find the farthest node 
    2. use this node and run BFS again to get the diameter 
    3. find both graphs' diameter 
        a. pick the middle node in both diameter , then the final diameter will be the minumum
        b. if one of the graph is too large , then need to consider the diameter of it 
'''

class Solution:
    def minimumDiameterAfterMerge(self, edges1: List[List[int]], edges2: List[List[int]]) -> int:
        def treeDiameter(edges):
            graph = defaultdict(list)
            for u, v in edges:
                graph[u].append(v)
                graph[v].append(u)

            nodes = [(0,-1)]

            while nodes:
                nn = []
                for node, p in nodes:
                    for nxt in graph[node]:
                        if nxt == p:
                            continue
                        nn.append((nxt, node))
                if len(nn) == 0:
                    break
                nodes = nn
            res = 0
            nodes = [(nodes[0][0], -1)]
            while nodes:
                nn = []
                for node, p in nodes:
                    for nxt in graph[node]:
                        if nxt == p:
                            continue
                        nn.append((nxt, node))
                if len(nn) == 0:
                    break
                res += 1
                nodes = nn
            return res

        df = treeDiameter(edges1)
        ds = treeDiameter(edges2)
        return max(df, ds, (df + 1) // 2 + (ds + 1) // 2 + 1)

