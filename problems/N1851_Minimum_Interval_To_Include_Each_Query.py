import bisect
import collections
import heapq
from typing import List


class Solution:
    def minInterval_TLE(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort(key=lambda x : x[1] - x[0] + 1)
        length = len(queries)
        mapping = collections.defaultdict(list)
        for i, q in enumerate(queries):
            mapping[q].append(i)
        queries = list(set(queries))
        queries.sort()
        res = [-1] * length
        for u, v in intervals:
            l = bisect.bisect_left(queries, u)
            if l == length:
                continue
            r = bisect.bisect_left(queries, v)
            if r == len(queries) or queries[r] != v:
                r -= 1
            for i in range(l, r+1):
                for j in mapping[queries[i]]:
                    if res[j] == -1:
                        res[j] = v - u + 1
            queries = queries[:l] + queries[r+1:]
        return res

    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        length, l = len(queries), len(intervals)
        queries = [(queries[i], i) for i in range(length)]
        queries.sort()
        intervals.sort()
        pq = []
        res = [-1] * length
        i = 0
        for q, index in queries:
            while pq and pq[0][1] < q:
                heapq.heappop(pq)

            while i < l and intervals[i][0] <= q:
                if intervals[i][1] >= q:
                    d = intervals[i][1] - intervals[i][0] + 1
                    heapq.heappush(pq, (d, intervals[i][1]))
                i += 1
            if pq:
                res[index] = pq[0][0]
        return res
