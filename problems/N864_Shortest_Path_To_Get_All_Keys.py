from typing import List
"""
use position ans status to filter duplication. 
status : how many keys I have now 
"""

class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        rows, cols = len(grid), len(grid[0])
        target = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '@':
                    start = (i, j)
                if grid[i][j].islower():
                    target += 1

        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        queue = [(start[0], start[1], 0, 0)]
        step = 0
        memo = set(queue)
        while queue:
            new_queue = []
            for r, c, count, key in queue:
                if count == target:
                    return step
                for i, j in directions:
                    row, col = r + i, c + j
                    if row < 0 or row >= rows or col < 0 or col >= cols:
                        continue
                    if grid[row][col] == '#':
                        continue
                    if grid[row][col].isupper():
                        val = (1 << (ord(grid[row][col]) - ord('A')))
                        if not key & val:
                            continue
                    new_count = count
                    new_key = key
                    if grid[row][col].islower():
                        if not key & (1 << (ord(grid[row][col]) - ord('a'))):
                            new_count += 1
                            new_key |= (1 << (ord(grid[row][col]) - ord('a')))
                    if (row, col, new_count, new_key) in memo:
                        continue
                    memo.add((row, col, new_count, new_key))
                    new_queue.append((row, col, new_count, new_key))
            step += 1
            queue = new_queue
        return -1