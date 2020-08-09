class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        queue = []
        row_len, col_len = len(grid), len(grid[0])
        fresh = set()
        for i in range(row_len):
            for j in range(col_len):
                if grid[i][j] == 2:
                    queue.append((i, j))
                elif grid[i][j] == 1:
                    fresh.add((i,j))

        if len(fresh) < 1:
            return 0

        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        res = 0
        while queue:
            temp  = []
            for i,j in queue:
                for x, y in directions:
                    if i + x < 0 or i + x >= row_len or j + y < 0  or j + y >= col_len:
                        continue
                    if grid[i+x][j+y] == 1:
                        grid[i+x][j+y] = 2
                        temp.append((i+x, j+y))
                        fresh.remove((i+x, j+y))
            res += 1 if temp else 0
            queue = temp
        if fresh:
            return -1
        else:
            return res




