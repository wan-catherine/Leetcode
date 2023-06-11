import collections
import heapq
from typing import List


class Solution:
    def findScore(self, nums: List[int]) -> int:
        length = len(nums)
        pq = []
        for i in range(length):
            heapq.heappush(pq, (nums[i], i))
        marked = [0] * length
        res = 0
        while pq:
            n, idx = heapq.heappop(pq)
            if marked[idx]:
                continue
            marked[idx] = 1
            res += n
            if idx > 0:
                marked[idx - 1] = 1
            if idx < length - 1:
                marked[idx + 1] = 1
        return res
