class Solution(object):
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        if not A or len(A) < 3:
            return True

        flag = 0
        for i in range(1,len(A)):
            if A[i] == A[i-1]:
                continue
            if A[i] > A[i-1]:
                if not flag:
                    flag = 1
                elif flag == -1:
                    return False
            else:
                if not flag:
                    flag = -1
                elif flag == 1:
                    return False

        return True

