"""
Minimax
Same as 486. Predict the Winner: https://leetcode.com/problems/predict-the-winner/
"""
class Solution(object):
    def stoneGame(self, piles):
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