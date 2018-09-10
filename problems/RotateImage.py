import math
class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix[0])

        for i in range(math.ceil(n / 2)):
            for j in range(i,n-i-1):
                matrix[i][j],matrix[j][n-1-i],matrix[n-1-i][n-1-j],matrix[n-1-j][i] = matrix[n-1-j][i],matrix[i][j], matrix[j][n-1-i],matrix[n-1-i][n-1-j]

