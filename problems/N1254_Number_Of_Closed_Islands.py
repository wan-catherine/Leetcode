class Solution(object):
    def closedIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows, cols = len(grid), len(grid[0])
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        def dfs(r, c):
            if grid[r][c]:
                return
            grid[r][c] = 1
            for i, j in directions:
                row, col = r+i, c+j
                if row < 0 or row >= rows or col < 0 or col >= cols:
                    continue
                if grid[row][col] == 1:
                    continue
                dfs(row, col)

        for i in range(cols):
            if grid[0][i] == 0:
                dfs(0, i)
            if grid[rows-1][i] == 0:
                dfs(rows-1, i)

        for i in range(rows):
            if grid[i][0] == 0:
                dfs(i,0)
            if grid[i][cols - 1] == 0:
                dfs(i, cols-1)

        res = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]:
                    continue
                res += 1
                dfs(i, j)
        return res

