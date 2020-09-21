import collections


class Solution(object):
    def maxProductPath(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows, cols = len(grid), len(grid[0])
        values = collections.defaultdict(list)
        values[(0, 0)].append(grid[0][0])
        values[(0, 0)].append(grid[0][0])

        for i in range(1, rows):
            values[(i, 0)].append(values[(i-1,0)][0]*grid[i][0])
            values[(i, 0)].append(values[(i-1,0)][1]*grid[i][0])

        for i in range(1, cols):
            values[(0, i)].append(values[(0,i-1)][0] * grid[0][i])
            values[(0, i)].append(values[(0,i-1)][1] * grid[0][i])

        for i in range(1, rows):
            for j in range(1, cols):
                vals = [values[(i-1,j)][0]*grid[i][j], values[(i-1,j)][1]*grid[i][j], values[(i,j-1)][0]*grid[i][j], values[(i,j-1)][1]*grid[i][j]]
                values[(i,j)].extend([max(vals), min(vals)])

        res = max(values[(rows-1, cols-1)])
        return res % (10**9 + 7) if res >= 0 else -1