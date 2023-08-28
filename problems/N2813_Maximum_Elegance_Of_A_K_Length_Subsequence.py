import collections
import heapq
from typing import List

"""
1. find the largest kth profit, it has t different categories 
2. Try to loop and find one which can add and becomes t + 1 categories 
"""

class Solution:
    def findMaximumElegance(self, items: List[List[int]], k: int) -> int:
        length = len(items)
        items.sort(reverse=True)
        mapping = collections.defaultdict(int)
        ps, cates = 0, 0
        pq = []
        for i in range(k):
            ps += items[i][0]
            mapping[items[i][1]] += 1
            heapq.heappush(pq, (items[i][0], items[i][1]))
        cates = len(mapping.keys())
        res = ps + cates ** 2
        for i in range(k, length):
            if items[i][1] in mapping.keys():
                continue
            while pq:
                profit, category = heapq.heappop(pq)
                if mapping[category] > 1:
                    ps -= profit
                    ps += items[i][0]
                    cates += 1
                    mapping[category] -= 1
                    mapping[items[i][1]] += 1
                    res = max(res, ps + cates ** 2)
                    break
        return res