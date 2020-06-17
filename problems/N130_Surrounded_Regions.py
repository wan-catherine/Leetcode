class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        self.board = board
        if not self.board or not len(self.board) or not len(self.board[0]):
            return
        self.row_len = len(self.board)
        self.col_len = len(self.board[0])

        visited = [[0] * self.col_len for _ in range(self.row_len)]
        stack = []
        for i in range(self.row_len):
            for j in range(self.col_len):
                if self.board[i][j] == 'X' or visited[i][j] == 1:
                    continue
                if not stack:
                    stack.append((i,j))
                    is_change = True
                    o_array = []
                while stack:
                    row, col = stack.pop()
                    if visited[row][col]:
                        continue
                    visited[row][col] = 1
                    o_array.append((row, col))
                    if is_change and self.is_border_O(row, col):
                        is_change = False
                    if row >= 1 and self.board[row-1][col] == 'O':
                        stack.append((row-1, col))
                    if col >= 1 and self.board[row][col-1] == 'O':
                        stack.append((row, col-1))
                    if row < self.row_len - 1 and self.board[row+1][col] == 'O':
                        stack.append((row+1, col))
                    if col < self.col_len -1 and self.board[row][col+1] == 'O':
                        stack.append((row, col+1))
                if is_change:
                    for t in o_array:
                        self.board[t[0]][t[1]] = 'X'
        return board

    def is_border_O(self, row, col):
        if self.board[row][col] == 'O':
            if row == 0 or col == 0:
                return True
            if row == self.row_len - 1 or col == self.col_len - 1:
                return True
        return False







