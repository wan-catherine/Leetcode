class Solution(object):
    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """
        if board[click[0]][click[1]] == 'M':
            board[click[0]][click[1]] = 'X'
            return board

        rows, cols = len(board), len(board[0])
        visited = [[0]*cols for _ in range(rows)]
        directions = [(1,0),(0,1),(-1,0),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)]
        stack = [click]
        while stack:
            row, col = stack.pop()
            visited[row][col] = 2
            count = 0
            neighbours = []
            for i, j in directions:
                new_row, new_col = row+i, col+j
                if new_row < 0 or new_row >= rows or new_col < 0 or new_col >= cols:
                    continue
                if board[new_row][new_col] == 'M':
                    count += 1
                    continue
                if visited[new_row][new_col] != 0:
                    continue
                visited[new_row][new_col] = 1
                neighbours.append([new_row, new_col])
            if count > 0:
                board[row][col] = str(count)
                for p, q in neighbours:
                    visited[p][q] = 0
            else:
                board[row][col] = 'B'
                stack.extend(neighbours)
        return board