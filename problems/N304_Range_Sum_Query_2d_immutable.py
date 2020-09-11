class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        self.flag = True
        if not matrix or not matrix[0]:
            self.flag = False
            return
        self.rows, self.cols = len(matrix), len(matrix[0])
        self.sum_matrix = [[0] * self.cols for _ in range(self.rows)]
        self.sum_matrix[0][0] = matrix[0][0]
        for row in range(1,self.rows):
            self.sum_matrix[row][0] = matrix[row][0] + self.sum_matrix[row-1][0]
        for col in range(1, self.cols):
            self.sum_matrix[0][col] = matrix[0][col] + self.sum_matrix[0][col-1]
        for row in range(1, self.rows):
            for col in range(1, self.cols):
                self.sum_matrix[row][col] = matrix[row][col] + self.sum_matrix[row-1][col] + self.sum_matrix[row][col-1] - self.sum_matrix[row-1][col-1]
        # print(self.sum_matrix)

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        if not self.flag or row1 < 0 or col1 < 0 or row2 >= self.rows or col2 >= self.cols:
            return
        row_up, col_up = row1 - 1, col2
        row_overlap, col_overlap = row1 - 1, col1 - 1
        row_left, col_left = row2, col1 - 1
        res = self.sum_matrix[row2][col2]
        if row1 >= 1:
            res -= self.sum_matrix[row_up][col_up]
        if col1 >= 1:
            res -= self.sum_matrix[row_left][col_left]
        if row1 >= 1 and col1 >= 1:
            res += self.sum_matrix[row_overlap][col_overlap]
        return res

# Your NumMatrix object will be instantiated and called as such:
matrix = [
  [3, 0, 1, 4, 2],
  [5, 6, 3, 2, 1],
  [1, 2, 0, 1, 5],
  [4, 1, 0, 1, 7],
  [1, 0, 3, 0, 5]
]
matrix = [[]]
obj = NumMatrix(matrix)
param_1 = obj.sumRegion(2, 1, 4, 3)
print(param_1)
param_1 = obj.sumRegion(1, 1, 2, 2)
print(param_1)
param_1 = obj.sumRegion(1, 2, 2, 4)
print(param_1)