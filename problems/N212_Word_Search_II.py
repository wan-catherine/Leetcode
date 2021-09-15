import collections
from typing import List


class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.is_end_of_word = False
        self.word = None

class Solution(object):
    def findWords_timeout(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        if not board and not board[0]:
            return []

        self.board = board
        self.rows = len(board)
        self.cols = len(board[0])
        self.diections = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        res = []
        for word in words:
            if self.is_exist(word):
                res.append(word)
        return res

    def is_exist(self, word):
        for row in range(self.rows):
            for col in range(self.cols):
                if self.board[row][col] != word[0]:
                    continue
                if self.has_word(row, col, 0, word):
                    return True
        return False

    def has_word(self, row, col, index, word):
        if index == len(word):
            return True

        if row < 0 or row >= self.rows or col < 0 or col >= self.cols or self.board[row][col] == '':
            return False

        if self.board[row][col] != word[index]:
            return False

        temp, self.board[row][col] = self.board[row][col], ''
        for direction in self.diections:
            if self.has_word(row + direction[0], col + direction[1], index + 1, word):
                temp, self.board[row][col] = '', temp
                return True
        temp, self.board[row][col] = '', temp
        return False

    def create_trie_tree(self, words):
        root = TrieNode()
        for word in words:
            cur = root
            for c in word:
                index = ord(c) - ord('a')
                if not cur.children[index]:
                    cur.children[index] = TrieNode()
                cur = cur.children[index]
            cur.is_end_of_word = True
            cur.word = word
        return root

    def findWords(self, board, words):
        if not board or not board[0]:
            return []

        root = self.create_trie_tree(words)
        self.board = board
        self.rows = len(board)
        self.cols = len(board[0])
        self.diections = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        res = set()
        for row in range(self.rows):
            for col in range(self.cols):
                self.walk(root, row, col, res)
        return list(res)

    def walk(self, node, row, col, res):
        if row < 0 or row >= self.rows or col < 0 or col >= self.cols or self.board[row][col] == '':
            return

        index = ord(self.board[row][col]) - ord('a')
        next_node = node.children[index]
        if not next_node:
            return

        if next_node.is_end_of_word:
            res.add(next_node.word)

        temp, self.board[row][col] = self.board[row][col], ''

        for direction in self.diections:
            self.walk(next_node, row + direction[0], col + direction[1], res)

        self.board[row][col] = temp

    # DFS + prune
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        rows, cols = len(board), len(board[0])
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        count = collections.defaultdict(int)
        for i in range(rows):
            for j in range(cols):
                count[board[i][j]] += 1

        def check(word):
            def dfs(r, c, index):
                if board[r][c] != word[index]:
                    return False
                if index == len(word) - 1:
                    return True
                visited[r][c] = 1
                for i, j in directions:
                    row, col = r + i, c + j
                    if row < 0 or row >= rows or col < 0 or col >= cols or visited[row][col]:
                        continue
                    if board[row][col] != word[index + 1]:
                        continue
                    visited[row][col] = 1
                    if dfs(row, col, index + 1):
                        return True
                    visited[row][col] = 0
                return False

            for i in range(rows):
                for j in range(cols):
                    visited = [[0] * cols for _ in range(rows)]
                    if dfs(i, j, 0):
                        return True
            return False

        res = []
        for word in words:
            if len(word) > rows * cols:
                continue
            cw = collections.Counter(word)
            flag = True
            for k, v in cw.items():
                if k not in count or count[k] < v:
                    flag = False
                    break
            if flag and check(word):
                res.append(word)
        return res

