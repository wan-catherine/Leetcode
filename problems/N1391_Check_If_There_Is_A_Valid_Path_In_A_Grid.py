class Solution(object):
    def hasValidPath(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: bool
        """
        rows, cols = len(grid), len(grid[0])
        visited = [[0]*cols for _ in range(rows)]
        def dfs(r, c):
            if r == rows - 1 and c == cols - 1:
                    return True

            if r < 0 or r >= rows or c < 0 or c >= cols:
                return False
            if visited[r][c]:
                return False
            visited[r][c] = 1
            if grid[r][c] == 1:
                flag = False
                if c+1 < cols and grid[r][c+1] in [1, 3,5]:
                    flag = dfs(r, c+1)
                if c-1 >= 0 and grid[r][c-1] in [1,4,6]:
                    flag = flag or dfs(r, c-1)
                return flag
            if grid[r][c] == 2:
                flag = False
                if r+1 < rows and grid[r+1][c] in [2,5,6]:
                    flag = dfs(r+1, c)
                if r-1 >=0 and grid[r-1][c] in [2,3,4]:
                    flag = flag or dfs(r-1, c)
                return flag
            if grid[r][c] == 3:
                flag = False
                if c-1>= 0 and grid[r][c-1] in [1,4,6]:
                    flag = dfs(r, c-1)
                if r+1 < rows and grid[r+1][c] in [2,5,6]:
                    flag = flag or dfs(r+1, c)
                return flag
            if grid[r][c] == 4:
                flag = False
                if c+1 < cols and grid[r][c+1] in [1,3,5]:
                    flag = dfs(r, c+1)
                if r+1 < rows and grid[r+1][c] in [2,5,6]:
                    flag = flag or dfs(r+1, c)
                return flag
            if grid[r][c] == 5:
                flag = False
                if r-1 >= 0 and grid[r-1][c] in [2,3,4]:
                    flag = dfs(r-1, c)
                if c-1 >= 0 and grid[r][c-1] in [1,4,6]:
                    flag = flag or dfs(r, c-1)
                return flag
            if grid[r][c] == 6:
                flag = False
                if r-1>=0 and grid[r-1][c] in [2,3,4]:
                    flag = dfs(r-1,c)
                if c+1 < cols and grid[r][c+1] in [1,3,5]:
                    flag = flag or dfs(r, c+1)
                return  flag
        return dfs(0,0)


