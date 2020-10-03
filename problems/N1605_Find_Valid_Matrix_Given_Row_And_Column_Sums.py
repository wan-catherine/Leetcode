class Solution(object):
    def restoreMatrix(self, rowSum, colSum):
        """
        :type rowSum: List[int]
        :type colSum: List[int]
        :rtype: List[List[int]]
        """
        rows, cols = len(rowSum), len(colSum)
        i, j = 0, 0
        res = [[0]*cols for _ in range(rows)]
        while i < rows and j < cols:
            v = min(rowSum[i], colSum[j])
            res[i][j] = v
            rowSum[i] -= v
            if rowSum[i] == 0:
                i += 1
            colSum[j] -= v
            if colSum[j] == 0:
                j += 1
        return res

