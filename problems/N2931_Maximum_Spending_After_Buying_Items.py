import sys
from typing import List


class Solution:
    def maxSpending(self, values: List[List[int]]) -> int:
        rows, cols = len(values), len(values[0])
        total = rows * cols
        d = 1
        res = 0
        arr = [cols-1] * rows
        while d <= total:
            cur, idx = sys.maxsize, 0
            for i in range(rows):
                if arr[i] < 0:
                    continue
                if values[i][arr[i]] < cur:
                    cur = values[i][arr[i]]
                    idx = i
            res += d * cur
            arr[idx] -= 1
            d += 1
        return res

