class Solution(object):
    def maxSumTwoNoOverlap_my_solution(self, A, L, M):
        """
        :type A: List[int]
        :type L: int
        :type M: int
        :rtype: int
        """
        length = len(A)
        prefix_l = [sum(A[:L])]

        for i in range(L, length):
            prefix_l.append(prefix_l[-1] + A[i] - A[i - L])

        prefix_m = [sum(A[:M])]
        for i in range(M, length):
            prefix_m.append(prefix_m[-1] + A[i] - A[i - M])

        res = 0
        for i in range(length - L + 1):
            for j in range(L+i, length - M + 1):
                res = max(res, prefix_l[i] + prefix_m[j])

            if i - M >= 0:
                for j in range(i-M+1):
                    res = max(res, prefix_l[i] + prefix_m[j])
        return res

    """
    lmax : max sum of contiguous L elements before last M elements
    mmax : max sum of contiguous M elements before last L elments
    
    """
    def maxSumTwoNoOverlap(self, A, L, M):
        length = len(A)
        prefix = A[:]
        for i in range(1, length):
            prefix[i] += prefix[i-1]

        lmax, mmax, res = prefix[L - 1], prefix[M - 1], prefix[L + M - 1]
        for i in range(L+M, length):
            lmax = max(lmax, prefix[i - M] - prefix[i - M - L]) # L before M
            mmax = max(mmax, prefix[i - L] - prefix[i - M - L]) # M before L
            res = max(res, lmax + prefix[i] - prefix[i - M], mmax + prefix[i] - prefix[i - L])

        return res
