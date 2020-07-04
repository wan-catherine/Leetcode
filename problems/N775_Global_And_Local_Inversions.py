"""
All local inversions are swaps between two adjacent elements only .
So we can check abs(i - A[i]) > 1, if so return False
"""
class Solution(object):
    def isIdealPermutation(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        for i in range(len(A)):
            if abs(i - A[i]) > 1:
                return False
        return True
