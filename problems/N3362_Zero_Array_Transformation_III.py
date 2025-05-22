import collections
import heapq
from typing import List


class Solution:
    def maxRemoval(self, nums: List[int], queries: List[List[int]]) -> int:
        ln, lq = len(nums), len(queries)
        queries.sort()
        maxpq, minpq = [], []
        j = 0
        for i in range(ln):
            while j < lq and queries[j][0] == i:
                heapq.heappush(maxpq, -queries[j][1])
                j += 1
            while nums[i] > len(minpq) and maxpq and -maxpq[0] >= i:
                v = heapq.heappop(maxpq)
                heapq.heappush(minpq, -v)
            if nums[i] > len(minpq):
                return -1
            while minpq and minpq[0] <= i:
                heapq.heappop(minpq)
        return len(maxpq)
