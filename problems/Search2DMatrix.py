class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if matrix == None or len(matrix) == 0 or len(matrix[0]) == 0:
            return False

        i = 0
        while i < len(matrix):
            if matrix[i][0] == target:
                return True
            elif matrix[i][0] > target:
                break
            else:
                i += 1
        if i < 1:
            return False

        j = 0
        while j < len(matrix[0]):
            if matrix[i - 1][j] == target:
                return True
            elif matrix[i - 1][j] < target:
                j += 1
            else:
                break
        return False

