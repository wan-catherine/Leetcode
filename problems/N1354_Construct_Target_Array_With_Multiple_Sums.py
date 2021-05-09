import heapq
from typing import List


class Solution:
    def isPossible(self, target: List[int]) -> bool:
        total = sum(target)
        pq = [-i for i in target]
        heapq.heapify(pq)
        while pq and abs(pq[0]) != 1:
            v = -heapq.heappop(pq)
            other = total - v
            if not other or v <= other:
                return False
            # prev = v - other
            # but if we write this way , test case [1,1000000000] will TLE
            # it can write v % other
            pre = v % other
            heapq.heappush(pq, -pre)
            total = other + pre
        return True