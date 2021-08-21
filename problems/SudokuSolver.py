from typing import List


class Solution:
    def solveSudoku(self, board):
        self.helper(board, 0, 0)
        return board

    def helper(self, board, i, j):
        i, j = self.findNext(board, i, j)
        if i > 8:
            return True
        possible = self.getNotExisted(board, i, j)
        for num in possible:
            board[i][j] = str(num)
            newi = i + j // 8
            newj = (j + 1) % 9
            if self.helper(board, newi, newj) == True:
                return True
            else:
                board[i][j] = "."
        return False

    def findNext(self, board, i, j):
        while i < 9 and j < 9 and board[i][j] != ".":
            if j == 8:
                j = 0
                i += 1
            else:
                j += 1
        return i, j

    def solveSudoku_failed(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        possible = {}
        num = {i: [] for i in range(0,9)}
        count = 0
        for i in range(0,9):
            for j in range(0,9):
                if board[i][j] == ".":
                    possible[(i,j)] = self.getNotExisted(board, i, j)
                    num[len(possible[(i, j)])].append((i,j))
                    count += 1
        while len(num[0]) < count:
            while len(num[1]) > 0:
                pair = num[1][0]
                i = pair[0]
                j = pair[1]

                board[i][j]=possible[(i,j)].pop()
                self.update(possible, num, pair, board)


            if len(num[2]) > 0 and self.isSafe(board, num, possible, num[2][0]):
                board[i][j] = possible[(num[2][0][0], num[2][0][1])].pop()
                self.update(possible, num, pair, board)

    def isSafe(self, board, num, possible, pair):
        res = True
        i = pair[0]
        j = pair[1]
        numCopy = num.copy()
        possibleCopy = possible.copy()
        board[i][j] = possibleCopy[(i,j)].pop()
        
        self.update(possibleCopy, numCopy, pair, board)
        for (i, j) in numCopy[0]:
            if board[i][j] == ".":
                res = False
                break
        return res



    def update(self, possible, num, pair, board):
        for (p, q) in possible:
            if (p == pair[0] or q == pair[1]) and board[pair[0]][pair[1]] in possible[(p, q)]:
                num[len(possible[(p,q)])].remove((p,q))
                num[len(possible[(p,q)]) - 1].append((p,q))
                possible[(p,q)].remove(board[pair[0]][pair[1]])
            elif p == pair[0] and q == pair[1]:
                num[1].remove((p,q))
                num[0].append((p,q))

        iplus = pair[0] // 3 * 3
        jplus = pair[1] // 3 * 3
        for p in [0, 1, 2]:
            for q in [0, 1, 2]:
                if (p + iplus*3, q + jplus*3) in possible and board[pair[0]][pair[1]] in possible[(p + iplus*3, q + jplus*3)]:
                    num[len(possible[(p + iplus*3, q + jplus*3)])].remove((p, q))
                    num[len(possible[(p + iplus*3, q + jplus*3)]) - 1].append((p, q))
                    possible[(p + iplus*3, q + jplus*3)].remove(board[pair[0]][pair[1]])

    def getNotExisted(self, board, i, j):
        existed = set()
        for row in range(0, 9):
            if board[row][j] != ".":
                existed.add(board[row][j])
            if board[i][row] != ".":
                existed.add(board[i][row])

        iplus = i // 3 * 3
        jplus = j // 3 * 3
        for p in [0, 1, 2]:
            for q in [0, 1, 2]:
                if board[p + iplus][q + jplus] != ".":
                    existed.add(board[p + iplus][q + jplus])
        s = set(str(i) for i in range(1,10))
        l = s.difference(existed)
        return l

    # 20210821 update
    def solveSudoku(self, board: List[List[str]]) -> None:
        def dfs(idx):
            if idx == len(empty):
                return True
            r, c = empty[idx]
            status = [0] * 10
            for i in range(9):
                if board[i][c] == '.':
                    continue
                status[int(board[i][c])] = 1
            for i in range(9):
                if board[r][i] == '.':
                    continue
                status[int(board[r][i])] = 1
            for i in range((r // 3) * 3, (r // 3) * 3 + 3):
                for j in range((c // 3) * 3, (c // 3) * 3 + 3):
                    if board[i][j] == '.':
                        continue
                    status[int(board[i][j])] = 1
            for i in range(1, 10):
                if status[i] == 1:
                    continue
                board[r][c] = str(i)
                # print(board)
                if dfs(idx + 1):
                    return True
                board[r][c] = '.'
        empty = []
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    empty.append((i,j))
        dfs(0)