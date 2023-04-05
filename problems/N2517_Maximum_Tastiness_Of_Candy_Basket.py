import heapq
import sys
from typing import List


class Solution:
    def maximumTastiness(self, price: List[int], k: int) -> int:
        sp = sorted(set(price))
        length = len(sp)
        if length < k:
            return 0

        def check(m):
            count = 1
            cur = 0
            for i in range(1, length):
                if sp[i] - sp[cur] < m:
                    continue
                count += 1
                cur = i
            if count >= k:
                return True
            return False

        l, r = 0, sp[-1] - sp[0]
        while l < r:
            m = (r - l + 1) // 2 + l
            if check(m):
                l = m
            else:
                r = m - 1
        return l