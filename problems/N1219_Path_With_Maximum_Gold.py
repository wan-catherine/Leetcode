class Solution(object):
    def getMaximumGold(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        self.rows, self.cols = len(grid), len(grid[0])
        res = 0
        self.directions = [(0,1),(1,0),(-1,0),(0,-1)]
        for i in range(self.rows):
            for j in range(self.cols):
                if not grid[i][j]:
                    continue
                visited = [[0] * self.cols for _ in range(self.rows)]
                res = max(res, self.dfs(i, j, grid, visited))
        return res

    def dfs(self, row, col, grid, visited):
        res = 0
        visited[row][col] = 1
        for i, j in self.directions:
            new_row, new_col = row+i, col+j
            if new_row < 0 or new_row >= self.rows or new_col < 0 or new_col >= self.cols:
                continue
            if not grid[new_row][new_col] or visited[new_row][new_col]:
                continue
            visited[new_row][new_col] = 1
            res = max(res, self.dfs(new_row, new_col, grid, visited))
            visited[new_row][new_col] = 0
        return res + grid[row][col]