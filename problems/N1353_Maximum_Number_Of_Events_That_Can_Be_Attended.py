import heapq


class Solution(object):
    def maxEvents_TLE(self, events):
        """
        :type events: List[List[int]]
        :rtype: int
        """
        if not events:
            return 0

        events.sort(key=lambda li: (li[1]))
        attended = [0] * (events[-1][1] + 1)
        count = 0
        for i, j in events:
            for k in range(i, j+1):
                if not attended[k]:
                    attended[k] = 1
                    count += 1
                    break
        return count

    def maxEvents(self, A):
        A.sort(reverse=1)
        h = []
        res = d = 0
        while A or h:
            if not h: d = A[-1][0]
            while A and A[-1][0] <= d:
                heapq.heappush(h, A.pop()[1])
            heapq.heappop(h)
            res += 1
            d += 1
            while h and h[0] < d:
                heapq.heappop(h)
        return res