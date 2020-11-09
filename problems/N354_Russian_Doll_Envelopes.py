import bisect
import sys


class Solution(object):
    def maxEnvelopes_TLE(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        if not envelopes:
            return 0

        envelopes.sort()
        length = len(envelopes)
        dp = [1] * length
        res = 1
        for i in range(1, length):
            for j in range(i):
                if envelopes[i][0] > envelopes[j][0] and envelopes[i][1] > envelopes[j][1]:
                    dp[i] = max(dp[i], dp[j] + 1)
                    res = max(res, dp[i])
        return res

    def maxEnvelopes(self, envelopes):
        if not envelopes:
            return 0
        envelopes.sort(key=lambda x : (x[0], -x[1]))
        arr = []
        for en in envelopes:
            index = bisect.bisect_left(arr, en[1])
            if index < len(arr):
                arr[index] = en[1]   #keep the smallest height in the array
            else:
                arr.append(en[1])
        return len(arr)