import bisect


class Solution(object):
    def kthSmallestPrimeFraction_TLE(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: List[int]
        """
        fractions = []
        length = len(A)
        for i in range(length-1, 0, -1):
            for j in range(i):
                num = A[j]/A[i]
                bisect.insort_left(fractions, (num, A[j], A[i]))
        return [fractions[K-1][1],fractions[K-1][2]]

    def kthSmallestPrimeFraction(self, A, K):
        length = len(A)
        def less_or_equal(val):
            count = 0
            for i in range(length):
                p = A[i] / val
                index = bisect.bisect_left(A, p)
                if index == length:
                    break
                count += length - index
            return count

        left, right = 0, 1
        while left < right:
            mid = (right + left) / 2
            count = less_or_equal(mid)
            if count > K:
                right = mid
            elif count < K:
                left = mid
            else:
                break

        ans = 0
        res = None
        for i in range(length):
            val = A[i] / mid
            index = bisect.bisect_left(A, val)
            if index < length:
                fraction = A[i] / A[index]
                if fraction > ans:
                    ans = fraction
                    res = [A[i], A[index]]
        return res