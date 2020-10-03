import bisect
import heapq

"""
Maintain a smallest heap for busy which contains a pair (expected finish time, server id)
Maintain a sorted list for all free servers . 

Each time a new request comes:
    1. check the busy heap, if any request finished before or at the new request's arrival time, if yes, remove it from busy, add it to the free
    2. check if there is any free server , if no , then drop the request
    3. if there is a free server, binary search the right server id, then add it into the busy heap. 
"""
class Solution(object):
    def busiestServers(self, k, arrival, load):
        """
        :type k: int
        :type arrival: List[int]
        :type load: List[int]
        :rtype: List[int]
        """
        busy = []
        free = [i for i in range(k)]
        count = [0] * k
        length = len(arrival)
        for i in range(length):
            while busy and busy[0][0] <= arrival[i]:
                time, id = heapq.heappop(busy)
                bisect.insort_left(free, id)
            if not free:
                continue
            index = bisect.bisect_left(free, i%k)
            if index == len(free):
                index = 0
            id = free[index]
            free.remove(id)
            heapq.heappush(busy, (arrival[i] + load[i], id))
            count[id] += 1
        maximum = max(count)
        res = [i for i in range(k) if count[i] == maximum]
        return res