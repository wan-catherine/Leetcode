"""
reverse to consider.
we first set a virtual root : rows * cols
remove all bricks from the hits, then add them according to the reverse order of hits : hits[::-1]
then do union for the graph which is same as grid and remove all bricks from the hits.
Then we add bricks back by the order of hits[::-1] to check the root's size.
ans = new root size - old root size - 1 (the hit itself)
"""
class Solution(object):
    def hitBricks(self, grid, hits):
        """
        :type grid: List[List[int]]
        :type hits: List[List[int]]
        :rtype: List[int]
        """
        rows, cols = len(grid), len(grid[0])
        root = rows*cols
        parents = [i for i in range(rows*cols+1)]
        sizes = [1] * (rows*cols+1)

        def find(x):
            while x != parents[x]:
                parents[x] = parents[parents[x]]
                x = parents[x]
            return x

        def union(p, q):
            pp, pq = find(p), find(q)
            if pp == pq:
                return
            parents[pp] = pq
            sizes[pq] += sizes[pp]

        def get_size(x):
            root = find(x)
            return sizes[root]

        def get_index(row, col):
            return row * cols + col

        graph = [col[:] for col in grid]
        for i, j in hits:
            graph[i][j] = 0

        for i in range(cols):
            if graph[0][i] == 1:
                union(get_index(0, i), root)

        for i in range(1, rows):
            for j in range(cols):
                if graph[i][j] == 0:
                    continue
                if graph[i-1][j] == 1:
                    union(get_index(i-1, j), get_index(i, j))
                if j > 0 and graph[i][j-1] == 1:
                    union(get_index(i, j-1), get_index(i, j))

        hl = len(hits)
        directions = [(-1,0), (1,0), (0, -1), (0, 1)]
        res = [0] * hl
        for index in range(hl-1, -1, -1):
            row, col = hits[index]
            if grid[row][col] == 0:
                continue

            origin = get_size(root)
            if row == 0:
                union(get_index(row, col), root)
            for i, j in directions:
                new_row, new_col = row + i, col + j
                if new_row < 0 or new_row >= rows or new_col < 0 or new_col >= cols or graph[new_row][new_col] == 0:
                    continue
                union(get_index(row, col), get_index(new_row, new_col))
            current = get_size(root)
            res[index] = max(0, current - origin - 1)
            graph[row][col] = 1
        return res




