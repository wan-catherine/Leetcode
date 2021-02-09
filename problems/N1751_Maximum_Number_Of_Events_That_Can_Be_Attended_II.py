import bisect


class Solution(object):
    def maxValue(self, events, k):
        """
        :type events: List[List[int]]
        :type k: int
        :rtype: int
        """
        events.sort(key=lambda x:x[1])
        events = [[0,0,0]] + events
        length = len(events)
        ends = [events[i][1] for i in range(length)]
        dp = [[0]*(k+1) for _ in range(length)]

        for i in range(1, length):
            for j in range(1, k+1):
                start = events[i][0]
                index = bisect.bisect_left(ends, start)
                if ends[index] >= start:
                    index -= 1
                dp[i][j] = max(dp[i - 1][j], events[i][2] + dp[index][j-1])
        return dp[-1][-1]

