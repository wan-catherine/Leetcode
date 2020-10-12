class Solution(object):
    """
    change one square into 3*3 grid.
    so it will become the island problem.
    """
    def regionsBySlashes_dfs(self, grid):
        """
        :type grid: List[str]
        :rtype: int
        """
        n = len(grid)
        length = 3 * n
        new_grid = [[0]*length for _ in range(length)]
        for i in range(n):
            for j in range(n):
                if grid[i][j] == '/':
                    new_grid[3 * i][3 * j + 2] = -1
                    new_grid[3 * i + 1][3 * j + 1] = -1
                    new_grid[3 * i + 2][3 * j] = -1
                elif grid[i][j] == '\\':
                    new_grid[3 * i][3 * j] = -1
                    new_grid[3 * i + 1][3 * j + 1] = -1
                    new_grid[3 * i + 2][3 * j + 2] = -1

        directions = [(0,1), (1,0), (-1,0), (0,-1)]

        def dfs(i, j, f):
            if new_grid[i][j] != 0:
                return
            new_grid[i][j] = f
            for r, c in directions:
                row, col = i + r, j + c
                if row < 0 or row >= length or col < 0 or col >= length:
                    continue
                if new_grid[i][j] == -1:
                    continue
                dfs(row, col, f)

        res = 0
        for i in range(length):
            for j in range(length):
                if not new_grid[i][j]:
                    res += 1
                    dfs(i, j, res)
        return res

    """
    consider the dot instead of considering square. 
    so for n squares , we have n+1 dots. 
    if '/' or '\' connects two dots . 
    Key point : 
        if two dots from the same group, it will add one more region
        if two dots from two different groups, it won't add more region, but connect two groups into one group
    """
    def regionsBySlashes(self, grid):
        n = len(grid)
        length = (n+1)**2
        parent = [-1] * length
        size = [0]*length

        for i in range(n+1):
            for j in range(n+1):
                idx = i * (n+1) + j
                parent[idx] = idx
                size[idx] = 1
                if i == 0 or i == n or j == 0 or j == n:
                    parent[idx] = 0

        def find_parent(i):
            if parent[i] != i:
                parent[i] = find_parent(parent[i])
            return parent[i]

        def union(i, j):
            pi = find_parent(i)
            pj = find_parent(j)
            if size[pi] < size[pj]:
                parent[pi] = pj
                size[pj] += size[pi]
            else:
                parent[pj] = pi
                size[pi] += size[pj]

        res = 1
        for i in range(n):
            for j in range(n):
                if grid[i][j] == ' ':
                    continue
                x, y = None, None
                if grid[i][j] == '/':
                    x = i * (n+1) + j + 1
                    y = (i+1) * (n+1) + j
                elif grid[i][j] == '\\':
                    x = i*(n+1) + j
                    y = (i+1)*(n+1) + j + 1

                if find_parent(x) == find_parent(y):
                    res += 1
                else:
                    union(x, y)
        return res




