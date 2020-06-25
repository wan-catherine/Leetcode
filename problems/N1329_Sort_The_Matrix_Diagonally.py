import collections


class Solution(object):
    def diagonalSort(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        rows = len(mat)
        cols = len(mat[0])
        mapping = collections.defaultdict(list)
        for row in range(rows):
            for col in range(cols):
                mapping[row-col].append(mat[row][col])

        for key in mapping:
            mapping[key].sort()

        for row in range(rows):
            for col in range(cols):
                mat[row][col] = mapping[row-col][0]
                del mapping[row-col][0]
        return mat


