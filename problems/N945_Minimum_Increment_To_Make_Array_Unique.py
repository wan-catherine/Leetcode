"""
First , I think about the intervals , then everything becomes too complicated.

Then, reading other's answer, there is a way to increase all needed number to the number+1 .

"""
class Solution(object):
    def minIncrementForUnique(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if not A:
            return 0
        A.sort()
        length = len(A)
        res = 0
        for i in range(1, length):
            if A[i] <= A[i-1]:
                res += A[i-1] - A[i] + 1
                A[i] = A[i-1] + 1
        return res

