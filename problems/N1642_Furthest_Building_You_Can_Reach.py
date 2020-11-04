import bisect
import heapq
from collections import deque


class Solution(object):
    def furthestBuilding_my(self, heights, bricks, ladders):
        """
        :type heights: List[int]
        :type bricks: int
        :type ladders: int
        :rtype: int
        """
        length = len(heights)
        total = 0
        heap = deque()
        heights = [heights[0]] + heights
        temp = 0
        for i in range(1, length+1):
            diff = heights[i] - heights[i-1]
            if diff <= 0:
                continue
            total += diff
            if not ladders:
                if total > bricks:
                    return i - 2
                else:
                    continue
            if len(heap) < ladders:
                temp += diff
                bisect.insort_left(heap, diff)
            elif diff > heap[0]:
                temp = temp + diff - heap[0]
                heap.popleft()
                bisect.insort_left(heap, diff)

            if total - temp > bricks:
                return i - 2
        return i - 1

    """
    Consider using ladders first. 
    Use priority queue to get the small height!
    """
    def furthestBuilding(self, heights, bricks, ladders):
        length = len(heights)
        heap = []
        for i in range(length - 1):
            diff = heights[i+1] - heights[i]
            if diff <= 0:
                continue
            heapq.heappush(heap, diff)
            if len(heap) > ladders:
                bricks -= heapq.heappop(heap)
            if bricks < 0:
                return i
        return length - 1