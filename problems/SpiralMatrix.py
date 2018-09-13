class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if matrix == None or len(matrix) < 1:
            return []

        rows = len(matrix)
        columns = len(matrix[0])

        if rows == 1:
            return matrix[0]

        res = []
        if columns == 1:
            for l in matrix:
                res.append(l[0])
            return res
        self.oneCycle(res, rows, columns, matrix, 0)

        return res


    def oneCycle(self, res, m, n, matrix, round):
        if m <= 0 or n <= 0:
            return

        if m == 1:
            for i in range(n):
                res.append(matrix[round][i + round])
            return
        if n == 1:
            for i in range(m):
                res.append(matrix[round + i][round])
            return

        for i in range(n):
            res.append(matrix[round][i + round])

        for j in range(1, m - 1):
            res.append(matrix[j + round][n - 1 + round])

        for k in range(n - 1,-1,-1):
            res.append(matrix[m - 1 + round][k + round])

        for v in range(m - 2, 0, -1):
            res.append(matrix[v + round][round])

        round += 1
        m -= 2
        n -= 2
        self.oneCycle(res, m, n, matrix, round)






