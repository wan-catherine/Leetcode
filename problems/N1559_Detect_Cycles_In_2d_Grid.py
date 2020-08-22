class Solution(object):
    def containsCycle(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: bool
        """
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0])

        self.visited = [[0]*self.cols for _ in range(self.rows)]
        self.directions = [[1,0],[-1,0],[0,1],[0,-1]]

        for i in range(self.rows):
            for j in range(self.cols):
                if self.visited[i][j]:
                    continue
                if self.dfs(i, j, -1, -1):
                    return True
        return False

    def dfs_(self, row, col, p_row, p_col):
        if self.visited[row][col]:
            return True
        self.visited[row][col] = 1
        for i, j in self.directions:
            new_row, new_col = row + i, col + j
            if new_row >= self.rows or new_col >= self.cols or new_row < 0 or new_col < 0:
                continue
            if self.grid[new_row][new_col] != self.grid[row][col]:
                continue
            if new_row == p_row and new_col == p_col:
                continue
            if self.dfs(new_row, new_col, row, col):
                return True
        # self.visited[row][col] = 0  we don't need to reset this .
        return False