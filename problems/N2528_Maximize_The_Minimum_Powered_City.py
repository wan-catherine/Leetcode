import bisect
import sys
from typing import List


class Solution:
    def maxPower(self, stations: List[int], r: int, k: int) -> int:
        length = len(stations)
        def check(m, k):
            arr = stations[:]
            cur = sum(arr[:r])
            for i in range(length):
                if i + r < length:
                    cur += arr[i + r]
                if i - r - 1 >= 0:
                    cur -= arr[i-r-1]
                if cur >= m:
                    continue
                diff = m - cur
                if diff > k:
                    return False
                cur = m
                arr[min(length-1, i+r)] += diff
                k -= diff
            return True

        l, rr = 0, sys.maxsize
        while l < rr:
            m = (rr - l + 1) // 2 + l
            if check(m, k):
                l = m
            else:
                rr = m - 1
        return l
