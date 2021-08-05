"""
Minimax
Same as 486. Predict the Winner: https://leetcode.com/problems/predict-the-winner/
"""
from typing import List


class Solution(object):
    def stoneGame_dfs(self, piles):
        """
        :type piles: List[int]
        :rtype: bool
        """
        memo = {}
        def dfs(i, j):
            if i == j:
                return piles[i],0
            if (i, j) in memo:
                return memo[(i, j)]
            left = dfs(i+1, j)
            right = dfs(i, j-1)
            if left[1] + piles[i] > right[1] + piles[j]:
                res = (left[1] + piles[i], left[0])
            else:
                res = (right[1] + piles[j], right[0])
            memo[(i, j)] = res
            return res

        scores = dfs(0, len(piles)-1)
        return scores[0] > scores[1]

    """
    dp[i][j]: the maximum diff for piles[i:j+1] 
                the maximum diff that the current candidate can get (it might be Alex/Bob)
    """
    def stoneGame(self, piles: List[int]) -> bool:
        length = len(piles)
        dp = [[0] * length for _ in range(length)]
        for i in range(1, length):
            dp[i-1][i] = abs(piles[i-1] - piles[i])
        for l in range(3, length+1):
            for i in range(length - l + 1):
                j = i + l - 1
                dp[i][j] = max(piles[i] - dp[i+1][j], piles[j] - dp[i][j-1])
        return dp[0][-1] > 0

    # update 20210805
    def stoneGame(self, piles: List[int]) -> bool:
        length = len(piles)
        memo = {}

        def helper(l, r):
            if l == r:
                return piles[l]
            if (l, r) in memo:
                return memo[(l, r)]
            val = max(piles[l] - helper(l + 1, r), piles[r] - helper(l, r - 1))
            memo[(l, r)] = val
            return val

        return True if helper(0, length - 1) > 0 else False