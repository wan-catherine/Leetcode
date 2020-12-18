import math
class Solution:
    def rotate_(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix[0])

        for i in range(math.ceil(n / 2)):
            for j in range(i,n-i-1):
                matrix[i][j],matrix[j][n-1-i],matrix[n-1-i][n-1-j],matrix[n-1-j][i] = matrix[n-1-j][i],matrix[i][j], matrix[j][n-1-i],matrix[n-1-i][n-1-j]

    """
    clockwise rotate
    first reverse up to down, then swap the symmetry 
    1 2 3     7 8 9     7 4 1
    4 5 6  => 4 5 6  => 8 5 2
    7 8 9     1 2 3     9 6 3
    
    anticlockwise rotate
    first reverse left to right, then swap the symmetry
    1 2 3     3 2 1     3 6 9
    4 5 6  => 6 5 4  => 2 5 8
    7 8 9     9 8 7     1 4 7

    """
    def rotate(self, matrix) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        length = len(matrix)
        for i in range(length // 2):
            matrix[i], matrix[length - i - 1] = matrix[length - i - 1], matrix[i]

        for i in range(length):
            for j in range(i, length):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]