class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        if not board or not board[0]:
            return 0

        ans = 0
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == 'X':
                    if i == 0 or board[i - 1][j] != 'X':
                        if j == 0 or board[i][j - 1] != 'X':
                            ans += 1
        return ans