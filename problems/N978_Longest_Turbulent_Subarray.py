"""
DP
dp_h[i] : the number of the turbulent subarray when including A[i] as the high point
dp_l[i] : the number of the turbulent subarray when including A[i] as the low point

status change as :
A[i] == A[i-1] : dp_h[i], dp_l[i] = 1, 1
A[i] > A[i-1] : dp_h[i] = dp_l[i-1] + 1, dp_l[i] = 1
A[i] < A[i-1] : dp_h[i] = 1, dp_l[i] = dp_h[i-1] + 1
"""
class Solution(object):
    def maxTurbulenceSize(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        length = len(A)
        dp_h = [1] * length
        dp_l = [1] * length
        res = 1
        for i in range(1, length):
            if A[i] > A[i-1]:
                dp_h[i] = dp_l[i-1] + 1
                dp_l[i] = 1
            elif A[i] < A[i-1]:
                dp_l[i] = dp_h[i-1] + 1
                dp_h[i] = 1
            else:
                dp_l[i], dp_h[i] = 1, 1
            res = max(dp_h[i], dp_l[i], res)
        return res
