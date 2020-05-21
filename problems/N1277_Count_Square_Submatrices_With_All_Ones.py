class Solution(object):
    def countSquares(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        if not matrix:
            return 0
        row_len = len(matrix)
        col_len = len(matrix[0])
        dp_table = [[None]*col_len for i in range(row_len)]

        res = 0
        for i in range(col_len):
            dp_table[0][i] = matrix[0][i]
            res += dp_table[0][i]

        for i in range(1, row_len):
            dp_table[i][0] = matrix[i][0]
            res += dp_table[i][0]


        for i in range(1, row_len):
            for j in range(1, col_len):
                if 0 in [matrix[i][j], matrix[i][j-1], matrix[i-1][j-1], matrix[i-1][j]]:
                    dp_table[i][j] = matrix[i][j]
                else:
                    dp_table[i][j] = matrix[i][j] + min(dp_table[i][j-1], dp_table[i-1][j-1], dp_table[i-1][j])
                res += dp_table[i][j]
        print(dp_table)
        return res


