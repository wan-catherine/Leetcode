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

        row = len(board)
        col = len(board[0])

        if row * col < len(word):
            return False

        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        starts = []
        for i in range(row):
            for j in range(col):
                if board[i][j] == word[0]:
                    starts.append((i,j))

        if len(starts) == 0:
            return False

        last = [(-1,-1)]
        return self.isValid(board,1, word, starts, directions, last)


    def isValid(self, board, index, word, starts, directions, last):
        row = len(board)
        col = len(board[0])
        if index == len(word):
            return True

        flag = False
        for i,j in starts:
            next = []
            tx,ty = i, j
            newLast = last.copy()
            newLast.append((i,j))
            for x,y in directions:
                if tx+x >= row or tx+x < 0 or ty+y < 0 or ty+y >= col:
                    continue
                if board[tx+x][ty+y] == word[index] and (tx+x, ty+y) not in last:
                    next.append((tx+x,ty+y))
                    flag = self.isValid(board,index+1,word, next, directions,newLast)
                if flag == True:
                    return flag
        return flag



