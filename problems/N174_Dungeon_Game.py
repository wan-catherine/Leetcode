from math import inf


class Solution(object):
    """
    dp[i][j] : the minimum health of the knight starts at dungeon[i][j] to save the princess
    """
    def calculateMinimumHP_dp(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        if not dungeon or not dungeon[0]:
            return 0
        row = len(dungeon)+1
        col = len(dungeon[0])+1
        dp_table = [[float(inf)]*col for _ in range(row)]
        dp_table[-1][-2], dp_table[-2][-1] = 1,1
        for i in range(row-2,-1,-1):
            for j in range(col-2,-1,-1):
                dp_table[i][j] = max(1, min(dp_table[i+1][j], dp_table[i][j+1]) - dungeon[i][j])
        return dp_table[0][0]
