import sys


class Solution:
    def findMinStep(self, board: str, hand: str) -> int:
        res = sys.maxsize
        lh = len(hand)

        def clean(board):
            newboard = board
            board = ""
            while (newboard != board):
                board = newboard;
                for i in range(len(board)):
                    j = i
                    while (j + 1 < len(board) and board[j + 1] == board[j]):
                        j += 1
                    if (j - i + 1 >= 3):
                        newboard = board[0:i] + board[j + 1:]
                        break
            return newboard

        def dfs(b, h):
            nonlocal res
            if not b:
                res = min(res, lh - len(h))
                return
            lb, l = len(b), len(h)
            for i in range(l):
                if i + 1 < l and h[i] == h[i+1]:
                    continue
                for j in range(lb):
                    if j + 1 < lb and b[j] == b[j+1]:
                        continue

                    nb = clean(b[:j] + h[i] + b[j:])
                    dfs(nb, h[:i] + h[i+1:])

        dfs(board, hand)
        return res if res < sys.maxsize else -1