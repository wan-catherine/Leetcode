import collections
from typing import List


class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        length = len(colors)
        graph = collections.defaultdict(set)
        indegrees = [0] * length
        for u, v in edges:
            graph[u].add(v)
            indegrees[v] += 1
        zero = [i for i in range(length) if indegrees[i] == 0]
        c = set([ord(a) - ord('a') for a in colors])
        res = 1
        for i in range(26):
            if i not in c:
                continue
            inde = indegrees[:]
            zeros = zero[:]
            nodes = len(zeros)
            # here is the key point
            # when we arrive node , the largest count of i is count[node]
            count = [0] * length
            for z in zeros:
                if ord(colors[z]) - ord('a') == i:
                    count[z] = 1

            while zeros:
                new_zeros = []
                for node in zeros:
                    for nxt in graph[node]:
                        clr = ord(colors[nxt]) - ord('a')
                        count[nxt] = max(count[nxt], count[node] + (1 if clr == i else 0))
                        res = max(res, count[nxt])
                        inde[nxt] -= 1
                        if inde[nxt] == 0:
                            nodes += 1
                            new_zeros.append(nxt)
                zeros = new_zeros
            if nodes != length:
                return -1
        return res


