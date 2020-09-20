import collections

"""
dp[i][diff] : the longest length of the subsequence which ends at ith , the diff is diff. 
"""
class Solution(object):
    def longestArithSeqLength(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        length = len(A)
        dp = collections.defaultdict(dict)
        res = 1
        for i in range(length):
            for j in range(i):
                diff = A[i] - A[j]
                if diff not in dp[j]:
                    dp[i][diff] = 2
                else:
                    dp[i][diff] = dp[j][diff] + 1
                res = max(res, dp[i][diff])
        return res
