import collections
from typing import List


class Solution:
    def countPairs(self, coordinates: List[List[int]], k: int) -> int:
        res = 0
        for t in range(k+1):
            mapping = collections.defaultdict(int)
            for x, y in coordinates:
                a, b = t ^ x, (k - t) ^ y
                idx = a * 10 ** 6 + b
                if idx in mapping:
                    res += mapping[idx]
                mapping[x * 10 ** 6 + y] += 1
        return res
