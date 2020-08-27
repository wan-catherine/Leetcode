class Solution(object):
    """
    check all points
    use dfs to check if this point can reach to the border.
    """
    def pacificAtlantic_slow(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        if not matrix or not matrix[0]:
            return None
        self.rows, self.cols = len(matrix), len(matrix[0])
        self.matrix = matrix
        res = []
        self.directions = [(0,-1), (-1,0),(1,0), (0,1)]
        for row in range(self.rows):
            for col in range(self.cols):
                pacific = self.dfs_slow(row, col, set(), True)
                atlantic = self.dfs_slow(row, col, set(), False)
                if pacific and atlantic:
                    res.append([row, col])
        return res

    def dfs_slow(self, row, col, visited, is_pacific):
        if is_pacific and (row == 0 or col == 0):
            return True
        if not is_pacific and (row == self.rows - 1 or col == self.cols - 1):
            return True
        visited.add((row,col))
        for i, j in self.directions:
            new_row, new_col = row + i, col + j
            if new_row < 0 or new_row >= self.rows or new_col < 0 or new_col >= self.cols:
                continue
            if self.matrix[new_row][new_col] > self.matrix[row][col]:
                continue
            if (new_row, new_col) in visited:
                continue
            if self.dfs(new_row, new_col, visited, is_pacific):
                return True
        return False

    def pacificAtlantic(self, matrix):
        if not matrix or not matrix[0]:
            return None
        self.rows, self.cols = len(matrix), len(matrix[0])
        self.matrix = matrix
        p_visited = [[0]*self.cols for _ in range(self.rows)]
        a_visited = [[0] * self.cols for _ in range(self.rows)]
        self.directions = [(0,-1), (-1,0),(1,0), (0,1)]
        for i in range(self.rows):
            self.dfs(i, 0, p_visited)
            self.dfs(i, self.cols-1, a_visited)

        for i in range(self.cols):
            self.dfs(0, i, p_visited)
            self.dfs(self.rows-1, i, a_visited)

        res = []
        for i in range(self.rows):
            for j in range(self.cols):
                if p_visited[i][j] and a_visited[i][j]:
                    res.append([i,j])
        return res

    def dfs(self, row, col, visited):
        visited[row][col] = 1
        for i, j in self.directions:
            new_row, new_col = row + i, col + j
            if new_row < 0 or new_row >= self.rows or new_col < 0 or new_col >= self.cols or self.matrix[row][col] > self.matrix[new_row][new_col]:
                continue
            if visited[new_row][new_col]:
                continue
            self.dfs(new_row, new_col, visited)

