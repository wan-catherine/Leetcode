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

