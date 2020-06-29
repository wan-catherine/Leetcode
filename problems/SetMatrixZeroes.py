class Solution:
    def setZeroes_before(self, matrix):
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

    """
    use first row/col to same the zero information. 
    Before that, need to check if the first row/col themselves need to change 
    """
    def setZeroes(self, matrix):
        if not matrix or not matrix[0]:
            return

        col_zero = False
        row_zero = False

        rows = len(matrix)
        cols = len(matrix[0])

        for row in range(rows):
            if matrix[row][0] == 0:
                col_zero = True
                break

        for col in range(cols):
            if matrix[0][col] == 0:
                row_zero = True
                break

        for row in range(1, rows):
            for col in range(1, cols):
                if matrix[row][col] == 0:
                    matrix[row][0], matrix[0][col] = 0, 0

        for row in range(1,rows):
            if matrix[row][0] == 0:
                for c in range(cols):
                    matrix[row][c] = 0

        for col in range(1,cols):
            if matrix[0][col] == 0:
                for r in range(rows):
                    matrix[r][col] = 0

        if row_zero:
            for col in range(cols):
                matrix[0][col] = 0
        if col_zero:
            for row in range(rows):
                matrix[row][0] = 0

        return matrix




