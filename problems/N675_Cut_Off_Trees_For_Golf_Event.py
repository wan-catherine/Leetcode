from typing import List

class Solution:
    def cutOffTree_TLE(self, forest: List[List[int]]) -> int:
        rows, cols = len(forest), len(forest[0])
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        mapping = {}
        pq = []
        for i in range(rows):
            for j in range(cols):
                if forest[i][j] > 1:
                    pq.append(forest[i][j])
                    mapping[forest[i][j]] = (i, j)
        pq.sort()
        res = 0
        pr, pc = 0, 0

        for v in pq:
            r, c = mapping[v]
            stack = [(pr, pc)]
            visited = [[0] * cols for _ in range(rows)]
            steps = 0
            flag = False
            while stack:
                new_stack = []
                for rr, cc in stack:
                    visited[rr][cc] = 1
                    if rr == r and cc == c:
                        # res += steps
                        flag = True
                        break
                    is_break = False
                    for i, j in directions:
                        row, col = rr + i, cc + j
                        if row < 0 or row >= rows or col < 0 or col >= cols or forest[row][col] == 0 or visited[row][col]:
                            continue
                        new_stack.append((row, col))
                        if row == r and col == c:
                            flag = True
                            res += steps + 1
                            is_break = True
                            break
                    if is_break:
                        break
                steps += 1
                stack = new_stack
            if not flag:
                return -1
            pr, pc = r, c
        return res

    def cutOffTree(self, forest: List[List[int]]) -> int:

        self.Row, self.Col = len(forest), len(forest[0])
        trees = []
        for r in range(self.Row):
            for c in range(self.Col):
                if forest[r][c] > 1:
                    trees.append((forest[r][c], r, c))
        trees.sort()
        res = 0
        sr, sc = 0, 0
        for height, tr, tc in trees:
            step = self.dist_BFS(sr, sc, tr, tc, forest)
            if step == -1:
                return -1
            res += step
            sr, sc = tr, tc
        return res

    def dist_BFS(self, sr: int, sc: int, tr: int, tc: int, forest: List[List[int]]) -> int:
        visited = [[False for _ in range(self.Col)] for _ in range(self.Row)]
        Q = [(sr, sc)]
        visited[sr][sc] = True
        step = 0
        while Q:
            cur_len = len(Q)
            for _ in range(cur_len):
                r, c = Q.pop(0)
                if (r, c) == (tr, tc):
                    return step
                for nr, nc in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                    if 0 <= nr < self.Row and 0 <= nc < self.Col:
                        if visited[nr][nc] == False and forest[nr][nc] >= 1:
                            Q.append((nr, nc))
                            visited[nr][nc] = True
            step += 1
        return -1



