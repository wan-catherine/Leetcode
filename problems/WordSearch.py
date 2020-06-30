class Solution:
    def exist_before(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if word == None:
            return True
        if board == None:
            return False

        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.isValid(board, 0, word, i, j, directions):
                    return True
        return False


    def isValid(self, board, index, word, row, col, directions):
        if index == len(word):
            return True
        if row >= len(board) or row < 0 or col < 0 or col >= len(board[0]) or board[row][col] != word[index]:
            return False

        temp, board[row][col] = board[row][col], ''
        flag = False

        for x,y in directions:
            flag =  flag or self.isValid(board,index+1, word, row+x, col+y, directions)
            # if flag == True:
            #     break
        board[row][col] = temp
        return flag

    #20200630
    def exist(self, board, word):
        if not board or not board[0]:
            return False

        self.board = board
        self.word = word
        self.rows = len(board)
        self.cols = len(board[0])
        self.diections = [(1,0),(0,1),(-1,0),(0,-1)]
        for row in range(self.rows):
            for col in range(self.cols):
                if board[row][col] != word[0]:
                    continue
                if self.has_word(row, col, 0):
                    return True
        return False

    def has_word(self, row, col, index):
        if index == len(self.word):
            return True

        if row < 0 or row >= self.rows or col < 0 or col >= self.cols:
            return False

        if self.board[row][col] != self.word[index]:
            return False
        temp, self.board[row][col] = self.board[row][col], ''
        for direction in self.diections:
            if self.has_word(row + direction[0], col + direction[1], index + 1):
                temp, self.board[row][col] = '', temp
                return True
        temp, self.board[row][col] = '', temp
        return False





