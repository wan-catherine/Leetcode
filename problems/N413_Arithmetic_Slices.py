class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        length = len(A)
        if length < 3:
            return 0

        previous = A[1] - A[0]
        res = []
        current = 2
        flag = True
        for i in range(2, length):
            diff = A[i] - A[i-1]
            if diff == previous:
                flag = False
                current += 1
            else:
                previous = diff
                res.append(current)
                current = 2
                flag = True
        if not flag:
            res.append(current)
        len_dp = max(res)
        dp = [0] * (len_dp + 1)
        for i in range(3, len_dp + 1):
            dp[i] = i - 2 + dp[i-1]

        return sum([dp[i] for i in res])
