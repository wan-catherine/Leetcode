import bisect
from typing import List


class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        length = len(events)
        starts = sorted(events, key=lambda x:x[0])
        right = [None] * length
        r = 0
        sarr = [None] * length
        for i in range(length-1, -1, -1):
            sarr[i] = starts[i][0]
            r = max(r, starts[i][2])
            right[i] = r
        ends = sorted(events, key=lambda x:(x[1], -x[2]))
        left = [None] * length
        l = 0
        earr = [None] * length
        for i in range(length):
            earr[i] = ends[i][1]
            l = max(l, ends[i][2])
            left[i] = l
        res = 0
        for i in range(length-1, -1, -1):
            s = starts[i][0]
            val = right[i]
            res = max(res, val)
            index = bisect.bisect_left(earr, s - 1)
            if index < length:
                if earr[index] == s - 1:
                    res = max(res, val + left[index])
                elif index > 0 and earr[index-1] < s:
                    res = max(res, val + left[index - 1])
        return res
