import collections
import sys

"""
DP
dp[i] means the i-th chat of key, need dp[i] steps . 
But the key point is there might be several duplicated chars in the ring.

So from i-1 to i,maybe different ways.
So we add the second dimension
==> dp[i][pos] : at pos position i-th char of key, it needs dp[i][pos] steps. 

dp[i][pos] = min(dp[i-1][pre_pos]) for pre_pos in .....

"""
class Solution(object):
    def findRotateSteps(self, ring, key):
        """
        :type ring: str
        :type key: str
        :rtype: int
        """
        m, n = len(ring), len(key)
        letter2pos = collections.defaultdict(list)
        for i, c in enumerate(ring):
            letter2pos[c].append(i)

        dp = [[sys.maxsize]*m for _ in range(n)]
        for i in letter2pos[key[0]]:
            dp[0][i] = min(i, m - i)

        for i in range(1, n):
            for pos in letter2pos[key[i]]:
                for pre_pos in letter2pos[key[i-1]]:
                    dp[i][pos] = min(dp[i][pos], dp[i-1][pre_pos] + min(abs(pre_pos-pos), m - abs(pre_pos - pos)))
        print(dp)
        return min(dp[n-1]) + n