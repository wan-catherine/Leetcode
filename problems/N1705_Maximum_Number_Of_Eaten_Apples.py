import heapq


class Solution(object):
    def eatenApples(self, apples, days):
        """
        :type apples: List[int]
        :type days: List[int]
        :rtype: int
        """
        res = 0
        heap = []
        i, length = 0, len(days)
        while i < length or heap:
            if i < length and apples[i] > 0:
                heapq.heappush(heap, [i+days[i], apples[i]])
            while heap and (heap[0][0] <= i or heap[0][1] <=0):
                heapq.heappop(heap)
            if heap:
                heap[0][1] -= 1
                res += 1
            i += 1
        return res