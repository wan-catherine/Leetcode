import heapq

"""
Dijkstra Algo : BFS + PQ
Key point here is add distance into the queue.
"""
class Solution(object):
    def shortestDistance(self, maze, start, destination):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: int
        """
        rows, cols = len(maze), len(maze[0])
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        queue = [(0, start[0], start[1])]
        visited = [[0]*cols for _ in range(rows)]
        while queue:
            dist, row, col = heapq.heappop(queue)
            if row == destination[0] and col == destination[1]:
                return dist
            if visited[row][col] == 1:
                continue
            visited[row][col] = 1
            for i, j in directions:
                r, c, d = row, col, dist
                while r+i >= 0 and r+i < rows and c+j >= 0 and c+j < cols and maze[r+i][c+j] == 0:
                    r += i
                    c += j
                    d += 1
                if visited[r][c] == 1:
                    continue
                heapq.heappush(queue, (d, r, c))
        return -1