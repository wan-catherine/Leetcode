from typing import List

"""
For column, it should only have two status : start with 1 or start with 0, and all other in the same row should be same pattern.
Same for row. 

"""
class Solution:
    def movesToChessboard(self, board: List[List[int]]) -> int:
        length = len(board)
        base = board[0][0]
        cnt1, cnt2 = 0, 0
        for j in range(length):
            if board[0][j] != base:
                cnt1 += 1
            else:
                cnt2 += 1
            for i in range(length):
                if board[0][j] != base:
                    if board[i][j] == board[i][0]:
                        return -1
                else:
                    if board[i][j] != board[i][0]:
                        return -1
        if abs(cnt1 - cnt2) > 1:
            return -1
        cnt1, cnt2 = 0, 0
        for i in range(length):
            if board[i][0] != base:
                cnt1 += 1
            else:
                cnt2 += 1
            for j in range(length):
                if board[i][0] != base:
                    if board[i][j] == board[0][j]:
                        return -1
                else:
                    if board[i][j] != board[0][j]:
                        return -1
        if abs(cnt1 - cnt2) > 1:
            return -1

        cdiff, rdiff = 0, 0
        for j in range(length):
            if board[0][j] != j%2:
                cdiff += 1
        for i in range(length):
            if board[i][0] != i%2:
                rdiff += 1
        res = 0
        if not length%2:
            res += min(cdiff, length - cdiff) // 2
            res += min(rdiff, length - rdiff) // 2
        else:
            if cdiff % 2:
                cdiff = length - cdiff
            if rdiff % 2:
                rdiff = length - rdiff
            res += (cdiff + rdiff) // 2
        return res