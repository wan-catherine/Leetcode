class Solution(object):
    def findDiagonalOrder_slow(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix or not matrix[0]:
            return []
        rows, cols = len(matrix), len(matrix[0])

        res = []
        for index in range(rows+cols-1):
            if index % 2:
                for i in range(index+1):
                    if i >= rows or index - i >= cols:
                        continue
                    res.append(matrix[i][index-i])
            else:
                for i in range(index, -1, -1):
                    if i >= rows or index - i >= cols:
                        continue
                    res.append(matrix[i][index - i])
        return res

    def findDiagonalOrder(self, matrix):
        if not matrix or not matrix[0]:
            return []
        rows, cols = len(matrix), len(matrix[0])

        res = []
        for index in range(rows + cols - 1):
            diag = []
            #This is the key part!!!
            r = 0 if index < cols else index - cols + 1
            c = index if index < cols else cols - 1
            while r < rows and c >= 0:
                diag.append(matrix[r][c])
                r += 1
                c -= 1
            if index % 2:
                res.extend(diag)
            else:
                res.extend(diag[::-1])
        return res
