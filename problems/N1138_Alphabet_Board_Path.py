class Solution(object):
    def alphabetBoardPath(self, target):
        """
        :type target: str
        :rtype: str
        """
        board = ["abcde", "fghij", "klmno", "pqrst", "uvwxy", "z"]
        letter_mapping = {}
        for row in range(len(board)):
            for col in range(len(board[row])):
                letter_mapping[board[row][col]] = (row, col)

        res = []
        row, col = 0, 0
        for i in target:
            new_row, new_col = letter_mapping[i]
            row_diff = new_row - row
            col_diff = new_col - col

            if row_diff == 0 and col_diff == 0:
                res.append('!')
            else:
                if i != 'z':
                    res.append('D'*row_diff if row_diff > 0 else 'U'*abs(row_diff))
                    res.append('R' * col_diff if col_diff > 0 else 'L' * abs(col_diff))
                else:
                    res.append('D' * (row_diff-1))
                    res.append('L' * abs(col_diff))
                    res.append('D')
                res.append('!')
            row, col = new_row, new_col

        return ''.join(res)

