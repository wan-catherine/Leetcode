class Solution:
    cols = {}
    diaone = {}
    diasecond = {}

    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.init(n)
        res = []
        self.getQueens(0, n, res)
        return len(res)

    def init(self,n):
        self.cols = {i:True for i in range(n)}
        self.diaone = {i:True for i in range(2*n - 1)}
        self.diasecond = {i: True for i in range(2 * n - 1)}

    def getQueens(self, row, n, res):
        if row == n:
            res.append(1)
            return

        for i in range(n):
            if self.canPut(i, row, n):
                self.update(i, row, n, res, False)
                self.getQueens(row+1, n , res)
                self.update(i, row, n, res, True)

    def canPut(self, col, row, n):

        return self.cols[col] and self.diaone[col + row] and self.diasecond[row - col + n - 1]

    def update(self, col, row, n, res, isPut):
        self.cols[col] = isPut
        self.diaone[col + row] = isPut
        self.diasecond[row - col + n - 1] = isPut

    def totalNQueens(self, n: int) -> int:
        grid = [[0] * n for _ in range(n)]
        res = 0

        def check(row, col):
            if grid[row][col]:
                return False
            for r in range(n):
                if grid[r][col]:
                    return False
            for c in range(n):
                if grid[row][c]:
                    return False
            directions = [(1, 1), (1, -1), (-1, -1), (-1, 1)]
            for i, j in directions:
                r, c = row, col
                while r >= 0 and r < n and c >= 0 and c < n:
                    if grid[r][c]:
                        return False
                    r += i
                    c += j
            return True

        def dfs(index):
            nonlocal res
            if index == n:
                res += 1
                return
            for c in range(n):
                if not check(index, c):
                    continue
                grid[index][c] = 1
                dfs(index + 1)
                grid[index][c] = 0

        dfs(0)
        return res