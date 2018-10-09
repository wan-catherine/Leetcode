class Solution:
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if matrix == None or len(matrix) == 0 or len(matrix[0]) == 0:
            return 0

        row = len(matrix)
        col = len(matrix[0])

        length = row if row > col else col
        base = [0] * length
        res = 0
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == "0":
                    base[j] = 0
                else:
                    base[j] += int(matrix[i][j])
            temp = self.getRec(base.copy())
            res = temp if temp > res else res
        return res

    def getRec(self, heights):
        indexes = []
        i = 0
        res = 0
        length = len(heights)
        heights.append(-1)
        while True:
            if i < length and (len(indexes) == 0 or heights[i] >= heights[indexes[-1]]):
                indexes.append(i)
                i += 1
            else:
                while len(indexes) > 0 and heights[indexes[-1]] > heights[i]:
                    index = indexes.pop()
                    if len(indexes) > 0:
                        temp = (i - indexes[-1] - 1) * heights[index]
                    else:
                        temp = i * heights[index]
                    res = temp if temp > res else res
            if i < length and len(indexes) == 0:
                heights[i - 1] = heights[i]
                indexes.append(i - 1)
            if i == length and len(indexes) == 0:
                break
        return res