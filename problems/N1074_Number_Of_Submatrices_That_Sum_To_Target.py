import collections
from typing import List

"""
flatten matrix
"""

class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        rows, cols = len(matrix), len(matrix[0])
        res = 0
        for index in range(rows):
            arr = [0] * cols
            for row in range(index, rows):
                for c in range(cols):
                    arr[c] += matrix[row][c]
                prefix = arr[:]
                if prefix[0] == target:
                    res += 1
                values = collections.defaultdict(int)
                values[prefix[0]] = 1
                for i in range(1, cols):
                    prefix[i] += prefix[i-1]
                    if prefix[i] == target:
                        res += 1
                    if prefix[i] - target in values:
                        res += values[prefix[i] - target]
                    values[prefix[i]] += 1
        return res
