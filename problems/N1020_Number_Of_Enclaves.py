class Solution(object):
    def numEnclaves(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        rows, cols = len(A), len(A[0])
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        def dfs(i, j):
            A[i][j] = 0
            for r, c in directions:
                row, col = i+r, j+c
                if row < 0 or row >= rows or col < 0 or col >= cols or A[row][col] == 0:
                    continue
                dfs(row, col)

        for i in range(rows):
            if A[i][0] == 1:
                dfs(i, 0)
            if A[i][cols-1] == 1:
                dfs(i, cols-1)

        for i in range(cols):
            if A[0][i] == 1:
                dfs(0, i)
            if A[rows-1][i] == 1:
                dfs(rows-1, i)

        res = 0
        for i in range(rows):
            for j in range(cols):
                if A[i][j] == 1:
                    res += 1
        return res
