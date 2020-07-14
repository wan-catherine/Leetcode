class Solution(object):
    def prevPermOpt1(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        length = len(A)
        if length == 1:
            return A

        if A[-1] < A[-2]:
            A[-1],A[-2] = A[-2],A[-1]
            return A

        for i in range(length -1, 0, -1):
            if A[i] >= A[i-1]:
                continue
            temp = A[i-1]
            index = i
            for j in range(i, length):
                if A[j] > A[index] and A[j] < temp:
                    index = j
            A[i-1],A[index] = A[index], A[i-1]
            break
        return A