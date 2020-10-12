class Solution(object):
    def shortestBridge(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        directions = [[1,0], [0,1], [-1,0], [0,-1]]
        length = len(A)
        ones, twos = set(), set()
        is_break = False
        for i in range(length):
            if is_break:
                break
            for j in range(length):
                if A[i][j]:
                    li = set([(i, j)])
                    while li:
                        new_li = set()
                        for r, c in li:
                            A[r][c] = 2
                            twos.add((r,c))
                            for i, j in directions:
                                row, col = r + i, c + j
                                if row < 0 or row >= length or col < 0 or col >= length or A[row][col] != 1 or A[row][col] == 2:
                                    continue
                                new_li.add((row, col))
                        li = new_li
                    is_break = True
                    break

        for i in range(length):
            for j in range(length):
                if A[i][j] == 1:
                   ones.add((i, j))

        def bfs(nodes, flip):
            while nodes:
                new_nodes = set()
                for node in nodes:
                    r, c = node
                    for i, j in directions:
                        row, col = r + i, c + j
                        if row < 0 or row >= length or col < 0 or col >= length or A[row][col] == 2:
                            continue
                        if A[row][col] == 1:
                            return flip
                        A[row][col] = 2
                        new_nodes.add((row, col))
                flip += 1
                nodes = new_nodes

        return bfs(twos, 0)

