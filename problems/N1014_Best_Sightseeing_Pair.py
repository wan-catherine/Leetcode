class Solution(object):
    def maxScoreSightseeingPair(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        length = len(A)

        i_sum = [0] * length
        j_sum = [0] * length

        for i in range(length):
            i_sum[i] = i+A[i]
            j_sum[i] = A[i]-i

        cur_max = j_sum[-1]
        for i in range(length-1, -1, -1):
            j_sum[i] = max(j_sum[i], cur_max)
            cur_max = j_sum[i]

        res = i_sum[0] + j_sum[1]
        for i in range(length-1):
            res = max(res, i_sum[i] + j_sum[i+1])

        return res