"""
dp[i] : results of A[j] | A[j+1] | ... | A[i] which ends at A[i]
time complexity : O(32N)
len(dp[i]) <= 32, because each time of '|' , for integer (32bits) , there are at most 32 different situation to be added into dp[i].
"""
class Solution(object):
    def subarrayBitwiseORs(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        length = len(A)
        dp = [set() for _ in range(length)]
        dp[0].add(A[0])
        res = set()
        res.add(A[0])
        for i in range(1, length):
            dp[i].add(A[i])
            for num in dp[i-1]:
                dp[i].add(A[i] | num)
            res.update(dp[i])
        return len(res)