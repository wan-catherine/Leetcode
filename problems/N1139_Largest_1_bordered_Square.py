"""
Calculate all element's [top_1, left_1]
The from the bottom_right to check each status.
choose the length = min(status[top_1, left_1] and check the related status.
Notice , we need to check length ~ 1 (or last maximum). test_largest1BorderedSquare_3
If the length can be 7, but the maximum can be 7 ~ 1 . we need to check all of them.
"""
class Solution(object):
    def largest1BorderedSquare(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows, cols = len(grid), len(grid[0])
        status = [[[0,0] for _ in range(cols)] for _ in range(rows)]

        if grid[0][0]:
            status[0][0] = [1,1]
        else:
            status[0][0] = [0,0]

        for i in range(1, cols):
            if grid[0][i]:
                status[0][i][0] = 1
                status[0][i][1] = status[0][i-1][1] + 1

        for i in range(1, rows):
            if grid[i][0]:
                status[i][0][0] = status[i-1][0][0] + 1
                status[i][0][1] = 1

        for i in range(1, rows):
            for j in range(1, cols):
                if grid[i][j]:
                    status[i][j][0] = status[i-1][j][0] + 1
                    status[i][j][1] = status[i][j-1][1] + 1

        maximum = 0
        for i in range(rows-1, -1, -1):
            for j in range(cols-1, -1, -1):
                for length in range(min(status[i][j]), maximum, -1):
                    if i - length + 1 < 0 or j - length + 1 < 0:
                        continue
                    if status[i-length+1][j][1] < length or status[i][j-length+1][0] < length:
                        continue
                    maximum = max(maximum, length)
                    break
        return maximum * maximum
