class Solution(object):
    def maxUncrossedLines(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        a_len = len(A)
        b_len = len(B)
        dp_table = [[0] * (1+b_len) for _ in range(1+a_len)]
        for i in range(1,a_len+1):
            for j in range(1,b_len+1):
                dp_table[i][j] = max(dp_table[i-1][j], dp_table[i][j-1], dp_table[i-1][j-1] + (1 if A[i-1] == B[j-1] else 0) )

        return dp_table[-1][-1]
