class Solution(object):
    def minDeletionSize(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        res, n, m = 0, len(A), len(A[0])
        is_sorted = [0] * (n - 1)
        for j in range(m):
            is_sorted2 = is_sorted[:]
            for i in range(n - 1):
                if A[i][j] > A[i + 1][j] and is_sorted[i] == 0:
                    res += 1
                    break
                is_sorted2[i] |= A[i][j] < A[i + 1][j]
            else:
                is_sorted = is_sorted2
        return res

