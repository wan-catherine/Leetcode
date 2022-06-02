import heapq
from typing import List

"""
Key point:
    put end of time into priority queue , so we can know when the room is free
"""

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        length = len(intervals)
        intervals.sort()
        pq = []
        res = 0
        for i in range(length):
            if pq and pq[0] <= intervals[i][0]:
                heapq.heappop(pq)
            heapq.heappush(pq, intervals[i][1])
            res = max(res, len(pq))
        return res