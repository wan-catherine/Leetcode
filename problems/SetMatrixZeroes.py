class Solution:
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        if matrix == None or len(matrix) == 0 or len(matrix[0]) == 0:
            return

        rows = len(matrix)
        cols = len(matrix[0])

        lr = [1] * rows
        lc = [1] * cols

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    lr[i] = 0;
                    break;

        for i in range(cols):
            for j in range(rows):
                if matrix[j][i] == 0:
                    lc[i] = 0;
                    break;

        for i in range(len(lr)):
            if lr[i] == 0:
                for c in range(cols):
                    matrix[i][c] = 0

        for i in range(len(lc)):
            if lc[i] == 0:
                for c in range(rows):
                    matrix[c][i] = 0




