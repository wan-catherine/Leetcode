class Solution(object):
    def swimInWater(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows, cols = len(grid), len(grid[0])
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        def check(th):
            nonlocal rows, cols
            if th < grid[0][0]:
                return False
            visited = set()
            visited.add((0,0))
            stack = [(0,0)]
            while stack:
                new_stack = []
                for r, c in stack:
                    if r == rows - 1 and c == cols - 1:
                        return True
                    for i, j in directions:
                        row, col = r+i, c+j
                        if row < 0 or row >= rows or col < 0 or col >= cols or (row, col) in visited or grid[row][col] > th:
                            continue
                        visited.add((row, col))
                        new_stack.append((row, col))
                stack = new_stack
            return False

        left, right = 0, rows*cols
        while left < right:
            mid = (right - left) // 2 + left
            if check(mid):
                right = mid
            else:
                left = mid + 1
        return left
