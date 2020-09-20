class Solution(object):
    def uniquePathsIII(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows, cols = len(grid), len(grid[0])
        visited = [[0]*cols for _ in range(rows)]
        total = 0
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    start = (i, j)
                if grid[i][j] == 0:
                    total += 1

        def dfs(i, j, zeros, res):
            if grid[i][j] == 0:
                zeros += 1
            elif grid[i][j] == 2:
                res += (1 if zeros == total else 0)
                return res
            for row, col in directions:
                new_row, new_col = i + row, j + col
                if new_row < 0 or new_row >= rows or new_col < 0 or new_col >= cols:
                    continue
                if visited[new_row][new_col]:
                    continue
                if grid[new_row][new_col] in [-1, 1]:
                    continue
                visited[new_row][new_col] = 1
                res = max(res, dfs(new_row, new_col, zeros, res))
                visited[new_row][new_col] = 0
            return res

        res = dfs(start[0], start[1], 0, 0)
        return res
