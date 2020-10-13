class Solution(object):
    def shortestPathBinaryMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        length = len(grid)
        if grid[0][0] or grid[length-1][length-1]:
            return -1
        directions = [(1,0),(0,1),(-1,0),(0,-1),(1,1),(-1,-1),(1,-1),(-1,1)]
        visited = [[0]*length for _ in range(length)]

        stack = set([(0,0)])
        step = 1
        while stack:
            new_stack = set()
            for r, c in stack:
                visited[r][c] = 1
                if r == c == length - 1:
                    return step
                for i, j in directions:
                    row, col = r+i, c+j
                    if row < 0 or row >= length or col < 0 or col >= length:
                        continue
                    if row == col == length-1:
                        return step + 1
                    if visited[row][col] or grid[row][col]:
                        continue
                    new_stack.add((row, col))
            step += 1
            stack = new_stack
        return - 1
