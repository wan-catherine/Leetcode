from typing import List


class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        rows, cols = len(board), len(board[0])
        dp = [[[0, 0] for _ in range(cols)] for _ in range(rows)]
        directions = [(0, 1), (1, 0), (1, 1)]
        dp[rows - 1][cols - 1][1] = 1
        for r in range(rows - 2, -1, -1):
            if board[r][cols - 1] == 'X' or dp[r + 1][cols - 1] == [-1, -1]:
                dp[r][cols - 1] = [-1, -1]
                continue
            dp[r][cols - 1][0] = dp[r + 1][cols - 1][0] + int(board[r][cols - 1])
            dp[r][cols - 1][1] = dp[r + 1][cols - 1][1]
        for c in range(cols - 2, -1, -1):
            if board[rows - 1][c] == 'X':
                dp[rows - 1][c] = [-1, -1]
                continue
            if dp[rows - 1][c + 1] == [-1, -1]:
                dp[rows - 1][c] = [-1, -1]
            else:
                dp[rows - 1][c][0] = dp[rows - 1][c + 1][0] + int(board[rows - 1][c])
                dp[rows - 1][c][1] = dp[rows - 1][c + 1][1]
        for r in range(rows - 2, -1, -1):
            for c in range(cols - 2, -1, -1):
                if board[r][c] == 'X':
                    dp[r][c] = [-1, -1]
                    continue
                maximum, count = -1, -1
                for i, j in directions:
                    row, col = r + i, c + j
                    if board[row][col] == 'X' or dp[row][col] == [-1, -1]:
                        continue
                    if dp[row][col][0] > maximum:
                        maximum = dp[row][col][0]
                        count = dp[row][col][1]
                    elif dp[row][col][0] == maximum:
                        count += dp[row][col][1]
                dp[r][c] = [maximum + (int(board[r][c]) if board[r][c] != 'E' and maximum >= 0 else 0), count]
        if dp[0][0] == [-1, -1]:
            return [0, 0]
        return [dp[0][0][0] % (10 ** 9 + 7), dp[0][0][1] % (10 ** 9 + 7)]