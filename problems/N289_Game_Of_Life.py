class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return
        self.rows, self.cols = len(board), len(board[0])
        changes = []
        for row in range(self.rows):
            for col in range(self.cols):
                count = self.caculate(board, changes, row, col)
                if board[row][col]:
                    if count[1] < 2 or count[1] > 3:
                        board[row][col] = 0
                        changes.append((row,col))
                else:
                    if count[1] == 3:
                        board[row][col] = 1
                        changes.append((row, col))
        return board


    def caculate(self, board, changes, row, col):
        count = {0:0, 1:0}
        if row + 1 < self.rows:
            if (row+1, col) in changes:
                count[1-board[row + 1][col]] += 1
            else:
                count[board[row+1][col]] += 1
        if row - 1 >= 0:
            if (row-1, col) in changes:
                count[1-board[row - 1][col]] += 1
            else:
                count[board[row-1][col]] += 1
        if col + 1 < self.cols:
            if (row, col+1) in changes:
                count[1-board[row][col + 1]] += 1
            else:
                count[board[row][col+1]] += 1
        if col - 1 >= 0:
            if (row, col-1) in changes:
                count[1-board[row][col - 1]] += 1
            else:
                count[board[row][col-1]] += 1
        if row - 1 >= 0 and col - 1 >= 0:
            if (row-1,col-1) in changes:
                count[1-board[row - 1][col - 1]] += 1
            else:
                count[board[row-1][col-1]] += 1
        if row + 1 < self.rows and col + 1 < self.cols:
            if (row+1, col+1) in changes:
                count[1-board[row + 1][col + 1]] += 1
            else:
                count[board[row+1][col+1]] += 1
        if row + 1 < self.rows and col - 1 >= 0:
            if (row+1, col-1) in changes:
                count[1-board[row + 1][col - 1]] += 1
            else:
                count[board[row+1][col-1]] += 1
        if row - 1 >= 0 and col + 1 < self.cols:
            if (row-1, col+1) in changes:
                count[1-board[row - 1][col + 1]] += 1
            else:
                count[board[row-1][col+1]] += 1
        return count




