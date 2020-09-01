class Solution(object):
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        rows, cols = len(matrix), len(matrix[0])
        stack = []
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j]:
                    continue
                stack.append((i,j))

        res = [[0]*cols for _ in range(rows)]
        visited = [[0]*cols for _ in range(rows)]
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        count = 0
        while stack:
            new_stack = []
            for row, col in stack:
                if visited[row][col] != 2:
                    visited[row][col] = 2
                    res[row][col] = count
                for i, j in directions:
                    new_row, new_col = i+row, j+col
                    if new_row < 0 or new_row >= rows or new_col < 0 or new_col >= cols:
                        continue
                    if visited[new_row][new_col]:
                        continue
                    visited[new_row][new_col] = 1
                    new_stack.append((new_row, new_col))
            count += 1
            stack = new_stack
        # print(res)
        return res
