from typing import List


class Solution:
    def ways(self, pizza: List[str], k: int) -> int:
        rows, cols = len(pizza), len(pizza[0])
        status = [[0]*(cols+1) for _ in range(rows+1)]
        for i in range(rows):
            for j in range(cols):
                status[i+1][j+1] = status[i][j+1] + status[i+1][j] - status[i][j] + (1 if pizza[i][j] == 'A' else 0)

        def check(lr, lc, rr, rc):
            if status[rr+1][rc+1] - status[rr+1][lc] - status[lr][rc+1] + status[lr][lc] > 0:
                return 1
            return 0

        memo = {}
        def dp(i, j, p):
            if (i, j, p) in memo:
                return memo[(i, j, p)]
            if p == 0:
                memo[(i, j, p)] = check(i, j, rows-1, cols-1)
                return memo[(i, j, p)]
            res = 0
            for ii in range(i, rows-1):
                res += dp(ii+1, j, p-1) * check(i, j, ii, cols-1)
            for jj in range(j, cols-1):
                res += dp(i, jj+1, p-1) * check(i, j, rows-1, jj)
            memo[(i, j, p)] = res
            return res
        return dp(0, 0, k-1) % (10**9+7)



