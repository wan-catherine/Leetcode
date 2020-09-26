class Solution(object):
    def matrixBlockSum(self, mat, k):
        """
        :type mat: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        rows, cols = len(mat), len(mat[0])
        for i in range(1, cols):
            mat[0][i] += mat[0][i-1]

        for i in range(1, rows):
            mat[i][0] += mat[i-1][0]

        for i in range(1, rows):
            for j in range(1, cols):
                mat[i][j] += mat[i-1][j] + mat[i][j-1] - mat[i-1][j-1]

        grid = [[0]*cols for _ in range(rows)]
        for i in range(rows):
            for j in range(cols):
                b_r_r = i + k if i + k < rows else rows - 1
                b_r_c = j + k if j + k < cols else cols - 1
                grid[i][j] = mat[b_r_r][b_r_c]
                if i - k - 1 >= 0:
                    grid[i][j] -= mat[i-k-1][b_r_c]
                if j - k - 1 >= 0:
                    grid[i][j] -= mat[b_r_r][j-k-1]
                if i - k - 1 >= 0 and j - k - 1 >= 0:
                    grid[i][j] += mat[i-k-1][j-k-1]
        return grid
