class Solution(object):
    def largestSubmatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        rows, cols = len(matrix), len(matrix[0])
        status = [[0] * cols for _ in range(rows)]
        for j in range(cols):
            status[0][j] = matrix[0][j]
            for i in range(1, rows):
                if matrix[i][j] == 0:
                    continue
                status[i][j] = status[i-1][j] + 1
        for i in range(rows):
            status[i].sort(reverse=True)

        res = 0
        for i in range(rows):
            for j in range(cols):
                if status[i][j] == 0:
                    continue
                cur = (j+1) * status[i][j]
                res = max(res, cur)
        return res
