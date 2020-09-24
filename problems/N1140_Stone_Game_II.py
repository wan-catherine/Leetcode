import sys


class Solution(object):
    def stoneGameII(self, piles):
        """
        :type piles: List[int]
        :rtype: int
        """
        length = len(piles)
        memo = {}
        suffix_sum = piles[:]
        for i in range(length-2, -1, -1):
            suffix_sum[i] += suffix_sum[i+1]
        suffix_sum = suffix_sum + [0]
        # print(suffix_sum)
        def dfs(i, m):
            if (i,m) in memo:
                return memo[(i,m)]
            if i >= length:
                return 0
            val = 0
            piles_sum = 0
            for x in range(1, 2*m + 1):
                if i + x - 1>= length:
                    break
                piles_sum += piles[i+x-1]
                val = max(val, piles_sum + suffix_sum[i+x] - dfs(i+x, max(x, m)))
            memo[(i,m)] = val
            return val
        # print(memo)
        return dfs(0, 1)
