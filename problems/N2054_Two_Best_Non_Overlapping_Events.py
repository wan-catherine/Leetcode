import bisect
from typing import List


class Solution:
    def maxTwoEvents_2021(self, events: List[List[int]]) -> int:
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

    def maxTwoEvents(self, events: List[List[int]]) -> int:
        events.sort(key=lambda x: (x[1], -x[2]))
        arr = []
        cur = 0
        for a, b, v in events:
            cur = max(cur, v)
            arr.append((b, cur))
        li = []
        res = 0
        for i in range(len(events)):
            a, b, c = events[i]
            res = max(res, c)
            idx = bisect.bisect_left(li, a - 1)
            if idx == 0 and (len(li) == 0 or li[idx] != a - 1):
                li.append(b)
                continue
            if idx == len(li) :
                idx = len(li) - 1
            elif li[idx] != a - 1:
                idx -= 1
            res = max(res, arr[idx][1] + c)
            li.append(b)
        return res


