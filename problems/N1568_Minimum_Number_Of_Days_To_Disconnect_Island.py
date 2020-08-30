"""
Key point:
The most steps we need is 2, No matther what kind of grid, we can only change two 1s to 0 , then it will become disconnected!!!
There are only three situations for this :
    1. There are 0 or more than 1 islands exist, so return 0
    2. There are exactly 1 island and we can convert once to make it disconnected
    3. There are exactly 1, and can't make it disconnected from step 2, then return 2.
"""
class Solution(object):
    def minDays(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0
        self.rows, self.cols = len(grid), len(grid[0])
        visited = [[0]*self.cols for _ in range(self.rows)]
        self.directions = [(0,1), (0,-1), (1,0), (-1,0)]
        count = 0
        # check how many islands exist
        for i in range(self.rows):
            for j in range(self.cols):
                if grid[i][j] == 0:
                    continue
                count += self.dfs(i, j, grid, visited)
        if count >= 2 or count == 0:
            return 0

        # there is exactly one island, so tried to convert 1 to 0
        for p in range(self.rows):
            for k in range(self.cols):
                if grid[p][k] == 0:
                    continue
                grid[p][k] = 0
                visited = [[0] * self.cols for _ in range(self.rows)]
                count = 0
                for i in range(self.rows):
                    for j in range(self.cols):
                        if grid[i][j] == 0:
                            continue
                        count += self.dfs(i, j, grid, visited)
                if count == 0 or count >= 2:
                    return 1
                grid[p][k] = 1

        return 2


    def dfs(self, row, col, grid, visited):
        if visited[row][col]:
            return 0
        visited[row][col] = 1
        for i, j in self.directions:
            new_row, new_col = row + i, col + j
            if new_row < 0 or new_row >= self.rows or new_col < 0 or new_col >= self.cols:
                continue
            if not grid[new_row][new_col]:
                continue
            self.dfs(new_row, new_col, grid, visited)
        return 1