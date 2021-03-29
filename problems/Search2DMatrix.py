class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        rows, cols = len(matrix), len(matrix[0])
        i = 0
        while i < rows:
            if target == matrix[i][0]:
                return True
            if target > matrix[i][0]:
                index = bisect.bisect_left(matrix[i], target)
                if index < cols and matrix[i][index] == target:
                    return True
                i += 1
            elif target < matrix[i][0]:
                break
        return False

