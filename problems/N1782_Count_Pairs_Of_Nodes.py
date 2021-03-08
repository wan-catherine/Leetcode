import bisect
import collections
from typing import List


class Solution:
    def countPairs(self, n: int, edges: List[List[int]], queries: List[int]) -> List[int]:
        degrees = [0] * (n+1)
        graph = collections.defaultdict(int)
        for u, v in edges:
            degrees[u] += 1
            degrees[v] += 1
            graph[tuple(sorted((u, v)))] += 1
        res = []
        sorted_degrees = sorted(degrees)
        for query in queries:
            ans = 0
            j = n
            # get number of degrees[a] + degrees[b] > query
            for i in range(1, n+1):
                if i >= j:
                    ans += n - i
                else:
                    while i < j and sorted_degrees[i] + sorted_degrees[j] > query:
                        j -= 1
                    ans += n - j
            # remove diff number
            for u, v in graph.keys():
                if degrees[u] + degrees[v] > query >= degrees[u] + degrees[v] - graph[(u, v)]:
                    ans -= 1
            res.append(ans)
        return res

        # for u, v in edges:
        #     u, v = min(u, v), max(u, v)  here must write in one line
        # if write into two lines, then the value of u already changed
        #     u = min(u, v)
        #     v = max(u, v)


