import collections
import bisect
from typing import List


class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        mapping = collections.defaultdict(int)
        for k, v in items:
            if k not in mapping:
                mapping[k] = v
            elif mapping[k] < v:
                mapping[k] = v
        keys = sorted(mapping.keys())
        prev = 0
        for key in keys:
            if mapping[key] < prev:
                mapping[key] = prev
            else:
                prev = mapping[key]
        length = len(keys)
        res = []
        for i, q in enumerate(queries):
            index = bisect.bisect_left(keys, q)
            if index == length:
                res.append(mapping[keys[-1]])
            elif keys[index] == q:
                res.append(mapping[keys[index]])
            elif keys[index] > q:
                if index > 0:
                    res.append(mapping[keys[index - 1]])
                else:
                    res.append(0)
        return res
