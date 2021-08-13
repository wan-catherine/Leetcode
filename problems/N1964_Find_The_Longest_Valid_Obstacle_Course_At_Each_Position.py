import bisect
import collections
from typing import List


class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        length = len(obstacles)
        arr, res = [obstacles[0]], [1]*length
        for i in range(1, length):
            index = bisect.bisect(arr, obstacles[i])
            if index >= len(arr):
                arr.append(obstacles[i])
            else:
                arr[index] = obstacles[i]
            res[i] = max(res[i], index + 1)
        return res


