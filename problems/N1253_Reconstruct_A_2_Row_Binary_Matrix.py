class Solution(object):
    def reconstructMatrix(self, upper, lower, colsum):
        """
        :type upper: int
        :type lower: int
        :type colsum: List[int]
        :rtype: List[List[int]]
        """
        row = 0
        count = 0
        for i in colsum:
            if i == 2:
                row += 1
            if i == 1:
                count += 1

        if upper - row + lower - row != count:
            return []

        length = len(colsum)
        res = [[0] * length for _ in range(2)]

        row1, row2 = upper - row, lower - row
        for i in range(length):
            if colsum[i] == 2:
                res[0][i], res[1][i] = 1, 1
            elif colsum[i] == 0:
                res[0][i], res[1][i] = 0, 0
            else:
                if row1 > 0:
                    res[0][i] = 1
                    row1 -= 1
                else:
                    res[1][i] = 1
                    row2 -= 1
        if row1 or row2:
            return []
        return res
