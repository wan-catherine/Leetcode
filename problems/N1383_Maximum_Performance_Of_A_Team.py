import heapq
from typing import List


class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        se = []
        for i in range(n):
            se.append((efficiency[i], speed[i]))
        se.sort(reverse=True)
        cur, res, pq = 0, 0, []
        for e, s in se:
            heapq.heappush(pq, s)
            cur += s
            if len(pq) > k:
                cur -= heapq.heappop(pq)
            res = max(res, e * cur)
        return res % (10 ** 9 + 7)
