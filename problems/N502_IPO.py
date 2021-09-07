import heapq
from typing import List


class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        pq = []
        res, length = w, len(profits)
        caps = [(capital[i], i) for i in range(length)]
        caps.sort(key=lambda x:x[0])
        i = 0
        while k > 0:
            while i < length and caps[i][0] <= res:
                idx = caps[i][1]
                heapq.heappush(pq, -profits[idx])
                i += 1
            if not pq:
                break
            res -= heapq.heappop(pq)
            k -= 1
        return res
