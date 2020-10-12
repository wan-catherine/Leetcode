class Solution(object):
    def colorBorder(self, grid, r0, c0, color):
        """
        :type grid: List[List[int]]
        :type r0: int
        :type c0: int
        :type color: int
        :rtype: List[List[int]]
        """
        rows, cols = len(grid), len(grid[0])
        status = [[0]*cols for _ in range(rows)]
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        def dfs(r, c, co):
            if status[r][c]:
                return
            status[r][c] = 1
            for i, j in directions:
                row, col = r+i, c+j
                if row < 0 or row >= rows or col < 0 or col >= cols:
                    grid[r][c] = color
                    continue
                if status[row][col]:
                    continue
                if grid[row][col] != co:
                    grid[r][c] = color
                    continue
                dfs(row, col, co)
        dfs(r0, c0, grid[r0][c0])
        return grid




