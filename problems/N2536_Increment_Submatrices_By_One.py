from typing import List


class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        res = [[0] * n for _ in range(n)]
        for que in queries:
            rl, cl, rr, cr = que
            for r in range(rl, rr + 1):
                res[r][cl] += 1
                if cr + 1 < n:
                    res[r][cr+1] -= 1
        for r in range(n):
            for i in range(1, n):
                res[r][i] += res[r][i-1]
        return res

