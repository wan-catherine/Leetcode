import bisect
from typing import List


class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        length = len(fruits)
        pos, presum = [], [0]
        for i in range(length):
            pos.append(fruits[i][0])
            presum.append(presum[-1] + fruits[i][1])
        res = 0
        mid = bisect.bisect_left(pos, startPos)
        j = 0
        for i in range(mid, length):
            while pos[j] <= startPos and (pos[i] - startPos + 2 * (startPos - pos[j])) > k:
                j += 1
            if pos[j] <= startPos or (pos[i] - startPos) <= k:
                res = max(res, presum[i+1] - presum[j])

        mid = bisect.bisect_left(pos, startPos)
        if mid == length or pos[mid] > startPos:
            mid -= 1
        j = length - 1
        for i in range(mid, -1, -1):
            while pos[j] >= startPos and (startPos - pos[i] + 2 * (pos[j] - startPos)) > k:
                j -= 1
            if pos[j] >= startPos or (startPos - pos[i]) <= k:
                res = max(res, presum[j+1] - presum[i])
        return res
