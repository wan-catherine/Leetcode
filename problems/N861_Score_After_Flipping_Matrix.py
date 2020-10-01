class Solution(object):
    def matrixScore(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        rows, cols = len(A), len(A[0])
        for i in range(rows):
            if A[i][0] == 0:
                for j in range(cols):
                    A[i][j] = 0 if A[i][j] == 1 else 1

        for i in range(1, cols):
            ones = 0
            for j in range(rows):
                if A[j][i] == 1:
                    ones += 1
            if ones > rows//2:
                continue
            for j in range(rows):
                A[j][i] = 0 if A[j][i] == 1 else 1
        # print(A)
        res = 0
        for i in range(rows):
            res += int(''.join([str(j) for j in A[i]]), 2)
        return res

