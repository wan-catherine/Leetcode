class Solution:
    def exist(self, board, word):
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



