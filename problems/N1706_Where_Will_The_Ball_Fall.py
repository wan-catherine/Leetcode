class Solution(object):
    def findBall(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[int]
        """
        rows, cols = len(grid), len(grid[0])
        res = [1] * cols
        for i in range(cols):
            c = i
            for r in range(rows):
                if grid[r][c] == 1:
                    c += 1
                    if c >= cols or grid[r][c] == -1:
                        res[i] = -1
                        break
                else:
                    c -= 1
                    if c < 0 or grid[r][c] == 1:
                        res[i] = -1
                        break
            if res[i] != -1:
                res[i] = c
        return res


