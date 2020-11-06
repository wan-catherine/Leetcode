import collections


class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        if not matrix:
            return 0
        res = 0
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        rows, cols = len(matrix), len(matrix[0])
        graph = collections.defaultdict(set)
        indegrees = [[0]*cols for _ in range(rows)]

        for row in range(rows):
            for col in range(cols):
                for i, j in directions:
                    r, c = row + i, col + j
                    if r < 0 or r >= rows or c < 0 or c >= cols:
                        continue
                    if matrix[r][c] < matrix[row][col]:
                        indegrees[row][col] += 1
                        graph[(r, c)].add((row, col))

        zero_ingrees = collections.deque()

        for row in range(rows):
            for col in range(cols):
                if not indegrees[row][col]:
                    zero_ingrees.append((row, col))

        # topological sort , smiliar as BFS
        while zero_ingrees:
            res += 1
            for _ in range(len(zero_ingrees)):
                row, col = zero_ingrees.popleft()
                for i, j in graph[(row, col)]:
                    indegrees[i][j] -= 1
                    if not indegrees[i][j]:
                        zero_ingrees.append((i,j))
        return res