class Solution(object):
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        length = len(grid)
        rows, cols = [0]* length, [0]*length
        for i in range(length):
            rows[i] = max(grid[i])
            for j in range(length):
                cols[i] = max(cols[i], grid[j][i])

        ans = 0
        for i in range(length):
            for j in range(length):
                value = min(rows[i], cols[j])
                ans += value - grid[i][j]
        return ans