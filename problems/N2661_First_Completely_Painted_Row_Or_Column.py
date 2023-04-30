from typing import List


class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        rows, cols = [0] * n, [0] * m
        mapping = {}
        for i in range(m):
            for j in range(n):
                mapping[mat[i][j]] = (i, j)

        for i, a in enumerate(arr):
            r, c = mapping[a]
            cols[r] += 1
            if cols[r] == n:
                return i
            rows[c] += 1
            if rows[c] == m:
                return i

