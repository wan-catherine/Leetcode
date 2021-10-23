from typing import List

class Solution:
    def placeWordInCrossword(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        length = len(word)
        def check(arr):
            nonlocal length
            if len(arr) != length:
                return False
            flag = True
            for i in range(length):
                if arr[i] == ' ':
                    continue
                if arr[i] != word[i]:
                    flag = False
                    break
            if flag:
                return True
            for i in range(length):
                if arr[i] == ' ':
                    continue
                if arr[i] != word[length-i-1]:
                    return False
            return True

        for i in range(rows):
            arr = []
            for j in range(cols):
                if board[i][j] == '#' or j == cols - 1:
                    if board[i][j] != '#' and j == cols - 1:
                        arr.append(board[i][j])
                    if check(arr[:]):
                        return True
                    arr = []
                else:
                    arr.append(board[i][j])

        for j in range(cols):
            arr = []
            for i in range(rows):
                if board[i][j] == '#' or i == rows - 1:
                    if board[i][j] != '#' and i == rows - 1:
                        arr.append(board[i][j])
                    if check(arr[:]):
                        return True
                    arr = []
                else:
                    arr.append(board[i][j])
        return False