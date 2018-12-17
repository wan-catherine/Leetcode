class Solution:
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if matrix == None or len(matrix) == 0:
            return 0

        rows = len(matrix)
        cols = len(matrix[0])

        cache = [[0] * cols for i in range(rows)]

        max = 0
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == '0':
                    cache[i][j] = 0
                elif i == 0 or j == 0:
                    cache[i][j] = int(matrix[i][j])
                else:
                    temp = min(cache[i-1][j], cache[i][j-1], cache[i-1][j-1])
                    cache[i][j] = int(matrix[i][j]) + temp
                if cache[i][j] > max:
                    max = cache[i][j]

        return max * max


