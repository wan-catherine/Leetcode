class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for row in board:
            l = [0] * 10
            for i in row:
                if i == ".":
                    continue
                if l[int(i)] != 0:
                    return False
                else:
                    l[int(i)] = 1
        i = 0
        for i in range(9):
            l = [0] * 10
            for row in board:
                if row[i] == ".":
                    continue
                if l[int(row[i])] != 0:
                    return False
                else:
                    l[int(row[i])] = 1

        for i in [0, 3, 6]:
            for j in [0, 3, 6]:
                l = [0] * 10
                for p in [0, 1, 2]:
                    for q in [0, 1, 2]:
                        if board[p + i][q + j] == ".":
                            continue
                        if l[int(board[p + i][q + j])] != 0:
                            return False
                        else:
                            l[int(board[p + i][q + j])] = 1

        return True

