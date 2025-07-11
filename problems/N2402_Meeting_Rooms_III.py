import heapq
from typing import List


class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        used = []
        meetings.sort()
        unused = [i for i in range(n)]
        heapq.heapify(unused)
        count = [0] * n
        for s, e in meetings:
            while used and used[0][0] <= s:
                _, idx = heapq.heappop(used)
                heapq.heappush(unused, idx)
            if unused:
                idx = heapq.heappop(unused)
                heapq.heappush(used, (e, idx))
            else:
                time, idx = heapq.heappop(used)
                heapq.heappush(used, (time + e - s, idx))

            count[idx] += 1
        res, c = 0, 0
        for i in range(n):
            if c < count[i]:
                c = count[i]
                res = i
        return res