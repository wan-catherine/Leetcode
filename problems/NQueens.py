import copy
from typing import List


class Solution:
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        res =[]
        temp=["."*n for i in range(n) ]
        cols = {i:False for i in range(n)}
        diaone = {i:False for i in range(2*n - 1)}
        diasecond = {i:False for i in range(2*n - 1)}

        self.checkRow(0, n, temp, res, cols, diaone, diasecond)
        return res

    def checkRow(self, row, n, temp, res, cols, diaone, diasecond):
        if row == n:
            res.append(copy.deepcopy(temp))
            return

        for col in range(n):
            if not self.available(row, col, n, cols, diaone, diasecond):
                continue
            self.update(row, col, n, temp, cols, diaone, diasecond, True)
            self.checkRow(row+1, n, temp, res, cols, diaone, diasecond)
            self.update(row, col, n, temp, cols, diaone, diasecond, False)

    def available(self, row, col, n, cols, diaone, diasecond):
        if cols[col] or diaone[row + col] or diasecond[row - col + n - 1]:
            return False
        return True

    def update(self, row, col, n, temp, cols, diaone, diasecond, isPut):
        if isPut:
            temp[row] = temp[row][0:col] + 'Q' + temp[row][col+1:]
        else:
            temp[row] = temp[row][0:col] + '.' + temp[row][col+1:]
        cols[col] = isPut
        diaone[row + col] = isPut
        diasecond[row - col + n - 1] = isPut

    def solveNQueens(self, n: int) -> List[List[str]]:
        status = [None] * n
        res = []
        def check_diagonal(row, col):
            res = True
            for r, c in enumerate(status):
                if c is None:
                    return res
                if c + r - 1 == row + col or c - r + 1 == col - row:
                    return False
            return True

        def dfs(r):
            if r == n:
                grid = [['.'] * n for _ in range(n)]
                for r, c in enumerate(status):
                    grid[r][c] = 'Q'
                ans = [''.join(li) for li in grid]
                res.append(ans)
                return
            if r == 0:
                pre = None
            else:
                pre = status[r-1]
            for c in range(n):
                if pre is None:
                    status[r] = c
                    dfs(r+1)
                    status[r] = None
                else:
                    if c in status or not check_diagonal(r,c):
                        continue
                    status[r] = c
                    dfs(r+1)
                    status[r] = None
        dfs(0)
        return res


