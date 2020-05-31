class Solution:
    def maximalRectangle_before(self, matrix):
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

    def maximalRectangle(self, matrix):
        if matrix == None or len(matrix) == 0 or len(matrix[0]) == 0:
            return 0

        col_len = len(matrix[0])

        res = 0
        temp_row = [0] * (col_len + 2)
        for row in matrix:
            for i in range(col_len):
                if row[i] == "0":
                    temp_row[i+1] = 0
                else:
                    temp_row[i+1] += int(row[i])
            # monotonic stack non-decreasing
            stack = []
            for index, value in enumerate(temp_row):
                while stack and temp_row[stack[-1]] > value:
                    cur = stack.pop()
                    left_index = stack[-1]
                    res = max(res, temp_row[cur]*(index-left_index-1))
                stack.append(index)
        return res