import heapq
import sys


class Solution(object):
    def minimumEffortPath_Dijkstra(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: int
        """
        rows, cols = len(heights), len(heights[0])
        efforts = [[sys.maxsize]*cols for _ in range(rows)]
        efforts[0][0] = 0
        pq = [(0, 0, 0)]
        directions = [(0,1),(1,0),(-1,0),(0,-1)]
        visited = set()
        while pq:
            effort, row, col = heapq.heappop(pq)
            visited.add((row, col))
            for i, j in directions:
                new_row, new_col = row + i, col +j
                if new_row < 0 or new_row >= rows or new_col < 0 or new_col >= cols or (new_row, new_col) in visited:
                    continue
                new_effort = max(effort, abs(heights[new_row][new_col] - heights[row][col]))
                if new_effort < efforts[new_row][new_col]:
                    efforts[new_row][new_col] = new_effort
                    heapq.heappush(pq, (new_effort, new_row, new_col))
        return efforts[-1][-1]

    """
    Binary search for a given threshold.
    """
    def minimumEffortPath(self, heights):
        rows, cols = len(heights), len(heights[0])
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        left, right = 0, 10**6 + 1

        def has_path(t):
            queue = [(0,0)]
            visited = set()
            while queue:
                row, col = queue.pop()
                if row == rows -1 and col == cols - 1:
                    return True
                visited.add((row, col))
                for i, j in directions:
                    new_row, new_col = row + i, col + j
                    if new_row < 0 or new_row >= rows or new_col < 0 or new_col >= cols or (new_row, new_col) in visited:
                        continue
                    if abs(heights[new_row][new_col] - heights[row][col]) > t:
                        continue
                    queue.append((new_row, new_col))
            return False


        while left < right:
            mid = (right - left) // 2 + left
            if has_path(mid):
                right = mid
            else:
                left = mid + 1
        return left

