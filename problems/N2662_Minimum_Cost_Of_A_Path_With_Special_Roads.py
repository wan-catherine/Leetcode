import heapq
from typing import List


class Solution:
    def minimumCost(self, start: List[int], target: List[int], specialRoads: List[List[int]]) -> int:
        dist = {}
        pq = []
        heapq.heappush(pq, (0, (start[0], start[1])))
        for _, _, x, y, _ in specialRoads:
            heapq.heappush(pq, (abs(start[0] - x) + abs(start[1] - y), (x, y)))
        res = target[0] - start[0] + target[1] - start[1]
        while pq:
            l, li = heapq.heappop(pq)
            x, y = li
            if (x, y) in dist:
                continue
            dist[(x, y)] = l
            res = min(res, l + abs(target[0] - x) + abs(target[1] - y))
            for i, j, p, q, s in specialRoads:
                if (p, q) not in dist:
                    heapq.heappush(pq, (abs(i-x) + abs(y-j) + s + l, (p, q)))
        return res