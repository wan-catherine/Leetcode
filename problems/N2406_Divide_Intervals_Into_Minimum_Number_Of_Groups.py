import heapq
from typing import List


class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        res = 0
        intervals.sort()
        pq = []
        for l, r in intervals:
            if pq and pq[0] < l:
                heapq.heappop(pq)
                heapq.heappush(pq, r)
            else:
                res += 1
                heapq.heappush(pq, r)
        return res