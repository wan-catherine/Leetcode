import heapq
import math
from typing import List


class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        m = len(quantities)
        maximum = max(quantities)
        if m == n:
            return maximum
        if sum(quantities) < n:
            return 1
        def check(num):
            ans = 0
            for q in quantities:
                ans += math.ceil(q / num)
            if ans <= n:
                return True
            return False
        l, r = 0, maximum
        while l < r:
            mid = (r - l) // 2 + l
            if check(mid):
                r = mid
            else:
                l = mid + 1
        return l



