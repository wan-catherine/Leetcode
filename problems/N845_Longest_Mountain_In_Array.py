class Solution(object):
    def longestMountain(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if not A:
            return 0
        length = len(A)
        if length < 3:
            return 0

        res, temp = 1, 1
        value= A[0]
        for i in range(1, length):
            A[i], value = A[i] - value, A[i]

            if A[i] > 0:
                if A[i-1] < 0:
                    temp = 2
                else:
                    temp += 1
            elif A[i] < 0:
                if temp > 1:
                    temp += 1
                res = max(res, temp)
            else:
                temp = 1
        return res if res > 2 else 0






