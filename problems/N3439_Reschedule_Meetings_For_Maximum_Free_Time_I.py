from typing import List


class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        length = len(startTime)
        arr = [(startTime[i], endTime[i], i) for i in range(length)]
        arr.sort()
        res = 0
        cur = 0

        if k >= len(arr):
            return eventTime - sum((arr[i][1] - arr[i][0]) for i in range(k))

        for i in range(k):
            cur += arr[i][1] - arr[i][0]

        for i in range(k, length):
            cur += arr[i][1] - arr[i][0]
            if i + 1 < length:
                right = arr[i+1][0]
            else:
                right = eventTime
            res = max(res, right - arr[i-k][0] - cur)
            if i == k:
                left = 0
            else:
                left = arr[i-k-1][1]
            res = max(res, arr[i][1] - cur - left)
            cur -= arr[i-k][1] - arr[i-k][0]
        return res