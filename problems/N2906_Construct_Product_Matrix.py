from typing import List


class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        row, col = len(grid), len(grid[0])
        zero = 0
        idx = None
        res = [[0] * col for _ in range(row)]
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 0 or grid[i][j] % 12345 == 0:
                    zero += 1
                    idx = [i, j]
        if zero >= 2:
            return res

        rr = []
        total = 1
        for i in range(row):
            cur = 1
            for j in range(col):
                if idx and idx == [i, j]:
                    continue
                cur *= grid[i][j]
            rr.append(cur)
            total *= cur
        if not idx:
            for i in range(row):
                for j in range(col):
                    res[i][j] = total // grid[i][j] % 12345
        else:
            res[idx[0]][idx[1]] = total % 12345
        return res