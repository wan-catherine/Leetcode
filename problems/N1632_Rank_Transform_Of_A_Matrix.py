import collections
"""
First, Greedy to get the rank . 
    1. sort the nums
    2. for next num's rank , it will be equal to the max(row, col) + 1
    
Second: consider those duplicated nums which share same row/col, they should have same rank . 
But for those duplicated nums which are not share same row/col, they maybe don't have same rank . 
So we need to use row/col to do union find grouping. 
"""
class Solution(object):
    def matrixRankTransform(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        rows, cols = len(matrix), len(matrix[0])
        max_rows, max_cols = [0] * rows, [0] * cols
        res = [[0] * cols for _ in range(rows)]

        d = collections.defaultdict(list)
        for i in range(rows):
            for j in range(cols):
                d[matrix[i][j]].append((i, j))

        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            px, py = find(x), find(y)
            if px != py:
                parent[px] = py

        for v in sorted(d.keys()):
            parent= list(range(rows + cols))
            # group nums on the same row/col
            for i, j in d[v]:
                union(i, j + rows)

            root_rank = collections.defaultdict(int)
            # craete new rank for the nums which have the same root (on the same row/col)
            for i, j in d[v]:
                root = find(i)
                root_rank[root] = max(root_rank[root], max(max_rows[i], max_cols[j]) + 1)

            # update the res and max_rows, max_cols
            for i, j in d[v]:
                root = find(i)
                rank = root_rank[root]
                res[i][j] = rank
                max_rows[i], max_cols[j] = rank, rank
        return res


