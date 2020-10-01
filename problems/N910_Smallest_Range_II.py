class Solution(object):
    def smallestRangeII(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        length = len(A)
        A.sort()
        diff = A[-1] - A[0]
        for i in range(0, length-1):
            maximum = max(A[i]+K, A[-1]-K)
            minimum = min(A[i+1]-K, A[0]+K)
            diff = min(diff, maximum-minimum)
        return diff