from typing import List


class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        stack = [(0,0,k)]
        visited = set()
        steps = 0
        while stack:
            new_stack = []
            for r, c, w in stack:
                if r == rows - 1 and c == cols - 1:
                    return steps
                for i, j in directions:
                    row, col = r + i, c + j
                    if row < 0 or row >= rows or col < 0 or col >= cols:
                        continue
                    if grid[row][col] and w >0 and (row, col, w-1) not in visited:
                        new_stack.append((row, col, w-1))
                        visited.add((row, col, w-1))
                        continue
                    if not grid[row][col] and (row,col,w) not in visited:
                        new_stack.append((row, col, w))
                        visited.add((row, col, w))
            steps += 1
            stack = new_stack
        return -1

