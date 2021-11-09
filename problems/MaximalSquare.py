from typing import List


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
                    print(max, i, j)

        return max * max

    """
    Similar as leetcode 85. 
    Here we use non-decreasing stack. 
    each time when we pop out , it's the lowest number amount [index:cur]
    """
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        arr = [0] * (cols + 2)
        res = 0
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == "1":
                    arr[c + 1] += 1
                else:
                    arr[c + 1] = 0
            stack = []
            for i in range(cols + 2):
                while stack and arr[stack[-1]] > arr[i]:
                    index = stack.pop()
                    res = max(res, min(arr[index], i - stack[-1] - 1))
                stack.append(i)
        return res ** 2





