import bisect
from typing import List


class Solution:
    def maxFreeTime(self, eventTime: int, startTime: List[int], endTime: List[int]) -> int:
        length = len(startTime)
        arr = [(startTime[i], endTime[i], i+1) for i in range(length)]
        arr.sort()
        arr = [(0,0,0)] + arr + [(eventTime,eventTime, length+1)]
        pq = []
        res = 0
        for i in range(length+1):
            res = max(res, arr[i+1][0] - arr[i][1])
            bisect.insort_left(pq, (arr[i+1][0] - arr[i][1], i))

        for i in range(length):
            le = arr[i+1][1] - arr[i+1][0]
            if (pq[-1][0] >= le and pq[-1][1] not in (i, i+1)) or (pq[-2][0] >= le and pq[-2][1] not in (i, i+1)):
                res = max(res, arr[i+2][0] - arr[i][1])
                continue
            if len(pq) > 2 and pq[-3][0] >= le:
                res = max(res, arr[i+2][0] - arr[i][1])
            else:
                res = max(res, arr[i+2][0] - arr[i][1] - le)
        return res
