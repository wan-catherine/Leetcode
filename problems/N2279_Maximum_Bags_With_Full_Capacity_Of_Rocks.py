import bisect
from typing import List


class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        res = 0
        length = len(capacity)
        require, li = 0, []
        for i in range(length):
            if capacity[i] == rocks[i]:
                res += 1
            else:
                val = capacity[i] - rocks[i]
                require += val
                bisect.insort_left(li, val)
        if additionalRocks >= require:
            return length
        i = 0
        while i < len(li) and additionalRocks >= li[i]:
            additionalRocks -= li[i]
            res += 1
            i += 1
        return res

