import heapq


class Solution(object):
    def trapRainWater(self, heightMap):
        """
        :type heightMap: List[List[int]]
        :rtype: int
        """
        rows, cols = len(heightMap), len(heightMap[0])
        heap, visited = [], set()
        for i in range(cols):
            heap.append((heightMap[0][i], 0, i))
            heap.append((heightMap[-1][i], rows-1, i))
            visited.add((0, i))
            visited.add((rows-1, i))

        for i in range(rows):
            heap.append((heightMap[i][0], i, 0))
            heap.append((heightMap[i][-1], i, cols-1))
            visited.add((i,0))
            visited.add((i, cols-1))

        res = 0
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        heapq.heapify(heap)
        maximum = 0
        while heap:
            val, r, c = heapq.heappop(heap)
            if val > maximum:
                maximum = val
            for i, j in directions:
                row, col = r + i, c + j
                if row < 0 or row >= rows or col < 0 or col >= cols or (row, col) in visited:
                    continue
                if heightMap[row][col] < maximum:
                    res += maximum - heightMap[row][col]
                visited.add((row, col))
                heapq.heappush(heap, (heightMap[row][col], row, col))
        return res
