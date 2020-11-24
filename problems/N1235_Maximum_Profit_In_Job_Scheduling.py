import bisect
"""
dp[i]: means at i time, we can get dp[i] profit. i is the endTime. 
Key point : 
    Need to compare with the cur maximum profit. If we take a job and it takes a long time but low profit, 
    then we don't need to take this job : dp[end] = max(cur, dp[ends[index-1]] + p)
"""

class Solution(object):
    def jobScheduling(self, startTime, endTime, profit):
        """
        :type startTime: List[int]
        :type endTime: List[int]
        :type profit: List[int]
        :rtype: int
        """
        arr, length = [], len(startTime)

        for i in range(length):
            arr.append((endTime[i], startTime[i], profit[i]))
        arr.sort()
        ends = [0] + [arr[i][0] for i in range(length)]

        dp = {0:0}
        cur = 0

        for i in range(length):
            end, start, p = arr[i]
            index = bisect.bisect(ends, start)
            dp[end] = max(cur, dp[ends[index-1]] + p)
            cur = dp[end]
        return cur





