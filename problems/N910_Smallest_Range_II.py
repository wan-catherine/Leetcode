"""
First sort the A.
a b c | d e f g
+ + +   - - - -

So we can know there should be some left part all add K, and then right part all subtract K.
But we don't know the index to sperate them, so we have to loop all possible index (0~length-1).
index means the last index which add K .
"""
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