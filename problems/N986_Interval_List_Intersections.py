class Solution(object):
    def intervalIntersection(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        if not A or not B:
            return None

        a_len = len(A)
        b_len = len(B)

        i, j = 0, 0
        res = []
        while i < a_len and j < b_len:
            if A[i][0] > B[j][1]:
                j += 1
                continue
            elif A[i][1] < B[j][0]:
                i += 1
                continue
            if A[i][0] > B[j][0]:
                if A[i][1] >= B[j][1]:
                    res.append([A[i][0], B[j][1]])
                    if A[i][1] == B[j][1]:
                        i += 1
                    j += 1
                elif A[i][1] < B[j][1]:
                    res.append([A[i][0], A[i][1]])
                    i += 1
            elif A[i][0] <= B[j][0]:
                if A[i][1] >= B[j][1]:
                    res.append([B[j][0], B[j][1]])
                    if A[i][1] == B[j][1]:
                        i += 1
                    j += 1
                elif A[i][1] < B[j][1]:
                    res.append([B[j][0], A[i][1]])
                    i += 1

        return res





