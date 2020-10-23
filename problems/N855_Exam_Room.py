import bisect
import heapq


class ExamRoom_(object):

    def __init__(self, N):
        """
        :type N: int
        """
        self.n = N
        self.arr = []

    def seat(self):
        """
        :rtype: int
        """
        if not self.arr:
            self.arr.append(0)
            return 0
        distance, index = self.arr[0], 0
        # A great way to get all intervals
        for left, right in zip(self.arr, self.arr[1:]):
            dis = (right - left) // 2
            if dis > distance:
                distance = dis
                index = (right - left) // 2 + left
        if self.n - 1 - self.arr[-1] > distance:
            index = self.n - 1
        bisect.insort(index, self.arr)

    def leave(self, p):
        """
        :type p: int
        :rtype: None
        """
        self.arr.remove(p)
"""
Use a heapq to save the intervals. 
first, end means the first seat and the last seat which are empty . 
"""

class ExamRoom:

    def __init__(self, N: int):
        self.heap = []
        self.firsts = {}
        self.ends = {}
        self.n = N
        self.put_interval(0, self.n - 1)

    def put_interval(self, first, end):
        if first == 0 or end == self.n - 1:
            priority = end - first
        else:
            priority = (end - first) // 2
        interval = [-priority, first, end, True]
        self.firsts[first] = interval
        self.ends[end] = interval
        heapq.heappush(self.heap, interval)

    def seat(self) -> int:
        while True:
            _, first, end, is_valid = heapq.heappop(self.heap)
            if is_valid:
                self.firsts.pop(first)
                self.ends.pop(end)
                break
        if first == 0:
            if first != end:
                self.put_interval(first+1, end)
            return first
        if end == self.n - 1:
            if first != end:
                self.put_interval(first, end - 1)
            return end
        index = (end - first) // 2 + first
        if index > first:
            self.put_interval(first, index - 1)
        if index < end:
            self.put_interval(index + 1, end)
        return index

    def leave(self, p: int) -> None:
        left, right = p-1, p+1
        first, end = p, p
        if left > 0 and left in self.ends:
            intervals = self.ends.pop(left)
            intervals[3] = False
            first = intervals[1]
        if right < self.n and right in self.firsts:
            intervals = self.firsts.pop(right)
            intervals[3] = False
            end = intervals[2]
        self.put_interval(first, end)
